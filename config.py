import numpy as np

BOUNDS = (20.0, 20.0)

START_POS = np.array([0.0, 0.0])
GOAL_POS = np.array([19.0, 19.0])

THREAT_VELOCITY = np.array([0.1, 0.05])
THREAT_INIT_POS = np.array([10.0, 10.0])
THREAT_RADIUS = 2.0

MAX_ITERATIONS = 500
STEER_SIZE = 1.0
SEARCH_RADIUS = 3.0
