d={'a':1, 'b': 2, 'c': 3}

invertido={}

invertido = {value: key for key, value in d.items()}

print(invertido)