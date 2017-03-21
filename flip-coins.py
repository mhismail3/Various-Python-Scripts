import random

def test1():
    good = [[1,0,1,0,1,0,1,0],
            [1,0,1,0,1,0,0,1],
            [1,0,1,0,0,1,0,1],
            [1,0,0,1,0,1,0,1],
            [0,1,0,1,0,1,0,1]]

    count = 0
    cases = list()
    
    while count < 25600:
        case = list()
        for i in range(8):
            case.append(random.randint(0, 1))

        if case in good: cases.append(1)
        else: cases.append(0)

        count += 1

    print(cases.count(1), len(cases))


def test2():
    cases = list()
    count = 0

    while count < (2**16):
        notwo = True
        case = list()
        
        for i in range(16):
            if case == []: case.append(random.randint(0,1))
            else:
                tmp = random.randint(0,1)
                case.append(tmp)
                if tmp == 1 and case[i-1] == 1:
                    notwo = False
                    break

        if case.count(1) == 7 and notwo == True: cases.append(1)
        else: cases.append(0)

        count += 1

    print(cases.count(1), len(cases))

#test1()
test2()
