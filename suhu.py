print ("PROGRAM KONVERSI TEMPERATURE")
print ("=============================")

celcius = float(input('masukan suhu celcius ='))
print('suhu =',celcius, 'C')

reamur = (4/5) * celcius
print('suhu dalam reamur =',reamur, 'R')

fahrenheit = ((9/5)*celcius)+32
print('suhu dalam fahrenheit =',fahrenheit, 'F')

kelvin = celcius + 273
print('suhu dalam kelvin =',kelvin, 'K')

print ("+++++++++++++++++++++++++++")
print ("\n FAHRENHEIT TO KELVIN \n")
print ("+++++++++++++++++++++++++++")

fahrenheit = float(input('Masukan Suhu Fahrenheit ='))
print('suhu =',fahrenheit, "F")

kelvin = ((9/5)*fahrenheit)-32 +273
print('suhu dalam kelvin =',kelvin,'K')

print("--------------------------------")
print("\n KELVIN TO FAHRENHEIT \n")
print("--------------------------------")

kelvin = float(input('Masukan Suhu Kelvin ='))
print('suhu =',kelvin, "K")

fahrenheit = (((9/5)*kelvin)-273)+32
print (' suhu dalam fahrenheit =',fahrenheit,"F")