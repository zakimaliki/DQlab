Membaca file dengan menggunakan pandas

Sebagai salah satu library untuk melakukan proses awal dari analisis data. Pandas juga memiliki kemampuan untuk membaca berbagai macam jenis file. Format yang bisa dibaca oleh pandas adalah berbagai macam: .txt, .csv, .tsv dan lainnya. Selain membaca file pandas tidak hanya membacanya saja. Namun, merubah data dari file menjadi bentuk dataframe yang akhirnya nanti bisa diakses, diagregasi dan diolah. Coba praktikan kode dibawah ini :

import pandas as pd

csv_data = pd.read_csv("shopping_data.csv")

print(csv_data)