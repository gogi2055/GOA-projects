#task 8

#8) შექმენით while loop'ი რომელიც გამოიტანს რიცხვებს 0-დან 1000-მდე 100-ის გამოტოვებით


number = 0


while number <= 1000:
    
    if number % 100 != 0 or number == 0:
       
        print(number)
    
    number += 1
