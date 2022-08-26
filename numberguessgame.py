
from random import randint

def main():

    numero = randint(1,100)
    arvaukset = 0
    
    while True:
        try:
            if arvaukset == 10: 
                print(f"\nHihihii hävisit pelin. Arvattava numero oli {numero}")
                break
            arvaus = int(input("\nMitä numeroa ajattelen väliltä 1-100? (Voit luovuttaa antamalla numeron 666)  "))
            if arvaus == numero: 
                print("\n")
                print("\nArvasit numeron oikein!")
                print(f"\nSinulla meni {arvaukset+1} yritystä arvata oikein")        
                break
            elif arvaus == 666:
                print("\nLuovutit")
                break
            else:
                if arvaus<numero and ((arvaus-numero)>25 or (arvaus-numero)<-25):
                    print("\nNyt meni ihan metsään. Minun numero on paljon isompi kuin arvauksesi. Arvaa uudestaan!")
                elif arvaus<numero and ((arvaus-numero)>10 or (arvaus-numero)>-10):  
                    print("\nNyt olet lähellä. Minun numero on isompi. Arvaa uudestaan!")                   
                elif arvaus<numero and ((arvaus-numero)<=10 or (arvaus-numero)<=-10):
                    print("\nMinun numero on isompi kuin arvauksesi. Arvaa uudestaan!")
                elif arvaus>numero and ((arvaus-numero)>25 or (arvaus-numero)<-25):
                    print("\nNyt meni ihan metsään. Minun numero on paljon pienempi kuin arvauksesi. Arvaa uudestaan!")       
                elif arvaus>numero and ((arvaus-numero)<10 or (arvaus-numero)<-10):
                    print("\nNyt olet lähellä. Minun numero on pienempi. Arvaa uudestaan!")
                elif arvaus>numero and ((arvaus-numero)>=10 or (arvaus-numero)>=-10):
                    print("\nMinun numero on pienempi kuin arvauksesi. Arvaa uudestaan!")
            arvaukset += 1
        except ValueError:
            print("\nSyöttö ongelma. Anna numero")
            continue

while True:
    print(3*"\n")
    pelireset = input("\nHaluatko pelata numeronarvauspeliä? (k/e):  ")
    if pelireset == "k":
        main()
    elif pelireset == "e":
        break