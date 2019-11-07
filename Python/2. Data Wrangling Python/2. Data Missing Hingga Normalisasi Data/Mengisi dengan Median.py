Berbeda dengan mean pada sesi sebelumnya. Median digunakan untuk data – data yang memiliki sifat outlier yang kuat. Kenapa median dipilih ? Median merupakan nilai tengah yang artinya bukan hasil dari perhitungan yang melibatkan data outlier. Pada beberapa kasus data outlier dianggap mengganggu dan sering dianggap noisy karena bisa mempengaruhi distribusi kelas dan mengganggu analisa pada klasterisasi (clustering).

import pandas as pd

csv_data = pd.read_csv("shopping_data_missingvalue.csv")

print(csv_data.median())

-- hasil

Sama dengan sesi sebelumnya dengan mean(). Untuk mengisi nilai yang kosong menggunakna fungsi fillna().

import pandas as pd

csv_data = pd.read_csv("shopping_data_missingvalue.csv")

print("Dataset yang masih terdapat nilai kosong ! :")

print(csv_data.head(10))

csv_data=csv_data.fillna(csv_data.median())

print("Dataset yang sudah diproses Handling Missing Values dengan Median :")

print(csv_data.head(10))

-- Hasil