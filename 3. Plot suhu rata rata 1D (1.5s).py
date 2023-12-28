import numpy as np
import matplotlib.pyplot as plt

# Mendefinisikan Variabel
a = 500  # Koefisien Difusivitas Termal [m^2/s]
panjang = 2.5  # Panjang plat [m]
waktu = 1.5  # Waktu simulasi [s]
node = 2.5  # Jumlah titik grid

dx = panjang / node  # Jarak antar titik grid [m]
dt = 0.5 * dx ** 2 / a  # Ukuran waktu simulasi [s]
t_n = int(waktu / dt)  # Jumlah iterasi simulasi
u = np.zeros(node) + 20  # Suhu awal plat [degC]

# Kondisi Batas
u[0] = 0  # Suhu ujung kiri plat [degC]
u[-1] = 100  # Suhu ujung kanan plat [degC]

# Inisialisasi waktu iterasi
counter = 0.001  # Mulai dari 0.001 detik
iteration_step = 50  # Setiap 50 iterasi
time_step = iteration_step * dt  # Waktu antara setiap iterasi

# Simulasi
time = []  # List untuk menyimpan waktu
mean_temperatures = []  # List untuk menyimpan suhu rata-rata
for i in range(t_n):
    w = u.copy()  # Menyalin data suhu untuk perhitungan
    for j in range(1, node - 1):  # Melooping setiap titik grid kecuali batas
        u[j] = (dt * a * (w[j - 1] - 2 * w[j] + w[j + 1]) / dx ** 2) + w[j]  # Perhitungan
    
    # Mencetak suhu rata-rata setiap 50 iterasi
    if (i + 1) % iteration_step == 0:
        time.append(counter)
        mean_temperatures.append(np.mean(u))
    
    counter += dt  # Menambah waktu simulasi

    if counter > waktu:  # Berhenti jika sudah mencapai waktu simulasi
        break

# Plot suhu rata-rata terhadap waktu
plt.figure()
plt.plot(mean_temperatures, time, marker='o')
plt.xlabel('Suhu Rata-rata (Celcius)')
plt.ylabel('Waktu (s)')
plt.title('Suhu Rata-rata terhadap Waktu')
plt.grid(True)
plt.show()
