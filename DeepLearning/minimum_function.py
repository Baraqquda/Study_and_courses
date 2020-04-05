import numpy as np

def num_deriv(func):
    h = 0.1 ** 10
    dx0 = np.array([h, 0.0])
    dx1 = np.array([0.0, h])
    return np.array([(func(minimum + dx0) - func(minimum))/h, (func(minimum + dx1) - func(minimum))/h])
    

def grad_descent(func):
    lr = 1
    eps = 0.1 ** 10
    global minimum
    minimum = np.array([0.0, 0.0])
    for i in np.linspace(-5.5, 5.5, 8):
        for j in np.linspace(-5.5, 5.5, 8):
            point = [i, j]
            step = 0
            while np.linalg.norm(point - minimum) > eps:
                step = step+1
                if step >=10000:
                    break
                minimum = point
                point = minimum - lr * num_deriv(func)
    return minimum
  