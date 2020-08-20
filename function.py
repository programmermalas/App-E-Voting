# Import library yang diperlukan
from os import system, name

# Membuat function yang diperlukan

def clear():
    if name == 'nt':
        _ = system("cls")
    
    else:
        _ = system("clear")

def sendData(namaFile, data):
    f = open(namaFile, "a")
    f.write(data)
    f.close()

def hitungPemilih(namaFile):
    with open(namaFile) as file:
        for i, l in enumerate(file):
            pass
    return i + 1
