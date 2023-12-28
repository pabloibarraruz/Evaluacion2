class MenuApp:
    def __init__(self):
        self.compras = []
        self.total_gastado = 0

    def agregar_compra(self):
        monto = float(input("Ingrese el monto de la compra: "))
        self.compras.append(monto)
        self.total_gastado += monto
        print(f"Compra de $ {monto} agregada correctamente.")

    def mostrar_compras(self):
        if not self.compras:
            print("No hay compras registradas.")
        else:
            print("Lista de compras:")
            for i, monto in enumerate(self.compras, 1):
                print(f"Compra {i}: ${monto}")

    def mostrar_total(self):
        print(f"Total gastado: ${self.total_gastado:.2f}")

    def main(self):
        while True:
            print("\nMenú:")
            print("1. Agregar compra")
            print("2. Mostrar compras")
            print("3. Mostrar total gastado")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_compra()
            elif opcion == "2":
                self.mostrar_compras()
            elif opcion == "3":
                self.mostrar_total()
            elif opcion == "4":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no es válida. Por favor, introduzca una opción válida.")

if __name__ == "__main__":
    app = MenuApp()
    app.main()
