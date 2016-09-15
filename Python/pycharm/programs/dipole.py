from matplotlib import pyplot as plt
from math import cos, sin, pi, log10
import numpy as np

theta = np.linspace(0, 360, 361)
theta_rad = np.zeros(len(theta))
F_theta = np.zeros(len(theta))
F_theta_dB = np.zeros(len(theta))


for i in range(0, len(theta)):
    theta_rad[i] = theta[i]*pi/180
    if theta[i] == 0 or theta[i] == 360 or theta[i] == 180:
        F_theta[i] = 1e-10
        F_theta_dB[i] = 20*log10(F_theta[i])
    else:
        F_theta[i] = abs(cos(pi/2*cos(theta[i]*pi/180))/sin(theta[i]*pi/180))
        F_theta_dB[i] = 20*log10(F_theta[i])

plt.figure(1, figsize=(14, 6), dpi=80, facecolor='w', edgecolor='k')
ax = plt.subplot(111, polar=True)
ax.set_theta_zero_location('N')
ax.set_theta_direction('clockwise')
ax.plot(theta_rad, F_theta_dB, color='r', linewidth=2)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plt.subplots_adjust(left=0.2, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)
ax.set_xticks(np.pi/180. * np.linspace(180,  -180, 12, endpoint=False))
ax.set_yticks(range(-40, 10, 10))
ax.set_title('dipole radiation pattern', y=1.1)
plt.savefig('dipole_pattern', dpi=200, facecolor='w', edgecolor='k')

plt.figure(2)
plt.plot(theta, F_theta)

plt.show()

# plot.figure(fig_num+n)
# ax = plot.subplot(111, polar=True)
# ax.set_theta_zero_location('N')
# ax.set_theta_direction('clockwise')
# ax.plot(data[1], data[2][0][i], color='r', linewidth=2, label="horizontal pol")
# ax.plot(data[1], data[2][1][i], color='b', linewidth=2, label="vertical pol")
# plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
# plot.subplots_adjust(left=0.2, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)
# ax.set_xticks(np.pi/180. * np.linspace(180,  -180, 12, endpoint=False))
# ax.set_yticks(range(-40, 0, 10))
# ax.set_title('dipole radiation pattern', y=1.1)
# plot.savefig('dipole_pattern', dpi=200, facecolor='w', edgecolor='k')