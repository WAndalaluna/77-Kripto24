def buat_kunci(teks_asli, kunci):
    kunci = list(kunci)
    if len(teks_asli) == len(kunci):
        return kunci
    else:
        for i in range(len(teks_asli) - len(kunci)):
            kunci.append(kunci[i % len(kunci)])
    return "".join(kunci)

def enkripsi_vigenere(teks_asli, kunci):
    teks_sandi = []
    for i in range(len(teks_asli)):
        x = (ord(teks_asli[i]) + ord(kunci[i])) % 26
        x += ord('A')
        teks_sandi.append(chr(x))
    return "".join(teks_sandi)

def dekripsi_vigenere(teks_sandi, kunci):
    teks_asli = []
    for i in range(len(teks_sandi)):
        x = (ord(teks_sandi[i]) - ord(kunci[i]) + 26) % 26
        x += ord('A')
        teks_asli.append(chr(x))
    return "".join(teks_asli)

def main():
    while True:
        print("Menu:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Keluar")
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            teks_asli = input("Masukkan teks asli: ").upper()
            kunci = input("Masukkan kunci: ").upper()
            kunci = buat_kunci(teks_asli, kunci)
            teks_sandi = enkripsi_vigenere(teks_asli, kunci)
            print("Teks terenkripsi:", teks_sandi)
        elif pilihan == '2':
            teks_sandi = input("Masukkan teks sandi: ").upper()
            kunci = input("Masukkan kunci: ").upper()
            kunci = buat_kunci(teks_sandi, kunci)
            teks_asli = dekripsi_vigenere(teks_sandi, kunci)
            print("Teks terdekripsi:", teks_asli)
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()