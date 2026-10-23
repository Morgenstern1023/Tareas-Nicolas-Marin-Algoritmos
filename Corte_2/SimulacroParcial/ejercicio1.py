def recoger(n, k): 
  if n == 0: 
    return 0 
  if n % 2 == 0: 
    return k + recoger(n - 1, k + 1) 
  return recoger(n - 1, k) 
print(recoger(5, 1))

#Imprime 3
# El maximo de frames que llega a tener la función son 6
# recoger(5, 1)
# recoger(4,1)
# recoger(3,2)
# recoger(2,2)
# recoger(1,3)
# recoger(0,3)

#Si se quita el caso n = 0, la función entraría en recursión infinita y nunca terminaría, porque siempre haria el recoger(n-1,k)

