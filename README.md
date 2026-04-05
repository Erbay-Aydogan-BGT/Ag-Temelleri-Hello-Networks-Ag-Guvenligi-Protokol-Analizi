# Ağ Güvenliği ve Protokol Analizi - Ağ temelleri - Hello networks 🔐
Ağ protokollerindeki zafiyetlerin keşfi ve analizi üzerine geliştirilmiş güvenlik araçları

Bu projenin temel amacı, ağ üzerindeki veri paketlerinin (network packets) nasıl yapılandırıldığını, bu paketlerin nasıl yakalanıp (sniffing) analiz edilebileceğini ve ağ protokollerindeki (TCP, UDP, ICMP, ARP vb.) güvenlik zafiyetlerinin nasıl tespit edilebileceğini pratik kod örnekleriyle göstermektir


(!) Hazır ve büyük güvenlik araçlarını (Nmap, Wireshark gibi) kullanmak yerine, temel seviyede Python scriptleri geliştirilerek:

Ağdaki açık kapıların (portların) nasıl keşfedildiği,

Yerel ağdaki (LAN) cihazların ARP protokolü ile nasıl tespit edildiği,
Şifresiz ağ trafiğinin nasıl dinlenip analiz edildiği teknik olarak incelenmiştir. 

Bu proje, siber güvenlikte "Keşif" (Reconnaissance) ve "Trafik Analizi" aşamalarını otomatize etme mantığını kavramak için tasarlanmıştır.
Projede nmap için de örnek temel çalışmalar bulunmaktadır

 # Ağın Kimlik Kartı: IP ve Subnet

 Tür	Açıklama	Örnek olarak durumu 
1- IP Adresi	İnternete veya yerel ağa bağlı her cihaza verilen dijital kimlik numarasıdır. Cihazların birbirini bulmasını sağlar.	192.168.1.15 (Yerel IP)

2- Subnet (Alt Ağ)	Büyük bir ağı daha küçük, yönetilebilir parçalara bölme işlemidir. Trafik kalabalığını önler.	255.255.255.0 (C maskesi)

3- Default Gateway	Yerel ağdaki cihazların dış dünyaya (internet) çıkmak için kullandığı "çıkış kapısı" olan cihazın (genelde modem) IP'sidir.	192.168.1.1

