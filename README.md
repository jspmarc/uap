# uap
Tugas Besar Pengkom K-71, 2019

Program ini adalah tiruan dari software/marketplace digital sangat besar yang sudah ada, yaitu Steam, hence "Uap".
Tujuan dari program ini adalah sebagai tugas besar dan tugas akhir untuk mata kuliah Pengenalan Komputasi. 

Fitur-fitur:
1. Memakai pickle untuk menyimpan database ke file txt di luar aplikasi, sehingga ketika aplikasi di-restart, dictionary/array tidak ke-reset.
Database pada program ini digunakan untuk:
  a. Menyimpan username dan password user.
  b. Menyimpan review-review dari semua game yang sudah ada ke dalam file masing2.
2. Bisa mengurutkan list berdasarkan abjad atau angka. Menggunakan algoritma sorting in-house (buatan sendiri) agar bisa mengurutkan beberapa array di dalam array (alias mengurutkan elemen matriks) berdasarkan elemen dari array yang ada di dalam array (alias elemen dari elemen matriks).


Function untuk menyimpan dictionary/array ke file luar agar tidak ke-reset saat membuka program:

///
import pickle

def save_obj(obj, name): #Menyimpan dictionary ke file luar
  with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f)

def load_obj(name): #Me-load dictionary dari file luar
    with open(name, 'rb') as f:
        return pickle.load(f)
///
refrensi: https://stackoverflow.com/questions/19201290/how-to-save-a-dictionary-to-a-file

Function untuk membersihkan terminal/konsol:

///
import os

os.system("clear") #Biasanya untuk terminal linux atau WSL
os.system("cls") #Biasanya untuk cmd
///
refrensi: https://stackoverflow.com/questions/4810537/how-to-clear-the-screen-in-python

Subprogram dari program Uap ini adalah:
1. Uap.py
2. Login.py
3. MenuGame.py
4. MetodeBayar.py
5. Review.py

Uap.py
Program ini adalah program yang akan di-run dan hanya berfungsi untuk membersihkan terminal/konsol. Setelah itu program ini akan memanggil Login.py.

Login.py
Subprogram ini berfungsi untuk register, login, atau mengganti password user. Cara kerjanya register dan mengganti password, user hanya perlu memasukkan username baru/lama, kemudian memasukkan password baru serta konfirmasinya. Jika konfirmasi benar, maka user akan langsung terdaftar atau password lama user akan "ditimpa" dengan password yang baru.

Untuk login, program hanya akan menerima input berupa username dan password, yang kemudian password akan dicek dengan password user yang ada di dictionary dan jika cocok akan masuk ke MenuGame.py. Akan tetapi, jika password salah atau username "tidak terdaftar" (alias tidak ada di dictonary), maka user akan dibawa ke menu awal lagi, diminta untuk register, login, atau mengganti password.

Untuk program ini, username dan password disimpan dalam suatu dictionary dengan username sebagai key dan password sebagai value. 
Dictionary kemudian disimpan dalam file eksternal UsernamesDictionaries.txt.
Dictionary dimuat ke variabel DictUsers dengan function load_obj() dan meyimpan ke file UsernamesDictionaries.txt dengan function save_obj().

MenuGame.py dan MetodeBayar.py
Pada program ini ada beberapa function dan prosedur. Function yang ada "sort" berarti berfungsi untuk sorting/mengurutkan elemen dari elemen matrix. "asc" berarti dari kecil ke besar atau huruf a--huruf z; "dsc" berarti sebaliknya. Prosedur yang ada "print" berarti prosedur untuk mengeprint sesuatu, apapun itu. Pada program ini, hanya dibutuhkan function load_obj() untuk memuat review untuk game yang dipilih user yang kemudian akan dipilih secara acak untuk ditunjukkan ke user. 

Apabila user telah memilih game, akan ditunjukkan informasi mengenai game yang user pilih, kemudian akan diprint cara-cara membayar game yang dipilih. Setelah itu akan dibawa ke beberapa function di file MetodeBayar.py.

di MetodeBayar.CekBayar() dan MetodeBayar.Transfer() ada (ListReviews, GameName) padahal tidak digunakan. Hal ini karena kedua function tersebut (secara khusus, CekBayar) adalah transit dari file MenuGame.py ke Review.py. Kedua argumen tersebut akan digunakan di prosedur Review.PendapatGame().

Review.py
Function pertama dari program ini adalah PendapatGame(). Pada bagian ini, ListReviews akan di-append atau ditambahkan elemennya, yaitu review user yang telah membeli gamenya. Selanjutnya, GameName akan digunakan sebagai key untuk suatu dictionary yang memuat beberapa nama file berekstensi .txt yang di tiap file berisi sebuah array of strings yang berelemenkan review-review user sebelumnya yang sudah pernah membeli game itu.

Setelah user memberikan review tentan game, user akan diminta untuk mereview pelayanan program Uap. Setelah itu user akan dikembalikan lagi ke MenuGame.py sehingga user bisa keluar dari file tersebut.
