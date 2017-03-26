def alphabet_position(letter):
    #matches letters with numbers where a = 0 and z = 25
    position = ord(letter.lower()) - 97
    return position

#test:print(alphabet_position(input("what letter do you want?")))

def rotate_character(char,rot):
    old_position = alphabet_position(char)
    new_position = old_position + int(rot)%26
    if char.isalpha() == True:
        if char.isupper() == True:
            return chr(new_position%26 + 97).upper()
        return chr(new_position%26 + 97)
    return char

def encrypt(text,rot):
    letters = list(text)
    encrypted_letters = []
    for letter in letters:
        encrypted_letters.append((rotate_character(letter,rot)))

    return "".join(encrypted_letters)
