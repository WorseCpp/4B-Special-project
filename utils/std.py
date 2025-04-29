import numpy as np
import matplotlib.pyplot as plt

c = [.1, 1.0, 10.0]
a = [13899, 25465, 158013]

p = np.polyfit(c, a, 1)

x = np.linspace(0, 10, 100)
y = np.polyval(p, x)

plt.plot(c, a, 'o', label='data')
plt.plot(x, y, label='fit')
plt.xlabel('Conc (ppm)')
plt.ylabel('Emission (a.u.)')
plt.title('Emission vs Concentration (R^2 = 0.9999)')
plt.legend()
plt.grid()
plt.show()