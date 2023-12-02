# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0, 4 * np.pi, 5)
# labels = map(lambda x: f"{x/np.pi}π", x)
# plt.xticks(x, labels)
# plt.show()
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
x = np.linspace(0, 4 * np.pi, 100)
plt.plot(x, np.sin(x))
plt.gca().xaxis.set_major_locator(MultipleLocator(np.pi))
plt.show()
