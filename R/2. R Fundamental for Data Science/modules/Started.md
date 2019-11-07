[Kembali](../README.md)
# Let’s Get Started with R
## Pendahuluan
Course "R Fundamental for Data Science" ini adalah course pembuka DQLab untuk topik pengolahan data menggunakan R.

Dengan durasi singkat, 15 menit. Anda akan mempelajari dan mendapatkan hal-hal berikut pada course ini
- Mengerti apa dan kenapa R digunakan oleh para data scientist dan dicari oleh perusahaan besar dunia.
- Menguasai dasar bahasa R seperti penggunaan teks, angka, dan rumus.
- Mengerti bagaimana membaca file Excel.
- Mengenali bagaimana grafik dihasilkan di R.
- Sertifikat pencapaian dari PHI-Integration dan Universitas Multimedia Nusantara (Kompas Group).

## Jadi, apa itu R?
R adalah nama sebuah bahasa pemrograman sekaligus software untuk pengolahan data dan grafik. R sangat popular saat ini karena memiliki jumlah fitur yang sangat besar - mencapai puluhan ribu fitur.

Mulai dari membaca file teks, membaca database, menghasilkan berbagai grafik, menghasilkan dashboard yang menarik, sampai ke penggunaan machine learning - semuanya tersedia di R.

Selain itu, R bersifat gratis dan open source. Artinya, dengan R kita tidak perlu biaya lisensi macam-macam untuk menggunakannya secara bebas dan luas.

Dengan alasan tersebutlah maka data scientist di dunia banyak yang menggunakan R.

## Kenapa Data Scientist menggunakan R?
Menurut Anda, apa saja alasan-alasan berikut yang membuat banyak data scientist menggunakan R?
- **Lebih Mudah Dipelajari (Easier)**
- **Lebih Cepat (Faster):**
- **Lebih kaya fitur (Richer)**
- **Telah terbukti (Proven)**

## Kenapa Data Scientist menggunakan R?
Apa sebenarnya yang membuat para data scientist tertarik belajar dan menggunakan R?
Ada empat alasan utama, yaitu:
- **Lebih Mudah Dipelajari (Easier)**: R relatif lebih mudah dipelajari dibandingkan dengan bahasa lain, seperti Java, C#, Javascript, dan lain-lain.
- **Lebih Cepat (Faster)**: Banyak fungsi R memberikan hasil jauh lebih cepat dibandingkan dengan aplikasi lain. Contoh: R dapat menghasilkan berbagai visualisasi yang menarik dalam waktu singkat, sehingga data scientist dapat jauh lebih produktif dalam memahami data dan menghasilkan informasi.
- **Lebih kaya fitur (Richer)**: Dengan puluhan ribu fitur yang terus berkembang, hampir semua permasalahan data dapat dijawab oleh R. Sebagai contoh, untuk mengatasi permasalahan optimasi stok di e-commerce, R memiliki fungsi menghasilkan rekomendasi product packaging.
- **Telah terbukti (Proven)**: R sudah digunakan oleh banyak data scientist perusahaan besar seperti Anz, Uber, dan Facebook dan memberikan solusi riil. Tidak heran jika akhirnya dari kisah sukses ini, banyak lowongan data scientist mencamtumkan R sebagai syarat keterampilan yang harus dimiliki.

Berbekal alasan-alasan tersebut, kami yakin Anda akan lebih percaya diri dengan membekali diri belajar R!

## Code Pertama!
Sejauh ini Anda harusnya sudah mengerti apa dan kenapa kita belajar R, mari kita mulai praktekkan penggunaan R dengan fitur Live Code Editor dari DQLab.
1. Ketikkan perhitungan 1+5 di dalam Code Editor.
2. Jalankan code tersebut dengan menekan tombol Run.
3. Jika berhasil dengan baik akan muncul hasil pada Console sebagai berikut.
4. Selesai.

**Tugas Praktek**

Kirimkan hasil dengan mengklik tombol Submit Code dan lanjutkan ke pelajaran berikutnya. Untuk tipe coding, maka Anda harus selalu menekan tombol ini untuk mengirimkan hasil.

