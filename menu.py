import os

def printMenu():
    print '\n','-----', 'Menu Glassfish', '-----', '\n'
    print '1)- Subir consola Vida'
    print '2)- Bajar consola Vida', '\n'
    print '3)- Subir consola Generales'
    print '4)- Bajar consola Generales', '\n'
    print '5)- Subir consola RRVV'
    print '6)- Bajar consola RRVV', '\n'
    print '0)- Salir', '\n'


def startMenu():

    os.system('clear')
    loop=True
    while loop:
        printMenu()

        
        choice = input("Ingrese una opcion [1-6] : ")

        if choice == 1:
            print 'Subiendo consola de Vida...'
            os.system('/opt/glassfish4/bin/asadmin start-domain domainVida')
            raw_input('\n Enter para continuar...')

        elif choice == 2:
            print 'Bajando consola de Vida...'
            os.system('/opt/glassfish4/bin/asadmin stop-domain domainVida')
            raw_input('\n Enter para continuar...')

        elif choice == 3:
            print 'Subiendo consola de Generales...'
            os.system('/opt/glassfish4/bin/asadmin start-domain domainGenerales')
            raw_input('\n Enter para continuar...')

        elif choice == 4:
            print 'Bajando consola de Generales...'
            os.system('/opt/glassfish4/bin/asadmin stop-domain domainGenerales')
            raw_input('\n Enter para continuar...')

        elif choice == 5:
            print 'Subiendo consola de RRVV...'
            os.system('/opt/glassfish4/bin/asadmin start-domain domainRRVV')
            raw_input('\n Enter para continuar...')

        elif choice == 6:
            print 'Bajando consola de RRVV...'
            os.system('/opt/glassfish4/bin/asadmin stop-domain domainRRVV')
            raw_input('\n Enter para continuar...')

        elif choice == 0:
            break
        else:
            raw_input("Opcion invalida, Enter para continuar...  ")

startMenu()