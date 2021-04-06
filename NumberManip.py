'''
1. Python code to repressetn number in USa format
2. python code to represent the hour minute and second in HH MM SS format
    i. enter hours minutes and seconds and check for overflow
'''
#import NumPy as np

def reverse(st):
    ans = ""
    for i in st:
        ans = i + ans
    return ans


def number(num):
    # (XXX)-XXX-XXXX 14 Characters
    ans = ""
    m=10
    count = 0
    while count < 14:
        if count == 4 or count == 8:
            ans += "-"
        elif count == 9:
            ans += ")"
        elif count == 13:
            ans += "("
        else:
            ans += str(int(num % m))
            num /= 10
        count += 1

    return reverse(ans)




def HMS():
    H = int(input("Enter hours: "))
    M = int(input("Enter minutes: "))
    S = int(input("Enter seconds: "))

    M += int(S / 60)
    S = int(S % 60)

    H += int(M / 60)
    M = int(M % 60)

    hours = ""
    minutes = ""
    seconds = ""
    if H == 0:
        hours = "00"
    elif H < 10:
        hours = str('0'+str(int(H)))
    else:
        hours = H

    if M == 0:
        minutes = "00"
    elif M < 10:
        minutes = str('0'+str(int(M)))
    else:
        minutes = M
    
    if S == 0:
        seconds = "00"
    elif S < 10:
        seconds = str('0'+str(int(S)))
    else:
        seconds = S

    print("In HH:MM:SS Format")
    print(hours,":",minutes,":",seconds)

print(number(8154998589))
HMS()
