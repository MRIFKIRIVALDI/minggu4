# konversi satuan temperature


print("\nPROGRAM KONVERSI TEMPERATURE\n")

celcius = float(input("Masukan suhu dalam celcius : "))
print("suhu",celcius, "Celcius")

#reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah ",reamur, "Reamur")

#fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit ",fahrenheit, "fahrenheit")

#kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah ", kelvin, "Kelvin")