palindrome = lambda x: x.upper().replace(" ","").strip()  ==  x[::-1].replace(" ","").upper().strip()

print( palindrome(" AniTA LAVA la tina  ") )