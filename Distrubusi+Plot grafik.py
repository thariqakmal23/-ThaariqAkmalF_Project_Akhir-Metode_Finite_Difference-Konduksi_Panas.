import numpy as np
import matplotlib.pyplot as plt

# Mendefinisikan Variabel
a = 50  # Koefisien Difusivitas Termal
panjang = 0.5  # Panjang plat [mm]
waktu = 1.5  # Waktu simulasi [s]
node = 50  # Jumlah titik grid

dx = panjang / node  # Jarak antar titik grid pada x [mm]
dy = panjang / node  # Jarak antar titik grid pada y [mm]
dt = min(dx**2 / (4 * a), dy**2 / (4 * a))  # Ukuran langkah waktu [s] (pilih yang,→ lebih kecil agar stabil)
t_nodes = int(waktu / dt)  # Jumlah iterasi simulasi
u = np.zeros((node, node)) + 20  # Suhu awal plat [ degC ] (2 dimensi )

# Kondisi batas
u[0, :] = 0  # Suhu tepi kiri ( variasi linear )
u[-1, :] = 100  # Suhu tepi kanan ( variasi linear )
u[:, 0] = np.linspace(0, 100, node)  # Suhu tepi bawah ( variasi linear )
u[:, -1] = np.linspace(0, 100, node)  # Suhu tepi atas ( variasi linear )

# Visualisasi distribusi suhu awal
fig, ax = plt.subplots()
ax.set_ylabel("y (cm)")
ax.set_xlabel("x (cm)")
pcm = ax.pcolormesh(u, cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm, ax=ax)
plt.ion()  # Mode interaktif

# Kumpulkan data untuk plot suhu rata-rata terhadap waktu
langkah_waktu = []
suhu_rata_rata = []

update_interval = 10
for counter in range(int(waktu / dt)):
    w = u.copy()  # Menyalin data suhu untuk perhitungan
    # Looping setiap titik grid kecuali batas
    dd_ux = (w[:-2, 1:-1] - 2 * w[1:-1, 1:-1] + w[2:, 1:-1]) / dx**2
    dd_uy = (w[1:-1, :-2] - 2 * w[1:-1, 1:-1] + w[1:-1, 2:]) / dy**2
    u[1:-1, 1:-1] = dt * a * (dd_ux + dd_uy) + w[1:-1, 1:-1]

    if counter % update_interval == 0:
        pcm.set_array(u)
        t_mean = np.mean(u)
        langkah_waktu.append(counter * dt)
        suhu_rata_rata.append(t_mean)
        print(f"t: {counter * dt:.3f} s, Suhu rata - rata : {t_mean:.2f} Celcius ")
        ax.set_title(f" Distribusi Suhu t: {counter * dt:.3f} s, suhu rata - rata ={t_mean:.3f}")
        if counter % (10 * update_interval) == 0:
            plt.draw()
            plt.pause(0.01)

# Plot suhu rata-rata terhadap waktu
fig, ax = plt.subplots()
ax.plot(langkah_waktu, suhu_rata_rata, label="Suhu Rata-Rata")
ax.set_xlabel("Waktu (s)")
ax.set_ylabel("Suhu Rata-Rata (Celcius)")
ax.legend()
ax.set_title("Plot Suhu Rata-Rata Terhadap Waktu")

# Simpan kedua plot sebagai gambar
fig.savefig("distribusi_suhu.png")
fig, ax = plt.subplots()
ax.plot(langkah_waktu, suhu_rata_rata, label="Suhu Rata-Rata")
ax.set_xlabel("Waktu (s)")
ax.set_ylabel("Suhu Rata-Rata (Celcius)")
ax.legend()
ax.set_title("Plot Suhu Rata-Rata Terhadap Waktu")
fig.savefig("plot_grafik.png")
plt.show()
