# Latihan Praktikum 3: Constructor dan Atribut
# Class Kendaraan dengan class attribute bahan_bakar dan instance attributes (merk, warna, tahun)

class Kendaraan:
    # Class attribute: berlaku untuk seluruh instance dari class Kendaraan
    bahan_bakar = "Bensin"

    # Constructor untuk inisialisasi instance attributes
    def __init__(self, merk, warna, tahun):
        # Instance attributes: unik untuk setiap objek kendaraan
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def info_kendaraan(self):
        return f"Kendaraan: {self.merk} | Warna: {self.warna} | Tahun: {self.tahun}"


# Instansiasi objek
mobil = Kendaraan("Toyota Avanza", "Hitam", 2021)
motor = Kendaraan("Honda Vario", "Merah", 2023)

print("=== 1. Informasi Masing-Masing Objek ===")
print(mobil.info_kendaraan())
print(motor.info_kendaraan())

print("\n=== 2. Akses Instance Attribute ===")
# Instance attribute hanya dapat diakses melalui objeknya masing-masing
print(f"Merk Mobil : {mobil.merk}")
print(f"Warna Mobil: {mobil.warna}")
print(f"Tahun Mobil: {mobil.tahun}")
print(f"Merk Motor : {motor.merk}")
print(f"Warna Motor: {motor.warna}")
print(f"Tahun Motor: {motor.tahun}")

print("\n=== 3. Akses Class Attribute ===")
# Class attribute dapat diakses langsung via nama Class maupun via instance objek
print(f"Akses via Class (Kendaraan.bahan_bakar) : {Kendaraan.bahan_bakar}")
print(f"Akses via Objek mobil (mobil.bahan_bakar): {mobil.bahan_bakar}")
print(f"Akses via Objek motor (motor.bahan_bakar): {motor.bahan_bakar}")

print("\n=== 4. Demonstrasi Perbedaan Perubahan Nilai ===")
# Mengubah class attribute dari Class berdampak ke semua instance
print("--> Mengubah Kendaraan.bahan_bakar menjadi 'Pertamax'")
Kendaraan.bahan_bakar = "Pertamax"
print(f"Kendaraan.bahan_bakar : {Kendaraan.bahan_bakar}")
print(f"mobil.bahan_bakar     : {mobil.bahan_bakar}")
print(f"motor.bahan_bakar     : {motor.bahan_bakar}")

# Mengubah attribute pada level objek hanya akan membuat attribute lokal pada objek tersebut
print("\n--> Mengubah bahan_bakar khusus pada objek mobil menjadi 'Solar'")
mobil.bahan_bakar = "Solar"
print(f"mobil.bahan_bakar     : {mobil.bahan_bakar} (instance override)")
print(f"motor.bahan_bakar     : {motor.bahan_bakar} (tetap mengikuti class attribute)")
print(f"Kendaraan.bahan_bakar : {Kendaraan.bahan_bakar} (class attribute tidak berubah)")

