# Import library / module yang diperlukan
from getpass import *
import function as fc

fc.clear()
print("Admin Login")
userAdmin = str(input("Username : "))
passAdmin = str(getpass("Password : "))

if userAdmin == "root" and passAdmin == "rafliano123":
    fc.clear()
    # Membuat loop
    while True:
        print("Selamat datang di halaman admin!")
        adminInput = str(input("> ")).lower()

        if adminInput == "help":
            print("\nExit  -Keluar dari halaman admin")
            print("Quit  -Keluar dari halaman admin")
            print("Show all data - menampilkan semua data pemilih")
            print("Show data where pemilih = 1 -Menampilkan data pemilih 1")
            print("Show data where pemilih = 2 -Menampilkan data pemilih 2\n")

        elif adminInput == "exit" or adminInput == "quit":
            fc.clear()
            print("\n\n\nTerimakasih sudah menggunakan program kami..\n\n\n")
            break
            
        elif adminInput == 'show all data':
            print(f"\n\nPemilih 01 berjumlah {fc.hitungPemilih('pemilih01.txt')}")
            print(f"Pemilih 02 berjumlah {fc.hitungPemilih('pemilih02.txt')}\n\n")

        elif adminInput == "show data where pemilih = 1":
            print(f"\n\nPemilih 01 berjumlah {fc.hitungPemilih('pemilih01.txt')}\n\n")

        elif adminInput == "show data where pemilih = 2":
            print(f"\n\nPemilih 02 berjumlah {fc.hitungPemilih('pemilih02.txt')}\n\n")
        
        else:
            print("\n\nPerintah tidak sah!\n\n")

else:
    print("\n\nUsername / Password salah!")