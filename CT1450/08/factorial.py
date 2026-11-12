def fact(i: int)-> int:
    sum:int = 1
    for i in range(i,1,-1):
        sum *= i
    return sum

if(__name__ == "__main__"):
    print(fact(5))
