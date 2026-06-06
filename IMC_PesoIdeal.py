import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class Persona:
    def __init__(self, peso, estaturaM, género, pesoIdeal=0):
        self.peso = peso
        self.estaturaM = estaturaM
        self.estaturaCM = estaturaM * 100  # ♥ Se deriva automáticamente de la estatura en metros
        self.género = género
        self.pesoIdeal = pesoIdeal

    def cálculo_imc(self):  # Calculamos el IMC uwu ♥
        return self.peso / (self.estaturaM ** 2)

    def mostrar_imc(self, imc):  # Aquí arroja el resultado de tu IMC y un mensajito uwu ♥♥
        if imc <= 18.0:
            return "Debajo de lo normal."
        elif imc <= 24.9:
            return "Peso normal ♥."
        elif imc <= 29.9:
            return "Sobrepeso."
        elif imc <= 34.9:
            return "Obeso."
        else:
            return "Muy obeso."

    def cálculo_PI(self):  # Aquí calculamos el peso ideal basado en género ♥
        if self.género == "h":
            F1, F2 = 2.25, 45
        else:
            F1, F2 = 2.7, 47.75
        self.pesoIdeal = ((self.estaturaCM - 152.4) / 2.54) * F1 + F2
        return self.pesoIdeal

    def pesoIdeal_ev(self):  # Evalúa el peso ideal en base a los datos proporcionados ♥♥
        limite = self.pesoIdeal * 0.10
        if self.peso < (self.pesoIdeal - limite):
            return "Debajo de su peso ideal :(."
        elif self.peso > (self.pesoIdeal + limite):
            return "Sobre su peso ideal :D."
        else:
            return "En su peso ideal ♥."


# ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ VALIDACIONES ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥

def validar_peso(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("♥ Favor de ingresar un valor positivo ♥.")
        except ValueError:
            print("♥ Favor de ingresar un número válido ♥.")


def validar_estaturaM(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("♥ Favor de ingresar un valor positivo ♥.")
            elif valor >= 3:
                print("♥ Favor de ingresar la estatura en METROS ♥.")
            else:
                return valor
        except ValueError:
            print("♥ Favor de ingresar un número válido ♥.")


def validar_género():
    while True:
        género = input("♥ Ingrese su género 'h' o 'm' ♥: ").strip().lower()
        if género in ["h", "m"]:
            return género
        else:
            print("♥ Opción inválida, favor de escribir 'h' o 'm'. ♥")


# ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ MOSTRAR IMÁGENES EN LA GRÁFICA IMC ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥

def mostrar_imagen_imc(imc, clasif):
    clasif_lower = clasif.lower()

    if "debajo" in clasif_lower:
        img_path = "bajo.png"
    elif "normal" in clasif_lower:
        img_path = "ideal.png"
    elif any(word in clasif_lower for word in ["sobrepeso", "obeso", "muy obeso"]):
        img_path = "obesidad.png"
    else:
        img_path = "bajo.png"

    try:
        img = mpimg.imread(img_path)
        plt.imshow(img)
        plt.axis('off')
        plt.title(f"IMC: {imc:.2f} → {clasif}")
        plt.show()
    except FileNotFoundError:
        print("Lo sentimos, la imagen no se encontró.")


# ♥ ♥ ♥ ♥  M E N Ú  ♥ ♥ ♥ ♥

def menú():
    print("\n ♥ MENÚ PRINCIPAL ♥")
    print("1. Calcular IMC ♥")
    print("2. Calcular Peso ideal ♥")
    print("3. Salir ♥")
    opc = input("♥ Selecciona una de las opciones anteriores ♥:  ").strip()
    return opc


# ♥ ♥ ♥ ♥ MAIN ♥ ♥ ♥ ♥

def main():
    while True:
        opc = menú()

        if opc == "1":
            print("\n ♥ CALCULAR IMC ♥")
            peso = validar_peso("♥ Ingrese su peso en kg ♥:  ")
            estaturaM = validar_estaturaM("♥ Ingrese su estatura en METROS ♥:  ")
            género = validar_género()

            persona = Persona(peso, estaturaM, género)
            imc = persona.cálculo_imc()
            clasif = persona.mostrar_imc(imc)

            print(f"\n ♥ Tu IMC es de ♥: {imc:.2f}")
            print(f" ♥ Tu IMC se clasifica como: {clasif}")

            mostrar_imagen_imc(imc, clasif)

        elif opc == "2":
            print("\n ♥ CALCULAR PESO IDEAL ♥")
            peso = validar_peso("♥ Ingrese su peso en kg ♥:  ")
            estaturaM = validar_estaturaM("♥ Ingrese su estatura en METROS ♥:  ")
            género = validar_género()

            persona = Persona(peso, estaturaM, género)
            pesoIdeal = persona.cálculo_PI()
            clasif_ideal = persona.pesoIdeal_ev()

            print(f"\n ♥ Tu peso ideal estimado es ♥: {pesoIdeal:.2f} kg.")
            print(f"♥ Usted está {clasif_ideal} ♥")

            plt.bar(["♥ Tu peso ♥", "♥ Peso ideal ♥"], [persona.peso, pesoIdeal], color=["pink", "magenta"])
            plt.title("♥ PESO ACTUAL   vs   PESO IDEAL ♥")
            plt.ylabel("Kilogramos")
            plt.show()

        elif opc == "3":
            print("\n ♥ GRACIAS POR UTILIZAR MI HUMILDE PROGRAMITA ♥")
            print(" \n ♥ ¡Hasta luego! ♥")
            break

        else:
            print("♥ Opción inexistente. Intenta nuevamente ♥")


if __name__ == "__main__":
    main()