array = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
]

n = ''
arrayout = []

def grouped(array, n):
    if n == '':
        n = 3
        grouped(array,n)

    else:
        for i in range(0, len(array), n):
            arrayout.append(array[i:i+n])
        print(arrayout)

grouped(array,n)