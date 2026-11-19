# LAPORAN PRAKTIKUM PEMROGRAMAN BERORIENTASI OBJEK
## MODUL 1: KONSEP DASAR OOP

**Program Studi:** S1 Teknik Informatika  
**Institusi:** Sekolah Tinggi Teknologi Bontang (STITEK Bontang)  
**Tanggal:** 17 November 2025 / Revisi 01  

---

## DAFTAR ISI
1. [Praktikum 1: Perbedaan Paradigma Prosedural vs OOP](#praktikum-1-perbedaan-paradigma-prosedural-vs-oop)
2. [Praktikum 2: Konsep Class dan Object](#praktikum-2-konsep-class-dan-object)
3. [Praktikum 3: Constructor dan Atribut](#praktikum-3-constructor-dan-atribut)
4. [Praktikum 4: Instance Methods](#praktikum-4-instance-methods)
5. [Tugas Praktikum: Implementasi Class Mahasiswa](#tugas-praktikum-implementasi-class-mahasiswa)
6. [Panduan Menyimpan Script ke GitHub](#panduan-menyimpan-script-ke-github)

---

## PRAKTIKUM 1: PERBEDAAN PARADIGMA PROSEDURAL VS OOP

### A. Kode Program

#### 1. Pendekatan Prosedural (`prosedural.py`)
```python
# Pendekatan Prosedural
def hitung_luas_persegi(sisi):
    return sisi * sisi

def hitung_keliling_persegi(sisi):
    return 4 * sisi

# Pemanggilan fungsi
sisi = 5
luas = hitung_luas_persegi(sisi)
keliling = hitung_keliling_persegi(sisi)

print(f"Luas persegi: {luas}")
print(f"Keliling persegi: {keliling}")
```

#### 2. Pendekatan OOP (`oop.py`)
```python
# Pendekatan OOP
class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi * self.sisi

    def hitung_keliling(self):
        return 4 * self.sisi

# Pembuatan object
persegi = Persegi(5)
print(f"Luas persegi: {persegi.hitung_luas()}")
print(f"Keliling persegi: {persegi.hitung_keliling()}")
```

### B. Hasil Eksekusi Program (Terminal Output)
```text
PS C:\Users\TUF\Documents\Semester 9\Pemrograman Berorientasi Objek\praktikum> python prosedural.py
Luas persegi: 25
Keliling persegi: 20

PS C:\Users\TUF\Documents\Semester 9\Pemrograman Berorientasi Objek\praktikum> python oop.py
Luas persegi: 25
Keliling persegi: 20
```

### C. Analisis Perbedaan Kedua Pendekatan
| Aspek | Pendekatan Prosedural (`prosedural.py`) | Pendekatan Berorientasi Objek / OOP (`oop.py`) |
| :--- | :--- | :--- |
| **Fokus Utama** | Berpusat pada *urutan langkah/fungsi* (tindakan/prosedur yang harus dilakukan). | Berpusat pada *objek* yang merepresentasikan entitas nyata (menggabungkan data dan perilaku). |
| **Pemisahan Data dan Fungsi** | Data (`sisi = 5`) terpisah secara bebas dari fungsi perhitungannya (`hitung_luas_persegi`). | Data (`sisi`) dan method (`hitung_luas`, `hitung_keliling`) terenkapsulasi di dalam satu kesatuan class `Persegi`. |
| **Akses dan Keamanan Data** | Variabel dapat diakses dan diubah secara bebas oleh fungsi mana pun tanpa proteksi (rawan modifikasi yang tidak diinginkan). | Data tersimpan rapi dalam atribut objek (`self.sisi`) dan diakses melalui method objek tersebut. |
| **Skalabilitas dan Reusabilitas** | Jika program semakin besar dengan banyak bangun datar, fungsi akan bercampur baur dan sulit dikelola (*spaghetti code*). | Sangat modular; mudah diperluas, mendukung pewarisan (*inheritance*), polimorfisme, dan penggunaan ulang kode (*reusability*). |
| **Representasi Dunia Nyata** | Menggambarkan proses matematis atau komputasi step-by-step. | Memodelkan konsep "Persegi" sebagai suatu benda nyata yang memiliki atribut (ukuran sisi) dan kemampuan (menghitung luas/kelilingnya sendiri). |

---

## PRAKTIKUM 2: KONSEP CLASS DAN OBJECT

### A. Contoh Kode (`class_object.py`)
```python
# Contoh Kode: Konsep Class dan Object
class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def perkenalan(self):
        return f"Halo, saya {self.nama} dengan NIM {self.nim}"

# Pembuatan object
mhs1 = Mahasiswa("Budi Santoso", "TI001")
mhs2 = Mahasiswa("Siti Aminah", "TI002")

print(mhs1.perkenalan())
print(mhs2.perkenalan())
```
**Output `class_object.py`:**
```text
Halo, saya Budi Santoso dengan NIM TI001
Halo, saya Siti Aminah dengan NIM TI002
```

### B. Latihan Praktikum: Class Dosen (`latihan_dosen.py`)
**Ketentuan Latihan:**
1. Buat class `Dosen` dengan atribut `nama` dan `nidn`.
2. Tambahkan method `ajar_mata_kuliah()` yang menerima parameter `mata_kuliah`.
3. Instansiasi 2 object dosen dan panggil methodnya.

**Kode Program:**
```python
# Latihan Praktikum 2: Konsep Class dan Object
class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def ajar_mata_kuliah(self, mata_kuliah):
        return f"Dosen {self.nama} (NIDN: {self.nidn}) sedang mengajar mata kuliah {mata_kuliah}."

# Instansiasi 2 object dosen
dosen1 = Dosen("Dr. Ir. Hendra Wijaya, M.Kom.", "0912057801")
dosen2 = Dosen("Sari Lestari, S.Kom., M.T.", "0925088502")

# Pemanggilan method
print(dosen1.ajar_mata_kuliah("Pemrograman Berorientasi Objek"))
print(dosen2.ajar_mata_kuliah("Struktur Data dan Algoritma"))
```

### C. Hasil Eksekusi Program
```text
PS C:\Users\TUF\Documents\Semester 9\Pemrograman Berorientasi Objek\praktikum> python latihan_dosen.py
Dosen Dr. Ir. Hendra Wijaya, M.Kom. (NIDN: 0912057801) sedang mengajar mata kuliah Pemrograman Berorientasi Objek.
Dosen Sari Lestari, S.Kom., M.T. (NIDN: 0925088502) sedang mengajar mata kuliah Struktur Data dan Algoritma.
```

---

## PRAKTIKUM 3: CONSTRUCTOR DAN ATRIBUT

### A. Contoh Kode (`constructor_atribut.py`)
```python
# Contoh Kode: Constructor dan Atribut
class Buku:
    # Class attribute
    perpustakaan = "Perpustakaan STITEK"

    # Constructor
    def __init__(self, judul, penulis, tahun):
        # Instance attributes
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def info_buku(self):
        return f"Buku {self.judul} oleh {self.penulis} ({self.tahun})"

# Instansiasi object
buku1 = Buku("Pemrograman Python", "John Doe", 2023)
buku2 = Buku("Struktur Data", "Jane Doe", 2022)

print(buku1.info_buku())
print(buku2.info_buku())
print(f"Lokasi: {Buku.perpustakaan}")
```
**Output `constructor_atribut.py`:**
```text
Buku Pemrograman Python oleh John Doe (2023)
Buku Struktur Data oleh Jane Doe (2022)
Lokasi: Perpustakaan STITEK
```

### B. Latihan Praktikum: Class Kendaraan (`latihan_kendaraan.py`)
**Ketentuan Latihan:**
1. Buat class `Kendaraan` dengan class attribute `bahan_bakar`.
2. Gunakan constructor untuk inisialisasi `merk`, `warna`, dan `tahun`.
3. Demonstrasikan perbedaan akses instance attribute dan class attribute.

**Kode Program:**
```python
# Latihan Praktikum 3: Constructor dan Atribut
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
```

### C. Hasil Eksekusi Program
```text
PS C:\Users\TUF\Documents\Semester 9\Pemrograman Berorientasi Objek\praktikum> python latihan_kendaraan.py
=== 1. Informasi Masing-Masing Objek ===
Kendaraan: Toyota Avanza | Warna: Hitam | Tahun: 2021
Kendaraan: Honda Vario | Warna: Merah | Tahun: 2023

=== 2. Akses Instance Attribute ===
Merk Mobil : Toyota Avanza
Warna Mobil: Hitam
Tahun Mobil: 2021
Merk Motor : Honda Vario
Warna Motor: Merah
Tahun Motor: 2023

=== 3. Akses Class Attribute ===
Akses via Class (Kendaraan.bahan_bakar) : Bensin
Akses via Objek mobil (mobil.bahan_bakar): Bensin
Akses via Objek motor (motor.bahan_bakar): Bensin

=== 4. Demonstrasi Perbedaan Perubahan Nilai ===
--> Mengubah Kendaraan.bahan_bakar menjadi 'Pertamax'
Kendaraan.bahan_bakar : Pertamax
mobil.bahan_bakar     : Pertamax
motor.bahan_bakar     : Pertamax

--> Mengubah bahan_bakar khusus pada objek mobil menjadi 'Solar'
mobil.bahan_bakar     : Solar (instance override)
motor.bahan_bakar     : Pertamax (tetap mengikuti class attribute)
Kendaraan.bahan_bakar : Pertamax (class attribute tidak berubah)
```

---

## PRAKTIKUM 4: INSTANCE METHODS

### A. Contoh Kode (`instance_methods.py`)
```python
# Contoh Kode: Instance Methods
class BankAccount:
    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.saldo = saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
            return f"Berhasil setor {jumlah}. Saldo: {self.saldo}"
        return "Jumlah setor harus positif"

    def tarik(self, jumlah):
        if 0 < jumlah <= self.saldo:
            self.saldo -= jumlah
            return f"Berhasil tarik {jumlah}. Saldo: {self.saldo}"
        return "Saldo tidak mencukupi"

    def info_saldo(self):
        return f"Saldo {self.pemilik}: {self.saldo}"

# Testing
akun = BankAccount("Alice", 1000)
print(akun.setor(500))
print(akun.tarik(200))
print(akun.info_saldo())
```
**Output `instance_methods.py`:**
```text
Berhasil setor 500. Saldo: 1500
Berhasil tarik 200. Saldo: 1300
Saldo Alice: 1300
```

### B. Latihan Praktikum: Class ManajerInventori (`latihan_inventori.py`)
**Ketentuan Latihan:**
1. Buat class `ManajerInventori` dengan methods: `tambah_barang`, `hapus_barang`, `lihat_inventori`.
2. Implementasikan penambahan dan pengurangan stok barang (`kurangi_stok`).
3. Demonstrasikan seluruh method yang telah dibuat.

**Kode Program:**
```python
# Latihan Praktikum 4: Instance Methods
class ManajerInventori:
    def __init__(self):
        # Menyimpan barang dalam bentuk dictionary {nama_barang: jumlah_stok}
        self.inventori = {}

    def tambah_barang(self, nama, jumlah):
        if jumlah <= 0:
            return f"[Gagal] Jumlah penambahan barang '{nama}' harus lebih dari 0."
        
        if nama in self.inventori:
            self.inventori[nama] += jumlah
            return f"[Sukses] Stok barang '{nama}' berhasil ditambah {jumlah}. Total stok sekarang: {self.inventori[nama]}."
        else:
            self.inventori[nama] = jumlah
            return f"[Sukses] Barang baru '{nama}' berhasil ditambahkan dengan stok {jumlah}."

    def kurangi_stok(self, nama, jumlah):
        if nama not in self.inventori:
            return f"[Gagal] Barang '{nama}' tidak ditemukan di dalam inventori."
        
        if jumlah <= 0:
            return f"[Gagal] Jumlah pengurangan barang '{nama}' harus lebih dari 0."
        
        if self.inventori[nama] < jumlah:
            return f"[Gagal] Stok barang '{nama}' tidak mencukupi (Tersedia: {self.inventori[nama]}, Diminta: {jumlah})."
        
        self.inventori[nama] -= jumlah
        return f"[Sukses] Stok barang '{nama}' berhasil dikurangi {jumlah}. Sisa stok sekarang: {self.inventori[nama]}."

    def hapus_barang(self, nama):
        if nama in self.inventori:
            del self.inventori[nama]
            return f"[Sukses] Barang '{nama}' berhasil dihapus dari inventori."
        return f"[Gagal] Barang '{nama}' tidak ditemukan di dalam inventori."

    def lihat_inventori(self):
        print("\n--- DAFTAR INVENTORI BARANG ---")
        if not self.inventori:
            print("Inventori kosong.")
        else:
            for nama, stok in self.inventori.items():
                print(f"- {nama}: {stok} unit")
        print("-------------------------------\n")


# Demonstrasi Penggunaan Method
toko = ManajerInventori()

print("=== 1. Menambahkan Barang ke Inventori ===")
print(toko.tambah_barang("Laptop Asus", 10))
print(toko.tambah_barang("Mouse Logitech", 25))
print(toko.tambah_barang("Keyboard Mechanical", 15))
toko.lihat_inventori()

print("=== 2. Menambah Stok Barang yang Sudah Ada ===")
print(toko.tambah_barang("Laptop Asus", 5))
toko.lihat_inventori()

print("=== 3. Mengurangi Stok Barang ===")
print(toko.kurangi_stok("Mouse Logitech", 10))
# Uji coba stok tidak mencukupi
print(toko.kurangi_stok("Keyboard Mechanical", 20))
toko.lihat_inventori()

print("=== 4. Menghapus Barang dari Inventori ===")
print(toko.hapus_barang("Mouse Logitech"))
# Uji coba hapus barang yang sudah tidak ada
print(toko.hapus_barang("Mouse Logitech"))
toko.lihat_inventori()
```

### C. Hasil Eksekusi Program
```text
PS C:\Users\TUF\Documents\Semester 9\Pemrograman Berorientasi Objek\praktikum> python latihan_inventori.py
=== 1. Menambahkan Barang ke Inventori ===
[Sukses] Barang baru 'Laptop Asus' berhasil ditambahkan dengan stok 10.
[Sukses] Barang baru 'Mouse Logitech' berhasil ditambahkan dengan stok 25.
[Sukses] Barang baru 'Keyboard Mechanical' berhasil ditambahkan dengan stok 15.

--- DAFTAR INVENTORI BARANG ---
- Laptop Asus: 10 unit
- Mouse Logitech: 25 unit
- Keyboard Mechanical: 15 unit
-------------------------------

=== 2. Menambah Stok Barang yang Sudah Ada ===
[Sukses] Stok barang 'Laptop Asus' berhasil ditambah 5. Total stok sekarang: 15.

--- DAFTAR INVENTORI BARANG ---
- Laptop Asus: 15 unit
- Mouse Logitech: 25 unit
- Keyboard Mechanical: 15 unit
-------------------------------

=== 3. Mengurangi Stok Barang ===
[Sukses] Stok barang 'Mouse Logitech' berhasil dikurangi 10. Sisa stok sekarang: 15.
[Gagal] Stok barang 'Keyboard Mechanical' tidak mencukupi (Tersedia: 15, Diminta: 20).

--- DAFTAR INVENTORI BARANG ---
- Laptop Asus: 15 unit
- Mouse Logitech: 15 unit
- Keyboard Mechanical: 15 unit
-------------------------------

=== 4. Menghapus Barang dari Inventori ===
[Sukses] Barang 'Mouse Logitech' berhasil dihapus dari inventori.
[Gagal] Barang 'Mouse Logitech' tidak ditemukan di dalam inventori.

--- DAFTAR INVENTORI BARANG ---
- Laptop Asus: 15 unit
- Keyboard Mechanical: 15 unit
-------------------------------
```

---

## TUGAS PRAKTIKUM: IMPLEMENTASI CLASS MAHASISWA

### A. Ketentuan Tugas
1. **Class**: `Mahasiswa`
2. **Atribut**:
   - *Instance attributes*: `nama`, `nim`, `jurusan`, `ipk`
   - *Class attribute*: `universitas = "STITEK Bontang"`
3. **Methods**:
   - `__init__(self, nama, nim, jurusan, ipk=0.0)`
   - `perkenalan_diri(self)`
   - `update_ipk(self, ipk_baru)` (dilengkapi validasi 0.0 - 4.0)
   - `predikat_kelulusan(self)`:
     - IPK $\ge$ 3.5 : "Cum Laude"
     - IPK $\ge$ 3.0 : "Sangat Memuaskan"
     - IPK $\ge$ 2.5 : "Memuaskan"
     - IPK $\ge$ 2.0 : "Lulus"
4. **Instansiasi & Demonstrasi**:
   - Membuat 3 objek mahasiswa dengan data berbeda.
   - Mendemonstrasikan seluruh method yang tersedia.

### B. Kode Program (`tugas_praktikum.py`)
```python
# ==============================================================================
# SEKOLAH TINGGI TEKNOLOGI BONTANG (STITEK)
# PROGRAM STUDI TEKNIK INFORMATIKA
# Praktikum : Pemrograman Berorientasi Objek (PBO)
# Modul 1   : Konsep Dasar OOP
# File      : tugas_praktikum.py
# ==============================================================================

class Mahasiswa:
    # 2.b. Class Attribute (berlaku untuk seluruh mahasiswa di institusi ini)
    universitas = "STITEK Bontang"

    # 3.a. Constructor (__init__) dengan default argument ipk=0.0
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        # 2.a. Instance Attributes
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = float(ipk)

    # 3.b. Method perkenalan_diri
    def perkenalan_diri(self):
        return (
            f"Halo, saya {self.nama} (NIM: {self.nim}), "
            f"mahasiswa program studi {self.jurusan} di {Mahasiswa.universitas} "
            f"dengan IPK saat ini {self.ipk:.2f}."
        )

    # 3.c. Method update_ipk
    def update_ipk(self, ipk_baru):
        if 0.0 <= ipk_baru <= 4.0:
            ipk_lama = self.ipk
            self.ipk = float(ipk_baru)
            return (
                f"[SUKSES] IPK mahasiswa {self.nama} ({self.nim}) berhasil diperbarui: "
                f"{ipk_lama:.2f} -> {self.ipk:.2f}."
            )
        else:
            return (
                f"[GAGAL] Nilai IPK {ipk_baru} tidak valid. "
                f"IPK harus berada pada rentang 0.0 hingga 4.0."
            )

    # 3.d. Method predikat_kelulusan
    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        else:
            return "Belum Memenuhi Syarat Kelulusan"


# ==============================================================================
# 4. INSTANSIASI & DEMONSTRASI METHOD
# ==============================================================================
if __name__ == "__main__":
    print("=" * 70)
    print("           DEMONSTRASI TUGAS PRAKTIKUM MODUL 1 - OOP          ")
    print(f"                   Universitas: {Mahasiswa.universitas}        ")
    print("=" * 70)

    # 4.a. Membuat 3 objek Mahasiswa dengan data berbeda
    mhs1 = Mahasiswa("Budi Santoso", "21001001", "Teknik Informatika", 3.75)
    mhs2 = Mahasiswa("Siti Aminah", "21001002", "Teknik Informatika", 3.25)
    mhs3 = Mahasiswa("Rizky Pratama", "21002005", "Sistem Informasi", 2.30)

    daftar_mahasiswa = [mhs1, mhs2, mhs3]

    # 4.b. Demonstrasi Method perkenalan_diri dan predikat_kelulusan
    print("\n--- 1. Perkenalan Diri & Predikat Kelulusan Awal ---")
    for i, mhs in enumerate(daftar_mahasiswa, 1):
        print(f"\n[Mahasiswa {i}]")
        print(mhs.perkenalan_diri())
        print(f"Predikat Kelulusan: {mhs.predikat_kelulusan()}")

    # 4.b. Demonstrasi Method update_ipk
    print("\n" + "=" * 70)
    print("--- 2. Demonstrasi Pembaruan IPK (update_ipk) ---")
    print("=" * 70)

    # Update IPK Mahasiswa 3 (dari 2.30 menjadi 2.85)
    print(f"\nStatus sebelum update: {mhs3.nama} memiliki IPK {mhs3.ipk:.2f} ({mhs3.predikat_kelulusan()})")
    print(mhs3.update_ipk(2.85))
    print(f"Status setelah update : {mhs3.nama} memiliki IPK {mhs3.ipk:.2f} ({mhs3.predikat_kelulusan()})")

    # Update IPK Mahasiswa 2 (dari 3.25 menjadi 3.65)
    print(f"\nStatus sebelum update: {mhs2.nama} memiliki IPK {mhs2.ipk:.2f} ({mhs2.predikat_kelulusan()})")
    print(mhs2.update_ipk(3.65))
    print(f"Status setelah update : {mhs2.nama} memiliki IPK {mhs2.ipk:.2f} ({mhs2.predikat_kelulusan()})")

    # Pengujian validasi input tidak valid
    print("\nPengujian Validasi Nilai IPK Tidak Valid:")
    print(mhs1.update_ipk(4.50))
    print(mhs1.update_ipk(-1.00))

    # Ringkasan Akhir
    print("\n" + "=" * 70)
    print("--- 3. Ringkasan Data Akhir Seluruh Mahasiswa ---")
    print("=" * 70)
    for mhs in daftar_mahasiswa:
        print(f"- {mhs.nama} ({mhs.nim}) | IPK: {mhs.ipk:.2f} | Predikat: {mhs.predikat_kelulusan()}")
    print("=" * 70)
```

### C. Hasil Eksekusi Program (Terminal Output)
```text
PS C:\Users\TUF\Documents\Semester 9\Pemrograman Berorientasi Objek\praktikum> python tugas_praktikum.py
======================================================================
           DEMONSTRASI TUGAS PRAKTIKUM MODUL 1 - OOP          
                   Universitas: STITEK Bontang        
======================================================================

--- 1. Perkenalan Diri & Predikat Kelulusan Awal ---

[Mahasiswa 1]
Halo, saya Budi Santoso (NIM: 21001001), mahasiswa program studi Teknik Informatika di STITEK Bontang dengan IPK saat ini 3.75.
Predikat Kelulusan: Cum Laude

[Mahasiswa 2]
Halo, saya Siti Aminah (NIM: 21001002), mahasiswa program studi Teknik Informatika di STITEK Bontang dengan IPK saat ini 3.25.
Predikat Kelulusan: Sangat Memuaskan

[Mahasiswa 3]
Halo, saya Rizky Pratama (NIM: 21002005), mahasiswa program studi Sistem Informasi di STITEK Bontang dengan IPK saat ini 2.30.
Predikat Kelulusan: Lulus

======================================================================
--- 2. Demonstrasi Pembaruan IPK (update_ipk) ---
======================================================================

Status sebelum update: Rizky Pratama memiliki IPK 2.30 (Lulus)
[SUKSES] IPK mahasiswa Rizky Pratama (21002005) berhasil diperbarui: 2.30 -> 2.85.
Status setelah update : Rizky Pratama memiliki IPK 2.85 (Memuaskan)

Status sebelum update: Siti Aminah memiliki IPK 3.25 (Sangat Memuaskan)
[SUKSES] IPK mahasiswa Siti Aminah (21001002) berhasil diperbarui: 3.25 -> 3.65.
Status setelah update : Siti Aminah memiliki IPK 3.65 (Cum Laude)

Pengujian Validasi Nilai IPK Tidak Valid:
[GAGAL] Nilai IPK 4.5 tidak valid. IPK harus berada pada rentang 0.0 hingga 4.0.
[GAGAL] Nilai IPK -1.0 tidak valid. IPK harus berada pada rentang 0.0 hingga 4.0.

======================================================================
--- 3. Ringkasan Data Akhir Seluruh Mahasiswa ---
======================================================================
- Budi Santoso (21001001) | IPK: 3.75 | Predikat: Cum Laude
- Siti Aminah (21001002) | IPK: 3.65 | Predikat: Cum Laude
- Rizky Pratama (21002005) | IPK: 2.85 | Predikat: Memuaskan
======================================================================
```

### D. Analisis Struktur dan Logika Program Tugas Praktikum
1. **Struktur Class dan Atribut**:
   - `universitas = "STITEK Bontang"` didefinisikan di luar method sebagai *Class Attribute*. Hal ini memastikan bahwa seluruh mahasiswa berbagi atribut asal kampus yang sama tanpa perlu menduplikasikannya di setiap instance memory objek.
   - `nama`, `nim`, `jurusan`, dan `ipk` didefinisikan dalam constructor `__init__` sebagai *Instance Attributes* menggunakan `self.nama`, `self.nim`, dst., sehingga setiap mahasiswa dapat menyimpan nilai identitas yang unik dan independen.
2. **Implementasi Methods**:
   - `perkenalan_diri`: Mengakses atribut objek secara terenkapsulasi dan merangkainya menjadi teks informasi identitas mahasiswa.
   - `update_ipk`: Menerapkan validasi rentang angka IPK (0.0 hingga 4.0). Fitur enkapsulasi ini mencegah pengubahan state atribut objek menjadi nilai yang tidak logis (misalnya nilai minus atau lebih dari 4.0).
   - `predikat_kelulusan`: Mengevaluasi atribut `self.ipk` dengan percabangan bertingkat sesuai ambang batas nilai yang ditentukan di modul, menghasilkan status akademik secara dinamis.
3. **Instansiasi Objek**:
   - Dibuat tiga objek berbeda: `mhs1` (IPK 3.75 - Cum Laude), `mhs2` (IPK 3.25 - Sangat Memuaskan), dan `mhs3` (IPK 2.30 - Lulus).
   - Saat method `update_ipk` dijalankan pada objek `mhs3` dan `mhs2`, pembaruan nilai tercatat secara langsung dan method `predikat_kelulusan()` secara otomatis menyesuaikan predikat terbarunya ("Memuaskan" dan "Cum Laude").

---

## PANDUAN MENYIMPAN SCRIPT KE GITHUB

Untuk memenuhi instruksi *"Simpan script di github anda masing-masing"*, berikut langkah-langkah yang dapat dijalankan di terminal:

1. **Buka Terminal di folder praktikum:**
   ```bash
   cd "c:\Users\TUF\Documents\Semester 9\Pemrograman Berorientasi Objek\praktikum"
   ```

2. **Inisialisasi Git Repository:**
   ```bash
   git init
   ```

3. **Tambahkan semua file ke staging area:**
   ```bash
   git add .
   ```

4. **Lakukan commit:**
   ```bash
   git commit -m "feat: Selesaikan Modul 1 Konsep Dasar OOP STITEK Bontang"
   ```

5. **Hubungkan ke repository GitHub Anda:**
   *(Ganti URL di bawah dengan URL repository GitHub Anda)*
   ```bash
   git branch -M main
   git remote add origin https://github.com/USERNAME-ANDA/NAMA-REPO-ANDA.git
   git push -u origin main
   ```

