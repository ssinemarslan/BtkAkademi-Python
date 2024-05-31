#Calısanların zamlı maaslarını hesaplama
print(5000-(5000*0.27))
print(4000-(4000*0.27))

#tekrar tekrar maaşı ve zam oranını yazmaktansa bunları değişkene tanımlamak daha pratiktir ve kod tekrarını azaltır.
MaasAli=5000
MaasAhmet=4000
vergi=0.27

print(MaasAli-(MaasAli*vergi))
print(MaasAhmet-(MaasAhmet*vergi))

#Değişken tanımlama kuralları
# rakam ile başlayamaz. 1number gibi yanlıştır.
# (Number1 doğru bir kullanımdır.)

number1=10
print(number1)

number1=20 #burada number1 değikeninin içindeki değeri değiştirdik.
print(number1)

number1 +=30 #enson number1 değişkeni 20ydi 20+30=number1 oldu
print(number1)

#buyuk kucuk harf duyarlılıgı vardır.Yani;
age=20
AGE=30
print(age)
print(AGE) #ikiside farkli birer değikendirler.

#Türkçe karakter kullanılmamalıdır.

##************************************##
x=1             #int
y=2.3           #float
name="Sinem"    #string
isStudent=True  #bool

#x, y, name, isStudent=(1, 2.3, "Sinem", True) #böyle tek bir satırda tanımlama da mümkündür.

a="10"
b="20"
print(a+b) #=>1020 #string ifade olduklarından yanyana yazdırılır.

firstName="Sinem"
lastName=" Arslan"
print(firstName+lastName) #Sinem Arslan




