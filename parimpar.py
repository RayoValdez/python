# par_impar.py
def check_par_impar(numar):
    if numar % 2 == 0:
        print(f"Numarul introdus {numar} este par.")
    else:
        print(f"Numarul introdus {numar} nu este par.")

# Get input for the number
numar = int(input("Introduceti un numar: "))

# Check and print if the number is even or odd
check_par_impar(numar)

