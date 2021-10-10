import math

jmlhbensin = 66.25
kapasitastangki = 50
jmlhbanyakpengisian = jmlhbensin / kapasitastangki
totalpengisian = math.ceil(jmlhbanyakpengisian)

print('Pak Budi harus melakukan pengisian bensin sebanyak ' + str(totalpengisian) + ' kali')
