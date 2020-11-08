import os
os.system('cd')
os.system('echo cd voron >> topo1us.sh')
os.system('echo python voron.py >> topo1us.sh')
os.system('chmod +x topo1us.sh')
print('для дальнейшего использования voron Вам достаточно ввести команду \033[31m./topo1us.sh\033[32m\n')
print('\nперезапустите систему\n(перезайдите в Termux).')