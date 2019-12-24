# Solution based on this explanation:
# https://www.reddit.com/r/adventofcode/comments/ee0rqi/2019_day_22_solutions/fbnkaju/


    deck_size = 119315717514047
    shuffle_rounds = 101741582076661
    stack = shuffle(range(119315717514047), instructions, shuffle_rounds)

    print("After shuffling the deck of", deck_size, "cards", shuffle_rounds, "times")
    print("the Number of card in position 2020 is:", stack[2020])
