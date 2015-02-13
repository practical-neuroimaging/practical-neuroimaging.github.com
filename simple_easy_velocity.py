from matplotlib import pyplot as plt
import numpy as np

plt.xkcd()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xticks([])
plt.yticks([])
ax.set_ylim([0, 1.2])

x = np.arange(0, 10, 0.1)
easy = 1 / (1.4 ** x)
simple = 1 - 1 / (1.6 ** x)

plt.plot(x, easy, x, simple)
plt.annotate('easy', xy=(5, 0.25))
plt.annotate('simple', xy=(5, 1))
plt.xlabel('time')
plt.ylabel('velocity')

plt.show()
plt.savefig('simple_easy_velocity.png')
