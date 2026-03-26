#My first python test
def what(x,y):
    if x==0:
        print(f"{x} is neither '+ve' nor '-ve'")
    else:
        if x>0:print(f"{x} is '+ve'")
        if x<0:print(f"{x} is '-ve'")
        if x and 1 == 0:
            print(f"{x} is even")
        else:
            print(f"{x} is odd")
    if x==y:
        print(f"{x} and {y} are equals")
    elif x>y:print(f"{x} is greater than {y}")
    elif x<y:print(f"{y} is greater than {x}")
    print(f"this is 'x' ---> {x} \n this is 'y' ---> {y} ")
    #to swap 'x' and 'y' 
    x,y=y,x
    #both 'x' and 'y' are swapped
    print(f"this is 'x' now ---> {x} \n this is 'y' now ---> {y} ")
    print(f"square of 'x'---> {x*x} \n cube of 'y'---> {y*y*y}")
    #test done succesfully...

def loops():
    for x in range(1,101):
        print(f"{x} ", end="")
    print("\n")
    for x in range(2,51,2):
        print(f"{x} ", end="")
    print("\n")
    n=int(input("Required natural number = "))
    s=0
    for x in range(1 ,n+1):
        s+=x
    print(f"{s} is the cumultative sum till the natural number")

def concept(x):
    if x<=1:
        print("neither prime nor composite")
    else:
        for i in range(2,int(x**0.5) + 1):
            if x % i == 0:
                print(f"{x} is a composite number")
                break
        else:
            print(f"{x} is a prime number")
    sx=str(x)
    lx=len(sx)
    print(f"number of digits in {x} is {lx}")
    rsx=sx[::-1]
    rsx=int(rsx)
    print(f"{x} reversed is {rsx}")
    if rsx<=1:
        print("neither prime nor composite")
    else:
        for i in range(2,int(x**0.5) + 1):
            if rsx % i == 0:
                print(f"{rsx} is a composite number")
                break
        else:
            print(f"{rsx} is a prime number")
    if x==rsx:
        print(f"{x} is a paindrome")
    else:
        print(f"{x} is not a palindrome")

def  strings(x):
    v,c=0,0
    for i in x:
        if i.lower() in "aeiou":
             v+=1
        else:
             c+=1
    print(f"vowels---> {v}")
    print(f"consonants---> {c}")
