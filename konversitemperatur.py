#Program meminta pengguna untuk memasukkan suhu dalam derajat Celsius menggunakan fungsi input() dan menyimpan nilai tersebut dalam variabel celsius.
celsius = float(input("Masukkan suhu dalam derajat Celsius: "))

#Program menghitung suhu dalam derajat Fahrenheit dengan rumus (celsius * 9/5) + 32 dan menyimpan nilai tersebut dalam variabel fahrenheit.
fahrenheit = (celsius * 9/5) + 32

#Program mencetak hasil konversi suhu dalam format yang telah ditentukan menggunakan fungsi print(). Perhatikan bahwa :.1f digunakan untuk membatasi jumlah desimal yang dicetak menjadi satu angka saja.
print(f"{celsius:.1f} derajat Celsius = {fahrenheit:.1f} derajat Fahrenheit")