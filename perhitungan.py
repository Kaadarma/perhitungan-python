# TUGAS 1 MENGHITUNG SEBUAH NILAI

#Jika menggunakan * = perkalian
#Jika menggunakan - = pengurangan
#Jika menggunakan / = pembagian
#Jika menggunakan + = penjumlahan 
#Jika menggunakan ** = pangkat
#Jika menggunakan % = modulus

A = 5
B = 3
X = 9

hasil = X * B
print (X,'*',B,'=', hasil)

#kali, modulus, pangkat, bagi, kurang, tambah
hasil = A * X % B ** A / B - B + A 
print (A,'*',X,'%',B,'**',A,'/',B,'-',B,'+',A,'=', hasil)

#kali, bagi, kurang 
hasil = X * B / A - X
print (X,'*',B,'/',A,'-',X,'=', hasil)

#Kurung percobaan 
hasil = (B * X) - A + X 
print ('(',B, '*',X,')-',A, '+' ,X, '=', hasil )

#hasil
y = float(input("masukan nilainya : "))
if (y>0 and y<5) or (y>8 and y<11):
    print(True)
else :
    print (False)

x = float (input("masukan nilai ke 2 : "))
if (0<y and 5>y) or (8<y and 11>y) :
    print (True)
else :
    print (False)

