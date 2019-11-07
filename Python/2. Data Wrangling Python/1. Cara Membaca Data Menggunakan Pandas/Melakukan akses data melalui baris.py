Selain melakukan akses data melalui kolom. Menggunakan pandas juga bisa melakukan akses dengan menggunakan baris. Berbeda dengan akses melalui kolom. Fungsi untuk menampilkan data dari suatu baris adalah fungsi .iloc[i] dimana [i] menunjukan urutan baris yang akan ditampilkan yang dimana indexnya diawali dari 0. Coba ketikan code dibawah ini untuk mempermudah :

import pandas as pd

csv_data = pd.read_csv("shopping_data.csv")

print(csv_data.iloc[5])