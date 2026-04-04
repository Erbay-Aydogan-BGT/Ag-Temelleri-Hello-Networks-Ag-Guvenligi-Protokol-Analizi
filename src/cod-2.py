                                                print("Ağ Trafiği Dinleyici (Scapy ile Sniffer)")
from scapy.all import sniff

# Her paket yakalandığında çalışacak fonksiyonumuz 
def paket_analiz(paket):
    # Eğer paket IP katmanına sahipse
    if paket.haslayer('IP'):
        kaynak_ip = paket['IP'].src
        hedef_ip = paket['IP'].dst
        print(f"Paket Yakalandı: {kaynak_ip} --> {hedef_ip}")

print("Ağ dinleniyor... (Durdurmak için CTRL+C)")
# Sadece 10 paket yakala ve analiz fonksiyonuna gönder
sniff(count=10, prn=paket_analiz)

#Amacı: Kendi ağ kartından geçen veri paketlerini yakalamak ve içindeki IP adreslerini okumak.

#(Not: Bu kodu Linux'ta çalıştırmak için terminalde sudo yetkisine ihtiyacın olacaktır, çünkü ağ kartına doğrudan erişir.)
