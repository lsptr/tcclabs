import math
import numpy as np
import matplotlib.pyplot as plt

intervals = [(0, np.pi / 2), (2, 10), (-3, 3)]
steps = [0.01, 0.005, 0.001]

functions = [
    lambda x: np.exp(-x ** 2),
    lambda x: np.sin(3 * x),
    lambda x: np.cos(5 * x) ** 2,
    lambda x: sum([(x ** (2 * n)) / math.factorial(2 * n) for n in range(10)])
]
function_names = ["e^(-x^2)", "sin(3x)", "cos^2(5x)", "sum(x^(2n)/(2n)!"]

for i, func in enumerate(functions):
    fig = plt.figure(figsize=(15, 10))

    for j, interval in enumerate(intervals):
        for k, h in enumerate(steps):
            ax = fig.add_subplot(3, 3, j * 3 + k + 1)

            x = np.arange(interval[0], interval[1] + h, h)
            y = func(x)

            x_orig = np.linspace(interval[0], interval[1], 1000)
            y_orig = func(x_orig)

            ax.plot(x_orig, y_orig, label="Original function", color="black")
            ax.plot(x, y, 'o', label=f"f, h={h}", markersize=2, color="red")

            ax.set_title(f"{function_names[i]} [{interval[0]}, {interval[1]}], h={h}")
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.legend()

    plt.tight_layout()
    plt.show()
