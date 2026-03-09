def main():
    try:
        with open("rosalind_rna.txt") as file:
            dna = file.read().strip()
    except FileNotFoundError:
        print("File does not exists")
    else:
        rna = dna.replace("T", "U")
        print(rna)

     

if __name__ == "__main__":
    main()
