from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if data != '\n': 
            print(">>> Data")
            print(data)

    def handle_comment(self, data):
        if data != '\n': 
            print(">>> Single-line Comment" if '\n' not in data else ">>> Multi-line Comment")
            print(data)
        
    
# html = ""       
# for i in range(int(input())):
#     html += input().rstrip()
#     html += '\n'

parser = MyHTMLParser()

with open('./input_II.html','r') as f:
    for line in f.readlines():
        parser.feed(line)

parser.close()