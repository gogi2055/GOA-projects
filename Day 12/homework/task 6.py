#task 6

#6) დაწერეთ if-else condition კოდი: თუ მომხმარებლის შემოტანილი ასაკი ნაკლებია 13, დაუპრინტეთ "You are kid",  
# თუ მეტია 13ზე და ნაკლებია 20ზე, დაუპრინტეთ "You are teenager", თუ მეტია 20'ზე, დაუპრინტეთ "You are grown up"


age = int(input("Enter your age: "))


if age < 13:
    print("You are a kid.")
elif 13 <= age < 20:
    print("You are a teenager.")
else:
    print("You are grown up.")
