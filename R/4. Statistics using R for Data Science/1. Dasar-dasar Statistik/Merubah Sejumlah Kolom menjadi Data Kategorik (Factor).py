Pada data_intro beberapa variabelnya bersifat kualitatif yaitu variabel jenis kelamin, produk, dan Tingkat_Kepuasan. Variabel tersebut harus di ubah jenis datanya menjadi faktor untuk mendapatkan karakteristik dari setiap pelanggan (observasi).

Untuk mengubah tipe data menjadi factor dapat menggunakan syntax berikut:

data_intro$Jenis.Kelamin <- as.factor(data_intro$Jenis.Kelamin)

data_intro$Produk <- as.factor(data_intro$Produk)

data_intro$Tingkat.Kepuasan <- as.factor(data_intro$Tingkat.Kepuasan)

Tugas:

## Mengubah data menjadi factor untuk membedakan data kualitatif dengan menggunakan functon as.factor
data_intro$Jenis.Kelamin <- as.factor(data_intro$Jenis.Kelamin)
data_intro$Produk <- as.factor(data_intro$Produk)
data_intro$Tingkat.Kepuasan <- as.factor(data_intro$Tingkat.Kepuasan)
## Melihat apakah sudah berhasil dalam mengubah variabel tersebut dengan menggunakan function str
str(data_intro$Jenis.Kelamin)
str(data_intro$Produk)
str(data_intro$Tingkat.Kepuasan)
