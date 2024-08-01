#task 3

#3) შექმენით while loop'ი, რომელიც დაიწყებს რიცხვების შეკრებას 1-დან, სანამ ჯამი არ გაუტოლდება 50-ს.


total_sum = 0
current_number = 1


while total_sum < 50:
    
    total_sum += current_number
    
    print(f"Adding {current_number}, total sum is now {total_sum}")
    
    current_number += 1


print(f"Final total sum is {total_sum}, which is >= 50.")
