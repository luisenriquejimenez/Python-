class cliente:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio

    def total(self,precio):
        total = precio*1.07
        return total

    def imprimir(self):
        return ""

if __name__ == '__main__':
    print('FONDA LA SABROSONA')
    print("------------------\n")

    cliente = input("Cliente: ")
    Menu = {1: 'Mondongo $1.50',
            2: 'Lengua $0.75',
            3: 'Pata $2.00'
            }

    print('\nMENU')
    print(Menu)
    opcion = int(input("Opcion: "))

    lista = [['mondongo', 1.5], ['lengua', 0.75], ['pata', 2.00]]
    if opcion == 1:
        precio = lista[0][1]
        comida = lista[0][0]
    elif opcion == 2:
        precio = lista[1][1]
        comida = lista[1][0]
    elif opcion == 3:
        precio = lista[2][1]
        comida = lista[2][0]
    else:
        print("Opcion invalida")

    total = precio

    print(cliente + ", debe pagar $" + str(total))

    pago = input("Pago? (S/N)")
    if pago.upper() == "S":
        print("Toma tu", comida + ",", cliente)
    else:
        print('Pedido cancelado!!!')
