def calculate_love_score(name1, name2):
    t = r = u = e = l = o = v = 0
    name = (name1 + name2).lower()
    for i in name:
        if i == 't':
            t += 1
        if i == 'r':
            r += 1
        if i == 'u':
            u += 1
        if i == 'e':
            e += 1
        if i == 'l':
            l += 1
        if i == 'o':
            o += 1
        if i == 'v':
            v += 1
    total1 = t + r + u + e
    total2 = l + o + v + e
    love_score = total1 * 10 + total2
    print(love_score)


calculate_love_score(name1="Kanye West", name2="Kim Kardashian")


