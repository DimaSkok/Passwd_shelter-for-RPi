alfa = '#$%&0123456789:;?@ABCDEFGHIJKLMNOPQRSUVWXYZ_`abcdefghijklmnopqrstuvwxyz '
key1 = ':xS;Y2qQK0ubz_7wH1yf6mOAa5%vNtoIRUM8gcn#3*DhrZ9WPe4BXJV@iEjl`?kd&FsCG$pL'
key2 = '@wDtJU7G9L%*kd?vg$IC:YMSEoi3WapRs4fQ;B#c02lNXeVxmrujhyq1HZ5`&n8OP_bA6KFz'
key3 = 'ekhW9;PDB$FupMUGd?o4`J:8fjHn1m6qx#ZVl&@5iazvIrQEb3KCgLys%_*AY2NOtS0Rc7Xw'
key4 = 'NOy%v@Ijxk1hblG?Sm_Rd`YDQ2gw$FM3C9pz4K7&Lq;eun8Pr0ciJZXH5EfA#V6B:*aoWsUt'
key5 = 'SrLt8ism*zx6ldBMvN2a37pE9&4kPK@WADG;Q:?Oy`H0gYV%UcnbqIh$Z1RX_o#J5jeuwFCf'
key0 = '432411331320401404214231320323001421030310204210213321203243401204114124'
keys = [key1, key2, key3, key4, key5]

#--------------------------------------------------
def writer (data):
    with open ('Shelter', 'a') as seo:
        seo.writelines(data)
        seo.close()
    return

def reader ():
    data = []
    with open('Shelter', 'r') as seo:
        data = seo.readlines()
        seo.close()
    return data

def deliter ():
    data = ''
    with open('Shelter', 'w') as seo:
        seo.writelines(data)
        seo.close()
    return
#--------------------------------------------------

text = reader()
copy_text = []

cheker = 0
for i in range(len(text)):
    copy_word = ''
    for j in range(len(text[i])):
        if cheker == (len(key0) - 1): cheker = 0
        index = keys[int(key0[cheker])].find(text[i][j])
        copy_word += alfa[index]
        cheker += 1
        # print(copy_word)
    copy_text = copy_word.split()
for i in range(len(copy_text)):
    copy_text[i] += '\n'
# print(copy_text)
deliter()
writer(copy_text)