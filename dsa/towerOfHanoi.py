def towerOfHanoi(n, frm, aux, to):
    if n > 0:
        towerOfHanoi(n - 1, frm, to, aux)
        print(f"Move {n} from {frm} to {to}.")
        towerOfHanoi(n - 1, aux, frm, to)


towerOfHanoi(4, 1, 2, 3)
