class Cliente:
    dias_reserva = 10 #Atributo de clase
    def __init__(self, nombre : str, numero : int, saldo : int = None):
        print("Construyendo el objeto",nombre)
        self.nombre = nombre.upper() #Atributos de instancia
        self.numero = numero
        self.saldo = saldo
        self.estado = None
        self.vehiculo_propio = False
        self._atributo_protected = "Atributo protegido"
        self.__atributo_privado = "El valor del atributo privado"

    def __del__(self):
        print("Destruyendo el objeto",self.nombre)

    def mostrar_atributo_privado(self):
        print("Atributo privado desde método de acceso:", self.__atributo_privado)

    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre : str) -> str:
        self.nombre = nombre.upper()
        return self.nombre

    @classmethod
    def soy_metodo_de_clase(cls):
        print(cls.dias_reserva)

    @staticmethod
    def soy_metodo_estatico():
        print("Soy un método estático")

    #Declarar el atributo como propiedad
    @property
    def atributo_privado(self):
        pass

    #Getter
    @atributo_privado.getter
    def atributo_privado(self):
        return self.__atributo_privado

    #Setter
    @atributo_privado.setter
    def atributo_privado(self, nuevo_valor):
        self.__atributo_privado = nuevo_valor


    def __str__(self) -> str:
        cliente_str = self.nombre + ":"+ str(self.numero) + ":" + str(self.saldo) + ":" + str(Cliente.dias_reserva)
        return cliente_str


claudia = Cliente("Caludia",150,2000)
fernando = Cliente("Fernando",151)
print(claudia.get_nombre())
print(fernando.get_nombre())
claudia.set_nombre("Claudia")
#fernando=None#Forzamos la destrucción del objeto
#del(fernando)#Forzamos la destrucción del objeto
print(fernando)
Cliente.dias_reserva=12
print(claudia)

#Potencialmente problemático - Se pueden agregar atributos en tiempo de ejecución
fernando.vehiculo_propios = True
print(fernando.vehiculo_propio)

#Invocación a método de clase
Cliente.soy_metodo_de_clase()
Cliente.soy_metodo_estatico()

#Acceso a atributos privados -- Sustituye __nombre_atributo por _Nombre_Clase__nombre_atributo
#No utilizar el acceso directo
print(fernando._Cliente__atributo_privado)
fernando.mostrar_atributo_privado()
print("Acceso a través de getter:", fernando.atributo_privado)
fernando.atributo_privado="Valor del atributo privado modificado"
print("Acceso a través de getter:", fernando.atributo_privado)

#Atributo protected
print(fernando._atributo_protected)

input("Pulsa ENTER para continuar...")


