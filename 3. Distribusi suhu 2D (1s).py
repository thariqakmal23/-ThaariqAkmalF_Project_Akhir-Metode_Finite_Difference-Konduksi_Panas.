import numpy as np
import matplotlib.pyplot as plt

a = 50
panjang = 0.5
waktu = 1
node = 50

dx = panjang / node
dy = panjang / node
dt = min(dx**2 / (4*a), dy**2 / (4 * a))

t_nodes = int(waktu / dt)
u = np.zeros((node, node)) + 20

#Kondisi batas
u[0, :] = np.linspace(100, 0, node)
u[-1, :] = np.linspace(0, 100, node)
u[:, 0] = np.linspace(0, 100, node)
u[:, -1] = np.linspace(0, 100, node)

#Visialisasu distribusi
fig, ax = plt.subplots()
ax.set_ylabel("y (cm)")
ax.set_xlabel("x (cm)")
pcm = ax.pcolormesh(u, cmap=plt.cm.jet, vmin=0, vmax =100)
plt.colorbar(pcm, ax=ax)

counter = 0
w = u.copy()

for i in range(1, node-1):
    for j in range(1, node-1):
        dd_ux = (w[i-1, j] - 2*w[i, j] + w[i+1, j]) / dx**2
        dd_uy = (w[i, j-1] - 2*w[i, j] + w[i, j+1]) / dx**2
        u[i, j] = dt * a * (dd_ux + dd_uy) + w[i,j]

t_mean = np.mean(u)
print(f"t: {counter:.3f} s, Suhu rata-rata: {t_mean:.2f} Celsius")

pcm.set_array(u)
ax.set_title(f"Distribusi Suhu t: {counter:.3f} s, suhu rata-rata={t_mean:.2f}")
plt.show()