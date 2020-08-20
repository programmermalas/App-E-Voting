# Import module function
import function as fc

# Membuat Loop
while True:
    fc.clear()
    print("SELAMAT DATANG DI PROGRAM E-VOTING")
    print("1. Pitagoras, Trigonometri")
    print("2. Aljabar, Vector")
    print("99. Exit")
    evoting = str(input("Masukkan Pilihan : "))

    if evoting == "1":
        fc.sendData(r"pemilih01.txt", r"""Pemilih 01
""")
    elif evoting == "2":
        fc.sendData(r"pemilih02.txt", r"""Pemilih 02
""")
    elif evoting == "99":
        fc.clear()
        print("\n\n\nTerimakasih sudah menggunakan program kami!\n\n\n")
        break
    else:
        fc.clear()
        print("\n\nMasukkan pilihan yang benar!\n\n")

