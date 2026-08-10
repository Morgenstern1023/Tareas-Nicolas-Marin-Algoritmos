#include <iostream>
#include <string>
using namespace std;

int main()
{
    int suma1al00 = 0;
    int sumando = 0;
    
    while (sumando <= 100) {
        suma1al00 = suma1al00 + sumando;
        sumando++;
    }
    
    cout << "la suma del 1 al 100 es: " << suma1al00;
}