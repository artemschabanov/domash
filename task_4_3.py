slovarb =  {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for s in list(slovarb.keys()):
    slovarb[s + str(len(s))] = slovarb.pop(s)
print(slovarb)