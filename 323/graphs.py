import numpy as np
import matplotlib.pyplot as plt

plt.figure (figsize = (16, 9), dpi = 200)

# First plot
# x = [25, 21, 19.7, 15.9, 14, 12.9, 10.0, 8.2, 6.1, 5]
# y = [12.6, 10.7, 9.26, 8.18, 7.32, 6.63, 5.16, 4.23, 3.10, 2.37]

#Second plot
x = [19.8, 24.7, 32.7, 48.6, 94.7, 132.2, 179.9, 219.2, 280.9]
y = [21, 20, 18.8, 16.8, 12.6, 10.2, 8.8, 7.9, 6.5]

plt.grid ()

# First plot
# plt.xlabel ("x, см")
# plt.ylabel ("I, мА")

#Second plot
plt.xlabel (r"$(R+R_0)^{-1}, 10^{-6} Ом^{-1}$")
plt.ylabel (r"$l_{max}$, см")

plt.plot (x, y, color = 'blue', linestyle = '-', marker = '+', linewidth = 0.5, markersize = 6, label = 'I(x)')

plt.legend ()

plt.show ()