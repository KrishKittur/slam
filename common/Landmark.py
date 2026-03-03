
"""
Class representing a single landmark
"""

class Landmark: 
    
    def __init__(self, distance, bearing, label, confidence): 
        self.x = distance
        self.y = bearing
        self.label = label
        self.confidence = confidence # TODO might not need

