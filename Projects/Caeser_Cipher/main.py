alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text,shift,direction):
        cipher_text = ""
        for letter in text:

            if letter not in alphabet:
                cipher_text += letter
            else:
                if direction == "decode":
                    shift *= -1

                new_index = alphabet.index(letter) + shift
                new_index %= len(alphabet)
                cipher_text += alphabet[new_index]
        print(f"Here is the {direction}d result:{cipher_text}")


caesar(text,shift,direction)