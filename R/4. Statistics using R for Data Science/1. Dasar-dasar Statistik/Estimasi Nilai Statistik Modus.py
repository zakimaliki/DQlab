Modus merupakan nilai yang menunjukan nilai yang sering muncul. Modus digunakan untuk data bertipe nominal dan ordinal.

Untuk menampilkan modus dari data dapat menggunakan syntax

Mode(data_intro$Produk)

Berikut penjelasan function diatas:

    Mode akan menampilkan nilai terbanyak pada variabel yang diamati.
    data_intro$Produk, merupakan kolom Produk dari variable data_intro.

Untuk menggunakan function Mode tersebut, menggunakan library tambahan bernama "pracma".

library(pracma)
## carilah modus untuk kolom Produk pada variable data_intro
Mode(data_intro$Produk)
## carilah modus untuk kolom Tingkat.Kepuasan pada variable data_intro
Mode(data_intro$Tingkat.Kepuasan)
