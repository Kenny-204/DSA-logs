flowerbed = [1, 0, 0, 0, 1, 0, 0]
n = 2


def can_place_flowers(flowerbed, n):
    available_space = 0
    i = 0
    while i < len(flowerbed):

        if flowerbed[i] == 0:
            if i == len(flowerbed) - 1 and flowerbed[i] == 0:
                if flowerbed[i - 1] == 0:
                    available_space += 1
            if i + 1 < len(flowerbed) and flowerbed[i + 1] == 0:
                available_space += 1
                i += 2
            else:
                available_space += 0
                i += 1
        else:

            i += 2

    print(available_space)
    return available_space >= n


print(can_place_flowers(flowerbed, n))

