website= "http://www.sinemarslan.com"
course="Python Kursu:Baştan Sona Python Programlama Rehberiniz (40 saat)"

#1-'Course' karakter dizisinde kaç karakter bulunmaktadır?
result=len(course)
print(result)
#2-'website' içinden www karakterlerini alın.
result2=website[7:10] #www karakterleri 7.ve 10.indekstedirler.
print(result2)
#3-'website' içinden com karaklerlerini alın.
result3=website[23:26] #burada baştan indeksi saymaya basladık.
print(result3)

#4-'course' içinden ilk 15 ve son 15 karakterleri alın.
result4=course[0:15]
print(result4)

result5=course[-15:] #ifadenin sondan 15 karakterini verir.
print(result5)

#5-'course' ifadesindeki karakterleri tersten yazdırın.
ters=course[::-1]
print(ters)

name,surname,age,job='Sinem','Arslan',24,'software tester'

#6-Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#'Benim adım Sinem Arslan,Yaşım 24 ve mesleğim software tester'
result6="Benim adım "+name+" "+surname +",Yaşım "+str(age)+" ve mesleğim "+job
print(result6)
result7=f"Benim adım {name} {surname},Yasım {age} ve mesleğim {job}" #bu da fsting ile yapılmış halidir.
print(result7)

#7-'Hello world' ifadesindeki w harfini 'W'ile değiştiriniz
yazi='Hello world'
result8=yazi.replace('w','W')
print(result8)

#'abc ifadesini yanyana 3 defa yazdırın.
result9='abc'*3
print(result9)