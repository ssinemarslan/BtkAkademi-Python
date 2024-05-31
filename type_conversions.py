#veri tür dönüsümleri
# x=input("1. sayi :")
# y=input("2. sayi :")
# print(type(x))
# print(type(y))
# toplam=int(x)+int(y)
# print(toplam)


name="Sinem"
surname="Arslan"
age=24
#print("My name is "+ name +" "+ surname +" and \nI am "+ str(age) + " years old")
#string karakter dizimine bakılır.
greeting="My name is "+ name +" "+ surname +" and \nI am "+ str(age) + " years old"
print(greeting[0]) #indexin 0. elemanı
print(greeting[3])
print(len(greeting))#indexin kaç karakterli oldugunu verir
print((len(greeting))-1) #kac elemanlı oldugunu verir.
#-1 deriz çünkü index 0dan saymaya başlar.
print(greeting[2:5]) #2. indexten 5e kadar yazar.
print(greeting[3:])#3ten sona kadar.
print(greeting[2:40:2])#2den 40 kadar 2şer 2şer gider.