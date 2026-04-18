def sonni_rim(raqam):
    if not isinstance(raqam, int) or raqam < 1 or raqam > 3999:
        return "Iltimos, 1 dan 3999 gacha bo'lgan son kiritng."
    
    rim = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
        90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    }
    
    son = ''
    for key in sorted(rim.keys(), reverse=True):
        while raqam >= key:
            son += rim[key]
            raqam -= key
    
    return son

print(sonni_rim(4))  # IV
print(sonni_rim(9))  # IX
print(sonni_rim(13))  # XIII
print(sonni_rim(44))  # XLIV
print(sonni_rim(1000))  # M
