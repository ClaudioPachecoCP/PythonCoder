from mi_paquete.cliente import Cliente

cliente1 = Cliente("Claudio", "Pacheco", "claudiop@email.com", "4956 28722", "Una calle nos separa 3011")
cliente2 = Cliente("Andrés", "Santurio", "andresS@correo.com", "8425 45242","Bulevar de los sueños rotos 8022")

print(cliente1.realizar_compra("celular"))
print(cliente1.datos_de_entrega())
print("Gracias por su compra",cliente1 )
print(" ")
print(cliente2.realizar_compra("tv"))
print(cliente2.datos_de_entrega())
print("Gracias por su compra",cliente2)