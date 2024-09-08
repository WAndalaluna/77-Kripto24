#include <iostream>
using namespace std;

string shift(string s, int k, bool encrypt)
{
    string s2;
    for (char c : s)
    {
        if (isalpha(c)) // Cek apakah karakter c adalah huruf
        {
            char base = islower(c) ? 'a' : 'A'; // Tentukan base ('a' untuk lowercase, 'A' untuk uppercase)
            int val = c - base;
            if (encrypt)
            {
                val = (val + k) % 26; // Enkripsi: Geser ke depan
            }
            else
            {
                val = (val - k + 26) % 26; // Dekripsi: Geser ke belakang
            }
            char c2 = base + val;
            s2 += c2;
        }
        else
        {
            s2 += c; // Jika bukan huruf, langsung tambahkan ke string hasil tanpa perubahan
        }
    }
    return s2;
}

int main() {
    string teks;
    int key;
    char pilihan;

    cout << "Masukkan Teks    = ";
    cin >> teks;
    cout << "Masukkan Key     = ";
    cin >> key;

    cout << "Pilih Operasi (e untuk enkripsi, d untuk dekripsi): ";
    cin >> pilihan;

    if (pilihan == 'e')
    {
        cout << "Hasil Enkripsi   = " << shift(teks, key, true) << endl;
    }
    else if (pilihan == 'd')
    {
        cout << "Hasil Dekripsi   = " << shift(teks, key, false) << endl;
    }
    else
    {
        cout << "Pilihan tidak valid!" << endl;
    }

    return 0;
}
