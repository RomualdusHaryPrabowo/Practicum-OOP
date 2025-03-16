class Employe :
  def __init__(self, nama, role, jamKerja, taskCompleted):
    self.nama = nama
    self.role = role
    self.jam_kerja = jamKerja
    self.task_complete = taskCompleted
 
class softwareEngineer (Employe): 
  def __init__(self):
    super().__init__('Aldo', 'Software Engineer', 5, 10)
    print(f'Performa Aldo ({self.role}) is coding')
  
  def evaluasiPerforma (self, pekerjaan, jamMelakukan):
    self.performa = (jamMelakukan / self.jam_kerja) * 1
    if self.performa >= 0.8 :
      print('Performa Tinggi')
    elif self.performa >= 0.5 and self.performa < 0.8 :
      print('Performa sedang')
    else:
      print('Performa rendah')
    
class DataScientist (Employe):
  def __init__(self):
    super().__init__('Elsha', 'Data Scientist', 8, 5)
    print(f'Performa Elsha ({self.role}) is analyzing data')
  
  def evaluasiPerforma (self, pekerjaan, jamMelakukan):
    self.performa = (pekerjaan / self.task_complete) * 1
    if self.performa >= 0.7:
      print('Performa Tinggi')
    elif self.performa >= 0.5 and self.performa < 0.7 :
      print('Performa sedang')
    else:
      print('Performa rendah')

class ProductManager (Employe):
  def __init__(self):
    super().__init__('Hypo', 'Product Manager', 9, 9)
    print(f'Performa Hypo ({self.role}) is managing the product roadmap')
  
  def evaluasiPerforma (self, pekerjaan, jamMelakukan):
    self.performa = ((pekerjaan * pekerjaan) / jamMelakukan) * 1
    if self.performa >= 0.7:
      print('Performa Tinggi')
    elif self.performa >= 0.5 and self.performa < 0.7:
      print('Performa sedang')
    else:
      print('Performa rendah')
    
 
pekerja1 = softwareEngineer()
pekerja1.evaluasiPerforma(4, 2)
print('\n')
pekerja2 = DataScientist()
pekerja2.evaluasiPerforma(2, 4)
print('\n')
pekerja3 = ProductManager()
pekerja2.evaluasiPerforma(6, 5)