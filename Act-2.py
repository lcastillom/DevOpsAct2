import argparse

class GestionClientes:
    def __init__(self):
        self.clientes = {}
    
    def agregar_cliente(self, id_cliente, nombre, email, telefono):
        if id_cliente in self.clientes:
            return "El cliente ya existe."
        else:
            self.clientes[id_cliente] = {'Nombre': nombre, 'Email': email, 'Teléfono': telefono}
            return "Cliente agregado correctamente."
    
    def modificar_cliente(self, id_cliente, nombre=None, email=None, telefono=None):
        if id_cliente in self.clientes:
            if nombre:
                self.clientes[id_cliente]['Nombre'] = nombre
            if email:
                self.clientes[id_cliente]['Email'] = email
            if telefono:
                self.clientes[id_cliente]['Teléfono'] = telefono
            return "Cliente modificado correctamente."
        else:
            return "Cliente no encontrado."
    
    def eliminar_cliente(self, id_cliente):
        if id_cliente in self.clientes:
            del self.clientes[id_cliente]
            return "Cliente eliminado correctamente."
        else:
            return "Cliente no encontrado."
    
    def mostrar_clientes(self):
        if self.clientes:
            return {id_cliente: datos for id_cliente, datos in self.clientes.items()}
        else:
            return "No hay clientes registrados."

# Ejemplo de uso
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gestión de Clientes")
    parser.add_argument("accion", choices=["crear", "actualizar", "consultar", "eliminar"], help="Acción a realizar")
    parser.add_argument("--id", type=int, help="ID del cliente")
    parser.add_argument("--nombre", help="Nombre del cliente")
    parser.add_argument("--email", help="Email del cliente")
    parser.add_argument("--telefono", help="Teléfono del cliente")
    
    args = parser.parse_args()
    
    gestion = GestionClientes()
    
    if args.accion == "crear":
        if args.id and args.nombre and args.email and args.telefono:
            print(gestion.agregar_cliente(args.id, args.nombre, args.email, args.telefono))
            print(gestion.mostrar_clientes())
        else:
            print("Faltan datos para crear el cliente.")
    
    elif args.accion == "actualizar":
        if args.id:
            gestion.agregar_cliente(1, "Juan", "juan@gmail.com", "123456789")
            print(gestion.modificar_cliente(args.id, args.nombre, args.email, args.telefono))
            print(gestion.mostrar_clientes())
        else:
            print("Falta el ID del cliente para actualizar.")
    
    elif args.accion == "consultar":
        gestion.agregar_cliente(1, "Juan", "juan@gmail.com", "123456789")
        gestion.agregar_cliente(2, "María", "maria@gmail.com", "987654321")
        gestion.agregar_cliente(3, "Pedro", "pedro@hotmail.com", "456123789")
        print(gestion.mostrar_clientes())

    elif args.accion == "eliminar":
        if args.id:
            gestion.agregar_cliente(1, "Juan", "juan@gmail.com", "123456789")
            print(gestion.eliminar_cliente(args.id))
            print(gestion.mostrar_clientes())