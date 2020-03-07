# Behavioural_Robotics

## Exercise 2a

**Task:**

Implement a neural network controller for a Gym problem (e.g. the CartPole-v0 problem). Initialize the network with random parameters, and evaluate the neuro-agent for 10 evaluation episodes each lasting 200 steps.

During each step of each episode, the activation of the neural network and the state of the actuator should be updated.


Evaluate the agent for multiple evaluation episodes (e.g. 10) each lasting up to 200 steps by summing the fitness collected during all episodes. CartPole-v0 problem returns a reward of 1 for each step in which the pole is balanced, the fitness will correspond to the total number of steps in which the agent manages to keep the pole balanced. 

Implement the steady state evolutionary strategy (Pagliuca, Milano and Nolfi, 2018)

**Implementation:**

- Initiolize parameters
- Make list of W1, W2, b1 and b2 - first layer, second layer, bias first layer and bias second layer, respectively
- Loop 10 times. Each time colculate layers of neurons and activation, colculate reward_summ each time reset observation
- 
