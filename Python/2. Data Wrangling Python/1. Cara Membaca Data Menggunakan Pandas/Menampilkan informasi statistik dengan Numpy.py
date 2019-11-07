Mengetahui informasi statistik pada suatu data sangat penting. Mulai dari distribusi data, nilai max atau min hingga standar deviasi dari suatu dataset. Jika datanya berjumlah dibawah 10 mungkin masih dikerjakan secara manual. Namun bayangkan jika datanya sudah mencapai ratusan bahkan ribuan. Tidak mungkin pastinya untuk dilakukan secara manual. Maka dari itu pentingnya fungsi describe() pada pandas. Fungsi describe() ini memungkinkan untuk mengetahui informasi statistik dari suatu dataset secara cepat. Coba untuk ketika program dibawah ini :

import pandas as pd

csv_data = pd.read_csv("shopping_data.csv")

print(csv_data.describe(include='all'))

-- Hasil

Note : Banyak nilai NaN yang tampil. Hal itu dikarenakan karena pada dataset ada format data string yang akhirnya memunculkan format NaN.

Untuk meminimalisir hal tersebut, dan memfilter hanya data numerical saja yang digunakan adalah menggunakan exclude=[‘O’] dimana fungsi itu akan mengabaikan data yang non numerical untuk diproses. Coba implementasikan code dibawah ini:

 

import pandas as pd

csv_data = pd.read_csv("shopping_data.csv")

print(csv_data.describe(exclude=['O']))

-- Hasil