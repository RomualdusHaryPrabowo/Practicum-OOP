class RekeningBank:
    nilaiTukar = {"IDR": 1, "USD": 16345, "EUR": 17781}
    
    def __init__(self, pemilik, saldo, mata_uang):
        self.pemilik = pemilik
        self.saldo = saldo
        self.mata_uang = mata_uang
    
    def tambah_saldo(self, jumlah):
        self.saldo += jumlah
        print(f'Anda menambah {jumlah} saldo\nSaldo menjadi = {self.saldo}')
    
    def tarik_saldo(self, jumlah):
        if self.saldo >= jumlah:
            self.saldo -= jumlah
            print(f'Anda menarik {jumlah} saldo\nSaldo menjadi = {self.saldo}')
        else:
            print("Saldo tidak mencukupi!")
    
    def terapkan_bunga(self):
        tingkat_bunga = 0.5 if self.saldo > 500 else 0.01
        self.saldo *= (1 + tingkat_bunga)
        print(f"Bunga diterapkan...\nSaldo baru = {self.mata_uang} {self.saldo}")
    
    def konversi_mata_uang(self, mata_uang_tujuan):
        print(f'Konversi ke {mata_uang_tujuan}')
        if self.saldo == 0 :
          print('Saldo tidak cukup!')
          exit()
        self.saldo *= self.nilaiTukar[self.mata_uang]
        print(f"Saldo baru = {mata_uang_tujuan} {self.saldo}")
        return self.saldo
       

nasabah1 = RekeningBank("Aldo", 1000, "IDR")
print(f"Rekening Aldo :\nSaldo Awal = {nasabah1.mata_uang} {nasabah1.saldo}")
nasabah1.terapkan_bunga()
nasabah1.tarik_saldo(100)
print('\n')
nasabah2 = RekeningBank("Elsha", 500, "EUR")
print(f"Rekening Elsha :\nSaldo Awal = {nasabah2.mata_uang} {nasabah2.saldo}")
nasabah2.konversi_mata_uang("IDR")
nasabah2.tambah_saldo(100)
