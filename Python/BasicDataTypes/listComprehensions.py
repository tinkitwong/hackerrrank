if __name__ == '__main__':
    x = 1
    y = 1
    z = 1
    n = 2
    # [[a,b,c for x,y,z in range(x,y,z)]]
    tmp = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1)]
    answer = [inner for inner in tmp if sum(inner) != n]
    print(answer)