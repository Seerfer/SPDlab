class Task:
    def __init__(self, r, p, q, id):
        self.id = int(id)
        self.r = int(r)
        self.p = int(p)
        self.q = int(q)

    def __repr__(self):
        return f"Task {self.id}:r={self.r}, p={self.p}, q={self.q}   "
