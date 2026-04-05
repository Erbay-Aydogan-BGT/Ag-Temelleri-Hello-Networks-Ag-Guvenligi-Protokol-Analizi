# Ağ Güvenliği ve Protokol Analizi - Ağ temelleri - Hello networks 🔐
Ağ protokollerindeki zafiyetlerin keşfi ve analizi üzerine geliştirilmiş güvenlik araçları

Bu projenin temel amacı, ağ üzerindeki veri paketlerinin (network packets) nasıl yapılandırıldığını, bu paketlerin nasıl yakalanıp (sniffing) analiz edilebileceğini ve ağ protokollerindeki (TCP, UDP, ICMP, ARP vb.) güvenlik zafiyetlerinin nasıl tespit edilebileceğini pratik kod örnekleriyle göstermektir


(!) Hazır ve büyük güvenlik araçlarını (Nmap, Wireshark gibi) kullanmak yerine, temel seviyede Python scriptleri geliştirilerek:

Ağdaki açık kapıların (portların) nasıl keşfedildiği,

Yerel ağdaki (LAN) cihazların ARP protokolü ile nasıl tespit edildiği,
Şifresiz ağ trafiğinin nasıl dinlenip analiz edildiği teknik olarak incelenmiştir. 

Bu proje, siber güvenlikte "Keşif" (Reconnaissance) ve "Trafik Analizi" aşamalarını otomatize etme mantığını kavramak için tasarlanmıştır.
Projede nmap için de örnek temel çalışmalar bulunmaktadır

#Ağ temelleri 
Bir sızma testi (Penetration Test) sürecinin başarılı olabilmesi için, verinin ağ üzerinde nasıl paketlendiğini ve hedeflerin nasıl adreslendiğini anlamak kesinlikle gerekiyor. 
Bu bölümde, projenin teknik altyapısını oluşturan temel kavramlar özetlenmiştir.

 

