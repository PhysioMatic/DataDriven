# For the optimal USER experience adjust the number of 'n' iterations. Try not to exceed the 1B, unless you have a
# very powerful PC with at least 32GB of RAM. Once fractal has been generated you can test its depth by zooming in.
# Enjoy!

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

n = 10000000

x = np.zeros(n)
y = np.zeros(n)

for i in range(n):
    kappa = np.random.randint(1, 4)
    x[i] = x[i - 1] / 2 + kappa - 1
    y[i] = y[i - 1] / 2
    if kappa == 2:
       y[i] += 2

plt.plot(x, y, 'b *', markersize=1)
plt.title('Sierpiński Triangle')
plt.axis('off')
plt.show()