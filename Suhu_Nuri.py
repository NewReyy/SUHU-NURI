nama =input("Nama : ")
nim =input("NIM : ")

print("KONVERSI SUHU DINAMIS NURI")
print("«===================================»")
print("C untuk Celcius")
print("F untuk Fahrenheit")
print("K untuk Kelvin")
print("R untuk Reamur")
suhu = input("Inputkan suhunya berapa? (format: 11C, 87F, 19K, 47R): ")
print("«===================================»")
temperatur = int(suhu[:-1])
masukan = suhu[-1]

if masukan.upper() == "C":
  rumus1 = float((9 * temperatur) / 5 + 32)
  rumus2 = float(temperatur + 273.15)
  rumus3 = float(4/5 * temperatur)
  jenis_suhu = "Celcius"
  jenis1 = "Fahrenheit"
  jenis2 = "Kelvin"
  jenis3 = "Reamur"
                
elif masukan.upper() == "F":
  rumus1 = float((temperatur - 32) * 5 / 9)
  rumus2 = float(((temperatur - 32) * 5 / 9) + 273.15)
  rumus3 = float(4/9 * (temperatur-32))
  jenis_suhu = "Fahrenheit"
  jenis1 = "Celsius"
  jenis2 = "Kelvin"
  jenis3 = "Reamur"
elif masukan.upper() == "K":
  rumus1 = float(temperatur - 273.15)
  rumus2 = float(((temperatur - 273.15) * 9 / 5)+32)
  rumus3 = float(4/5 * (temperatur-273))
  jenis_suhu = "Kelvin"
  jenis1 = "Celcius"
  jenis2 = "Fahrenheit"
  jenis3 = "Reamur"
elif masukan.upper() == "R":
  rumus1 = float((5/4) * temperatur)
  rumus2 = float((9/4 * temperatur) + 32)
  rumus3 = float((5/4 * temperatur) + 273)
  jenis_suhu = "Reamur"
  jenis1 = "Celcius"
  jenis2 = "Fahrenheit"
  jenis3 = "Kelvin"
else :
	print("Format penulisan berbeda!! Perhatikan Penulisan Masukan Kembali!!")
	
print(temperatur,jenis_suhu,"=","{:.1f}".format(rumus1),jenis1)
print(temperatur,jenis_suhu,"=","{:.1f}".format(rumus2),jenis2)
print(temperatur,jenis_suhu,"=","{:.1f}".format(rumus3),jenis3)
