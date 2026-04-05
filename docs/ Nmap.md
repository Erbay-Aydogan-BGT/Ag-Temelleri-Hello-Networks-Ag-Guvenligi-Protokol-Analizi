"Sektörel Araçlar ile Analiz (Nmap & Wireshark)"

1- Nmap, kendi yazdığımız basit socket scriptinin çok daha gelişmiş, endüstri standardı halidir.
Sadece portun açık olup olmadığını değil, o portta çalışan yazılımın adını ve sürümünü de bulur.

⚙️ Kullanım Örneği (Terminal): sudo nmap -sV -p 21,22,80,443 192.168.1.1 ⚙️

Parametrelerin Anlamı:

-sV: Servis Versiyonu tespiti (Açık olan portta tam olarak hangi uygulamanın çalıştığını bulmaya çalışır).

-p: Sadece belirtilen portları tarar (Zaman kazanmak için).

 Neden/Amaç Açıklaması:
🔒> "Kendi yazdığımız Python scripti bir kapının açık olup olmadığını kontrol ederken, Nmap o kapının arkasında kimin olduğunu ve hangi dili konuştuğunu (versiyon bilgisini) söyler. 
Bulunan versiyon bilgisi (örneğin Apache 2.4.49), sızma testinin bir sonraki aşamasında uygun zafiyeti (exploit) aramak için kritik bir veridir."🔒

2. Wireshark (ve Tshark) ile Derin Paket Analizi
Scapy ile ağdaki paketlerin başlıklarını okuyabiliriz, ancak devasa bir ağ trafiğini analiz etmek, filtrelemek ve paketlerin içindeki veriyi (payload) görmek için Wireshark kullanılır. Wireshark'ın terminal versiyonu olan tshark, otomasyon için harikadır.
