Setelah melakukan analisis deskriptif sebelumnya, agar lebih jelas bagaimana gambaran/sebaran dari data maka kita perlu membuat grafik dari masing-masing variabel. Grafik disini juga dapat sebagai analisis eskplorasi yang akan membantu dalam membangun hipotesis.

Untuk mendapatkan visualisasi dasar dari setiap variabel pada R bisa menggunakan perintah berikut

plot(data_intro$Jenis.Kelamin)

hist(data_intro$Pendapatan)

Berikut penjelasan function diatas:

    plot digunakan untuk variabel bertipe Factor - function ini menghasilkan grafik Bar Plot.
    hist untuk variabel bertipe numerik seperti int - function ini menghasilkan grafik Histogram.

Tujuan dari plot dan hist adalah untuk mengetahui sebaran data.

## Carilah sebaran data kolom Jenis.Kelamin dari variable data_intro
plot(data_intro$Jenis.Kelamin)

## Carilah sebaran data dari Pendapatan dari variable data_intro
hist(data_intro$Pendapatan)

## Carilah sebaran data dari Produk dari variable data_intro
plot(data_intro$Produk)

## Carilah sebaran data dari Harga dari variable data_intro
hist(data_intro$Harga)

## Carilah sebaran data dari Jumlah dari variable data_intro
hist(data_intro$Jumlah)

## Carilah sebaran data dari Total dari variable data_intro
hist(data_intro$Total)

## Carilah sebaran data dari Tingkat.Kepuasan dari variable data_intro
plot(data_intro$Tingkat.Kepuasan)
