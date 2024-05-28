import numpy as np
import random
from collections import defaultdict

# Definición del entorno del Truco Argentino
class TrucoEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.state = self.init_state()
        return self.state

    def init_state(self):
        # Implementa la inicialización del estado del juego
        # Por ejemplo, la mano inicial del jugador y del oponente
        return {
            'player_hand': self.deal_hand(),
            'opponent_hand': self.deal_hand(),
            'current_round': 0
        }

    def deal_hand(self):
        # Reparte una mano de tres cartas al azar
        deck = list(range(1, 41))  # Supongamos que tenemos 40 cartas
        return random.sample(deck, 3)

    def step(self, action):
        # Implementa la lógica para tomar una acción y actualizar el estado del juego
        # Aquí action puede ser 'play_card', 'envido', 'truco', etc.
        reward = 0
        done = False

        # Actualiza el estado según la acción tomada

        return self.state, reward, done, {}

    def get_legal_actions(self):
        # Retorna una lista de acciones legales en el estado actual
        return ['play_card_1', 'play_card_2', 'play_card_3', 'envido', 'truco']

# Implementación del agente de Q-Learning
class QLearningAgent:
    def __init__(self, actions, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.q_table = defaultdict(lambda: np.zeros(len(actions)))
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.actions = actions

    def choose_action(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.actions)
        else:
            return self.actions[np.argmax(self.q_table[str(state)])]

    def update_q_table(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[str(next_state)])
        td_target = reward + self.gamma * self.q_table[str(next_state)][best_next_action]
        td_error = td_target - self.q_table[str(state)][self.actions.index(action)]
        self.q_table[str(state)][self.actions.index(action)] += self.alpha * td_error

# Entrenamiento del agente
env = TrucoEnv()
agent = QLearningAgent(actions=env.get_legal_actions())

num_episodes = 1000

for episode in range(num_episodes):
    state = env.reset()
    done = False

    while not done:
        action = agent.choose_action(state)
        next_state, reward, done, _ = env.step(action)
        agent.update_q_table(state, action, reward, next_state)
        state = next_state

    if (episode + 1) % 100 == 0:
        print(f'Episode {episode + 1}/{num_episodes} completed.')

# Visualizar la Q-Table entrenada
import pprint
pprint.pprint(dict(agent.q_table))
