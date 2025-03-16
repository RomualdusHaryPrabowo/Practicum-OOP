class Tumbuhan:
  def __init__(self, nama, kebutuhanAir, kebutuhanPupuk):
    self.nama = nama 
    self.kebutuhan_air = kebutuhanAir
    self.kebutuhan_pupuk = kebutuhanPupuk
  
  def calculate_needs(self, airHujan, kelembapanTanah):
    self.kebutuhanPasti_air = self.kebutuhan_air - airHujan 
    self.kebutuhanPasti_pupuk = self.kebutuhan_pupuk - kelembapanTanah
    
    print(f'Laporan Cuaca :\nCurah hujan : {airHujan}\nKelembapan tanah : {kelembapanTanah}\nKebutuhan air : {self.kebutuhanPasti_air}\nKebutuhan pupuk : {self.kebutuhanPasti_pupuk}')
    
class Tanaman1 (Tumbuhan):
  def __init__(self):
    super().__init__('Sawi', 80, 50)
    print(f'Tumbuhan sawi di kebun')
    
class Tanaman2 (Tumbuhan):
  def __init__(self):
    super().__init__('Bayam', 85, 60)
    print(f'Tumbuhan bayam di kebun')

sayur1= Tanaman1()
sayur1.calculate_needs(20, 10)
print('\n')
sayur2 = Tanaman2()
sayur2.calculate_needs(40, 20)  


    