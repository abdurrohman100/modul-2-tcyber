# modul-2-tcyber

## Crytography

Cryptography adalah permasalahan untuk memecahkan suatu text yang terenkripsi untuk mendapatkan flag. Cryptography sendiri adalah problem analisis dan optimasi. Untuk memudahkan dalam mengerjakan soal cryptography kalian bisa mulai belajar bahasa python. 

Terdapat beberapa jenis metode enkripsi yang akan kita bahas.

### ASCII Encoding 
Pada ASCII enoding biasanya akan diberikan pesan berupa angka dalam format desimal atau hexadecimal. Ciri dari ASCII sendiri biasanya teerdiri dari value dari huruf dan angka pada  [ascii table]([https://link](https://www.ascii-code.com/)). Contoh tools yang bisa dipakai seperti [ini](https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html).
- 0-9 -> 49-57
- AZ -> 65-90 , 97-122
  
Contoh :
>[Character Encoding](https://ctflearn.com/challenge/115)
>In the computing industry, standards are established to facilitate information interchanges among American coders. Unfortunately, I've made communication a little bit more difficult. Can you figure this one out? 41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D

<details>
  <summary>Flags</summary>
  
  >ABCTF{45C11_15_U53FUL}
  
</details>


### Base Encoding
Pada Base xx encoding berarti akan terdapat xx karakter dasar yang masing masing memiliki index tersendiri. Setiap base encoding memiliki algoritma tersendiri untuk melakukan encoding.
Pada [base64](https://en.wikipedia.org/wiki/Base64) contohnya setiap string akan diubah menjadi binary, baru kemudian akan di dibagi menjadi 6 bits. 6 bits tersebut akan diubah sesuai index pada base64. Untuk menyelesaikanya bisa menggunakan pemrograman python atau menggunakan tools yang sudah ada diinternet seperti [ini](https://www.base64encode.org/) atau [ini](https://gchq.github.io/CyberChef/).

Contoh:
>[Base 2 2 the 6](https://ctflearn.com/challenge/192)
>There are so many different ways of encoding and decoding information nowadays... One of them will work! Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9

<details>
  <summary>Flags</summary>
  
  >CTF{FlaggyWaggyRaggy}
</details>


## Caesar Cipher
Caesar Cipher adalah enkripsi yang menggunakan urutan abjad sebagai enkripksi.
MISAL Caesar cipher dari Hello World dengan shift 10, akan mengubah urutan abjad yang awalnya dimulai dengan a/A menjadi k/K. Artinya string "Hello World" akan diubah menjadi "Rovvy gybvn".
Caesar cipher biasanya memiliki ciri tersusun dari susunan abjad yang abstrak.  Cara menyelesaikanya biasanya menggunakan script pyhton atau menggunakan [solver online](https://www.xarg.org/tools/caesar-cipher/).

## Vignere Cipher
Vignere Cipher merupakan pengembangan Caesar Cipher, dimana string dienkripsi dengan kumpulan caesar cipher. Jika suatu string tidak bisa di decode menggunakan Caesar cipher maka bisa jadi itu adalah Vignere cipher. Tantangan pada problem ini biasanya mmencari key yang dubutuhkan untuk melakukan dekripsi.
<!-- ![Vignere Table](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Vigen%C3%A8re_square_shading.svg/800px-Vigen%C3%A8re_square_shading.svg.png) -->

Pada table Vignere kita bisa melihat bahwa table itu berisi kumpulan caesar cipher.
Misal kita punya strings "VIGNERE" dan key "TCKS", 

![TCKS Vignere Table](https://github.com/abdurrohman100/modul-2-tcyber/blob/master/src/TCKS.png)


Kita lakukan enkripsi seperti berikut. Huruf V akan di caesar cipher denga shift sebanyak T sehingga menghasilkan O, I di shift dengan C sehinggga menghasilkna K, G di shift dengan K menghasilkan Q, N di shift dengan S menghasilkan F, kemudia key nya kembali lagi ke T. sehingga E dishift dengan T menghasilkan X dan seterusnya. Untuk dekripsinya tinggal dibalik mengurangi pesan yang sudah terenkripsi dengan keynya. 
Untuk penyelesaikan permasalahan ini bisa menggunakan python atau menggunakan website seperti [ini](http://www.counton.org/explorer/codebreaking/vigenere-cipher.php).

Contoh
>[Vigenere Cipher](https://ctflearn.com/challenge/305)
>The vignere cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers based on the letters of a keyword.I’m not sure what this means, but it left lying around: blorpy gwox{RgqssihYspOntqpxs}
<details>
  <summary>Flags</summary>
  
  >FLAG{CiphersAreAwesome}
</details>


## Subtitution Cipher 
Subtitution Cipher mirip dengan Caesar cipher hanya saja kita bebas mennganti set alphabetnya. Pada problem ini biasanya kita harus menebak alphabet set nya untuk mendapatkan hasil enkripsinya,
>[Subtitution Cipher](https://ctflearn.com/challenge/238)
>Someone gave me this, but I haven't the slightest idea as to what it says! https://mega.nz/#!iCBz2IIL!B7292dJSx1PGXoWhd9oFLk2g0NFqGApBaItI_2Gsp9w Figure it out for me, will ya?
<details>
  <summary>Isi File</summary>
  
  
>MIT YSAU OL OYGFSBDGRTKFEKBHMGCALSOQTMIOL. UTFTKAMTR ZB DAKQGX EIAOF GY MIT COQOHTROA HAUT GF EASXOF AFR IGZZTL. ZT CTKT SGFU, MIT YSACL GF A 2005 HKTLTFM MODTL MIAF LMADOFA GK A CTTQSB LWFRAB, RTETDZTK 21, 1989 1990, MIT RKTC TROMGKL CAL WHKGGMTR TXTKB CGKSR EAF ZT YGWFR MIT EGFMOFWTR MG CGKQ AM A YAOMIYWS KTHSOTL CITKT IGZZTL, LMBST AOD EASXOF, AMMAEQ ZGMI LORTL MG DAKQL, "CIAM RG EGFMKGSSOFU AF AEMWAS ZGAKR ZGVTL OF MIT HKTHAKTFML FADT, OL ODHWSLOXT KADHAUTL OF CIOEI ASCABL KTYTKTFETL MIT HALLCGKR, CIOEI DGFTB, AFR MITB IAR SOMMST YKGFM BAKR IOL YKWLMKAMTR EGSGK WFOJWT AZOSOMB COMI AFR OFROLHTFLAMT YGK MTAEI GMITK LMWROTL, AKT ACAKRL ZARUTL, HWZSOLITR ZTYGKT CTSS AL A YOKT UKGLL HSAFL CTKT GKOUOFASSB EIAKAEMTKL OF MIT LMKOH MG CIOEI LTTD MG OM CITF MTDHTKTR OF AFR IASSGCOFU MITB'KT LODHSB RKACOFU OF UOXTL GF" HKOFEOHAS LHOMMST ROLMGKM, KTARTKL EGDOEL AKT WLT, CAMMTKLGF MGGQ MCG 16-DGFMIL AYMTK KTLOLMAQTL A DGKT EKTAM RTAS MG EASXOF GYMTF IGZZTL MG ARDOML "LSODB, "ZWM OM'L FADTR A FOUIM GWM LIT OL HGOFM GY FGM LTTF IGZZTL MIT ZGGQL AM MIAM O KTDAOFOFU ZGGQ IADLMTK IWTB AKT AHHTAKAFET: RTETDZTK 6, 1995 DGD'L YKADTL GY EASXOF UOXTF A CAUGF, LGDTMODTL MIAM LG OM'L YAMITKT'L YADOSB FG EAFETSSAMOGFLIOH CAL HKTLTFML YKGD FGXTDZTK 21, 1985 SALM AHHTAK AZLTFET OF AFGMITKCOLT OM IAHHB MG KWF OM YGK MIOL RAR AL "A SOMMST MG MGSTKAMT EASXOF'L YADOSB RKACF ASDGLM EGDDTFRTR WH ZTOFU HTGHST OFLMAFET, UTM DAKKOTR ZB A RAFET EASXOF'L GWMSAFROLOFU MIT FTCLHAHTK GK MAZSGOR FTCLHAHTK ZWLOFTLL LIGC OL GF!" AFR LHKOFML GY EIOSRKTF'L RAR'L YKWLMKAMTR ZB MWKF IWDGK, CAL HWZSOE ROASGU MITKT'L FGM DWEI AL "'94 DGRTKFOLD" CAMMTKLGF IAL RTSOUIML GY YAFMALB SOYT CAMMTKLGF LABL LTKXTL AL AF AKMOLML OL RTLMKWEMOGF ZWLOFTLL, LHAETYAKTK GY MIT GHHGKMWFOMOTL BGW ZGMI A MGHOE YGK IOL IGDT MGFUWT-OF-EITTQ HGHWSAK MIAM OM CAL "IGF" AFR JWAKMTK HAUT DGKT LHAEOGWL EAFETSSAMOGF MIT HAOK AKT ESTAKSB OF HLBEIOE MKAFLDGUKOYOTK'L "NAH" LGWFR TYYTEM BGW MIOFQTK CAMMTKLGF ASLG UKTC OFEKTROZST LHAET ZWBL OF EGDDGFSB CIOST GMITKCOLT OM'L FADT OL FGMAZST LMGKBSOFT UAXT MIT GHHGKMWFOMOTL BGW EAFETSSAMOGF MIT "EASXOF GYYTK MG DAQT IOD OFEGKKTEM AFLCTKL CAMMTK AKMCGKQ GMITK GYMTF CIOEI OL TXORTFM MG GMITK LMKOH OL MG MITOK WLT GY KWSTL MIAM LIGCF GF LAFROYTK, CIG WLTL A EKGCJWOSS ZT LTTF "USWTR" MG MIT GFSB HTKL AFR IOL YAMITK LWHHGKM OL SWFEISOFT UAXT MITLT MIOF A BTAK OF DWSMODAMTKOAS AFR GZMAOF GF LAFMALB, IOL WLT, CAMMTKL ROASGUWT OL AF "AKMOLM'L LMAMWL AL "A ROD XOTC OF MIT TLLTFMOASSB MG DAQT IOD LTTD MG OFESWRTR MIAM EASXOF OL AF GRR ROASGUWT DGLM GY MIT ESWZ IAL TVHKTLLOGF GWMLORT AXAOSAZST MG
</details>

<details>
  <summary>Flags</summary>
  
  >IFONLYMODERNCRYPTOWASLIKETHIS
</details>



## RSA 
RSA adalah sebuah enkripsi dengan mengggunakan suatu public key tertentu. Kemudian untuk melakukan dekripsi kita harus menggunaan private key. RSA ini termasuk problems yang sering muncul pada perlombaan ctf. Untuk lebih jelas mengenai RSA bisa dibaca [disini](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) dan [disni](https://ctf101.org/cryptography/what-is-rsa/). Untuk step by step bisa dilihat [disini](https://www.cryptool.org/en/cto-highlights/rsa-step-by-step). Biasanya problem RSA ini kebanyakan diselesaikan dengan scripting bahasa python atau menggunakan RSATool.
