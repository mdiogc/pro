VOWELS = 'aeiou'
famous_sentence = 'Supercalifragilisticoespialidoso'

number_vowels = 0
for letter in famous_sentence.lower():
    if letter in VOWELS:
        number_vowels += 1
print(number_vowels)
