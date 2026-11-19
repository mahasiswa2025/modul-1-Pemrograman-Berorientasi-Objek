# Contoh Kode: Konsep Class dan Object
class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def perkenalan(self):
        return f"Halo, saya {self.nama} dengan NIM {self.nim}"

# Pembuatan object
mhs1 = Mahasiswa("Yudha Achmad", "202212056")
mhs2 = Mahasiswa("Nasyah Dheamita", "202212057")

print(mhs1.perkenalan())
print(mhs2.perkenalan())

