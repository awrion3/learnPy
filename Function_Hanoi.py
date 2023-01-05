#
def hanoi(o, srt, end, tmp):
    if o == 1:
        print(srt, "->", end)
    else:
        hanoi(o-1, srt, tmp, end)
        print(srt, "->", end)
        hanoi(o-1, tmp, end, srt)
#
def hCnt(n):
    return ((2**n)-1)

#
n = int(input("o numbers: "))
hanoi(n, "A", "B", "C")
#
print(f"{hCnt(n)} times")