
#task 3

#3) შექმენით if else condition  რომელიც მომხმარებელს გაუკეთებს ფასდაკლებას თუ ის 18 წელზე ნაკლებისაა ან სტუდენტია

age=int(input("Enter your age: "))
is_student = input("are your student? ")
if is_student=="yes":
    is_student == True
else:
    is_student== False

if age < 18 or is_student == True:
    print("discount")
else:
    print("regualar price")