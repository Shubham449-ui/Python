count = 0
first_string  = input("Enter the String number 1 :: ")
second_string = input("Enter the String number 2 :: ")

if len(first_string) != len(second_string):
    print("Distance Must Be equal ")
else:

    for i in range(len(first_string)):
        if first_string[i]!=second_string[i]:
            count = count+1

print("Hamming Distance :: ",count)
