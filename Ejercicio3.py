if __name__ == '__main__':
    import re

    palabra = input("Placa a Evaluar: ",)

    if re.match('^([A-Z]{1,2}||[0-9]{1,2})[0-9]{4,5}$', palabra):

        #print("Coincidencia")

        if re.match('^MB[0-9]{4}$', palabra):

            print("Placa de Metro Bus")
        else:

            if re.match('^E[0-9]{4}$', palabra):
                print("Placa de Fiscal o Juez")

            else:

                if re.match('^PR[0-9]{4}$', palabra):
                    print("Placa de Periodista")
                else:

                    if re.match('^CP[0-9]{4}$', palabra):
                        print("Placa de la ACP")
                    else:

                        if re.match('^D[0-9]{4}$', palabra):
                            print("Placa de Vehiculos de Demostracion")
                        else:

                            if re.match('^CC[0-9]{4}$', palabra):
                                print("Placa de Cuerpo de Clausula")
                            else:

                                if re.match('^CH[0-9]{4}$', palabra):
                                    print("Placa de Cuerpo Honorario")
                                else:

                                    if re.match('^MI[0-9]{4}$', palabra):
                                        print("Placa de Mision Diplomatico")

                                    else:

                                        if re.match('^CD[0-9]{4}$', palabra):
                                            print("Placa de Cuerpo Diplomatico")
                                        else:

                                            if re.match('^M([A-Z]{2}||[0-9]){5}$', palabra):
                                                print("Placa de Moto")
                                            else:

                                                if re.match('^T[0-9]{5}', palabra):
                                                    print("Placa de Taxi")
                                                else:

                                                    if re.match('^RI[0-9]{4}', palabra):
                                                        print("Placa de Taxi Ruta interna")

                                                    else:
                                                        if re.match('[A-Z]{2}[0-9]{4}$', palabra):
                                                            print("Placa Particular")

                                                            if re.match('[A-Z][0-9]{5}', palabra):
                                                                print("Placa Particular")


    else:
        print('Error Digitos invalidos')
