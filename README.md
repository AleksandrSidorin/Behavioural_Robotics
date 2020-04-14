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
- Loop 10 times. Each time reset observation
- Loop 10 times. Each time colculate layers of neurons and activation, colculate reward_summ
- Take 5 W and b where reward_sum was max
- Add Gausian noise to the rest of W and b
- Loop again and as a result we have only best values of W and b for the task

[Code](https://github.com/AleksandrSidorin/Behavioural_Robotics/blob/master/NN%20controller%20for%20a%20Gym%20problem%20(CartPole-v0).py)

<img width="565" alt="Снимок экрана 2020-03-07 в 7 05 26 AM" src="https://user-images.githubusercontent.com/55827366/76136484-1b944a80-6043-11ea-9c41-a49755cd9898.png">

## Exercise 3

**Task:**

Run few replications of the experiment by using different seeds. Use the pre-prepared acrobot.ini file included in the ./xacrobot directory. Plot performance across generations and then observe the behavior of evolved robots.

By running the programm with differient seed I got this result:

This Graf shows how Best Fit depends on Seed value:

<img width="401" alt="Снимок экрана 2020-03-13 в 11 14 24 AM" src="https://user-images.githubusercontent.com/55827366/76602654-74b91e00-651c-11ea-964c-dd3709007cd7.png">

## Exercise 4

**Task:**

Evolve the robots with the original reward functions and then compare the behavior of robots evolved with the original and revised reward functions, e.g. in the case of the hopper and halfcheetah. 

1) Describe the difference between the two functions. Describe how the behaviour of the evolved robots differ.

The original one is summary of:

1. _alive_ - shows if the robot height above ground 
2. _progress_ - movement of the robot to the target direction.
3. _electricity_cost_ - penalty due to cost of using robot's motors.
4. _joints_at_limit_cost_ - penalty due to stucking joints of the robot.
5. _feet_collision_cost_ - penalty given if another leg is touching other objects, that makes robot avoiding smashing feet into itself.

The modified one (for example, for humanoid) is summary of:

1. _progress_ - the same
2. _1.0_ - bonus - robot receives to avoid falling.
3. _feet_cost_ - shows if both of the feet on the ground or not.
4. _joints_at_limit_cost_ - the same 
5. _angle_offset_cost_ - penalty that shows how much is angle offset between the robot and the target.

I ran two environments - halfcheetah and humanoid with both of reward functions at the same time. Humanoid had better results, agents were could move to the the target. Halfcheetah function robots could not do it. They have fallen down always. 

2) Explain why the original rewards functions are not suitable for evolutionary strategies ?

The idea of evolutionary algorithm is that there are several agents. They are learned at the same time in one generation. Then, the algorithm choose the best ones and produces new for starting the next generation. When  break rule happens loop stops. 

## Exercise 5

**Task:**

Implementing a new Gym/Bullet environment

I got good desirable results: two-wheeled robot balance itself very good.

![IMAGE 2020-04-14 4:01:01 PM](https://user-images.githubusercontent.com/55827366/79227802-24114980-7e69-11ea-933a-063dc15f2e5b.jpg)

