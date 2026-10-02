#include <bits/stdc++.h>
using namespace std;

vector<int> siguienteMayor(const vector<int>& a) {
    int n = a.size();
    vector<int> result(n, -1);
    stack<int> pila;

    for (int i = 0; i < n; ++i) {
        while (!pila.empty() && a[i] > a[pila.top()]) {
            result[pila.top()] = a[i];
            pila.pop();
        }
        pila.push(i);
    }

    return result;
}
vector<int> reemplazoMenosUnoPorCero(const vector<int>& a) {
    vector<int> result = a;
    for (int& x : result) {
        if (x == -1) x = 0;
    }
    return result;
}
vector<int> siguienteMayorDistancia(const vector<int>& a) {
        int n = a.size();
    vector<int> result(n, -1);
    stack<int> pila;

    for (int i = 0; i < n; ++i) {
        while (!pila.empty() && a[i] > a[pila.top()]) {
            result[pila.top()] = a[i];
            int ind = pila.top();
            pila.pop();
            result[ind] = i - ind;
        }
        pila.push(i);
    }
    return reemplazoMenosUnoPorCero(result);
}
int main() {
    vector<int> a= {73,74,75,71,69,72,76,73};
    for (int x: siguienteMayorDistancia(a)) cout<<x<<" ";
}