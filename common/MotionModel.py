import numpy as np

"""
This class represents the vehicle in terms of standard robot coordinates. 
It includes a basic bicycle motion model 
"""
class Vehicle: 

    def __init__(self, start_x, start_y, start_v, start_psi, start_omega, start_delta):
        self.x = start_x
        self.y = start_y
        self.v = start_v
        self.psi = start_psi
        self.omega = start_omega
        self.delta = start_delta

    def update_with_mm(self, v, delta, dt): 
        """
        Applies an odometry update
        """
        self.delta = delta
        self.v = v
        self.omega = v * np.tan(self.delta) * dt
        self.psi = self.psi + self.omega * dt
        self.x = self.x + v * np.cos(self.psi) * dt
        self.y = self.y + v * np.sin(self.psi) * dt





