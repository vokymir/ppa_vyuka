import math

def f(x:float, a:float) -> float:
    if x == 0: return math.inf
    return 1/x * math.sin(math.pi * a * x)

# pro zadanou konstantu a, a pro x z intervalu <od; do> s krokem 0.1 ve formátu:
def f_for_range(start:float, end:float, a:float):
    step:float = 0.1
    num_steps:int = int( (end - start) / step )

    for i in range(num_steps + 1):
        x:float = start + i * step
        y:float = f(x,a)
        print(f"{x};{y}")

if __name__ == "__main__":
    f_for_range(0,1,4)