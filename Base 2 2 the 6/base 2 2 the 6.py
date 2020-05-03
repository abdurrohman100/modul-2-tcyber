# https://ctflearn.com/challenge/192
# https://www.asciitohex.com
# Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9

# hint Base 2 2 the 6 --> 2 square 6

import base64
# https://docs.python.org/3/library/base64.html
messege = "Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9"
decoded= base64.b64decode(messege)
hasil = decoded.decode('ascii')
print(hasil)

    
