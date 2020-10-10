def repeat_inside(line):
    x = []
    for i in range(1,int((len(line)+1)/2)+1):
        x.append(line[:i])
        print(x)
        for j in range(i,len(line),i):
            print(j)
            print(line[j:j+i])
            if line[j:j+i] in x[-1]:
                print('yes')
                x[-1] = x[-1]+line[j:j+i]


    return line
repeat_inside('aaaaa')
repeat_inside('aabbff')

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert repeat_inside('aaaaa') == 'aaaaa', "First"
#     assert repeat_inside('aabbff') == 'aa', "Second"
#     assert repeat_inside('aababcc') == 'abab', "Third"
#     assert repeat_inside('abc') == '', "Forth"
#     assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
#     print('"Run" is good. How is "Check"?')
