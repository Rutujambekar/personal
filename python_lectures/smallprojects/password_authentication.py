import getpass
data = {"rutuj_amb":'345123', "amb_rutuj":'897561'}
username = input("enter your username:")
password = getpass.getpass("enter your password:")
for i in data.keys:
    if username == i:
        while password!=data.get(i):
            password = getpass.getpass("enter your password again:")
        break
print("verified password")    
