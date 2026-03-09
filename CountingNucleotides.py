def main():
    try:
        with open("rosalind_dna.txt") as ficheiro:
            dna = ficheiro.read().strip()

        print(contador(dna))
    except FileNotFoundError:
        print("File not Found")




def contador(texto):
    a = texto.count("A")
    t= texto.count("T")
    c= texto.count("C")
    g= texto.count("G")
    return f"{a} {c} {g} {t}"


if __name__ == "__main__":
    main()