def vocale1 (x):
    vocali = ['a','e','i','o','u','A','E','I','O','U']
    if x in vocali:
        print(f'{x} è una vocale')
    else:
        print(f'{x} non è una vocale')

my_vowel = 'a'
vocale1('a')