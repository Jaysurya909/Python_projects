from spellchecker import SpellChecker

spell = SpellChecker()

class spelling:
    def input(self):
        text=input("Enter your sentence")
        self.list=text.split()
        
    def corrector(self):
        self.mistakes=[]
        for i,words in enumerate(self.list):
            if spell.correction(words)!=words:
                self.mistakes.append(spell.correction(words))
                self.list[i]=spell.correction(words)
        
        print(self.mistakes)
        print(self.list)
        
a1=spelling()
a1.input()
a1.corrector()



