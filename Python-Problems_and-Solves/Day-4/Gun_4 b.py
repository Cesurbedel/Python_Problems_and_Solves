import time

def geri_say(number):
    for i in range(number, -1, -1):
        print(i)
        time.sleep(1)  # Her sayıdan sonra 1 saniye bekle

try:
    number = int(input("Geriye doğru sayılacak bir sayı girin: "))
    geri_say(number)
except ValueError:
    print("Lütfen geçerli bir sayı girin.")
