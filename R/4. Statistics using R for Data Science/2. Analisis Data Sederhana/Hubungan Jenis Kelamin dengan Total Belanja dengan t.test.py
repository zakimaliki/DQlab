Berdasarkan kasus diatas kita akan melihat hubungan antara data kategorik dan numerik, yaitu variabel jenis kelamin dan total belanja. Sebelum menguji hubungannya, sebaiknya dilihat perbedaan rata-rata total belanja untuk laki-laki dan perempuan dengan visualisasi yaitu menggunakan boxplot. Boxplot grafik statistik dari data dengan komponen lima ukuran statistik yaitu Min, Q1,Q2, Q3, dan Max. Untuk lebih jelasnya mengenai boxplot dapat dilihat gambar dibawah ini

Selanjutnya analisis inferensia yaitu untuk mengetahui apakah ada perbedaan rata-rata total belanja pada laki-laki dan perempuan maka digunakan statistik uji t-test.

Untuk melakukan visualisasi boxplot dan uji statistik t-test pada R tahapannya sebagai berikut

boxplot(Total~Jenis.Kelamin,data = data_intro)
t.test(Total~Jenis.Kelamin,data = data_intro)

Function boxplot digunakan untuk melihat secara grafik rata-rata total belanja pada laki-laki dan perempuan, sedangkan perintah t.test digunakan untuk melihat hubungan secara statistik. Penggunaan kedua fungsi diatas yaitu variabel pertama yang bertipe numerik, sedangkan variabel kedua variabel kategorik. Hipotesis t-test sebagai berikut :

    Null hipotesis : tidak ada perbedaan rata-rata total belanja antara laki-laki dan perempuan
    Hipotesis alternatif : ada perbedaan rata-rata total belanja antara laki-laki dan perempuan


## carilah boxplot antara variabel jenis kelamin dengan total belanja
boxplot(Total~Jenis.Kelamin,data = data_intro)

## analisis bagaimana hubungan jenis kelamin dengan total belanja mengunakan uji statistik t-test
t.test(Total~Jenis.Kelamin,data = data_intro) 
