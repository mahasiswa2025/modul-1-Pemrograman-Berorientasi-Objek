# Latihan Praktikum 2: Konsep Class dan Object
# Class Dosen dengan atribut nama dan nidn, serta method ajar_mata_kuliah

class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def ajar_mata_kuliah(self, mata_kuliah):
        return f"Dosen {self.nama} (NIDN: {self.nidn}) sedang mengajar mata kuliah {mata_kuliah}."

# Instansiasi 2 object dosen
dosen1 = Dosen("Ir. Abadi Nugroho, S.Kom., M.Kom.", "1104129002")
dosen2 = Dosen("Herri Susanto, S.S, M.Hum", "1118097701")

# Pemanggilan method
print(dosen1.ajar_mata_kuliah("Pemrograman Berorientasi Objek"))
print(dosen2.ajar_mata_kuliah("Bessai Berinta"))

