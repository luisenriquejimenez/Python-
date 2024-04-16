if __name__ == '__main__':
    # crear lista
    lista1 = ['bah', 'beh', 'bih', 'boh']
    print(lista1)

    # recorrer lista
    for elemento in lista1:
        print(elemento)

    # compara lista
    lista2 = ['beh', 'bah', 'boh', 'bih']
    if lista1 == lista2:
        print("son identicas")

    # Longitud lista
    print(len(lista1))

    # concatenar lista
    print(lista1 + lista2)

    # numero maximo y minimo
    lista3 = [1, 2, 3, 4, 5]
    print(max(lista3))
    print(min(lista3))

    # listas enlazdas
    lista4 = ['Esto es', [1, 2, 3], 75]
    print(lista4)

    # Manipular datos
    lista5 = ['o', 'p', 'a']
    lista5.append('z')
    print(lista5)
    lista5.insert(0, 'x')
    print(lista5)
    lista5.extend(lista3)
    print(lista5)
    lista5.remove('z')
    print(lista5)
    for i in range(5):
        lista5.pop()
    print(lista5)
    lista5[0] = 's'
    print(lista5)

    # replicar lista
    lista6 = [1, 2, 3]
    print(lista6 * 2)

    # slicing
    lista7 = ['carimanola', 'pajarilla', 'bofe']
    print(lista7[1:2])
    lista8 = []
    for i in range(100):
        lista8.append(i)
    print(lista8[6:70])
    print(lista8[:51])
    print(lista8[25:])
