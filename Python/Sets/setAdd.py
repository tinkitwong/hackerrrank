from typing import Counter


def countCountries(a):
    N = 7
    set_countries = set()
    for _ in range(N):
        set_countries.add(a[_])
    print(len(set_countries))


a=["UK","China","USA","France","New Zealand", "UK", "France"]
countCountries(a)