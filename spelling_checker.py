from spellchecker import SpellChecker

spell = SpellChecker()

class spelling:
    def input(self):    # Taking the user input sentence
        text=input("Enter your sentence")
        self.list=text.split()
        
    def corrector(self):    # Correcting the sentence
        self.mistakes=[]
        for i,words in enumerate(self.list):
            if spell.correction(words)!=words:
                self.mistakes.append(spell.correction(words))
                self.list[i]=spell.correction(words)
        
        #print(self.list)
    
    def print_corrected(self):  # Printing the corrected sentence
        print("The misspelled words are",self.mistakes)
        for i in self.list:
            print(f"{i} ",end="")
            
            

a1=spelling()
a1.input()
a1.corrector()
a1.print_corrected()



