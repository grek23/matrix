import numpy as np
from PIL import Image


def main():

    print("Here is a matrix")

    n_by_n = 512
    S = np.zeros((n_by_n, n_by_n), dtype=np.int16)
    S = axis(S)
    S = square(S, 256, (256, 256))
    S = circle(S, 64, (128, 128))  # (256,256)
    S = diag(S)

    img = Image.fromarray(S)
    img.show()
    # print(S)


def axis(arr):
    row = len(arr[:])
    col = len(arr[0][:])
    yaxis = int(len(arr[:])/2)
    xaxis = int(len(arr[:])/2)

    i = 0
    while i < row:
        j = 0
        while j < col:
            if j == yaxis:
                arr[i][j] = 255
            if i == xaxis:
                arr[i][j] = 255
            j = j+1
        i = i + 1
    return arr


def diag(arr):
    i = 0
    while i < len(arr[:]):
        j = 0
        while j < len(arr[0][:]):
            if i == j:
                arr[i][j] = 255
            j = j + 1
        i = i + 1

    i = len(arr[:])-1

    while i >= 0:
        j = 0
        while j < len(arr[:]):
            if (i + j) == 512:
                arr[i][j] = 255
            j = j+1
        i = i - 1

    return arr


def square(arr, length, center):
    x = center[0]
    y = center[1]

    print(f"center = ({x},{y}) and length = {length}")

    # determine end points
    # for bottom edge: column starts at x - length/2
    # for top edge: column starts at x + length/2
    i = 0
    while i < len(arr[:]) - x/2 + 1:
        if (i >= x - length/2) and (i <= x + length/2):
            arr[x + int(length/2)][i] = 255
            arr[x - int(length/2)][i] = 255
        i = i+1

    # determine the left side column
    #
    j = 0
    while j < len(arr[0][:]) - y/2 + 1:
        if (j >= y - length/2) and (j <= y + length/2):
            arr[j][y + int(length/2)] = 225
            arr[j][x - int(length/2)] = 255

        j = j + 1

    print(f" row = {x + int(length/2)}")
    # print(f"")

    return arr


def circle(arr, rad, origin):
    z1 = origin[0]
    z2 = origin[1]
    coords = []
    pi = np.pi
    slices = 512
    print(f"size of array = {np.size(arr)}")

    # create circle coordinates
    # x = rad * cos(theta) + x offset
    # y = rad * sin(theta) + y offset
    i = 0
    while i <= slices:
        x = int(rad*np.cos(i*2*pi/slices) + z1)
        y = int(rad*np.sin(i*2*pi/slices) + z2)
        coords.append([x, y])
        i = i + 1

    for coord in coords:
        arr[coord[0]][coord[1]] = 255
        # arr[-1*coord[1]][coord[0]] = 255

        # add some fuzz
        # arr[coord[0]+1][coord[1]] = 200
        # arr[coord[0]][coord[1]+1] = 128
        # arr[coord[0]-1][coord[1]-1] = 200

    return arr


if __name__ == '__main__':
    main()
