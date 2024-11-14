# https://www.codewars.com/kata/58fd4bbe017b2ed4e700001b/python

def cards_and_pero(st):
    suits = {'P': set(), 'K': set(), 'H': set(), 'T': set()}
    
    for i in range(0, len(st), 3):
        suit = st[i]
        number = int(st[i+1:i+3])  
        
        
        if number in suits[suit]:
            return [-1, -1, -1, -1]
            
        suits[suit].add(number)
    
    missing_cards = []
    for suit in ['P', 'K', 'H', 'T']:
        missing = 13 - len(suits[suit])
        missing_cards.append(missing)
    
    return missing_cards