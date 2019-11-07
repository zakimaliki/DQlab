Untuk mengetahui ada nilai kosong atau NULL/NAN pada suatu dataset, dengan menggunakan fungsi pandas kita tidak perlu untuk melihat satu persatu baris data. Bayangkan jika kita memilki 1000 baris data. Apakah kita harus melihat semua baris data tersebut ? Tentu saja tidak. Maka dari itu di pandas disediakan fungsi untuk mengecek apakah ada data yang kosong. Coba praktikan kode dibawah ini.

import pandas as pd

csv_data = pd.read_csv("shopping_data.csv")

print(csv_data.isnull().values.any())

-- Hasil

Hasil pada panel console akan keluar seperti berikut :

False

Note : data yang digunakan merupakan data yang lengkap. Maka dari itu output yang dihasilkan False. Coba Sekarang ganti dengan dataset yang memang terdapat data yang kosong. Coba ketikkan kode dibawah ini.

import pandas as pd

csv_data = pd.read_csv("shopping_data_missingvalue.csv")

print(csv_data.isnull().values.any())

Klik Tombol :: TOMBOL RUN::

Hasil pada panel console akan keluar seperti berikut :

True