import gymnasium as gym
import simpful as sf

FS = sf.FuzzySystem()

# zmienne lingwistyczne dla kąta
angle = sf.AutoTriangle(3, terms=['negative', 'zero', 'positive'], universe_of_discourse=[-1, 1])
FS.add_linguistic_variable("angle", angle)

# zmienne lingwistyczne dla prędkości
speed = sf.AutoTriangle(3, terms=['negative', 'zero', 'positive'], universe_of_discourse=[-1, 1])
FS.add_linguistic_variable("speed", speed)

# zmienne lingwistyczne dla prędkości kątowej
angular_speed = sf.AutoTriangle(3, terms=['negative', 'zero', 'positive'], universe_of_discourse=[-8, 8])
FS.add_linguistic_variable("angular_speed", angular_speed)

# zmienne lingwistyczne dla akcji
action = sf.AutoTriangle(3, terms=['negative', 'zero', 'positive'], universe_of_discourse=[-2, 2])
FS.add_linguistic_variable("action", action)

# reguły
R1 = "IF (angle IS negative) AND (speed IS negative) AND (angular_speed IS negative) THEN (action IS positive)"
R2 = "IF (angle IS zero) AND (speed IS zero) AND (angular_speed IS zero) THEN (action IS zero)"
R3 = "IF (angle IS positive) AND (speed IS positive) AND (angular_speed IS positive) THEN (action IS negative)"
FS.add_rules([R1, R2, R3])

# gra Pendulum
env = gym.make('Pendulum-v1', render_mode='human')
observation, _ = env.reset()

for _ in range(1000):
    env.render()

    FS.set_variable("angle", observation[0])
    FS.set_variable("speed", observation[1])
    FS.set_variable("angular_speed", observation[2])

    inferred_action = FS.Mamdani_inference(["action"])
    observation, reward, terminated, truncated, info = env.step([inferred_action["action"].item()])

    if terminated or truncated:
        break

env.close()