#include <iostream>
#include <string>
using namespace std;

// Clase PuntoAcopio con al menos tres atributos encapsulados (código, barrio, total recogido) y dos métodos con lógica real, por ejemplo registrarRecoleccion(kilos) y superaMeta(meta).
// Clase MaterialEspecial que herede de la anterior, agregue un atributo propio y redefina la descripción.
// Arreglo o lista con al menos cuatro objetos mezclando ambas clases, recorriéndolo y mostrando la descripción de cada uno. En C++ usar punteros a la clase base y verificar que virtual esté bien aplicado.

class PuntoAcopio {
private:
    int codigo;
    string barrio;
    float totalrecogido;

public:
    // Constructor
    PuntoAcopio(int c, string b, float t) : codigo(c), barrio(b), totalrecogido(t) {}

    //Setters
    virtual void setCodigo(int c) { codigo = c; }   
    virtual void setBarrio(string b) { barrio = b; }
    virtual void setTotalRecogido(float t) { totalrecogido = t; }

    //Getters
    virtual int getCodigo() const { return codigo; }
    virtual string getBarrio() const { return barrio; }
    virtual float getTotalRecogido() const { return totalrecogido; }

    // Método para registrar recolección
    void registrarRecoleccion(float kilos) {
        totalrecogido += kilos;
    }
    // Método para verificar si supera la meta
    bool superaMeta(float meta) const {
        if (totalrecogido > meta) {
            cout << "Se ha superado la meta." << endl;
            return true;
        } else {
            cout << "No se ha superado la meta." << endl;
            return false;
        }
    }
    virtual void descripcion() const {
        cout << "Código: " << codigo << ", Barrio: " << barrio << ", Total Recogido: " << totalrecogido << endl;
    }
};  

class MaterialEspecial : public PuntoAcopio {
private:
    string tipoMaterial;
public:
    // Constructor
    MaterialEspecial(int c, string b, float t, string tipo) : PuntoAcopio(c, b, t), tipoMaterial(tipo) {}

    // Setter
    void setTipoMaterial(string tipo) { tipoMaterial = tipo; }

    // Getter
    string getTipoMaterial() const { return tipoMaterial; }

    // Redefinir la descripción
    void descripcion() const override {
        cout << "Código: " << getCodigo() << ", Barrio: " << getBarrio() << ", Total Recogido: " << getTotalRecogido() << ", Tipo de Material: " << tipoMaterial << endl;
    }
};
