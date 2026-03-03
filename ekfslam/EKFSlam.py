
import numpy as np 

"""
Implementation of the ekf slam algorithm
"""
class EKFSlam: 
    
    def __init__(self, vehicle, Q, R): 
        self.state = np.empty(3) # state
        self.state_covariance = np.diag([100, 100, 100])
        self.vehicle = vehicle
        self.last_predicted_timestamp = 0
        self.last_updated_timestamp = 0 
        self.num_observed_landmarks = 0
        self.known_landmarks = {}

        self.R = R
        self.Q = Q

    def predict(self, inputs, timestamp):
        # Update State
        dt = timestamp - self.last_predicted_timestamp
        self.last_predicted_timestamp = timestamp

        v = self.vehicle.v
        omega = self.vehicle.omega
        theta = self.state[2]

        self.state = self.h(inputs, timestamp) 
        self.Fx = np.eye(3, 3 + 2 * self.num_observed_landmarks)

        h = np.array([
            -(v/omega) * np.sin(theta) + (v/omega) * np.sin(theta + omega * dt),
            (v/omega) * np.cos(theta) - (v/omega) * np.cos(theta + omega * dt),
            omega * dt 
        ])

        self.state = self.state + self.Fx.T * h

        # Compute Jacobian and update state covariance
        Gx = np.eye(3)
        Gx[0][2] = -(v/omega) * np.cos(theta) + (v/omega) * np.cos(theta + omega * dt)
        Gx[1][2] = -(v/omega) * np.sin(theta) + (v/omega) * np.sin(theta + omega * dt)
        I = np.eye(self.num_observed_landmarks)

        G = np.block(Gx, I)

        self.state_covariance = G @ self.state_covariance @ G.T + self.R
        
    def update(self, observed_landmarks):
        """
        Performs an update; for now observed_landmarks is just a dict that maps labels --> (range, bearing) tuples
        """
        for landmark_label in observed_landmarks: 
            if landmark_label not in observed_landmarks: 
                # TODO fix indexing
                landmark_num = observed_landmarks[landmark_num]
                landmark_index = 3 + 2 * self.num_observed_landmarks
                self.state[landmark_index] = landmark[0] * np.cos(landmark[1] + self.state[2])
                self.state[landmark_index + 1] = landmark[0] * np.sin(landmark[1] + self.state[2])

            landmark = [67, 67] # TODO goon

            delta = np.array([
                landmark[0] - self.state[0],
                landmark[1] - self.state[1]
            ])

            q = delta.T @ delta
            
            z = np.array([
                np.sqrt(q), 
                np.atan2(delta[1], delta[0]) - self.state[2]
            ])
            


            

            
            
        

