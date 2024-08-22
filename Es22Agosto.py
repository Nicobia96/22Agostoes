#imposto i valori da inserire in input per ogni figura geometrica

lato = float(input("inserire il valore del lato del quadrato: "))


raggio = float(input("inserire il valore del raggio della circonferenza: "))


base = float(input("inserire il valore della base del rettangolo: "))


altezza = float(input("inserire il valore dell' atezza del rettangolo: "))

# do la stampa  di tutti i tipi di perimetri
print(f"Il perimetro del quadrato e': {lato*4}")


print(f"La circonferenza del cerchio e':{2*3.14*raggio} ")


print(f"Il perimetro del rettangolo e': {base*2 + altezza*2} ")