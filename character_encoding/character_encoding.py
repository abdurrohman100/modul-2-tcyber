#https://ctflearn.com/challenge/115
#soal
messege="41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D"
#buat list karakternya
messegelist=messege.split()
#buat list untuk menyimpan hasil
hasil=""

for i in messegelist:
    #ubah base 16 jadi integer
    temp= int(i,16)
    #ubah integer menjadi string
    hasil+=chr(temp)
#print
print (hasil)
    