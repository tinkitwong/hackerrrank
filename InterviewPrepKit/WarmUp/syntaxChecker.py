def checker():
    with open("socks.py", 'r') as f:
        lines = f.readlines()
    f.close()
    print(lines)

    """ Grammer Rules 
    
    Prefix Characters


    Suffix Characters 
    \n 
    
    in-built types
    for / while 
    """
    def errorMessage(index, line):
        return f"ERROR: line {index} and line {line}"
    
    # def error()
    for line in lines:
        if line.startswith("def"):
            # check if the assertion 
            if line.endswith("():\n") == False:
                return errorMessage(lines.index(line), line)
            

checker()