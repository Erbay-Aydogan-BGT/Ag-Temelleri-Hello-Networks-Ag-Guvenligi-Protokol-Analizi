# 1- Ağın Kimlik Kartı: IP ve Subnet
 Ağdaki her cihazın bir adresi (IP) ve bu adresin hangi mahallede (Subnet) olduğunu belirleyen bir maskesi vardır.

 Tür	Açıklama	Örnek olarak durumu 
 
1- IP Adresi	İnternete veya yerel ağa bağlı her cihaza verilen dijital kimlik numarasıdır. Cihazların birbirini bulmasını sağlar.	192.168.1.15 (Yerel IP)

2- Subnet (Alt Ağ)	Büyük bir ağı daha küçük, yönetilebilir parçalara bölme işlemidir. Trafik kalabalığını önler.	255.255.255.0 (C maskesi)

3- Default Gateway	Yerel ağdaki cihazların dış dünyaya (internet) çıkmak için kullandığı "çıkış kapısı" olan cihazın (genelde modem) IP'sidir.    
       192.168.1.1


# 2. Sistemin Kapıları: Portlar ve Servisler

Bir IP adresine ulaştığında, o cihazın içinde hangi servisle konuşacağını portlar belirler. 
Bir evi IP adresi, evin içindeki kapıları da portlar gibi düşünebilirsin. 
Sızma testinde amacımız "açık unutulmuş" veya "güvensiz" kapıları bulmaktır.

Port No	 -   Servis Adı      -   	Açıklama ve Örnek

22  -------	     SSH	 ----------          Uzaktan güvenli komut satırı erişimi sağlar. Genelde Linux sunucuları yönetmek için kullanılır.

80	  -------     HTTP	      --- ------     Şifresiz web trafiğidir. Tarayıcıya http://... yazdığında bu kapıdan girersin.

443	 --- ----    HTTPS	      ---------     Şifreli ve güvenli web trafiğidir. Günümüzdeki çoğu web sitesi bu güvenli kapıyı kullanır.

21	       FTP	             Dosya aktarım protokolüdür. Eskiden çok yaygındı, şimdi yerini daha güvenli yöntemlere bıraktı.

