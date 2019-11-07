Tidak hanya dengan menentukan dari kolom dan baris. Menggunakan pandas kita juga bisa memanggil suatu data dari suatu baris dan kolom tertentu dalam satu waktu. Perhatikan dan coba kode dibawah ini :

import pandas as pd

csv_data = pd.read_csv("shopping_data.csv")

print(csv_data['Age'].iloc[1])

print("Cuplikan Dataset:")

print(csv_data.head())