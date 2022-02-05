def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):
        decimal = str(i) 
        octal = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        binary = bin(i)[2:]
        justificationLen = len(bin(number)[2:])
        print(decimal.rjust(justificationLen, " "), octal.rjust(justificationLen, " "), hexa.rjust(justificationLen, " "), binary.rjust(justificationLen, " "))
        # print(i.rjust(len(bin(i[2:]))," "), oct(i)[2:].center(len(bin(i[2:]))," "), hex(i)[2:].center(len(bin(i[2:]))," "), bin(i)[2:])
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)