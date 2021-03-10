'''
Write code that will print out the anagrams (words that use the same
letters) from a paragraph of text.

'''

word = sorted('rac')
alternatives = ['car', 'girl', 'tofu', 'rca']

for alt in alternatives:
    if word == sorted(alt):
        print(alt)