Setelah tadi menampilkan suatu kelompok data. Bagaimana jika ingin menampilkan data dari baris ke 5 sampai ke 20. Dari suatu dataset. Untuk mengantisipasi hal tersebut pandas pun juga baik range untuk baris saja, kolom saja dan range untuk baris dan kolom.

Akses range pada suatu kolom dan baris tertentu, untuk mencobanya silahkan ketikan kode dibawah ini :

import pandas as pd

csv_data = pd.read_csv("shopping_data.csv")

print("Menampilkan data ke 5 sampai kurang dari 10 :")

print(csv_data['Age'].iloc[5:10])

Menampilkan suatu range data tertentu pada suatu baris saja. Cobalah ketikan kode dibawah ini :

import pandas as pd

csv_data = pd.read_csv("shopping_data.csv")

print("Menampilkan data ke 5 sampai kurang dari 10 dalam satu baris:")

print(csv_data.iloc[5:10])