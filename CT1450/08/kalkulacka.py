def input_number() -> int:   # funkce nacte ze vstupu cislo    
    while True:
        try:
            return int(input("CISLO: "))
        except:
            print("TOTO NENI CISLO")

def input_operator() -> str: # nacte operator
    operator:str
    while True:
        operator = input("OPERATOR: ")
        if operator in ["+","-","="]:
            return operator

def calculate() -> int: # provede ceeeeelou radu vypoctu
    sum:int = input_number()

    while True:
        operator:str = input_operator()
        if operator == "=":
            break

        cislo:int = input_number()

        if operator == "+":
            sum += cislo
        elif operator == "-":
            sum -= cislo

    return sum

if __name__ == "__main__":
    print(calculate())