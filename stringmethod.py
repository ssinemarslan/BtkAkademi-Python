message="Hello There.My name is Sinem Arslan"

# message=message.upper()#herseyi büyük harfe cevirir.
# message=message.lower()#küçük harfe çevirir.
# message=message.title()#her kelimenin basını büyük harfe cevirir
# message=message.capitalize()#metinde sadece ilk harfi büyük yazar.
# message=message.strip()#bastaki boslugu siler.
# message=message.split()#metini kelime kelime ayırır.yani dizi elemanı olur.

index=message.find("Sinem")#metinde sinemi bulur kelimenin ilk hangi indexe denk geldiğini bulur.
print(index)

print(message)
isFound=message.startswith("H")#metin h ile baslayıp baslamadıgını kontrol eder baslıyosa true döner.
isFound=message.endswith("n")#bu da metin sonu
message=message.replace("Sinem","Çınar")#sinem kısmını çınara cevir.
print(isFound)