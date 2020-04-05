class Neuron:

    def __init__(self, w, f = lambda x: x):
        self.w = w
        self.f = f

    def forward(self, x):
        sum = 0
        self.x = x
        for i in range(len(x)):
              sum = sum + self.w[i] * x[i]
        return self.f(sum)

    def backlog(self):
        return self.x
