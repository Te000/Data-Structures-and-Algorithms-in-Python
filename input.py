def main():

    nTests = input()
    nTests = int(nTests)
    dic = {
        0 : 1, #k
        1 : 3,
        2 : 1,
        3 : 9,
        4 : 7,
        5 : 3,
        6 : 1,
        7 : 9,
        8 : 7,
        9 : 3,
        10 : 1, #a
    }
    while nTests > 0:
        test = input()
        test = int(test)
        nTests -= 1
        sum = 0
        # First break up int to its components, then Add them as mentioned in a for loop 
        for j in range(11):
            add = test%10
            test /= 10
            sum += dic.get(j) * add

        # Check result modulo 10
        flag = sum%10
        
        if (flag == 0):
            print('Y')
        else:
            print('N')
        

if __name__ == '__main__':
    main()