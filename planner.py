import numpy as np

class RRTStar:
    def __init__(self, env, start, goal, max_iter=500, steer_size=1.0, search_radius=3.0):
        self.env = env
        self.start = np.array(start)
        self.goal = np.array(goal)
        self.max_iter = max_iter
        self.steer_size = steer_size
        self.search_radius = search_radius
        self.nodes = [{'pos': self.start, 'parent': None, 'cost': 0}]

    def get_dist(self, n1, n2):
        return np.linalg.norm(n1['pos'] - n2['pos'])

    def plan(self):
        for _ in range(self.max_iter):
            rand_point = np.random.uniform(0, self.env.bounds[0], 2)

            nearest = min(self.nodes, key=lambda n: self.get_dist(n, {'pos': rand_point}))

            direction = rand_point - nearest['pos']
            dist = np.linalg.norm(direction)
            if dist > self.steer_size:
                direction = (direction / dist) * self.steer_size
            new_pos = nearest['pos'] + direction

            if self.env.is_collision(new_pos):
                continue

            near_nodes = [n for n in self.nodes if self.get_dist(n, {'pos': new_pos}) < self.search_radius]
            parent = nearest
            min_cost = nearest['cost'] + self.get_dist(nearest, {'pos': new_pos})

            for n in near_nodes:
                cost = n['cost'] + self.get_dist(n, {'pos': new_pos})
                if cost < min_cost:
                    min_cost = cost
                    parent = n

            new_node = {'pos': new_pos, 'parent': parent, 'cost': min_cost}
            self.nodes.append(new_node)

            for n in near_nodes:
                cost = new_node['cost'] + self.get_dist(n, {'pos': new_pos})
                if cost < n['cost']:
                    n['parent'] = new_node
                    n['cost'] = cost

        return self.nodes
