<p align="center">
  <img src="https://github.com/Mummanajagadeesh/aws-deepracer-rl-models/blob/fcce91ec023cc5628e17f487fc6003ed06ce8cf6/2024_world_firstrace_student.49456e799ed44657bac8.svg" alt="AWS DeepRacer First Race 2024"/>
</p>

# AWS DeepRacer Reinforcement Learning Models

Welcome to the AWS DeepRacer reinforcement learning (RL) models repository. Here, you’ll find a collection of **trained RL models** designed for AWS DeepRacer, a fully autonomous 1/18th scale race car capable of navigating tracks independently using machine learning.

## Repository Overview

This repository contains models built using custom **reward functions** crafted in Python. These functions guide the DeepRacer’s behavior, rewarding effective actions and discouraging less optimal ones, with the ultimate aim of completing laps autonomously in **under 2 minutes**.

### Key Features
- **Reinforcement Learning**: Models are trained with a focus on RL, where actions are rewarded or penalized to drive the car's learning process.
- **Proximal Policy Optimization (PPO)**: The models utilize the PPO algorithm, balancing exploration (trying new actions) with exploitation (choosing the best-known actions), to progressively improve lap times and navigation efficiency.

---

## AWS DeepRacer: Core Technical Components

### 1. **Simulation Environment**
   AWS DeepRacer uses **Amazon SageMaker** to train and simulate models. The platform provides various track environments, enabling developers to simulate diverse conditions and optimize model performance across different challenges.

### 2. **Reward Functions**
   Reward functions define the car's decision-making logic, guiding it by incentivizing actions like staying on the track, maintaining optimal speed, and navigating curves efficiently. Crafting custom reward functions allows for targeted behavior adjustments, leading to more sophisticated track performance.

### 3. **Training Algorithms**
   The models in this repository utilize **Proximal Policy Optimization (PPO)**, an RL algorithm that facilitates stable and efficient learning. PPO iteratively adjusts the model based on successful actions, helping the car progressively learn the optimal path and behavior for autonomous navigation.

### 4. **Hyperparameter Tuning**
   Key hyperparameters affect model training and are essential for tuning:
   - **Learning Rate**: Determines the speed at which the model updates based on feedback.
   - **Batch Size**: Specifies the number of samples processed per training iteration.
   - **Discount Factor (Gamma)**: Balances the car’s focus between immediate and future rewards, impacting long-term decision-making.

### 5. **Action Space**
   Action space defines the car’s movement options, such as possible steering angles and speed settings. A carefully chosen action space ensures faster learning for simpler tracks and provides the flexibility needed for more complex circuits.

---

## AWS DeepRacer Workflow

### Step 1: Model Training
Model training begins with creating a simulation environment where the DeepRacer car learns to navigate a track. Training involves:
   - **Selecting an Action Space**: Define the range of possible movements (e.g., speed and angles) the car can take.
   - **Defining the Reward Function**: Customizing a reward function is critical to shaping the model’s decision-making.
   - **Configuring Hyperparameters**: Adjust parameters like learning rate, batch size, and discount factor to influence training outcomes.

### Step 2: Model Evaluation
   - **Simulated Evaluation**: After training, the model is tested in a simulation to assess its track navigation skills, monitoring metrics such as lap time, completion rate, and consistency.
   - **Fine-tuning**: Based on evaluation results, adjust the reward function, action space, or hyperparameters for improved performance.

### Step 3: Model Deployment
   - After successful simulation, models can be deployed on a physical AWS DeepRacer car for real-world testing.
   - **Real-World Testing**: Deploy the model to a physical track to observe and fine-tune its performance under real conditions.

---

## Getting Started with AWS DeepRacer

1. **Set Up AWS Account**: Create an AWS account and configure permissions for Amazon SageMaker and AWS DeepRacer.
2. **Train a Model**: In the AWS DeepRacer console, define the action space, reward function, and hyperparameters, and start a training job.
3. **Evaluate and Iterate**: Use the simulation environment to test model performance and refine settings as necessary.
4. **Deploy on Physical Car** (Optional): For real-world applications, deploy your model on a physical DeepRacer car to test its capabilities on an actual track.

---

## Useful Links

- [Udacity AI Programming with Python Nanodegree](https://www.udacity.com/course/ai-programming-python-nanodegree--nd089)
- [Udacity AWS AI ML Scholarship](https://www.udacity.com/scholarships/aws-ai-ml-scholarship-program)
- [AWS DeepRacer Tips](https://aws.amazon.com/deepracer/racing-tips/)
- [AWS DeepRacer Official Site](https://student.deepracer.com/home)

---

AWS DeepRacer combines machine learning with autonomous driving, providing a hands-on way to explore and understand reinforcement learning. By following these steps, you can train your own RL model and apply it in both simulated and real-world environments to unlock the potential of autonomous navigation.
