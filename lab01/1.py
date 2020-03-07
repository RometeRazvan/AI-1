def first_implementation(word_list):
    words = word_list.split(" ")
    words.sort()
    return words[-1]


assert (first_implementation("Ana are mere rosii si galbene") == 'si')
assert (first_implementation("Ana are mere rosii galbene") == 'rosii')
assert (first_implementation("Ana are mere galbene") == 'mere')
