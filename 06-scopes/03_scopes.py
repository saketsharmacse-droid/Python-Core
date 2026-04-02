x = 99
def func1():
    x = 88
    def func2():
        print(x)
    return func2
myResult = func1()
myResult()

#closure concept: jab bhi hum kisi function ke andar koi function define karte hai toh uss inner function ke paas uss outer function ke variables ki access hoti hai, chahe outer function ka execution complete ho chuka ho.
#references mei sirf line 4 aur 5 bus gys toh usko value kaise pta?
# this is called as bag theory, where unn function definitions se accociated sabhi variables values bhi jaati hai, unn values ki references bhi pass hoti hai.
