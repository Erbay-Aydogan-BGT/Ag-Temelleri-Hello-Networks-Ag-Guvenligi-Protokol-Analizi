print("ÖRNEK-1 Temel Port Tarayıcı (Socket ile)")
#Ağ Güvenliği ve Protokol Analizi" konusu ile ilgili birkaç örnek verelim ilk başta basit ve anlaşılır kısımda python ile başlayacağım temel mantığı anlayabilmek içindir.
import socket

hedef_ip = "192.168.1.1"
# Kendi modeminin veya sanal makinenin IP'sini yazabilirsin örnek amaçı böyle yazdım
aranacak_portlar = [21, 22, 80, 443] 

print(f"{hedef_ip} üzerinde port taraması başlatılıyor...")

for port in aranacak_portlar:
# IPv4 (AF_INET) ve TCP (SOCK_STREAM) için bir soket oluşturmak istiyorum
    soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1) # 1 saniye içinde cevap gelmezse geçsin atlasın 
    
 # Hedef IP ve Porta bağlanmayı deneme durumu
    sonuc = soket.connect_ex((hedef_ip, port))
    
    if sonuc == 0:
        print(f"[+] Port {port} AÇIK")
    else:
        print(f"[-] Port {port} KAPALI")
        
    soket.close()

#Amac: Hedef sistemde hangi servislerin (Web sunucusu, SSH, FTP vb.) dışarıya açık olduğunu bulmak. Sızma testlerinin ilk adımı olan "Keşif" aşamasıdır.
