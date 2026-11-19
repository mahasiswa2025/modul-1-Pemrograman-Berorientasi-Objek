# Latihan Praktikum 4: Instance Methods
# Class ManajerInventori dengan methods: tambah_barang, hapus_barang, kurangi_stok, lihat_inventori

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

