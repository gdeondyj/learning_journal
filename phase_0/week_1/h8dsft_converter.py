x = float(input('Masukan suhu: '))      #input angka yang akan digunakan untuk conversi

def k_ke_c(kc):                         #function untuk mengubah dari kelvin ke celcius
    kce = kc - 273.15                   #rumus
    return kce                          #mengubah (update) nilai kce

def k_ke_f(kf):                         #function untuk mengubah dari kelvin ke fahrenheit
    kfa = (((kf-273.15)*9/5)-32)        #rumus
    return kfa                          #mengubah (update) nilai kfa

def c_ke_k(ck):                         #function untuk mengubah dari celsius ke kelvin
    cke = ck + 273.15                   #rumus
    return cke                          #mengubah (update) nilai cke

def c_ke_f(cf):                         #function untuk mengubah dari celsius ke fahrenheit
    cfa = ((cf*9/5)+32)                 #rumus
    return cfa                          #mengubah (update) nilai cfa


def f_ke_c(fc):                         #function untuk mengubah dari fahrenheit ke celsius
    fce = ((fc-32)*5/9)                 #rumus
    return fce                          #mengubah (update) nilai fce

def f_ke_k(fk):                         #function untuk mengubah dari fahrenheit ke kelvin
    fke = ((((fk-32)*5/9)+273.15))      #rumus
    return fke                          #mengubah (update) nilai fke

kcel = k_ke_c(x)                        #memanggil function k_ke_c dengan input x
print(x, 'Kelvin =', kcel, '°Celsius')                 #mencetak conversi kelvin ke celsius

fceh = f_ke_c(x)                        #memanggil function f_ke_c dengan input x
print(x, '°Fahrenheit =', fceh, '°Celsius')                 #mencetak conversi fahrenheit ke celsius

ckel = c_ke_k(x)                        #memanggil function c_ke_k dengan input x
print(x, '°Celsius =', ckel, 'Kelvin')                   #mencetak conversi celsius ke kelvin

fkel = f_ke_k(x)                        #memanggil function f_ke_k dengan input x
print(x, '°Fahrenheit =', fkel, "Kelvin")                   #mencetak conversi fahrenheit ke kelvin

cfah = c_ke_f(x)                        #memanggil function c_ke_f dengan input x
print(x, '°Celsius =', cfah, '°Fahrenheit')              #mencetak conversi celsius ke fahrenheit

kfah = k_ke_f(x)                        #memanggil function k_ke_f dengan input x
print(x, 'Kelvin =', kfah, '°Fahrenheit')              #mencetak conversi kelvin ke fahrenheit