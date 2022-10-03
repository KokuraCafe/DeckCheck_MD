from get_service import *
from read_ocr import *


def main():
    service = get_service()
    input_file = 'tmp/deck.jpg'
    output = read_ocr(service, input_file)
    print(output)
    
if __name__=="__main__":
    main()