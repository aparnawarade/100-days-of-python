alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(text,shift):
  cipher_text=''
  for letter in text:
    if letter in alphabet:
      position=alphabet.index(letter)
      new_position=position+shift
      if new_position>25:
        new_position=new_position-26
      new_letter=alphabet[new_position]
      cipher_text+=new_letter
    else:
      cipher_text+=letter  
  return cipher_text 
  
answer=True
while answer:
  direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text=input("Type your message:\n").lower()
  shift=int(input(f"Type the shift number:\n"))
  if direction=='encode':
    cipher_text=encrypt(text,shift)
    print(f"The encoded text is {cipher_text}")
  elif direction=='decode':
    cipher_text=encrypt(text,shift*-1)
    print(f"The decoded text is {cipher_text}")
  ans=(input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")).lower()
  if ans=='no':
    answer=False
    print('Goodbye')
