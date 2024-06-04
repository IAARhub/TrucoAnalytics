import socket
import numpy as np

class QLearningAgent:
    def __init__(self, n_actions, n_states):
        self.n_actions = n_actions
        self.n_states = n_states
        self.q_table = np.zeros((n_states, n_actions))

    def choose_action(self, state, epsilon):
        if np.random.uniform(0, 1) < epsilon:
            return np.random.choice(self.n_actions)
        else:
            return np.argmax(self.q_table[state])

    def update_q_table(self, state, action, reward, next_state, alpha, gamma):
        old_q_value = self.q_table[state, action]
        next_max = np.max(self.q_table[next_state])
        new_q_value = (1 - alpha) * old_q_value + alpha * (reward + gamma * next_max)
        self.q_table[state, action] = new_q_value

def state_to_numeric(state):
    # Convertir el estado del juego en un formato numérico
    return 0  # Ejemplo, necesitas implementar esto

def communicate_with_server(command):
    HOST = 'localhost'  # Dirección del servidor
    PORT = 6666         # Puerto del servidor

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(command.encode())
        data = s.recv(1024)

    return data.decode()

# Parámetros de entrenamiento
epsilon = 0.1
alpha = 0.1
gamma = 0.9
episodes = 1000

# Creamos el agente Q-Learning
n_actions = 3  # Jugar carta, aceptar, rechazar (ejemplo)
n_states = 10  # Ajustar según sea necesario
agent = QLearningAgent(n_actions, n_states)

# Loop de entrenamiento
for episode in range(episodes):
    state = communicate_with_server("state")
    state = state_to_numeric(state)

    while True:
        action = agent.choose_action(state, epsilon)
        action_command = f"play {action}"  # Ajustar según sea necesario
        next_state = communicate_with_server(action_command)
        reward = 0  # Obtener la recompensa del estado del juego (debes ajustar esto)
        next_state = state_to_numeric(next_state)

        agent.update_q_table(state, action, reward, next_state, alpha, gamma)

        state = next_state
        if reward != 0:  # Ajustar la condición de finalización del juego
            break
