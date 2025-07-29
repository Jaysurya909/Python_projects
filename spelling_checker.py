from spellchecker import SpellChecker

spell = SpellChecker()

class spelling:
    def input(self):
        text=input("Enter your sentence")
        self.list=text.split()
        
    def corrector(self):
        self.mistakes=[]
        for words in self.list:
            if spell.correction(words)!=words:
                self.mistakes.append(spell.correction(words))
        
        print(self.mistakes)

        
a1=spelling()
a1.input()
a1.corrector()



