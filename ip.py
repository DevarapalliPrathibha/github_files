import os,ipaddress

os.system('cls')

while True:
    ip = input('Enter IP Addresss:')
    try:
        print(ipaddress.ip_address(ip))
        print('IP Vaild')
    except:
        print('-'*50)
        print('IP is Not Vaild')
    finally:
        if ip == 'mango':
            print('Script Finished')
            break

print(os.system("ipconfig"))