from spellchecker import SpellChecker

spell = SpellChecker()

corrector=spell.unknown(['Dp','not','dp','dhat'])

for words in corrector:
    print(spell.correction(words))