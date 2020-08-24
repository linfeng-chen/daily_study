import math
def beeramid(bonus, price):
    if bonus==0:
        return 1
    if price==0:
        return 1
    if bonus<price:
        return 0;
    temp = [i**2 for i in range(int(bonus//price)+1)]
#     print(temp)
    sum = 0
    for i in range(len(temp)-1):
        sum += temp[i] * price
        if sum>=bonus or (sum+temp[i+1]*price)>bonus:
           break

#     print(i,sum)
    return i

if __name__=="__main__":
    # x = beeramid(0,1)

    x = beeramid(0,0)
    print(x)
    # x = (beeramid(21, 1.5), 3)
    # x = (beeramid(-1, 4), 0)