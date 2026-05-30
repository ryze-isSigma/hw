import random

too = random.randint(1, 20)

print("Bi 1-ees 20-in hoorond neg too bodloo teriin ol")

while True:
    taamag = int(input("Toogoo oruul "))

    if taamag < too:
        print("Minii bodson too arai ih baina")
    elif taamag > too:
        print("Minii bodson too arai baga baina")
    else:
        print("zov taasan b")
        break



