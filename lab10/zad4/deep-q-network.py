import gymnasium as gym
import numpy as np
import tensorflow as tf
from tensorflow.keras import models, layers, optimizers
from collections import deque
import random

class DQN(tf.keras.Model):
  def __init__(self, action_size):
    super(DQN, self).__init__()
    self.dense1 = layers.Dense(24, activation='relu')
    self.dense2 = layers.Dense(24, activation='relu')
    self.dense3 = layers.Dense(action_size, activation=None)

  def call(self, x):
    x = self.dense1(x)
    x = self.dense2(x)
    return self.dense3(x)

class Agent:
  def __init__(self, state_size, action_size):
    self.state_size = state_size
    self.action_size = action_size
    self.memory = deque(maxlen=2000)
    self.gamma = 0.99
    self.epsilon = 1.0
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
    state = tf.convert_to_tensor([state], dtype=tf.float32)
    q_values = self.model(state)
    return np.argmax(q_values[0].numpy())

  def replay(self, batch_size):
    minibatch = random.sample(self.memory, batch_size)
    for state, action, reward, next_state, done in minibatch:
      target = reward
      if not done:
        next_state = tf.convert_to_tensor([next_state], dtype=tf.float32)
        target = reward + self.gamma * np.amax(self.model(next_state)[0].numpy())
      state = tf.convert_to_tensor([state], dtype=tf.float32)
      target_f = self.model(state).numpy()
      target_f[0][action] = target
      target_f = tf.convert_to_tensor(target_f, dtype=tf.float32)
      with tf.GradientTape() as tape:
        predictions = self.model(state)
        loss = self.loss_function(target_f, predictions)
      grads = tape.gradient(loss, self.model.trainable_variables)
      self.optimizer.apply_gradients(zip(grads, self.model.trainable_variables))
    if self.epsilon > self.epsilon_min:
      self.epsilon *= self.epsilon_decay

  def load(self, name):
    self.model = models.load_model(name)

  def save(self, name):
    self.model.save(name)

  def simulate(self, env, episodes=10):
    for e in range(episodes):
      state = env.reset()[0]
      done = False
      total_reward = 0
      while not done:
        state = tf.convert_to_tensor([state], dtype=tf.float32)
        action = self.act(state)
        next_state, reward, done, _, _ = env.step(action)
        state = next_state
        total_reward += reward
        env.render()
      print(f"Episode: {e+1}, Total Reward: {total_reward}")


env = gym.make("CartPole-v1", render_mode="human")
state_size = env.observation_space.shape[0]
action_size = env.action_space.n
agent = Agent(state_size, action_size)

episodes = 10
batch_size = 32

for e in range(episodes):
  state = env.reset()[0]
  for time in range(500):
    action = agent.act(state)
    next_state, reward, done, _, _ = env.step(action)
    agent.memorize(state, action, reward, next_state, done)
    state = next_state
    if done:
      print(f"Episode: {e+1}/{episodes}, Score: {time}, Epsilon: {agent.epsilon:.2}")
      break
    if len(agent.memory) > batch_size:
      agent.replay(batch_size)

agent.simulate(env)