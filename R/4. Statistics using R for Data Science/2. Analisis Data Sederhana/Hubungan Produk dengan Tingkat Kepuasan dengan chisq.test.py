Berdasarkan kasus diatas kita akan melihat hubungan antara data kategorik dan kategorik, yaitu variabel jenis produk dan tingkat kepuasan. Sebelum menguji hubungannya, sebaiknya dilakukan tabulasi silang sebagai analisis deskriptif. Selanjutnya analisis inferensia yaitu menguji apakah ada hubungan maka dapat digunakan chi-square test.

Untuk melakukan tabulasi dan uji statistik chi-square test pada R tahapannya sebagai berikut

table(data_intro$Produk,data_intro$Tingkat.Kepuasan)
chisq.test(table(data_intro$Produk,data_intro$Tingkat.Kepuasan))

Perintah table untuk melihat tabulasi antar variabel kategorik, sedangkan perintah chisq.test digunakan untuk melihat hubungan secara statistik.

Dengan hipotesis sebagai berikut :

    H0 : tidak ada hubungan antara jenis produk dan tingkat kepuasan.
    Ha : terdapat hubungan antara jenis produk dan tingkat kepuasan  

## Carilah tabulasi silang antara kolom jenis produk (Produk) dan tingkat kepuasan (Tingkat.Kepuasan) dari variable data_intro
table(data_intro$Produk,data_intro$Tingkat.Kepuasan)

## Analisis bagaimana hubungan jenis produk dengan tingkat kepuasan mengunakan uji korelasi
chisq.test(table(data_intro$Produk,data_intro$Tingkat.Kepuasan)) 