candies = [2, 3, 5, 1, 3]
extraCandies = 3


def greatest_No_Candies(candies, extraCandies):
    output = []
    mostCandies = max(candies)

    for candy in candies:
        print(candy + extraCandies,mostCandies)
        if (candy + extraCandies) >= mostCandies:
            output.append(True)

        else:
            output.append(False)

    return output


print(greatest_No_Candies(candies, extraCandies))
