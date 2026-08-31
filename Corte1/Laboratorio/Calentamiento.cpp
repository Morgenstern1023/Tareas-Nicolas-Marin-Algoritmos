#include <iostream>
using namespace std;

int v[4] = {5, 3, 9, 1};
int main() {
    int* p = v;
    cout << *(p + 2);
    // Esto imprimirá el valor 9, que es el tercer elemento del arreglo v.
    return 0;
}