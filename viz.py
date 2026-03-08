import matplotlib.pyplot as plt
import matplotlib.patches as patches
from config import BOUNDS

def render(nodes, threat_pos, threat_r):
    plt.clf()
    plt.xlim(0, BOUNDS[0])
    plt.ylim(0, BOUNDS[1])

    for node in nodes:
        if node['parent']:
            p1 = node['pos']
            p2 = node['parent']['pos']
            plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k-', alpha=0.3)

    circle = patches.Circle(threat_pos, threat_r, color='red', alpha=0.5)
    plt.gca().add_patch(circle)

    plt.plot(0, 0, 'go', label='Start')
    plt.plot(BOUNDS[0]-1, BOUNDS[1]-1, 'bo', label='Goal')

    plt.pause(0.01)