## Apa dan Kenapa R?
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/tFgd5VxOLLs/0.jpg)](https://www.youtube.com/watch?v=tFgd5VxOLLs)

## Teks dan Angka
Selain perhitungan, R bisa berisi perintah yang sangat singkat, hanya berisi angka atau teks saja yang akan ditampilkan apa adanya.
Cobalah ketik angka 9 dan teks "Budi" berikut pada Code Editor.
```
9
"Budi"
```
Klik tombol play dan pada panel Console akan muncul hasil berikut.
```
> 9 
[1] 9 
> "Budi" 
[1] "Budi"
```
Catatan: Tanda > tidak perlu diketik
|Elemen output   | Keterangan |
|----------------|------------|
|>               |Prompt dari R, adalah tanda dari R untuk menerima input perintah|
|9               |Teks angka 9|
|[1] 9           |[1] menunjukkan isi dari posisi pertama output. Kebetulan disini output hanya ada satu item, yaitu angka 9 – jadi hanya itulah yang ditampilkan.|
|[1] "Budi"      |Output dari urutan pertama, yaitu teks "Budi" – jadi posisinya otomatis adalah 1.|

**Tugas Praktek**

Lanjutkan perintah pada code editor dengan angka 10 dan teks "Susi". Klik tombol "Submit Code" untuk melanjutkan ke praktek selanjutnya.

## Menampilkan dengan Print
Pada praktek sebelumnya kita bisa menampilkan teks dan angka dengan menuliskannya secara langsung, tapi akan lebih baik apabila kita menggunakan fungsi bernama print.

1. Mari kita ketik dua perintah print berikut pada code editor.
```
print("Hello World")
print(3 + 4)
```

2. Jika dijalankan akan muncul hasil berikut.
```
> print("Hello World")
[1] "Hello World"

> print(3 + 4)
[1] 7
```

Dengan demikian hasilnya akan sama apabila kita langsung mengetikkan teks ataupun formula tersebut.

**Tugas Praktek**
Cobalah tambahkan perintah untuk menampilkan hasil perhitungan 2 kali 3 dengan perintah print. 

Tips kali ini: Anda bisa mengklik tombol Hint pada setiap pelajaran coding jika mengalami kesulitan.

Jika sudah selesai, klik tombol Submit Code untuk melanjutkan ke pelajaran berikutnya.

## #Tips: Merubah Tema Code Editor
Code Editor memiliki tema terang dan gelap, saat ini yang muncul adalah tema terang. Namun DQLab mengerti bahwa kebanyakan data scientist dan developer suka background editor yang berwarna gelap, mari kita coba.

1. Pada code editor telah tersedia banyak perintah dengan warna latar putih. Catatan: Anda tidak perlu mengerti dan menjalankan code tersebut saat ini.

2. Sekarang klik tombol "Toggling Editor" yang terdapat di Code Editor.

3. Hasilnya tema Code Editor berubah menjadi latar gelap.

4. Selesai

## Huruf Besar dan Kecil di R
Huruf besar dan huruf kecil sangat perlu diperhatikan pada penulisan program R, atau dengan kata lain R sangat case sensitive.

Ini artinya teks seperti "Budi" dan "BUDI" adalah berbeda karena ada perbedaan karakter kapital untuk huruf u, d dan i.

**Tugas Praktek**

Ketik pada teks editor dua teks, dengan isi "hello world" dan "Hello World". Untuk teks kedua, karakter pertama dijadikan huruf besar. Jalankan dan kirimkan jawaban Anda dengan Submit Code.

## Vector dengan Fungsi c
Subbab ini akan belajar apa yang dinamakan vector, dan bagaimana dibuat dengan fungsi c. 

1. Ketikkan c(10:40) berikut pada bagian Code Editor, yang berguna untuk membuat rangkaian angka dari 10 s/d 40. 
```
c(10:40)
```

2. Klik tombol      dan pada panel Console akan muncul tambahan output sebagai berikut.
```
> c(10:40)
[1] 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34
[26] 35 36 37 38 39 40
```
Catatan: Tanda > tidak perlu diketik

3. Terlihat perintah c(10:40) membuat tiga puluh rangkaian angka yang dimulai dari 10 dan diakhiri nilai 40. Rangkaian angka yang dibuat dengan fungsi c ini disebut dengan vector - yaitu suatu struktur data yang bisa menyimpan lebih dari satu data yang sama.
Teks [1] menunjukkan tampilan posisi pertama dari rangkaian angka, yaitu angka 10. Dan teks [26] menunjukkan tampilan posisi kedua puluh enam dari rangkaian angka, yaitu angka 35.

4. Sekarang coba ubahlah perintah di atas merubah huruf c kecil menjadi huruf C besar.
```
C(10:40)
```

5. Klik tombol Run dan pada panel R Console akan muncul tambahan output sebagai berikut.
```
> C(10:40)
object not interpretable as a factor
```
Kalimat pesan berwarna merah artinya perintah tersebut tidak dapat dijalankan dan mengakibatkan error atau kesalahan. Huruf c dan C disini memiliki arti yang sangat berbeda.

**Tugas Praktek**

Hapus seluruh perintah pada Code Editor, kemudian buat suatu rangkaian angka 5 s/d 10 pada Code Editor dengan menggunakan function c.

## Variable
Bagaimana, so far masih asik saja ya dengan pelajaran R sejauh ini? Pastinya ya. Kali ini kita akan bahas mengenai variable, yaitu suatu memori di sistem R yang dapat menyimpan data dan digunakan dengan suatu nama. 

Syntax atau cara penulisannya adalah sebagai berikut.

```
nama_variable <- [nilai yang kita perlu simpan]
```
Operator <- mewakili simbol anak panah dimana nilai di samping kanan disimpan pada variable di sebelah kiri. Operator ini disebut juga sebagai assignment operator.

Untuk memahami hal ini, mari kita langsung praktekkan saja.

1. Buat vector berupa rangkaian angka 1 sampai dengan 10, kemudian kita simpan dalam satu variable bernama angka.
```
angka <- c(1:10)
```

2. Jalankan perintah tersebut, hasil pada Console hanya seperti ini. Hanya perintah yang ditampilkan, tidak ada data vector.
```
> angka <- c(1:10) 
```

3. Jalankan keseluruhan perintah, jika lancar maka tampilan hasilnya adalah sebagai berikut.
```
> angka <- c(1:10)

> print(angka)
 [1]  1  2  3  4  5  6  7  8  9 10 
 ```
Terlihat angka berisi data-data vector seperti praktek kita pada subbab sebelumnya.

4. Selesai.

**Tugas Praktek**

Tambahkan variabel angka2 yang isinya adalah vector dengan rangkaian angka 5 sampai 10. Kemudian tampilkan variabel angka2 tersebut dengan fungsi print.

Jalankan dan kirimkan hasilnya dengan tombol Submit Code.

## Comment
Comment atau komentar adalah teks tidak dianggap sebagai code yang bisa dieksekusi dan biasanya digunakan sebagai catatan untuk penjelasan code. Untuk membuat comment sangat mudah, caranya adalah menuliskan tanda pagar (#) diikuti dengan teks komentar.

Mari kita praktekkan langsung dengan langkah-langkah berikut.

1. Ketikkan komentar setelah perhitungan matematika seperti contoh di bawah ini pada code editor. 
```
2 + 2 #Ini adalah baris komentar
```

2. Jika dijalankan dengan lancar, maka Anda akan mendapatkan hasil berikut.
```
> 2 + 2 #Ini adalah baris komentar
 [1] 4
```

Dari proses ini kelihatan bahwa comment "Ini adalah baris komentar" tidak diproses oleh R dan tidak menampilkan apapun. 

3. Selesai.

**Tugas Praktek**

Sebagai praktek, tambahkan komentar "Ini adalah komentar penutup" pada baris baru. Jalankan dan klik tombol Submit Code untuk melanjutkan ke bagian berikutnya.

Catatan: huruf besar dan huruf kecil berpengaruh pada saat submit code.

## Kesimpulan
Selamat, Anda telah menyelesaikan bab pertama dari course "Fundamental R for Data Science". Dengan demikian Anda telah menguasai keterampilan dasar R berikut:

- Mengetahui apa dan kenapa R digunakan terutama oleh para Data Scientist.
- Mengolah dan menampilkan data angka maupun teks dengan perintah print.
- Melakukan proses perhitungan matematika.
- Menjelaskan sifat R yang case sensitive - huruf besar dan huruf kecil adalah berbeda.
- Membuat vector - sebuah struktur data yang terdiri dari beberapa nilai.
- Menyimpan data perhitungan ke dalam variable - sehingga dapat digunakan pada bagian code lain.
- Memberikan komentar atau comment untuk memberi penjelasan pada code.