Pada suatu kasus data yang kita baca cukup banyak atau loading yang lama. Untuk memastikan data kita terbaca dengan baik dan bisa menampilkan data sebagian untuk ditampilkan secara benar. Kita bisa memakai fungsi head(). Bisa dituliskan kode dibawah ini untuk prakteknya:

import pandas as pd

csv_data = pd.read_csv("shopping_data.csv")

print(csv_data.head())