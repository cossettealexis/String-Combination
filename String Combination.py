
while(True):
    word = input("Input String : ")

    if(len(word) >= 3):
        print(word[0:3] + word[-2: ])

    else:
        print("Combination Not Allowed")
