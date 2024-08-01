#task 2

#2) შექმენით while loop'ი რომელიც დათვლის რიცხვებს 1დან 100მდე თუმცა გამოტოვებს რიცხვებს 50დან 60მდე.


number = 1


while number <= 100:
    
    if 50 <= number <= 60:
        
        number += 1
        continue
    
    
    print(number)
    
    
    number += 1
