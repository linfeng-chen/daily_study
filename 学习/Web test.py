def checkio(words_set):

    words_set = list(words_set)
    print(words_set)
    for i in range(len(words_set)):
        for j in range(len(words_set)):
            # if words_set[i] in words_set[j] and words_set[i]!=words_set[j]:
            if words_set[i] in words_set[j][len(words_set[j])-len(words_set[i]):] and i!=j:
                print(words_set[i],words_set[j])
                return True
    return False

checkio({"hello", "lo", "he"})
checkio({"hello", "la", "hellow", "cow"})
if __name__ == '__main__':
    print("Example:")
    print(checkio({"hello", "lo", "he"}))

    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
    print("Done! Time to check!")
