from PIL import Image
import numpy as np 
import pprint

def levenshtein_distance(s, t):
    m = len(s)
    n = len(t)
    d = [[0] * (n + 1) for i in range(m + 1)]  

    for i in range(1, m + 1):
        d[i][0] = i

    for j in range(1, n + 1):
        d[0][j] = j
    
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                cost = 0
            else:
                cost = 1
            d[i][j] = min(d[i - 1][j] + 1,      # deletion
                          d[i][j - 1] + 1,      # insertion
                          d[i - 1][j - 1] + cost) # substitution   

    return d[m][n]



I1 = np.concatenate(np.asarray(Image.open('crop595_460.png').convert('L')))
I2 = np.concatenate(np.asarray(Image.open('crop843_523.png').convert('L')))
pprint.pprint(I1)
l_dist = levenshtein_distance(I1, I2)

print("Levenshtein Distance between 1  & 2 is " + str(l_dist))