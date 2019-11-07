Terkadang pada beberapa kasus. 1 kolom dengan kolom yang lain memiliki skala yang berbeda. Seperti cuplikan gambar dibawah ini.

No	usia 	Masa Kerja (Tahun) 	Gaji
1	50		30					10000000
2	30		10					5000000

Antara usia dan Masa Kerja masih memiliki range yang sama dalam skala puluhan. Namun, jika Kolom Usia dan Masa Kerja dibandingkan dengan Gaji memiliki range nilai yang berbeda dimana, Usia dan Masa Kerja memiliki range puluhan dan Gaji mempunyai range nilai jutaan. Memang terlihat sederhana, namun hal ini bisa menjadi masalah besar dalam contoh kasus klasterisasi atau klasifikasi. Masuk pada kasus K-means yang sudah pernah dibahas sebelumnya. K-means merupakan algoritma klasterisasi (clustering) yang menggunakan perhitungan jarak dalam prosesnya. Sekarang coba bayangkan :

Jika tidak ada normalisasi maka jelas perhitungan kmeans diatas akan tergantung pada Gaji. Kenapa ? Karena gaji berdomain jutaan dan 2 kolom lainnya hanya berdomain puluhan. Berapapun usia dan masa kerja seseorang tidak akan berpengaruh terhadap penilaian suatu perusahaan. Perbedaan skala pada setiap kolom ini merupakan hal yang sangat wajar dan sering terjadi dan inilah pentingnya normalisasi. Normalisasi sangat penting terutama untuk yang menggunakan perhitungan jarak dengan menggunakan metode apapun.