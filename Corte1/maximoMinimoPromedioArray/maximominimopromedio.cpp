#include <iostream>
#include <algorithm>
using namespace std;

int main () {
    int edad[5] = {23, 25, 34, 29, 16};
    sort(edad, edad + 5);
    cout << "Edad mínima: " << edad[0] << "\n";
    cout << "Edad máxima: " << edad[4] << "\n";
    cout << "Edad promedio: " << (edad[0] + edad[1] + edad[2] + edad[3] + edad[4]) / 5.0 << "\n";
    return 0;
}
