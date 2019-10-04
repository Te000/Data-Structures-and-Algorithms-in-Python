freqDic = {}
with open('P2_34.py') as f:
    #Read source file and calculate the frequences
    for line in f:
        for char in line:
            if char.isalpha():
                freqDic[char] = freqDic.get(char, 0) + 1
                
#plot the frequences
for alpha in range(ord('a'), ord('z')+1):
    alpha = chr(alpha)
    print("%s " % (alpha) + "-"*freqDic.get(alpha, 0))
for alpha in range(ord('A'), ord('Z')+1):
    alpha = chr(alpha)
    print("%s " % (alpha) + "-"*freqDic.get(alpha, 0))