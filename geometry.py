import numpy as np

class Environment:
    def __init__(self, bounds):
        self.bounds = bounds
        self.threats = []

    def update_threats(self, threat_list):
        """updates the list of active threats.
        threat_list should be a list of dictionaries: {'pos': np.array, 'r': float}"""
        self.threats = threat_list

    def is_collision(self, point):
        """checks if a point is within any threat radius.
        Returns True if collision detected"""
        if not (0 <= point[0] <= self.bounds[0] and 0 <= point[1] <= self.bounds[1]):
            return True

        for threat in self.threats:
            if np.linalg.norm(point - threat['pos']) < threat['r']:
                return True
        return False
