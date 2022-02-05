if __name__ == '__main__':
    n = 5
    arr = map(int, "2 3 6 6 5".split())
    answer = list(set(arr))
    answer.sort()
    print(answer[-2])