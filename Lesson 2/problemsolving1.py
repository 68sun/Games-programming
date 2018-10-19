
words=["xxx", "aaa", "r5t6yy", "g", "wow"]
for x in words:
    if len(x)<2:
        continue
    elif x[0] != x[-1]:
        continue
    print(x)
