from random import choice
howbig = int(float(input("inserta el numero de caracteres que quieres en tu password    ")))

letters = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
numbers = ("1","2","3","4","5","6","7","8","9","0")
others = ("%" , "!" , "#" , "$" , "&" , "/" , "(" , ")" , "=" , "@" , "'" , "," )
total = letters + numbers + others
password = []

for i in range(howbig):
    caracter = choice( total )
    password.append( caracter )

password = "".join( password )
print("your password is  " + password)
