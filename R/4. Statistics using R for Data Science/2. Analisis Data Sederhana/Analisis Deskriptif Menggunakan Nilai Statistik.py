Untuk melakukan analisis deskriptif setiap variabel pada R, kita dapat menggunakan function berikut.

summary(data_intro)

Function summary akan menampilkan kesimpulan pada variabel masing-masing. Untuk variabel bertipe character akan menampilkan panjang datanya. Variabel bertipe factor akan menampilkan jumlah data pada masing-masing kelas. Sedangkan untuk variabel bertipe numerik akan memunculkan nilai minimum, Q1,Q2 (median), Q3, mean, dan maximum.

Pengertian dari masing-masing istilah itu adalah sebagai berikut :

    Minimum adalah nilai observasi terkecil.
    Kuartil pertama (Q1), yang memotong 25 % dari data terendah.
    Median (Q2) atau nilai pertengahan.
    Kuartil ketiga (Q3), yang memotong 25 % dari data tertinggi.
    Maksimum adalah nilai observasi terbesar.
    
## carilah summary data dari data_intro
summary(data_intro)