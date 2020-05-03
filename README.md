# modul-2-tcyber

## Crytography

Cryptography adalah permasalahan untuk memecahkan suatu text yang terenkripsi untuk mendapatkan flag. Cryptography sendiri adalah problem analisis dan optimasi. Untuk memudahkan dalam mengerjakan soal cryptography kalian bisa mulai belajar bahasa python. 

Terdapat beberapa jenis metode enkripsi yang akan kita bahas.

### ASCII Encoding 
Pada ASCII enoding biasanya akan diberikan pesan berupa angka dalam format desimal atau hexadecimal. Ciri dari ASCII sendiri biasanya teerdiri dari value dari huruf dan angka pada  [ascii table]([https://link](https://www.ascii-code.com/)). Contoh tools yang bisa dipakai seperti [ini](https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html).
- 0-9 -> 49-57
- AZ -> 65-90 , 97-122
  
Contoh :
[Character Encoding](https://ctflearn.com/challenge/115)
>In the computing industry, standards are established to facilitate information interchanges among American coders. Unfortunately, I've made communication a little bit more difficult. Can you figure this one out? 41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D
<details>
  <summary>Solve</summary>
  
  >Ubah jadi integer kemudian ubah jadi ASCII
<details>
  <summary>Flags</summary>
  
  >ABCTF{45C11_15_U53FUL}
  
</details>
  
</details>



### Base Encoding
Pada Base xx encoding berarti akan terdapat xx karakter dasar yang masing masing memiliki index tersendiri. Setiap base encoding memiliki algoritma tersendiri untuk melakukan encoding.
Pada [base64](https://en.wikipedia.org/wiki/Base64) contohnya setiap string akan diubah menjadi binary, baru kemudian akan di dibagi menjadi 6 bits. 6 bits tersebut akan diubah sesuai index pada base64. Untuk menyelesaikanya bisa menggunakan pemrograman python atau menggunakan tools yang sudah ada diinternet seperti [ini](https://www.base64encode.org/) atau [ini](https://gchq.github.io/CyberChef/).

Contoh:
[Base 2 2 the 6](https://ctflearn.com/challenge/192)
>There are so many different ways of encoding and decoding information nowadays... One of them will work! Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9
<details>
  <summary>Solve</summary>
  
  >Decode dengan base64
<details>
  <summary>Flags</summary>
  
  >CTF{FlaggyWaggyRaggy}
</details>
  
</details>


## Caesar Cipher
Caesar Cipher adalah enkripsi yang menggunakan urutan abjad sebagai enkripksi.
MISAL Caesar cipher dari Hello World dengan shift 10, akan mengubah urutan abjad yang awalnya dimulai dengan a/A menjadi k/K. Artinya string "Hello World" akan diubah menjadi "Rovvy gybvn".
Caesar cipher biasanya memiliki ciri tersusun dari susunan abjad yang abstrak.  Cara menyelesaikanya biasanya menggunakan script pyhton atau menggunakan [solver online](https://www.xarg.org/tools/caesar-cipher/).

## Subtitution Cipher 
Subtitution Cipher mirip dengan Caesar cipher hanya saja kita bebas mennganti set alphabetnya.
## Vignere Cipher
Vignere Cipher merupakan pengembangan Caesar Cipher, dimana string dienkripsi dengan kumpulan caesar cipher. Jika suatu string tidak bisa di decode menggunakan Caesar cipher maka bisa jadi itu adalah Vignere cipher. Tantangan pada problem ini biasanya mmencari key yang dubutuhkan untuk melakukan dekripsi.
<!-- ![Vignere Table](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Vigen%C3%A8re_square_shading.svg/800px-Vigen%C3%A8re_square_shading.svg.png) -->

Pada table Vignere kita bisa melihat bahwa table itu berisi kumpulan caesar cipher.
Misal kita punya strings "VIGNERE" dan key "TCKS", 
![alt](/src/CKS.png)
Kita lakukan enkripsi seperti berikut. Huruf V akan di caesar cipher denga shift sebanyak T sehingga menghasilkan O, I di shift dengan C sehinggga menghasilkna K, G di shift dengan K menghasilkan Q, N di shift dengan S menghasilkan F, kemudia key nya kembali lagi ke T. sehingga E dishift dengan T menghasilkan X dan seterusnya. Untuk dekripsinya tinggal dibalik mengurangi pesan yang sudah terenkripsi dengan keynya. 
Untuk penyelesaikan permasalahan ini bisa menggunakan python atau menggunakan website seperti [ini](http://www.counton.org/explorer/codebreaking/vigenere-cipher.php).


## RSA 
RSA adalah sebuah enkripsi dengan mengggunakan suatu public key tertentu. Kemudian untuk melakukan dekripsi kita harus menggunaan private key. RSA ini termasuk problems yang sering muncul pada perlombaan ctf. Untuk lebih jelas mengenai RSA bisa dibaca [disini](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) dan [disni](https://ctf101.org/cryptography/what-is-rsa/). Biasanya problem RSA ini harus diselesaikan dengan bahasa python atu menggunakan RSA Tool.