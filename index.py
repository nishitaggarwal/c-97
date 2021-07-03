#%%
import random
x = random.randint(0,9)
typedNumber = int(input("Enter the number you guessed "))


if (x != typedNumber ):
    print("Alas! YOU LOOSE")
    print("The Number was:" , x)
    print("YOU May Win Next Time")
elif(x == typedNumber):
    print("CONGRATULATIONS !! You are great")
    print("The Guessed number was:" , x)


# %%
