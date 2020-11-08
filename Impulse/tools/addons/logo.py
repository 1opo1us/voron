# Import modules
import sys
from colorama import Fore

# Logo
print(rf"""{Fore.MAGENTA}t o p o 1 u s - -{Fore.RESET}""")

lor=open('tools\addons\opw.txt','r')
lor=lor.read()
pos=input(str(lor))

if pos=='topo1us' or pos=='dbrnjhbz' or pos=='afhe':
    ops=open('tools\addons\openn.txt')
    ops=ops.read()
    print(str(ops))
else:
    rol=open('tools\addons\opwe.txt')
    rol=rol.read()
    print(str(rol))
    sys.exit()