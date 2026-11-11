from math import sin, pi, inf

def evaluate_fn(a:float, x:float) -> float:
    if x == 0: return inf
    return 1/x * sin(pi * a * x)

def wave(a:float, x0:float, x1:float):
    step:float = 0.1
    steps:int = int((x1 - x0) / step)
    for i in range(0, steps + 1):
        x:float = x0 + i * step
        y:float = evaluate_fn(a, x)
        print(f"{x};{y}")

if __name__ == "__main__":
    wave(4, 0, 1)