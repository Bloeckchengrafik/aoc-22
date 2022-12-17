def stage(data: list[str]):
    t = {}
    y = {}

    for i in data:
        i = i.replace("=", " ").replace(",", "").replace(";", "")
        i = i.split()

        y[i[1]] = int(i[5])
        t[i[1]] = i[10:]

    from collections import deque as de

    q = de([(0, (), "AA", 0)])
    v = set()
    w = 0

    print(y)
    while q:
        a, b, c, d = q.popleft()
        if a == 30:
            w = max(w, d)
            print(w)
            continue
        if (b, c) in v:
            continue
        v.add((b, c))

        dd = d
        for i in b:
            dd += y[i]
        if y[c] != 0:
            if c not in b:
                q.append((a + 1, tuple(list(b) + [c]), c, dd))

        for i in t[c]:
            q.append((a + 1, b, i, dd))
