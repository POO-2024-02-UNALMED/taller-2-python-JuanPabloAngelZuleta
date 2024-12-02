class Asiento:
    def __init__(self, color: str, precio: float, registro: int):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, nuevo_color: str) -> None:
        colores_permitidos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if nuevo_color in colores_permitidos:
            self.color = nuevo_color


class Motor:
    def __init__(self, cilindros: int, tipo: str, registro: int):
        self.cilindros = cilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, nuevo_registro: int) -> None:
        self.registro = nuevo_registro

    def asignarTipo(self, nuevo_tipo: str) -> None:
        tipos_permitidos = ["gasolina", "electrico"]
        if nuevo_tipo in tipos_permitidos:
            self.tipo = nuevo_tipo


class Auto:
    cantidadCreados = 0  

    def __init__(self, modelo: str, precio: float, asientos: list, marca: str, motor: Motor, registro: int):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1 

    def cantidadAsientos(self) -> int:
        return sum(1 for asiento in self.asientos if isinstance(asiento, Asiento))

    def verificarIntegridad(self) -> str:
        registros_asientos = {asiento.registro for asiento in self.asientos if isinstance(asiento, Asiento)}
        if len(registros_asientos) == 1 and self.registro in registros_asientos and self.registro == self.motor.registro:
            return "Auto original"
        else:
            return "Las piezas no son originales"