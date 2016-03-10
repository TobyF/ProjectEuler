# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
#how many letters would be used?

def Teenies(x):
    teens = str.split(
        "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen")
    y = teens[x]
    return y


def Tens(x):
    tens = str.split("twenty thirty fourty fifty sixty seventy eighty ninety")
    y = tens[x - 2]
    return y


def SpeechModule(x):
    x = int(x)
    S = ""
    if x < 20:
        S = Teenies(x)
        return S

    elif x < 100:
        y = x // 10
        z = x % 10
        if z == 0:
            S = Tens(y)
        else:
            S = Tens(y) + "" + Teenies(z)
        return S
    elif x < 1000:
        a = x // 100
        print("a:", a)
        b = x % 100
        print("b:", b)
        c = b // 10
        print("c:", c)
        d = b % 10
        print("d:", d)
        if d == 0 or b < 20:
            S = Teenies(a) + "hundredand" + Tens(c)
        else:
            S = Teenies(a) + "hundredand" + Tens(c) + "" + Teenies(d)
        return S
    elif x == 1000:
        return "onethousand"


y = 111
print(SpeechModule(y))
print(len(SpeechModule(y)))

##total = ""    
##for i in range(1,1001):
##    total += SpeechModule(i)
##print(len(total))
