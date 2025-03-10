
class robot(): #class of robot
  #atribut class robot
  health_point = 500 #atribut (max health point)
  tambah_healthPoint = 2 #atribut jumlah menambah health point
  def diserang(self, robotLwn): #fungsi untuk mengurangi health point
    damage = 100 #deklarasi jumlah damage 
    robotLwn.health_point -= damage #mengurangi health point dengan damage
    print (f'ANDA MENYERANG LAWAN!!!\n Hp lawan sekarang ({robotLwn.health_point})')
    if robotLwn.health_point <= 0: 
      print ('ANDA MENANG!!!')
      exit()
  def tambahHP(self): #fungsi untuk menambah health point
    if self.health_point < 500 and self.health_point == 400: #moment of truth (hanya bisa menambahkan hp jika hp <500 tapi hp = 400) --> hanya bisa menambah 1 kali
     self.health_point += self.tambah_healthPoint #menambah health point 
     print(f'HEALTH POINT ANDA ({self.health_point})')
    else : #kondisi jika gagal menambah health point
      print(f'GAGAL MENAMBAHKAN HP. HP anda ({self.health_point})')

#objek class
robotHypo = robot()
robotRom = robot()

#looping permainan jika hp kedua objek > 0
while robotHypo.health_point != 0 and robotRom.health_point != 0:
  print ('============================================================')
  print ('GILIRAN ROBOT HYPO')
  print ('MENU AKSI : \n1. SERANG LAWAN\n2. TAMBAH HEALT POINT')
  pilihan = int(input('Pilih aksi anda : '))
  if pilihan == 1 :
    robotHypo.diserang(robotRom) #memanggil fungsi diserang
  elif pilihan == 2 :
    robotHypo.tambahHP() #memanggil fungsi tambahHP
  print ('============================================================')
  print('GILIRAN ROBOT ROM')
  print ('MENU AKSI : \n1. SERANG LAWAN\n2. TAMBAH HEALT POINT')
  pilihan = int(input('Pilih aksi anda : '))
  if pilihan == 1 :
    robotRom.diserang(robotHypo) #memanggil fungsi diserang
  elif pilihan == 2 : 
    robotRom.tambahHP()  #memanggil fungsi tambahHP
      



