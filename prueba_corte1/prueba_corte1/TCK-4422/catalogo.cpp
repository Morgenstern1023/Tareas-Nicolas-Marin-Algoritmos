// ============================================================
//  Cívica Software  ·  TCK-4422  ·  Severidad P1
//  Sistema: PrestaLab  —  Nueva funcionalidad: catalogo mixto
//  El reporte imprime siempre "Recurso generico". Debe imprimir
//  la descripcion propia de cada tipo.
// ============================================================
#include <iostream>
#include <string>
using namespace std;

class Recurso {
protected:
    string codigo;
    bool   prestado;
public:
    Recurso(string c) : codigo(c), prestado(false) {}
    ~Recurso() {}

    void prestar()  { prestado = true; }
    bool estaPrestado() const { return prestado; }
// Se agrega virtual para que pueda ser sobreescrita con override en las clases hijas
    virtual string descripcion() const { return "Recurso generico " + codigo; }
};

// PENDIENTE: clase LibroFisico (hereda de Recurso, agrega autor)
//            descripcion() debe devolver:  "Libro " + codigo + " de " + autor
//Se agrega la clase LibroFisico que hereda de Recurso y agrega el atributo autor, se implementan los getters y setters y se sobreescribe la función descripcion para que devuelva la descripción de libro fisico y no de recurso
class LibroFisico : public Recurso {
private:
    string autor;
public:
    //Constructor
    LibroFisico(string c, string a) : Recurso(c), autor(a) {}
    //Getters y setters
    string getAutor() const { return autor; }
    void setAutor(string a) { autor = a; }
    //Se sobreescribe descripción para que devuelva la descripción de libro fisico y no de recurso
    string descripcion() const override { return "Libro " + codigo + " de " + autor; }
};

// PENDIENTE: clase Equipo (hereda de Recurso, agrega horasUso)
//            descripcion() debe devolver:  "Equipo " + codigo + " (" + horas + "h)"
//Se agrega la clase Equipo que hereda de Recurso y agrega el atributo horasUso, se implementan los getters y setters y se sobreescribe la función descripcion para que devuelva la descripción de equipo y no de recurso
class Equipo : public Recurso {
private:
    int horasUso;
public:
    //Constructor
    Equipo(string c, int h) : Recurso(c), horasUso(h) {}
    //Getters y setters
    int getHorasUso() const { return horasUso; }
    void setHorasUso(int h) { horasUso = h; }
    //Se sobreescribe descripción para que devuelva la descripción de equipo y no de recurso
    string descripcion() const override { return "Equipo " + codigo + " (" + to_string(horasUso) + "h)"; }
};

int main() {
    const int N = 3;
    Recurso* catalogo[N] = { nullptr, nullptr, nullptr };
    catalogo[0] = new Recurso("RG-001");
    // Se eliminan catalogo[1] y catalogo[2] de comentarios
    catalogo[1] = new LibroFisico("LF-002", "Borges");
    catalogo[2] = new Equipo("EQ-003", 12);
    //Usamos el metodo prestar() de la clase Recurso para marcar el libro como prestado
    catalogo[1]->prestar();   // se presta el libro

    int prestados = 0;
    for (int i = 0; i < N; i++) {
        if (catalogo[i] == nullptr) continue;
        cout << catalogo[i]->descripcion();
        if (catalogo[i]->estaPrestado()) { cout << "  [PRESTADO]"; prestados++; }
        cout << endl;
    }

    for (int i = 0; i < N; i++) {
        delete catalogo[i];   // delete sobre nullptr es seguro
        //Se agrega catalogo[i] = nullptr para evitar el pointer colgante después de liberar la memoria
        catalogo[i] = nullptr;
    }

};
