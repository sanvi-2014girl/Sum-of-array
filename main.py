def arraysum(a):
    length = len(a)
    if length == 1:
        return a[0]
    return a[0] + arraysum(a[1:])
a = [1,2,234,234,745,3,6,653]
print("Array total sum:",arraysum(a))