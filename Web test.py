def checkio(array: list) -> int:
    sum=0
    print(array)
    if len(array)==0:
        return sum
    for i in range(0,len(array)):
        if i%2==0:
            # print(array[i])
            sum+=array[i]
            # print(sum)
    sum = sum*array[-1]
    # print(sum)
    return sum





num=[-37,-36,-19,-99,29,20,3,-7,-64,84,36,62,26,-76,55,-24,84,49,-65,41]
checkio(num)