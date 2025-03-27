import math


def calculator():
    print("Bienvenido a la calculadora básica")
    print("Opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Exponente")
    print("6. Logaritmo (base 10)")
    print("7. Ingresar operación en formato matemático")


    try:
        choice = int(input("Selecciona una opción (1/2/3/4/5/6/7): "))
        if choice not in [1, 2, 3, 4, 5, 6, 7]:
            print("Opción no válida. Intenta de nuevo.")
            return

        if choice in [1, 2, 3, 4, 5]:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))

            if choice == 1:
                print(f"El resultado de la suma es: {num1 + num2}")
            elif choice == 2:
                print(f"El resultado de la resta es: {num1 - num2}")
            elif choice == 3:
                print(f"El resultado de la multiplicación es: {num1 * num2}")
            elif choice == 4:
                if num2 == 0:
                    print("Error: No se puede dividir entre cero.")
                else:
                    print(f"El resultado de la división es: {num1 / num2}")
            elif choice == 5:
                print(f"El resultado del exponente es: {num1 ** num2}")
        elif choice == 6:
            num = float(input("Introduce el número para calcular el logaritmo: "))
            if num <= 0:
                print("Error: El logaritmo solo está definido para números positivos.")
            else:
                print(f"El resultado del logaritmo base 10 es: {math.log10(num)}")
        elif choice == 7:
            operation = input("Introduce la operación matemática (por ejemplo, 3 + 5): ")
            try:
                result = eval(operation)
                print(f"El resultado de la operación '{operation}' es: {result}")
            except Exception as e:
                print(f"Error al evaluar la operación: {e}")
    except ValueError:
        print("Entrada no válida. Por favor, introduce números.")

# Ejecutar la calculadora
if __name__ == "__main__":
    calculator()
    