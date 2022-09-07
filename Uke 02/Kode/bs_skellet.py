#Dette er et minimalt skellet av et binært søketre
#Funksjonene og resten av datastrukturen må implementeres selv
#legg til så mange tilleggsfunskjoner som du trenger!
#Lykke til :)

class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

        # Her må dere tenke frem til hvilke typer selff.value, self.left og self.right er

class BinarySearchTree:

    def __init__(self):
        self.root = None #Når vil denne oppdateres?
        self.size = None #Hvilken verdi skal størrelsen være når treet opprettes?
        #Hva er det første inputtet i inputfilen? Ta hensyn til det og.
        
    
    def contains(self, value):
        #Ta inspirasjon fra pseudokode på foilene
        #Hint: Rekursjon
        return

    def insert(self, value):
        #Ta inspirasjon fra pseudokode på foilene
        #Hint: Rekursjon
        return
    
    def remove(self,value):
        #Ta inspirasjon fra pseudokode på foilene
        #Hint: Rekursjon
        return
    
    def size():
        #Størrelse av nåværende tre
        return
    


#Enkel kjøre eksempel på hvordan man kan bruke stdin og stdout for å teste løsnignen sin på kattis! :)
def main():
    #Tips: Lag et instanse av binersøketre objektet
    #Hint: Når i inputen skal treet oppdateres? Hvordan oppdaterer du instansen din ved bruk av inputtet

    #Stdin
    #Stdin på python er en enkel input() kall.
    #Tips: Tenk på hvor ofte du må kalle på input. Når skal du stoppe å kalle på input
    #Hint: Hver linje i input filen er en ny input


    #Stdout
    #Stdout på pythn er en enkel print() kall.
    #Dette print setningen skal være på samme format som oppgaven ber om
    #flere 
    return

#Hint: Kall på main() som dette
if __name__ == "__main__":
    main()

#Nå har du alle redskapene til å implementere og teste koden din på kattis!
#Lykke til!