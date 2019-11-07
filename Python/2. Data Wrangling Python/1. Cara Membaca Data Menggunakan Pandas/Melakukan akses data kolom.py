Dalam suatu analisis data ada kalanya kita hanya butuh melakukan akses beberapa data saja dan tidak perlu harus menampilkan semua data. Pada pandas kita bisa melakukan akses dalam berbagai kebutuhan. Mulai dari hanya akses kolom tertentu ataupun baris tertentu. Pada sesi kali ini kita akan mencoba untuk melakukan akses beberapa kolom tertentu pada suatu dataset.

Pertama yang harus dilakukan untuk melakukan akses kolom adalah mengetahui nama – nama kolom yang ada. Coba ketikan kode dibawah ini untuk melihat nama kolom yang ada.

import pandas as pd

csv_data = pd.read_csv("shopping_data.csv")

print(csv_data.columns)

Klik Tombol Run

Hasil pada panel console akan keluar seperti berikut :

Index(['CustomerID', 'Genre', 'Age', 'Annual Income (k$)',
       'Spending Score (1-100)'],
      dtype='object')

Note : Pada dataset ini ada 5 kolom termasuk class. Dimana 4 kolom  merupakan data numerik dan 1 kolom merupakan data string. Pada praktek selanjutnya kita akan mencoba mengakses data age. Untuk melakukannya coba tuliskan kode dibawah ini :

import pandas as pd

csv_data = pd.read_csv("shopping_data.csv")

print(csv_data['Age'])