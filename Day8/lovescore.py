def calculate_love_score(name1,name2):
    
    name=(name1+name2).upper()
    digit1=name.count('T')+name.count('R')+name.count('U')+name.count('E')
    digit2=name.count('L')+name.count('O')+name.count('V')+name.count('E')
    score=str(digit1)+str(digit2)
    print(f'{score}')
calculate_love_score(name1="Kanye West", name2="Kim Kardashian")
