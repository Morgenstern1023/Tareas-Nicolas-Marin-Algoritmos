
comparaciones = 0
v = [42, 17, 93, 8, 55, 31] 
for i in range(1, len(v)): 
    actual = v[i] 
    j = i - 1 
    while j >= 0 and v[j] > actual: 
        v[j + 1] = v[j] 
        j -= 1 
        comparaciones += 1
    v[j + 1] = actual

#Impresiondel paso a paso
for i in range(len(v)):
    print(f"Paso {i}: {v[:i+1]}")
print(f"Total de comparaciones: {comparaciones}")
