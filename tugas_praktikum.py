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

