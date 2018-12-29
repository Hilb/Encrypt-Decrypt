

alphabet = {
    'a': 'b',
    'b': 'c',
    'c': 'a',
    'z': '-',
    'y': 'z',
    'o': '1',
    'l': '%',
    'd': '`',
    'k': '^',
    'e': 'l'

}

inv_map = {v: k for k, v in alphabet.items()}



def main():
    guess()



def replaceMultiple(mainString):
    toRet = "";
    for x in range(0,len(mainString)):
        letter = mainString[x];
        if letter in alphabet:
            toRet += alphabet[mainString[x]]
        else:
            toRet+= letter;

    return toRet


def decode(mainString):
    toRet = "";
    for x in range(0,len(mainString)):
        letter = mainString[x];
        if letter in alphabet:
            toRet += alphabet.get(mainString[x])
        else:
            toRet +=letter


    return toRet


def checkKey():

    for key in alphabet:
        val = alphabet[key]
        print("checking "+val)
        if(val in alphabet):
            print("inside "+val+" check")
            for val in alphabet:
                val = alphabet[val]
                print("Curr val "+val)
            if (val != key and val not in alphabet):
                return False
        else:
            return False



    return True;


def check2():
    for key in alphabet:
        key1 = alphabet[key]
        count=0
        while key1 in alphabet:
            if key1 == key:
                break
            key1=alphabet[key1]
            count += 1
            if count>len(alphabet):
                return False
        if key1 != key:
            return False

    return True


def guess():
    import random
    import math
    num = random.randint(1,101)

    val = 0;
    tries = 0;

    while(val != num and tries < int(math.log(100,2))+1):
        val = int(input("Please enter a number between 1 and 100: "))
        if(val > num):
            print("The number is lower")
        elif(val < num):
            print("The number is higher")

        tries += 1

    if(val == num):
        print("You got it!")
    else:
        print("Close but not quite")



if __name__ == '__main__':
    main()