
import sys
from setup import PACKAGE_NAME, ROOT_PATH

def main(): 
    print (f"{PACKAGE_NAME}: RTSAI")
    if (len(sys.argv) == 1 and sys.argv[0] == f'{ROOT_PATH}/{PACKAGE_NAME}'): 
        print (f"{PACKAGE_NAME}: Hello World! ")
