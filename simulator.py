import numpy as np
from config import *
from geometry import Environment
from planner import RRTStar

class Simulator:
    def __init__(self):
        self.env = Environment(BOUNDS)
        self.threat_pos = THREAT_INIT_POS
        self.threat_vel = THREAT_VELOCITY

    def run_step(self):
        self.threat_pos += self.threat_vel

        self.env.update_threats([{'pos': self.threat_pos, 'r': THREAT_RADIUS}])

        planner = RRTStar(self.env, START_POS, GOAL_POS, MAX_ITERATIONS, STEER_SIZE, SEARCH_RADIUS)
        return planner.plan(), self.threat_pos
