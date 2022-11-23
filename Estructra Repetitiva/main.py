print("##########ESTRUCTURA REPETITIVA##########\n");

print("*****Menu*****\n");
print("1.Tabla de multiplicacion.");
print("2.Numeros impares.");
print("3.Números múltiplos.");
print("4.Salir.\n");
menu = int(input("Ingrese su opción: "))

if menu == 1:
    numTabla = int(input("Ingrese el número de tabla a multiplicar: "));
    numFinalizaTabla = int(input("Ingrese hasta que valor debe finalizar su tabla: "));

    if numTabla < 0:
        numTabla = (numTabla*-1);

        for i in range(numFinalizaTabla):
            multiplicador = int(1);
            multiplicador = i+1;
            resultado = int(numTabla*multiplicador);
            print(str(numTabla)+" * "+str(multiplicador)+" = "+str(resultado));

elif menu == 2:
    numMax = int(input("Ingrese el valor máximo: "));

    for i in range(numMax):
        if i % 2 == 1:
            print(i)

elif menu == 3:
    num1 = int(input("Ingrese un número (1 al 100): "))

    for i in range(100):
        if i % num1 == 0:
            print(i)