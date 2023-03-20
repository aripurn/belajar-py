print ("hello  world") 
print ("Ari Purnomo Aji")
print ("==== Buccellati Ultimate =====")
print ("ARI"*3)

a = 5
b = 3

hasil = a + b
print(a,'+',b,'=',hasil)    

hasil = a - b
print(a,'-',b'=',hasil)

hasil = a * b
print(a,'x',b,'=',hasil)

hasil = a / b
print(a,':',b,'=',hasil) 

#eksponen perpangkatan 
hasil = a ** b
print(a,'pangkat',b,'=',hasil)

#modulus
hasil = a % b #operasi sisa pembagian
print(a,'%',b,'=',hasil)

#floor Division
hasil = a // b #pembulatan pembagian antonim modulus
print(a,'//',b,'=',hasil)

#prioritas operasi
'''
1. ()
2. eksponen **
3. * / // % 
4, + -
'''
c = 22

hasil = (a**b)*c/a-a//b%c-a*c
print('(',a,'*',b,')','+',c,'/',a,'-',a,'//',b,'%',c,'+',a,'**',c,'=',hasil)


