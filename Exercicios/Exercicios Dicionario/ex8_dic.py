d1={'a': 1, 'b': 2}
d2={'c': 3, 'd': 4}

d_final={}

for chave in d1:

    d_final[chave]=d1[chave]

for chave in d2:

    d_final[chave]=d2[chave]

print(d_final)