# imposto come input un Menu di selezione per la figura
Menu = int(input("Premi 1 per quadrato , Premi 2 per cerchio , Premi 3 per rettangolo: "))
# imposto condizione if uguale a 1 per stampare il perimetro del quadrato
if Menu == 1:
    lato = float(input("inserire il valore del lato del quadrato: "))
    print(f"Il perimetro del quadrato e': {lato*4}")
# Imposto condizione elif uguale 2 per stampare la circonferenza del cerchio   
elif Menu == 2:
    raggio = float(input("inserire il valore del raggio della circonferenza: "))
    print(f"La circonferenza del cerchio e':{2*3.14*raggio} ")
# Imposto condizione elif uguale a 3 per stampare il profilo del rettangolo
elif Menu == 3:
    base = float(input("inserire il valore della base del rettangolo: "))
    altezza = float(input("inserire il valore dell' atezza del rettangolo: "))
    print(f"Il perimetro del rettangolo e': {base*2 + altezza*2} ")
# imposto condizione else finale la stampa che non e' staa selezionata alcuna figura disponibile dall'input iniziale Menu    
else :
    print("Nessuna figura geometrica disponibile selezionata")
