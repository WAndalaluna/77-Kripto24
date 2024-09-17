# Nama     : Wildan Rahmantya Andalaluna
# NPM      : 140810220077
# Kelas    : A
# Program  : Hill Cipher

import numpy as np

def char_to_number(x):
    return ord(x) - 65

def number_to_char(x):
    return chr(x + 65)

def mod_inverse(A, M):
    for X in range(1, M):
        if (A % M) * (X % M) % M == 1:
            return X
    return -1

def input_key(n):
    key = list(map(int, input("Masukkan nilai key matrix (dipisahkan spasi): ").split()))
    key = np.array(key).reshape(n, n) % 26
    print("Key Matrix: ")
    print(key)
    return key

def input_text(prompt):
    text = input(f"Masukkan {prompt}: ").replace(' ', '').upper()
    return text

def hill(method, text, key, n):
    key_det = int(np.linalg.det(key))
    if key_det % 2 == 0 or key_det == 13:
        print("Determinan bukan ganjil selain 13. Key tidak ada karena invers tidak ada.")
        return

    if len(text) % n != 0:
        last_char = text[-1]
        text += last_char * (n - len(text) % n)

    text_in_number = list(map(char_to_number, text))
    text_vector = np.array(text_in_number).reshape(-1, n)
    result = np.array([], dtype=int)

    if method == 'dekripsi':
        det_inverse = mod_inverse(key_det % 26, 26)
        key = (det_inverse * np.round(key_det * np.linalg.inv(key)).astype(int) % 26)

    for vector in text_vector:
        temp = np.matmul(key, vector.reshape(n, 1)) % 26
        result = np.append(result, temp)

    result = list(map(number_to_char, result))
    return ''.join(result)

def find_key(pt, ct, m):
    pt_in_number = list(map(char_to_number, list(pt)))
    pt_vector = np.array(pt_in_number).reshape(int(len(pt)/m), m)
    p_matrix = np.array([], dtype=int)
    ct_in_number = list(map(char_to_number, list(ct)))
    ct_vector = np.array(ct_in_number).reshape(int(len(ct)/m), m)
    c_matrix = np.array([], dtype=int)
    for i in range(m):
        c_matrix = np.append(c_matrix, ct_vector[i])
        p_matrix = np.append(p_matrix, pt_vector[i])
    c_matrix = np.transpose(c_matrix.reshape(m,m))
    p_matrix = np.transpose(p_matrix.reshape(m,m))
    p_det = int(np.linalg.det(p_matrix))
    if p_det % 2 == 0 or p_det == 13 :
        print("Determinan bukan ganjil selain 13. INVERS TIDAK ADA MAKA KEY TIDAK ADA.")
        return
    p_det_inverse = mod_inverse(p_det % 26, 26)
    p_inverse = (p_det_inverse * np.round(p_det * np.linalg.inv(p_matrix)).astype(int) % 26)
    key = np.matmul(c_matrix, p_inverse) % 26
    return key

def main():
    while True:
        print("\nHome")
        print("1. Enkripsi\n2. Dekripsi\n3. Cari Key\n4. Keluar")
        pilihan = input("Pilihan: ")

        if pilihan in ['1', '2']:
            n = int(input("\nMasukkan ukuran key matrix (n x n): "))
            key = input_key(n)
            text = ''
            while len(text) < n:
                text = input_text("text")
                if len(text) < n:
                    print("n harus bilangan prima terkecil sebagai faktor dari jumlah karakter")

            if pilihan == '1':
                print(f"\nPlaintext: {text}")
                output = hill("enkripsi", text, key, n)
                print(f"Ciphertext: {output}")
            elif pilihan == '2':
                print(f"\nCiphertext: {text}")
                output = hill("dekripsi", text, key, n)
                print(f"Plaintext: {output}")

        elif pilihan == '3':
            pt = input_text("plaintext")
            ct = input_text("ciphertext")
            m = int(input("\nMasukkan nilai m: "))
            print(f"\nPlaintext: {pt}\nCiphertext: {ct}")
            key = find_key(pt, ct, m)
            if key is not None:
                print("key:")
                print(key)

        elif pilihan == '4':
            break

        else:
            print("\nInput tidak sesuai.\n")

if __name__ == "__main__":
    main()

 
