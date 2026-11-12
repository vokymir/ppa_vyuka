
def input_number() -> int:   # funkce nacte ze vstupu cislo    
    num: int 

    while True:
        try:
            num = int(input("Zadejte cislo: "))
            return num
        except:
            print("Toto neni cislo")


def input_operator() -> str: # nacte operator
    op: str 

    while True:
        op = input("Zadejte operator: ")

        if op in ["+","-","="]:
            return op
        else:
            print("Toto neni operator")


def calculator() -> int:
    sum: int = input_number()

    while True:
        op: str = input_operator()

        if op == "=":
            break

        cislo: int = input_number()

        if op == "+":
            sum += cislo
        elif op == "-":
            sum -= cislo

    return sum


if __name__ == "__main__":
    res: int = calculator()
    print(res)