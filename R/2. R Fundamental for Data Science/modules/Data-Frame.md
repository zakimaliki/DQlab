[Kembali](../README.md)
# Data Frame dan File Excel
## Pendahuluan
Dengan berbekal teori dan praktek sebelumnya, sekarang kita telah siap membahas mengenai tiga hal berikut yang akan banyak digunakan di keseharian menggunakan R.

- Data Frame
- Package
- Menggunakan package untuk membaca file Excel

Klik tombol Next berikut untuk melanjutkan.

## Akses Vector di Data Frame
Dari praktek sebelumnya, terlihat ternyata data frame memiliki banyak kolom. Lalu bagaimana caranya agar kita bisa mengakses satu kolom saja, misalkan fakultas?

Gampang sekali ternyata, caranya adalah menggunakan accessor dengan tanda $ yang diikuti dengan nama kolom. Untuk lebih jelasnya, mari kita praktekkan langsung:

1. Pada code editor Anda saat, isinya hampir sama dengan pelajaran sebelumnya dimana terdapat satu data frame dengan nama info_mahasiswa dengan tiga kolom vector, yaitu fakultas, jumlah_mahasiswa, dan akreditasi.

2. Sekarang tambahkan perintah berikut di akhir baris dari code editor.
```
print(info_mahasiswa$fakultas)
```

Maka akan seperti ini:
```
#Membuat tiga variable vector
fakultas <- c("Bisnis", "D3 Perhotelan", "ICT", "Ilmu Komunikasi", "Seni dan Desain")
jumlah_mahasiswa <- c(260, 28, 284, 465, 735)
akreditasi <- c("A","A","B","A","A")

#Membuat data frame dari kedua vector di atas
info_mahasiswa <- data.frame(fakultas, jumlah_mahasiswa, akreditasi)

#Menampilkan kolom fakultas
print(info_mahasiswa$fakultas)

#Menampilkan kolom jumlah_mahasiswa
```

3. Jalankan code tersebut, dan jika lancar maka hasilnya adalah sebagai berikut.
```
> print(info_mahasiswa$fakultas)
[1] Bisnis          D3 Perhotelan   ICT             Ilmu Komunikasi
[5] Seni dan Desain
Levels: Bisnis D3 Perhotelan ICT Ilmu Komunikasi Seni dan Desain
```

Ada output baru yang belum dijelaskan sebelumnya, yaitu Levels. Ini akan dibahas secara lebih lengkap di modul data preparation DQLab, untuk saat ini abaikan saja.

4. Selesai.

**Tugas Praktek**
Tambahkan code untuk menampilkan kolom jumlah_mahasiswa dari data frame info_mahasiswa. 

## Data Frame
Data frame adalah jenis struktur data yang dirancang seperti table, dimana terdapat satu atau beberapa kolom banyak data.

|fakultas           |jumlah_mahasiswa   |akreditasi     |
|-------------------|-------------------|---------------|
|Bisnis             |260                |A              |
|D3 Perhotelan      |28                 |A              |
|ICT                |284                |B              |
|Ilmu komunikasi    |465                |A              |
|Seni dan desain    |735                |A              |

Untuk membuat data frame kita bisa gunakan vector dan fungsi bernama data.frame. Agar dapat memahami lebih baik, kita langsung gunakan contoh praktek dimana kita akan buat tabel data jumlah mahasiswa di suatu universitas dengan dua kolom: fakultas dan jumlah_mahasiswa.

Berikut adalah langkah demi langkah untuk membuat data frame tersebut:

1. Buatlah vector untuk jumlah mahasiswa dengan fungsi c (di bawah comment "Membuat dua variable vector" pada code editor).
```
jumlah_mahasiswa <- c(260, 28, 284, 465, 735)
```
Berbeda dengan bab sebelumnya, kita tidak menggunakan tanda titik dua disini untuk membuat range, tapi mengetikkannya angka satu per satu. Disini ada lima angka sebagai isi dari vector..

2. Buat lagi satu vector untuk nama-nama fakultas. 
```
fakultas <- c("Bisnis", "D3 Perhotelan", "ICT", "Ilmu Komunikasi", "Seni dan Desain")
```
Disini kembali vector yang dibuat agak berbeda, dimana isinya adalah teks-teks yang mewakili sejumlah fakultas. Jumlahnya juga lima - sama jumlah isi variable vector sebelumnya untuk membuat data frame.

3. Kedua variable vector yang bernama jumlah_mahasiswa dan fakultas tersebut kemudian digabung dengan fungsi data.frame seperti berikut.

```
info_mahasiswa <- data.frame(fakultas, jumlah_mahasiswa)
```
Fungsi data.frame bisa menerima banyak vector, disini kita masukkan dua variable vector yang telah kita buat di langkah 1 dan 2.

4. Tampilkan isi dari info_mahasiswa dengan fungsi print.
```
print(info_mahasiswa)
```
Sejauh ini, isi pada code editor Anda saat ini harusnya seperti berikut.
