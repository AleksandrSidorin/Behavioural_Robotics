#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import gym
import numpy as np
env = gym.make('CartPole-v0')

pvariance = 0.1 # variance of initial parameters
ppvariance = 0.02 # variance of perturbations
nhiddens = 5 # number of hidden neurons
# the number of inputs and outputs depends on the problem
# we assume that observations consist of vectors of continuous value
# and that actions can be vectors of continuous values or discrete actions
ninputs = env.observation_space.shape[0]
if (isinstance(env.action_space, gym.spaces.box.Box)):
    noutputs = env.action_space.shape[0]
else:
    noutputs = env.action_space.n

W = []
B = []
for i in range(10): #10
    W1 = np.random.randn(nhiddens, ninputs) * pvariance # first layer
    W2 = np.random.randn(noutputs, nhiddens) * pvariance # second layer
    b1 = np.zeros(shape=(nhiddens, 1)) # bias first layer
    b2 = np.zeros(shape=(noutputs, 1)) # bias second layer
    forW = [W1, W2]
    forB = [b1, b2]
    W.append(forW)
    B.append(forB)

for _ in range (10):

    rew_summ_list = []

    for i in range(10): 
        observation = env.reset()
        reward_summ = 0

        for _ in range(200): 
    # convert the observation array into a matrix with 1 column and ninputs rows
            observation.resize(ninputs,1)
            Z1 = np.dot(W[i][0], observation) + B[i][0]
            A1 = np.tanh(Z1)
            Z2 = np.dot(W[i][1], A1) + B[i][1]
            A2 = np.tanh(Z2)
    # if actions are discrete we select the action corresponding to the most activated unit
            if (isinstance(env.action_space, gym.spaces.box.Box)):
                action = A2
            else:
                action = np.argmax(A2)

            env.render()
            observation, reward, done, info = env.step(int(action))
            reward_summ = reward_summ + reward

            if done:
                    break

        rew_summ_list.append(reward_summ) 

    print(rew_summ_list)

    for k in range(len(rew_summ_list) - 1):
        for n in range(len(rew_summ_list) - k - 1):
            if rew_summ_list[n] > rew_summ_list[n + 1]:
                rew_summ_list[n], rew_summ_list[n + 1] = rew_summ_list[n + 1], rew_summ_list[n]
                W[n], W[n+1] = W[n+1], W[n]
                B[n], B[n+1] = B[n+1], B[n]
    
    for t in range(0, 5):
        W[t][0] = W[t][0] + np.random.normal(0, 1, (nhiddens, ninputs))
        W[t][1] = W[t][1] + np.random.normal(0, 1, (noutputs, nhiddens))
        B[t][0] = B[t][0] + np.random.normal(0, 1, (nhiddens, 1))
        B[t][1] = B[t][1] + np.random.normal(0, 1, (noutputs, 1))

