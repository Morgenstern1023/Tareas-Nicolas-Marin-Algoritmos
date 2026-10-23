int v[] = {103, 118, 127, 134, 149, 156, 168, 175, 182, 190, 203, 219}; 
// idx: 0 1 2 3 4 5 6 7 8 9 10 11 
int buscar(int v[], int n, int x) { 
 int izq = 0, der = n - 1; 
 while (izq <= der) { 
 int medio = (izq + der) / 2; 
 if (v[medio] == x) return medio; 
 if (v[medio] < x) izq = medio + 1; 
 else der = medio - 1; 
 } 
 return -1; 
}

