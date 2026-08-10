#include <iostream>
using namespace std;

int main()
{
    float deuda = 0;
    float deudaDescuento = 0;
    
    cout << "Escriba su deuda: ";
    cin >> deuda;
    
    if (deuda > 60000 && deuda < 150000) {
        deudaDescuento = deuda * 0.8;
    }
    else if (deuda < 300000) {
        deudaDescuento = deuda * 0.7;
    }
    else if (deuda < 800000) {
        deudaDescuento = deuda * 0.6;
    }
    else {
        deudaDescuento = deuda * 0.5;
    }
    cout << "su nueva deuda es: " << deudaDescuento;
}