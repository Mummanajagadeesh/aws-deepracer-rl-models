<p align="center">
  <img src="https://github.com/Mummanajagadeesh/aws-deepracer-rl-models/blob/fcce91ec023cc5628e17f487fc6003ed06ce8cf6/2024_world_firstrace_student.49456e799ed44657bac8.svg" alt="AWS DeepRacer First Race 2024"/>
</p>


# AWS DeepRacer Reinforcement Learning Models

This repository contains a collection of **trained reinforcement learning models** for AWS DeepRacer, an autonomous 1/18th scale race car that is capable of driving itself around a track using machine learning.

## Overview

All models in this repository are trained using custom **reward functions** written in Python. These reward functions guide the car's behavior by rewarding desirable actions and penalizing less optimal ones. The goal is to make the car complete laps autonomously within a certain range of time, with a key performance target being to finish a lap in **under 2 minutes**.

The car's driving decisions are made solely based on the algorithms provided to it, with no human intervention once the race begins.

## Algorithm: Proximal Policy Optimization (PPO)

All models and agents in this repository use the **Proximal Policy Optimization (PPO)** algorithm. PPO is a popular reinforcement learning algorithm that works by balancing exploration (trying new actions) and exploitation (choosing the best-known actions) to optimize the car's behavior over time. It updates the policy in a way that ensures stability and improves training efficiency, making it a powerful tool for continuous control tasks like autonomous driving.

## IMP LINKS

<!--chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/https://cdn.sanity.io/files/tlr8oxjg/production/85a57092f82acfa28186b72fd7017ce61a9cb9f6.pdf?utm_campaign=acq_100_auto_ndxxx_syllabus_global&utm_source=blueshift&utm_medium=email&utm_content=acq_100_auto_ndxxx_auto-syllabus-updated-1_global&bsft_clkid=f3ae0b7c-912c-4081-82d9-0752bfb8ae8d&bsft_uid=765ae608-91eb-4e2e-b413-a26987a76326&bsft_mid=7255381a-3ef8-4c5f-9486-a52c62e9ff69&bsft_eid=c83a107a-3d0c-4569-7d43-6310e1357f42&bsft_txnid=059e8b0d-a7c3-4f25-8f20-0d49c3592ffd&bsft_mime_type=html&bsft_ek=2024-10-14T05%3A21%3A11Z&bsft_aaid=affd8710-61ff-4001-baca-1d4a7303381d&bsft_lx=2&bsft_tv=20-->

UDACITY AI PROGRAMMING WITH PYTHON NANODEGREE  : https://www.udacity.com/course/ai-programming-python-nanodegree--nd089

UDACITY AWS AI ML SCHOLARSHIP : https://www.udacity.com/scholarships/aws-ai-ml-scholarship-program

SYLLABUS : https://emc.udacity.com/c/aws-esperanza/catalog/Bh8dTV4FgDfxsqEI/i/nd/nd089

CATALOG : https://emc.udacity.com/c/aws-esperanza/me

DEEPRACER SITE : https://student.deepracer.com/home

TIPS : https://aws.amazon.com/deepracer/racing-tips/




# AWS DeepRacer Guide

AWS DeepRacer is a powerful platform that provides a hands-on learning environment for reinforcement learning (RL). Designed for developers of all levels, DeepRacer allows you to train and evaluate RL models using a 1/18th scale autonomous car in both simulated and physical environments.

This guide will cover the basics of AWS DeepRacer, including technical details on how it works, its core components, and steps to get started with model training and deployment.

---

## Overview of AWS DeepRacer

AWS DeepRacer introduces reinforcement learning through the use of an autonomous vehicle. The goal is to develop an RL model that can guide the car to complete a track as efficiently as possible, typically aiming to minimize lap times. 

### Key Concepts in AWS DeepRacer

- **Reinforcement Learning (RL)**: Unlike traditional programming, RL focuses on training agents by rewarding them for desirable actions, allowing them to learn optimal behaviors through trial and error.
- **Action Space**: Set of actions the car can take, including speed and steering angles. The chosen action space directly influences the model’s training and performance.
- **Reward Function**: The model’s core logic that rewards or penalizes actions taken by the car. This function guides the car’s behavior by encouraging it to follow a path on the track.

---

## AWS DeepRacer Workflow

### 1. **Model Training**

Training a model involves setting up an environment where the car can learn to navigate a track.

   - **Select Action Space**: Define possible actions for the car (e.g., specific speeds and turning angles).
   - **Define Reward Function**: The reward function is critical in shaping the car's behavior. AWS DeepRacer offers templates, but custom reward functions can be developed to optimize track performance.
   - **Hyperparameters**: Configure hyperparameters such as batch size, learning rate, and discount factor. These influence the RL model’s training and adaptability.

### 2. **Model Evaluation**

   - **Simulated Evaluation**: After training, models are tested in a simulation to check how well the car navigates the track. You’ll monitor metrics like lap time, completion rate, and consistency.
   - **Fine-tuning**: Based on performance in simulation, make adjustments to the reward function, action space, or hyperparameters to improve model performance.

### 3. **Deploying the Model**

   - Once a model is trained and optimized in the simulator, it can be deployed on a physical AWS DeepRacer car for real-world testing.
   - **Testing in Real-World Environments**: Deploy the trained model to the physical car and observe its performance in a real-world setting, making further adjustments as necessary.

---

## Technical Components of AWS DeepRacer

### **1. Simulation Environment**
   - The simulation uses Amazon SageMaker, AWS’s machine learning platform, for model training.
   - The simulator provides various tracks, allowing models to learn in multiple environments with different levels of complexity.

### **2. Reward Functions**
   - Reward functions guide the car by incentivizing behaviors like staying on the track, maintaining certain speeds, and taking efficient paths through curves.
   - Customizing a reward function allows for specialized behaviors that can significantly improve model performance.

### **3. Training Algorithms**
   - AWS DeepRacer uses **Proximal Policy Optimization (PPO)**, a popular reinforcement learning algorithm that balances exploration and exploitation.
   - PPO helps the model learn from both successes and mistakes, iterating toward an optimal strategy for the defined reward function.

### **4. Hyperparameter Tuning**
   - The training process is influenced by various hyperparameters:
     - **Learning Rate**: Controls how much the model’s parameters are updated with each step.
     - **Batch Size**: Defines the number of training samples processed before the model updates.
     - **Discount Factor (Gamma)**: Balances immediate versus long-term rewards in model training.

### **5. Action Space**
   - Defines the range of actions the car can take (e.g., possible speed and steering values).
   - Choosing a smaller, precise action space can help models learn faster and improve performance on simpler tracks, while a larger action space might be necessary for more complex tracks.

---
