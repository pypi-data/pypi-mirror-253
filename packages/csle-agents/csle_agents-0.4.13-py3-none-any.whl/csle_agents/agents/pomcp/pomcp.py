from typing import List, Union, Callable, Any, Dict, Tuple
import time
import random
import numpy as np
from csle_common.dao.simulation_config.base_env import BaseEnv
from csle_common.dao.training.policy import Policy
from csle_common.logging.log import Logger
from csle_agents.agents.pomcp.belief_tree import BeliefTree
from csle_agents.agents.pomcp.belief_node import BeliefNode
from csle_agents.agents.pomcp.action_node import ActionNode
from csle_agents.agents.pomcp.pomcp_util import POMCPUtil
import csle_agents.constants.constants as constants


class POMCP:
    """
    Class that implements the POMCP algorithm
    """

    def __init__(self, A: List[int], gamma: float, env: BaseEnv, c: float,
                 initial_belief: Dict[int, float], planning_time: float = 0.5, max_particles: int = 350,
                 reinvigoration: bool = False,
                 reinvigorated_particles_ratio: float = 0.1, rollout_policy: Union[Policy, None] = None,
                 value_function: Union[Callable[[Any], float], None] = None, verbose: bool = False,
                 default_node_value: float = 0, parallel_rollout: bool = False,
                 num_parallel_processes: int = 10, num_evals_per_process: int = 10, prior_weight: float = 1.0,
                 prior_confidence: int = 0) -> None:
        """
        Initializes the solver

        :param S: the state space
        :param A: the action space
        :param gamma: the discount factor
        :param env: the environment for sampling
        :param c: the weighting factor for UCB
        :param initial_belief: the initial belief state
        :param planning_time: the planning time
        :param max_particles: the maximum number of particles (samples) for the belief state
        :param reinvigorated_particles_ratio: probability of new particles added when updating the belief state
        :param reinvigoration: boolean flag indicating whether reinvigoration should be done
        :param rollout_policy: the rollout policy
        :param verbose: boolean flag indicating whether logging should be verbose
        :param default_node_value: the default value of nodes in the tree
        :param parallel_rollout: boolean flag indicating whether parallel rollout should be used
        :param num_parallel_processes: number of parallel processes
        :param num_evals_per_process: number of evaluations per process
        :param prior_weight: the weight to put on the prior
        :param prior_confidence: the prior confidence (initial count)
        """
        self.A = A
        self.env = env
        o, info = self.env.reset()
        self.root_observation = info[constants.COMMON.OBSERVATION]
        self.gamma = gamma
        self.c = c
        self.planning_time = planning_time
        self.max_particles = max_particles
        self.reinvigorated_particles_ratio = reinvigorated_particles_ratio
        self.rollout_policy = rollout_policy
        self.initial_visit_count = 0
        self.value_function = value_function
        self.initial_belief = initial_belief
        self.reinvigoration = reinvigoration
        self.default_node_value = default_node_value
        self.parallel_rollout = parallel_rollout
        self.num_parallel_processes = num_parallel_processes
        self.num_evals_per_process = num_evals_per_process
        self.prior_weight = prior_weight
        root_particles = POMCPUtil.generate_particles(num_particles=self.max_particles, belief=initial_belief)
        self.tree = BeliefTree(root_particles=root_particles, default_node_value=self.default_node_value,
                               root_observation=self.root_observation, initial_visit_count=self.initial_visit_count)
        self.verbose = verbose
        self.prior_confidence = prior_confidence

    def compute_belief(self) -> Dict[int, float]:
        """
        Computes the belief state based on the particles

        :return: the belief state
        """
        belief_state = {}
        particle_distribution = POMCPUtil.convert_samples_to_distribution(self.tree.root.particles)
        for state, prob in particle_distribution.items():
            belief_state[state] = round(prob, 6)
        return belief_state

    def rollout(self, state: int, history: List[int], depth: int, max_rollout_depth: int) -> float:
        """
        Perform randomized recursive rollout search starting from the given history
        until the max depth has been achieved

        :param state: the initial state of the rollout
        :param history: the history of the root node
        :param depth: current planning horizon
        :param max_rollout_depth: max rollout depth
        :return: the estimated value of the root node
        """
        if depth > max_rollout_depth:
            if self.value_function is not None:
                o = self.env.get_observation_from_history(history=history)
                return self.value_function(o)
            else:
                return 0
        if self.rollout_policy is None or self.env.is_state_terminal(state):
            a = POMCPUtil.rand_choice(self.A)
        else:
            a = self.rollout_policy.action(o=self.env.get_observation_from_history(history=history))
        _, r, _, _, info = self.env.step(a)
        s_prime = info[constants.COMMON.STATE]
        o = info[constants.COMMON.OBSERVATION]
        if s_prime not in self.initial_belief:
            self.initial_belief[s_prime] = 0.0
        o = info[constants.COMMON.OBSERVATION]
        return float(r) + self.gamma * self.rollout(state=s_prime, history=history + [a, o], depth=depth + 1,
                                                    max_rollout_depth=max_rollout_depth)

    def simulate(self, state: int, max_rollout_depth: int, c: float, history: List[int],
                 max_planning_depth: int, depth=0, parent: Union[None, BeliefNode, ActionNode] = None) \
            -> Tuple[float, int]:
        """
        Performs the POMCP simulation starting from a given belief node and a sampled state

        :param state: the sampled state from the belief state of the node
        :param max_rollout_depth: the maximum depth of rollout
        :param max_planning_depth: the maximum depth of planning
        :param c: the weighting factor for the ucb acquisition function
        :param depth: the current depth of the simulation
        :param history: the current history (history of the start node plus the simulation history)
        :param parent: the parent node in the tree
        :return: the Monte-Carlo value of the node and the current depth
        """

        # Check if we have reached the maximum depth of the tree
        if depth > max_planning_depth:
            if len(history) > 0 and self.value_function is not None:
                o = self.env.get_observation_from_history(history=history)
                return self.value_function(o), depth
            else:
                return 0, depth

        # Check if the new history has already been visited in the past of should be added as a new node to the tree
        observation = -1
        if len(history) > 0:
            observation = history[-1]
        if observation != -1 and self.value_function is not None:
            value = self.value_function(self.env.get_observation_from_history(history))
        else:
            value = self.default_node_value
        current_node = self.tree.find_or_create(history=history, parent=parent, observation=observation,
                                                initial_visit_count=self.prior_confidence, initial_value=value)

        # If a new node was created, then it has no children, in which case we should stop the search and
        # do a Monte-Carlo rollout with a given base policy to estimate the value of the node
        if not current_node.children:
            # since the node does not have any children, we first add them to the node
            # obs_vector = self.env.get_observation_from_history(current_node.history)
            # dist = self.rollout_policy.model.policy.get_distribution(
            #     obs=torch.tensor([obs_vector]).to(self.rollout_policy.model.device)).log_prob(
            #     torch.tensor(self.A).to(self.rollout_policy.model.device)).cpu().detach().numpy()
            # dist = list(map(lambda i: (math.exp(dist[i]), self.A[i]), list(range(len(dist)))))
            # rollout_actions = list(map(lambda x: x[1], sorted(dist, reverse=True, key=lambda x: x[0])[:3]))
            rollout_actions = self.A
            # for action in self.A:
            for action in rollout_actions:
                self.tree.add(history + [action], parent=current_node, action=action, value=self.default_node_value)

            # Perform the rollout from the current state and return the value
            if self.parallel_rollout and self.rollout_policy is not None:
                R = self.env.parallel_rollout(policy_id=self.rollout_policy.id,
                                              num_processes=self.num_parallel_processes,
                                              num_evals_per_process=self.num_evals_per_process,
                                              max_horizon=max_rollout_depth, state_id=state)
                return float(R), depth
            else:
                self.env.set_state(state=state)
                return (self.rollout(state=state, history=history, depth=depth, max_rollout_depth=max_rollout_depth),
                        depth)

        # If we have not yet reached a new node, we select the next action according to the
        # UCB strategy
        random.shuffle(current_node.children)
        o = self.env.get_observation_from_history(current_node.history)
        next_action_node = sorted(
            current_node.children, key=lambda x: POMCPUtil.ucb_acquisition_function(
                x, c=c, rollout_policy=self.rollout_policy, o=o, prior_weight=self.prior_weight), reverse=True)[0]

        # Simulate the outcome of the selected action
        a = next_action_node.action
        self.env.set_state(state=state)
        _, r, _, _, info = self.env.step(a)
        o = info[constants.COMMON.OBSERVATION]
        s_prime = info[constants.COMMON.STATE]
        if s_prime not in self.initial_belief:
            self.initial_belief[s_prime] = 0.0

        # Recursive call, continue the simulation from the new node
        assert isinstance(next_action_node, ActionNode)
        R, rec_depth = self.simulate(
            state=s_prime, max_rollout_depth=max_rollout_depth, depth=depth + 1,
            history=history + [next_action_node.action, o],
            parent=next_action_node, c=c, max_planning_depth=max_planning_depth)
        R = float(r) + self.gamma * R

        # The simulation has completed, time to backpropagate the values
        # We start by updating the belief particles and the visit count of the current belief node
        if isinstance(current_node, BeliefNode):
            current_node.particles += [state]

        # Next we update the statistics and visit counts of the action node
        if isinstance(next_action_node, ActionNode):
            next_action_node.update_stats(immediate_reward=r)
        current_node.visit_count += 1
        next_action_node.visit_count += 1
        next_action_node.value += (R - next_action_node.value) / next_action_node.visit_count

        return float(R), rec_depth

    def solve(self, max_rollout_depth: int, max_planning_depth: int) -> None:
        """
        Runs the POMCP algorithm with a given max depth for the lookahead

        :param max_rollout_depth: the max depth for rollout
        :param max_planning_depth: the max depth for planning
        :return: None
        """
        Logger.__call__().get_logger().info(
            f"Starting POMCP, max rollout depth: {max_rollout_depth}, max planning depth: {max_planning_depth}, "
            f"c: {self.c}, planning time: {self.planning_time}, gamma: {self.gamma}, "
            f"max particles: {self.max_particles}, "
            f"reinvigorated_particles_ratio: {self.reinvigorated_particles_ratio}")
        begin = time.time()
        n = 0
        state = self.tree.root.sample_state()
        self.env.set_state(state)
        print(self.env.get_true_table())
        print(self.env.decoy_state)
        print(self.env.scan_state)
        while time.time() - begin < self.planning_time:
            n += 1
            state = self.tree.root.sample_state()
            _, depth = self.simulate(state=state, max_rollout_depth=max_rollout_depth, history=self.tree.root.history,
                                     c=self.c,
                                     parent=self.tree.root, max_planning_depth=max_planning_depth, depth=0)
            if self.verbose:
                action_values = np.zeros((len(self.A),))
                best_action_idx = 0
                best_value = -np.inf
                for i, action_node in enumerate(self.tree.root.children):
                    action_values[action_node.action] = action_node.value
                    if action_node.value > best_value:
                        best_action_idx = i
                        best_value = action_node.value
                Logger.__call__().get_logger().info(
                    f"Planning time left {self.planning_time - time.time() + begin}s, "
                    f"best action: {self.tree.root.children[best_action_idx].action}, "
                    f"value: {self.tree.root.children[best_action_idx].value}, "
                    f"count: {self.tree.root.children[best_action_idx].visit_count}, "
                    f"planning depth: {depth}")
                # , 31:{action_values[31]}

    def get_action(self) -> int:
        """
        Gets the next action to execute based on the state of the tree. Selects the action with the highest value
        from the root node.

        :return: the next action
        """
        root = self.tree.root
        action_vals = [(action.value, action.action) for action in root.children]
        for a in root.children:
            Logger.__call__().get_logger().info(f"action: {a.action}, value: {a.value}, "
                                                f"visit count: {a.visit_count}")
        return int(max(action_vals)[1])

    def update_tree_with_new_samples(self, action_sequence: List[int], observation: int, observation_vector: List[int],
                                     max_negative_samples: int = 20) -> Dict[int, float]:
        """
        Updates the tree after an action has been selected and a new observation been received

        :param action_sequence: the action sequence that was executed
        :param observation: the observation that was received
        :param max_negative_samples: the maximum number of negative samples that can be collected before
              trajectory simulation is initialized
        :param observation_vector: the observation vector that was received
        :return: the updated belief state
        """
        self.env.add_observation_vector(obs_vector=observation_vector, obs_id=observation)
        root = self.tree.root
        if len(action_sequence) == 0:
            raise ValueError("Invalid action sequencee")
        action = action_sequence[-1]

        # Since we executed an action we advance the tree and update the root to the the node corresponding to the
        # action that was selected
        child = root.get_child(action)
        if child is not None:
            new_root = child.get_child(observation)
        else:
            raise ValueError(f"Could not find child node for action: {action}")

        # If we did not have a node in the tree corresponding to the observation that was observed, we select a random
        # belief node to be the new root (note that the action child node will always exist by definition of the
        # algorithm)
        if new_root is None:
            # Get the action node
            action_node = root.get_child(action)
            if action_node is None:
                raise ValueError("Chould not find the action node")

            if action_node.children:
                # If the action node has belief state nodes, select a random of them to be the new root
                new_root = POMCPUtil.rand_choice(action_node.children)
            else:
                # or create the new belief node randomly
                random_belief = {}
                for s in list(self.initial_belief.keys()):
                    random_belief[s] = 1 / len(self.initial_belief)
                particles = POMCPUtil.generate_particles(num_particles=self.max_particles, belief=random_belief)
                if self.value_function is not None:
                    initial_value = self.value_function(observation)
                else:
                    initial_value = self.default_node_value
                new_root = self.tree.add(history=action_node.history + [observation], parent=action_node,
                                         observation=observation, particle=particles, value=initial_value,
                                         initial_visit_count=self.prior_confidence)

        # Check how many new particles are left to fill
        if isinstance(new_root, BeliefNode):
            particle_slots = self.max_particles - len(new_root.particles)
        else:
            raise ValueError("Invalid root node")
        negative_samples_count = 0
        if particle_slots > 0:
            if self.verbose:
                Logger.__call__().get_logger().info(f"Filling {particle_slots} particles")
            particles = []
            # fill particles by Monte-Carlo using reject sampling
            while len(particles) < particle_slots:
                if negative_samples_count >= max_negative_samples:
                    particles += POMCPUtil.trajectory_simulation_particles(
                        o=observation, env=self.env, action_sequence=action_sequence, verbose=self.verbose,
                        num_particles=(particle_slots - len(particles)))
                else:
                    s = root.sample_state()
                    self.env.set_state(state=s)
                    _, r, _, _, info = self.env.step(action)
                    s_prime = info[constants.COMMON.STATE]
                    o = info[constants.COMMON.OBSERVATION]
                    if o == observation:
                        particles.append(s_prime)
                        negative_samples_count = 0
                    else:
                        negative_samples_count += 1
            new_root.particles += particles

        # We now prune the old root from the tree
        self.tree.prune(root, exclude=new_root)
        # and update the root
        self.tree.root = new_root
        # and compute the new belief based on the updated particles
        new_belief = self.compute_belief()

        # To avoid particle deprivation (i.e., that the algorithm gets stuck with the wrong belief)
        # we do particle reinvigoration here
        if self.reinvigoration and len(self.initial_belief) > 0 and any([prob == 0.0 for prob in new_belief.values()]):
            if self.verbose:
                Logger.__call__().get_logger().info("Starting reinvigoration")
            # Generate same new particles randomly
            random_belief = {}
            for s in list(self.initial_belief.keys()):
                random_belief[s] = 1 / len(self.initial_belief)
            mutations = POMCPUtil.generate_particles(
                num_particles=int(self.max_particles * self.reinvigorated_particles_ratio),
                belief=random_belief)

            # Randomly exchange some old particles for the new ones
            for particle in mutations:
                new_root.particles[np.random.randint(0, len(new_root.particles))] = particle

            # re-compute the current belief distribution after reinvigoration
            new_belief = self.compute_belief()
        return new_belief
