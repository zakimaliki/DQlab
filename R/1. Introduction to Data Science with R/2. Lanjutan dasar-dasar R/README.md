# Lanjutan dasar-dasar R

## Comment pada R
Comment merupakan teks untuk menambahkan keterangan pada code kita, sehingga kita akan ingat apa yang dilakukan ketika membuka kembali code tersebut.

Comment tidak dianggap sebagai code yang bisa dieksekusi

Pada R penggunaan comment adalah dengan mengawali suatu teks dengan tanda '#'.

Berikut ini contoh penggunaan comment

```
10 + 7 #Ini adalah baris komentar 
```
atau seperti ini
```
#Ini adalah baris komentar.
10 + 7
```

## Praktik Penggunaan Comment
Ketikkan suatu komentar setelah perhitungan matematika berikut ini pada Code Editor.
```
10 + 7 #Ini adalah baris komentar
```
Cobalah dijalankan dengan Run Code, dan jika lancar, maka Anda akan mendapatkan hasil berikut.
```
> 10 + 7 #Ini adalah baris komentar
 [1] 17
```
Dari proses ini kelihatan bahwa comment tidak diproses oleh R, jadi yang ditampilkan hanya hasil perhitungan matematika.

## Vector pada R
Vector adalah suatu struktur data yang dapat menyimpan lebih dari satu data yang digunakan pada di R.
Penggunaannya sangat sederhana, yaitu menggunakan fungsi c disertai data-data yang ingin disimpan.
```
c(5, 10, 20)
```
ini artinya Anda menyimpan nilai 5, 10 dan 20 dalam satu struktur. Dan jika Anda ingin menyimpan rangkaian angka yang terutut, misalkan angka 1 sampai dengan 20 dapat diketikkan sebagai berikut.
```
c(1:20)
```
Mari kita praktekkan pada bagian berikutnya.

## Praktek Penggunaan Vector - Bagian Satu
Ketikkan perintah c(3, 10, 15) pada Code Editor.
```
c(3, 10, 15)
```
Klik tombol Run Code dan perhiatikan output yang dihasilkan pada bagian Console sebagai berikut.
```
> c(3, 10, 15)
[1]  3 10 15
```
Terlihat perintah c(3, 10, 15) ini membuat tiga rangkaian angka yaitu 3, 10 dan 15 yang disimpan dan ditampilkan bersamaan dalam suatu vector.

## Praktek Penggunaan Vector - Bagian Dua
Selain mengetikkan satu per satu data pada vector, kita juga bisa membuat rangkaian data dengan operator titik dua. Cobalah ketik perintah berikut pada code editor.
```
c(1:5)
```
Klik tombol Run Code dan perhatikan output yang dihasilkan pada bagian Console sebagai berikut.
```
> c(1:5)
[1] 1 2 3 4 5
```
Terlihat perintah c(1:5) membuat vector dengan lima rangkaian angka yang dimulai dari 1 dan diakhiri nilai 5.

## Menggunakan Fungsi Summary
Kekuatan di R adalah fungsi analisa yang kaya, salah satunya adalah fungsi bernama summary yang bisa digunakan untuk mensimpulkan data yang lagi kita proses.

Cobalah ketik perintah untuk melihat karakteristik dari vector berikut.
```
summary(c(1:5))
```
Jalankan dan Anda akan mendapatkan hasil pada Console seperti berikut. Scroll ke bawah untuk penjelasannya.
```r
Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
      1       2       3       3       4       5 
```
Ini artinya dari vector tersebut terdapat angka paling kecil 1 (Min), angka paling besar 5 (Max), angka rata-rata 3 (Mean), dan angka tengah 3 (Median). Untuk 1st Qu dan 3rd Qu kita abaikan dulu.

## Selamat untuk Anda!
Anda baru saja mempelajari dasar awal Bahasa Pemrograman R sebagai langkah awal menjadi seorang Data Scientist.

Masih banyak modul pelajaran yang akan Anda pelajari lebih dalam  untuk mengaplikasikan teknik data science secara tepat menggunakan berbagai studi kasus Industri.

