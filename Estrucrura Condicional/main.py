print("++++++++++++++ESTRUCTURA CONDICIONAL++++++++++++++ \n");

print("MENU\n");
print("1.Valor mayor y menor con dos números.");
print("2.Mayor, medio y menor valor con tres números.");
print("3.Comprobar si la suma es multiplo de 7.");
print("4.Promedio par o impar con tres números.");
print("5.Telefonía.");
print("6.Salir.\n")
menu=int(input("Ingrese su opción:"));

if menu == 1:
    num1 = int(input("Ingrese el primer número: "));
    num2 = int(input("Ingrese el segundo número: "));

    if num1 > num2:
        print("El numero mayor es "+str(num1)+", y el menor es "+str(num2));
    elif num2 > num1:
        print("El numero mayor es "+str(num2)+", y el menor es "+str(num1));
    else:
        print("Ambos son iguales");

elif menu == 2:
    num1 = int(input("Ingrese el primer número: "));
    num2 = int(input("Ingrese el segundo número: "));
    num3 = int(input("Ingrese el tercer número: "));

    if num1 > num2 and num1 > num3:

        if num2 > num3:
            print("Numero mayor: " + str(num1));
            print("Numero medio: " + str(num2));
            print("Numero menor: " + str(num3));
        else:
            print("Numero mayor: " + str(num1));
            print("Numero medio: " + str(num3));
            print("Numero menor: " + str(num2));
    elif num2 > num1 and num2 > num3:

        if num1 > num3:
            print("Numero mayor: " + str(num2));
            print("Numero medio: " + str(num1));
            print("Numero mayor: " + str(num3));
        else:
            print("Numero mayor: " + str(num2));
            print("Numero medio: " + str(num3));
            print("Numero menor: " + str(num1));
    elif num3 > num1 and num3 > num2:
        if num1 > num2:
            print("Numero mayor: " + str(num3));
            print("Numero medio: " + str(num1));
            print("Numero menor: " + str(num2));
        else:
            print("Numero mayor: " + str(num3));
            print("Numero medio: " + str(num2));
            print("Numero menor: " + str(num1));

elif menu == 3:
    num1 = int(input("Ingrese el primer número: "));
    num2 = int(input("Ingrese el segundo número: "));
    num3 = int(input("Ingrese el tercer número: "));

    resultado = float(num1+num2+num3);

    if resultado % 7 == 0:
        print(str(resultado) + ", es multiplo de 7");
    else:
        print(str(resultado) + ", no es multiplo de 7");

elif menu == 4:
    num1 = int(input("Ingrese el primer número: "));
    num2 = int(input("Ingrese el segundo número: "));
    num3 = int(input("Ingrese el tercer número: "));

    promedio = float((num1+num2+num3)/3)

    if promedio % 2 == 0:
        print(str(promedio) + ", es par");
    else:
        print(str(promedio) + ", es impar");

elif menu == 5:
    name = str(input("Ingrese su nombre: "));
    print("LOS PRIMEROS 25 MINUTOS SON GRATIS")
    minNacionales = int(input("Ingrese los minutos nacionales consumidos(Q): "));
    minInternacionales = int(input("Ingrese los minutos internacionales consumidos(Q): "));

    resultado1 = float(minInternacionales+minNacionales)

    if resultado1 <= 25:
        print("Minutos gratis.")
    elif minNacionales <= 25:
        acum  = float(minNacionales-25);
        minInternacionales = acum
        Total1 = float(minInternacionales * 2.25);
    else:
        minNacionales-=25
        total1 = (minNacionales*0.5)+(minInternacionales*2.25)

    print("\nFACTURA.\n");
    print("Usuario "+name)
    print("Total a pagar: Q"+str(Total1));

elif menu == 6:
    print("Saliendo...")
    exit();