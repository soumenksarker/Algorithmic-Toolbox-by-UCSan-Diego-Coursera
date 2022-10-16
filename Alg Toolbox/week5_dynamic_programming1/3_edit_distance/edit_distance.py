# python3
# Uses python3
def edit_distance(s, t):
    s = list(s)
    t = list(t)
    n = len(s)
    m = len(t)
    ed = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(1, n+1):
        ed[i][0] = i
    for j in range(1, m+1):
        ed[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                ed[i][j] = ed[i-1][j-1]
            elif s[i-1] != t[j-1]:
                ed[i][j] = min(ed[i-1][j-1] + 1, ed[i-1][j] + 1, ed[i][j-1] + 1)
    # for i in range(n+1):
    #     for j in range(m+1):
    #         print(edm[i][j], end=" ")
    #     print()
    return ed[n][m]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
