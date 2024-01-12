def min_umbrellas(weather):
    home, work, umbrellas = 0, 0, 0
    need_umbrella = ["rainy", "thunderstorms"]
    for num, i in enumerate(weather, 1):
        if i in need_umbrella:
            if num % 2 != 0:
                if not home:
                    work += 1
                    umbrellas += 1
                else:
                    home -= 1
                    work += 1
            else:
                if not work:
                    home += 1
                    umbrellas += 1
                else:
                    work -= 1
                    home += 1
    return umbrellas
