import sys


def main():
    try:
        with open("rosalind_revc.txt") as file:
            texto = file.read().strip()

    except FileNotFoundError:
        sys.exit("file does not exists")
    
    rev = texto[::-1]

    for letra in rev:
        match letra:
            case "A":
                print("T", end="")
            case "T":
                print("A", end="")
            case "C":
                print("G", end="")
            case "G":
                print("C", end="")
            




if __name__ == "__main__":
    main()