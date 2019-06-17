import sys
from html.parser import HTMLParser
import requests


class MyHTMLParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.print_flag = False
        self.print_2_flag = False

    # HTML Parser Methods
    def handle_starttag(self, startTag, attrs):
        if startTag == 'code':
            for element in attrs:
                if ('data-bufr' in element) and ('start' in element):
                    self.print_flag = True

                if ('data-bufr' in element) and ('end' in element):
                    self.print_2_flag = True

    def handle_data(self, data):
        if self.print_flag:
            data = data.replace('\\n', "\r\n")
            print(data)

        if self.print_2_flag:
            self.print_flag = False
            self.print_2_flag = False


# creating an object of the overridden class
parser = MyHTMLParser()

url = 'https://kunden.dwd.de/bufrviewer/uploadFile'

try:
    files = {'file': open(sys.argv[1], 'rb')}
    r = requests.post(url, files=files)
    # Feeding the content
    parser.feed(str(r.text))
except IndexError:
    print("Usage: python3 bufr2txt.py <input.bufr>")
    sys.exit(1)
