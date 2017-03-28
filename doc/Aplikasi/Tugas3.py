print("Regional 1 : Harimau, Ayam, Gajah")
print("Manusia harus memindahkan semuanya dengan benar ke Regional 2")
a = raw_input('Mana Yang Harus Dipindahkan ? : ')
if a == "ayam":
        print("\nRegional 1 : Harimau, Gajah")
        print("Regional 2 : Ayam")
        b = raw_input('Lanjutkan, Pindahkan siapa ? : ')
        if b == "gajah":
                print("\nRegional 1 : Harimau")
		print("Regional 2 : Ayam, Gajah")
                c = raw_input('Lanjutkan, Pindahkan siapa ? : ')
                if c == "ayam":
                        print("\nRegional 1 : Harimau, Ayam ")
                        print("Regional 2 : Gajah")
                        d = raw_input('Lanjutkan, Pindahkan siapa ? : ')
                        if d == "harimau":
                                print("\nRegional 1 : Ayam ")
                                print("Regional 2 : Gajah, Harimau")
                                e = raw_input('Lanjutkan, Pindahkan siapa ? : ')
                                if e == "ayam":
                                        print("\nRegional 2 : Gajah, Harimau, Ayam")
                                        print("Selamat, Anda berhasil")
                                else:
                                        print('Maaf, Anda gagal')
                        else:
                                print('Maaf, Anda gagal')
                else:
                        print('Maaf, Anda gagal')
        else:
                print('Maaf, Anda gagal')
else:
        print('Maaf, Anda gagal')