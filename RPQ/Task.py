class Task:
    def __init__(self, r, p, q, id):
        self.id = int(id)
        self.r = int(r)
        self.p = int(p)
        self.q = int(q)

    def __repr__(self):
        return f"Task {self.id}:r={self.r}, p={self.p}, q={self.q}   "

    def get_r(self):
        return self.r

    def get_p(self):
        return self.p

    def get_q(self):
        return self.q