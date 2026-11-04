
MATRIZ DE ADYACENCIA
              CEN  NOR  SUR  ORI  OCC  CHA  USA  BOS  VER
     CENTRO     0    1    1    1    0    0    0    0    0
      NORTE     1    0    0    0    1    1    0    0    1
        SUR     1    0    0    0    0    1    1    1    0
    ORIENTE     1    0    0    0    0    0    1    0    0
  OCCIDENTE     0    1    0    0    0    0    0    1    0
  CHAPINERO     0    1    1    0    0    0    1    1    1
    USAQUEN     0    0    1    1    0    1    0    0    1
       BOSA     0    0    1    0    1    1    0    0    1
     VEREDA     0    1    0    0    0    1    1    1    0

LISTA DE ADYACENCIA
      CENTRO -> NORTE, SUR, ORIENTE
       NORTE -> CENTRO, OCCIDENTE, CHAPINERO, VEREDA
         SUR -> CENTRO, CHAPINERO, USAQUEN, BOSA
     ORIENTE -> CENTRO, USAQUEN
   OCCIDENTE -> NORTE, BOSA
   CHAPINERO -> NORTE, SUR, USAQUEN, BOSA, VEREDA
     USAQUEN -> SUR, ORIENTE, CHAPINERO, VEREDA
        BOSA -> SUR, OCCIDENTE, CHAPINERO, VEREDA
      VEREDA -> NORTE, CHAPINERO, USAQUEN, BOSA

GRADO DE CADA VERTICE (cuantas vias salen de el)
      CENTRO: 3
       NORTE: 4
         SUR: 4
     ORIENTE: 2
   OCCIDENTE: 2
   CHAPINERO: 5
     USAQUEN: 4
        BOSA: 4
      VEREDA: 4

V = 9 vertices,  E = 16 aristas
  Matriz : 81 casillas en memoria. Existe arista? O(1). Recorrer vecinos: O(V) = 9 casillas.
  Lista  : 32 referencias en memoria. Existe arista? O(grado). Recorrer vecinos: O(grado).
  Densidad = 2E / (V(V-1)) = 0.44  ->  grafo DISPERSO: conviene lista
  Conecta BOSA con CENTRO? matriz=false  lista=false
  Conecta BOSA con NORTE? matriz=false  lista=false
  Conecta BOSA con SUR? matriz=true  lista=true
  Conecta BOSA con ORIENTE? matriz=false  lista=false
  Conecta BOSA con OCCIDENTE? matriz=true  lista=true
  Conecta BOSA con CHAPINERO? matriz=true  lista=true
  Conecta BOSA con USAQUEN? matriz=false  lista=false
  Conecta BOSA con VEREDA? matriz=true  lista=true


  PYTHON

  MATRIZ DE ADYACENCIA
             CEN  NOR  SUR  ORI  OCC  CHA  USA  BOS  VER
     CENTRO    0    1    1    1    0    0    0    0    0
      NORTE    1    0    0    0    1    1    0    0    1
        SUR    1    0    0    0    0    1    1    1    0
    ORIENTE    1    0    0    0    0    0    1    0    0
  OCCIDENTE    0    1    0    0    0    0    0    1    0
  CHAPINERO    0    1    1    0    0    0    1    1    1
    USAQUEN    0    0    1    1    0    1    0    0    1
       BOSA    0    0    1    0    1    1    0    0    1
     VEREDA    0    1    0    0    0    1    1    1    0

LISTA DE ADYACENCIA
      CENTRO -> NORTE, SUR, ORIENTE
       NORTE -> CENTRO, OCCIDENTE, CHAPINERO, VEREDA
         SUR -> CENTRO, CHAPINERO, USAQUEN, BOSA
     ORIENTE -> CENTRO, USAQUEN
   OCCIDENTE -> NORTE, BOSA
   CHAPINERO -> NORTE, SUR, USAQUEN, BOSA, VEREDA
     USAQUEN -> SUR, ORIENTE, CHAPINERO, VEREDA
        BOSA -> SUR, OCCIDENTE, CHAPINERO, VEREDA
      VEREDA -> NORTE, CHAPINERO, USAQUEN, BOSA

GRADO DE CADA VERTICE (cuantas vias salen de el)
      CENTRO: 3
       NORTE: 4
         SUR: 4
     ORIENTE: 2
   OCCIDENTE: 2
   CHAPINERO: 5
     USAQUEN: 4
        BOSA: 4
      VEREDA: 4

V = 9 vertices,  E = 16 aristas
  Matriz : 81 casillas en memoria. ¿Existe arista? O(1). Recorrer vecinos: O(V) = 9 casillas.
  Lista  : 32 referencias en memoria. ¿Existe arista? O(grado). Recorrer vecinos: O(grado).
  Densidad = 2E / (V(V-1)) = 0.44  ->  grafo DISPERSO: conviene lista
  ¿BOSA conecta con CENTRO? matriz=False  lista=False
  ¿BOSA conecta con NORTE? matriz=False  lista=False
  ¿BOSA conecta con SUR? matriz=True  lista=True
  ¿BOSA conecta con ORIENTE? matriz=False  lista=False
  ¿BOSA conecta con OCCIDENTE? matriz=True  lista=True
  ¿BOSA conecta con CHAPINERO? matriz=True  lista=True
  ¿BOSA conecta con USAQUEN? matriz=False  lista=False
  ¿BOSA conecta con VEREDA? matriz=True  lista=True