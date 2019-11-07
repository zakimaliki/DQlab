Salah satu metode yang bisa dikatakan solusi yang umum pada kasus general data science adalah mengisi data kosong dengan menggunakan mean dari masing – masing kolom. Pertama kita harus menentukan mean dari masing – masing kolom. Pada pandas terdapat fungsi mean() untuk menentukan nilai mean dari masing – masing kolom. Mean sendiri digunakan untuk data yang memiliki sedikit sifat outlier/noisy/anomali dalam sebaran datanya maupun isinya.  Coba ketikkan program dibawah ini :

import pandas as pd

csv_data = pd.read_csv("shopping_data_missingvalue.csv")

print(csv_data.mean())

-- Hasil

Fungsi mean sendiri berfungsi untuk menampilkan  nilai mean (rata-rata ) dari setiap kolom. Nilai inilah nanti yang akan mengisi dari nilai yang kosong dari dataset yang mengalami kasus missing value. Untuk mengisi nilai yang kosong menggunakan fungsi fillna(). Coba ketikkan program dibawah ini :

import pandas as pd

csv_data = pd.read_csv("shopping_data_missingvalue.csv")

print(csv_data.mean())

print("Dataset yang masih terdapat nilai kosong ! :")

print(csv_data.head(10))

csv_data=csv_data.fillna(csv_data.mean())

print("Dataset yang sudah diproses Handling Missing Values dengan Mean :")

print(csv_data.head(10))

-- Hasil