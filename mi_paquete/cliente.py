class Cliente:
    def __init__(self, nombre, apellido, correo, telefono, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono= telefono
        self.direccion = direccion

    def realizar_compra(self, producto):
        return f"{self.nombre} {self.apellido} ha comprado: {producto}"         

    def datos_de_entrega(self):
        return f"\nSe ha enviado a la dirección: {self.direccion} \nSu factura ha sido enviada correctamente al email: {self.correo} \nLe avisaremos cuando estemos en su domicilio al: {self.telefono}"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"