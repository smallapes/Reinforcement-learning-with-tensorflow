"""
Reinforcement learning maze example.

Red rectangle:          explorer.
Black rectangles:       hells       [reward = -1].
Yellow bin circle:      paradise    [reward = +1].
All other states:       ground      [reward = 0].

This script is the main part which controls the update method of this example.
The RL is in RL_brain.py.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""

from maze_env import Maze
from RL_brain import QLearningTable


def update():
    for episode in range(100):
        # initial observation
        observation = env.reset()

        while True:
            # fresh env
            env.render()

            # RL choose action based on observation
            action = RL.choose_action(str(observation))

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)

            # RL learn from this transition
            """
            Qlearning 是一个 off-policy 的算法, 因为里面的 max action 让 Q table 的更新
            可以不基于正在经历的经验(可以是现在学习着很久以前的经验,甚至是学习他人的经验). 
            
            不过这一次的例子, 我们没有运用到 off-policy, 而是把 Qlearning 用在了 on-policy 上, 也就是现学现卖, 将现在经历的直接当场学习并运用. 
            https://mofanpy.com/tutorials/machine-learning/reinforcement-learning/tabular-q1
            """
            RL.learn(str(observation), action, reward, str(observation_))

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            if done:
                break

    # end of game
    print('game over')
    env.destroy()

if __name__ == "__main__":
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))

    env.after(100, update)
    env.mainloop()