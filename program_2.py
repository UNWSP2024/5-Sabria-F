#By: Sabria Fafach
#Date: Febuary 2, 2025
#Title: program_2.py

def get_answer(number_1,number_2):
    print(f"    {number_1}")
    print(f"+   {number_2:0.0f}")
    print("------------")
    answer= int(input("Enter your answer:"))
    return answer


def sum_numbers(number_1,number_2):
    sum=number_1+number_2
    return sum

def main():
    for number_1 in (326,457,598,487,569,265,254):
        answer=get_answer(number_1,number_2)
        sum=sum_numbers(number_1,number_2)
        if answer==sum:
            print("Congratulations you got the right answer!")
        else:
            print("Sorry you got the wrong answer.")
            return

number_2=50
while number_2<1000:
    number_2=(number_2*3)/2
    main()