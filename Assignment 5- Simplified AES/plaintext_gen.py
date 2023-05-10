
mapping = {'f':'0000', 'g':'0001', 'h':'0010', 'i':'0011', 'j':'0100', 'k':'0101', 'l':'0110', 'm':'0111', 'n':'1000', 'o':'1001', 'p':'1010', 'q':'1011', 'r':'1100', 's':'1101', 't':'1110', 'u':'1111'}

inverse_mapping = {}

for key in list(mapping.keys()):
    inverse_mapping[mapping[key]] = key


file = open("plaintexts.txt", "w")
for i in range(8):
    for j in range(8):
        fir = chr(ord('f')+j)
        for k in range(16):
            sec = chr(ord('f')+k)
            if fir=='f' and sec=='f':
                continue
            text = 'ff'*i + fir+sec+ 'ff'*(7-i)
            file.write(text+"\n")

file.close()
