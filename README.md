# AWS DeepRacer Reinforcement Learning Models

This repository contains a collection of **trained reinforcement learning models** for AWS DeepRacer, an autonomous 1/18th scale race car that is capable of driving itself around a track using machine learning.

## Overview

All models in this repository are trained using custom **reward functions** written in Python. These reward functions guide the car's behavior by rewarding desirable actions and penalizing less optimal ones. The goal is to make the car complete laps autonomously within a certain range of time, with a key performance target being to finish a lap in **under 2 minutes**.

The car's driving decisions are made solely based on the algorithms provided to it, with no human intervention once the race begins.

## Algorithm: Proximal Policy Optimization (PPO)

All models and agents in this repository use the **Proximal Policy Optimization (PPO)** algorithm. PPO is a popular reinforcement learning algorithm that works by balancing exploration (trying new actions) and exploitation (choosing the best-known actions) to optimize the car's behavior over time. It updates the policy in a way that ensures stability and improves training efficiency, making it a powerful tool for continuous control tasks like autonomous driving.

## AWS AI/ML Scholarship by Udacity

These models were trained as part of the **AWS AI/ML Scholarship Program** by **Udacity**. Upon achieving a lap time of under 2 minutes and completing other scholarship modules, participants are eligible to apply for the **AI Programming with Python Nanodegree** program.
