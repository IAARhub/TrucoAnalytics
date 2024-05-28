import pytrucoengine as pte
import numpy as np
import random
from collections import defaultdict

# Definición del entorno del Truco usando PyTrucoEngine
class TrucoEnv:
    def __init__(self):
        self.game = pte.Game()
        self.reset()

    def reset(self):
        self.game.reset()
        self.state = self.get_state()
        return self.state

    def get_state(self):
        # Retorna una representación del estado actual del juego
        player_hand = self.game.players[0].hand
        opponent_hand = self.game.players[1].hand
        return {
            'player_hand': [card.rank for card in player_hand],
            'opponent_hand': [card.rank for card in opponent_hand],  # Este es solo un ejemplo, en un juego real no conocerías la mano del oponente
            'current_round': self.game.rounds
        }

    def step(self, action):
        # Toma una acción en el juego
        done = False
        reward = 0
        if action.startswith('play_card_'):
            card_index = int(action.split('_')[-1])
            card = self.game.players[0].hand[card_index]
            self.game.play_card(card)

        # Actualizar el estado y calcular la recompensa
        self.state = self.get_state()
        if self.game.is_over():
            done = True
            reward = self.calculate_reward()

        return self.state, reward, done, {}

    def calculate_reward(self):
        # Calcula la recompensa basada en el estado del juego
        if self.game.winner() == 0:
            return 1
        elif self.game.winner() == 1:
            return -1
        else:
            return 0

    def get_legal_actions(self):
        # Retorna una lista de acciones legales en el estado actual
        actions = [f'play_card_{i}' for i in range(len(self.game.players[0].hand))]
        if self.game.can_envido(0):
            actions.append('envido')
        if self.game.can_truco(0):
            actions.append('truco')
        return actions

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
