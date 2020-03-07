def single_words(word_list):
    words = word_list.split(" ")
    words_dict = dict()
    for word in words:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1

    single_list = []
    for word in words_dict.keys():
        if words_dict[word] == 1:
            single_list.append(word)
    return single_list


assert(single_words("ana are ana are mere rosii ana") == ['mere', 'rosii'])
assert(single_words("ana ana are mere rosii ana") == ['are', 'mere', 'rosii'])
assert(single_words("ana are mere rosii") == ['ana', 'are', 'mere', 'rosii'])
