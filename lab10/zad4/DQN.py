import gym
import numpy as np
import tensorflow as tf
from tensorflow.keras import models, layers, optimizers
from collections import deque
import random


class DQN(tf.keras.Model):
    def __init__(self, action_size):
        super(DQN, self).__init__()
        self.hidden_layers = [layers.Dense(24, activation='relu') for _ in range(2)]
        self.output_layer = layers.Dense(action_size, activation=None)

    def call(self, inputs):
        x = inputs
        for layer in self.hidden_layers:
            x = layer(x)
        return self.output_layer(x)


class Agent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=2000)
        self.gamma = 0.99  # discount rate
        self.epsilon = 1.0  # exploration rate
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.01
        self.learning_rate = 0.001
        self.model = DQN(action_size)
        self.optimizer = optimizers.Adam(learning_rate=self.learning_rate)
        self.loss_function = tf.keras.losses.MeanSquaredError()

    def memorize(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        q_values = self.model(tf.convert_to_tensor([state], dtype=tf.float32))
        return np.argmax(q_values[0].numpy())

    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)

        for state, action, reward, next_state, done in minibatch:
            target_q_value = reward if done else reward + self.gamma * np.amax(
                self.model(tf.convert_to_tensor([next_state], dtype=tf.float32))[0].numpy())
            with tf.GradientTape() as tape:
                q_values = self.model(tf.convert_to_tensor([state], dtype=tf.float32))
                loss = self.loss_function(target_q_value, q_values[0][action])
            grads = tape.gradient(loss, self.model.trainable_variables)
            self.optimizer.apply_gradients(zip(grads, self.model.trainable_variables))

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def load(self, name):
        self.model.load_weights(name)

    def save(self, name):
        self.model.save_weights(name)


def simulate(agent, env_name='CartPole-v1', episodes=10):
    env = gym.make(env_name)
    for e in range(episodes):
        state = env.reset()
        total_reward = 0
        done = False

        while not done:
            action = agent.act(state)
            next_state, reward, done, _ = env.step(action)
            total_reward += reward
            env.render()
            state = next_state

        print(f"Episode: {e + 1}, Total Reward: {total_reward}")


if __name__ == "__main__":
    env_name = "CartPole-v1"
    env = gym.make(env_name)
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n

    agent = Agent(state_size, action_size)
    episodes = 1000
    batch_size = 32

    for e in range(episodes):
        state