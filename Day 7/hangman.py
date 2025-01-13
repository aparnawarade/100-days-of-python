import random

#create a word list
word_list = ['baloon', 'sample', 'machine', 'robinhoo']
#choose random word
choosen_word = random.choice(word_list)
print(choosen_word)
#ask user the letter checknif letter is corrcet or not
#if corrcet place it in the word if not reduce a life
lives=len(choosen_word)
#Create an empty string called placeholder
placeholder = ''
for _ in range(len(choosen_word)):
  placeholder = placeholder + '_'
game_over = False
correct_letters=[]
while not game_over:
  display = ''
  guess = input('Guess a letter: ').lower()
  for ch in choosen_word:
    if ch == guess:
      display = display + ch
      correct_letters.append(ch)
    elif ch in correct_letters:
      display=display+ch
    else:
      display = display + '_'
  if guess not in choosen_word:
    print('You have lost a life')
    lives=lives-1
    print(f'you have {lives} left')
    if lives==0:
      game_over=True
      print('You lose')
  if "_" not in display:
    print('You win')
    break
  print(display)
