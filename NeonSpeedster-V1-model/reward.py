def reward_function(params):
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    progress = params['progress']
    steps = params['steps']
    speed = params['speed']
    steering_angle = abs(params['steering_angle'])
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']

    # Reward default value
    reward = 1e-3  # Setting a small default reward to encourage staying on the track

    # Reward for staying on track
    if all_wheels_on_track and (0.5 * track_width - distance_from_center) >= 0.05:
        reward = 1.0

        # Additional reward for speed
        reward += (speed ** 2)

        # Penalize for sharp steering angles to encourage smoother driving
        if steering_angle > 15:
            reward *= 0.8

        # Calculate the direction of the next waypoint
        next_point = waypoints[closest_waypoints[1]]
        prev_point = waypoints[closest_waypoints[0]]
        track_direction = (next_point[1] - prev_point[1]) / (next_point[0] - prev_point[0])

        # Calculate the direction the car is facing
        car_direction = params['heading']

        # Reward for heading in the correct direction
        heading_reward = 1.0 - (abs(track_direction - car_direction) / 0.7)

        # Combine rewards
        reward += heading_reward

    return float(reward)
