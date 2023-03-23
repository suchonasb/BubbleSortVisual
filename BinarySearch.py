import time

# Binary search algorithm


def Binary_Search(data, drawData, timeTick, item):
    n = len(data)
    low = 0
    high = n - 1
    isfound = False

    while low <= high:
        mid = (low + high) // 2
        drawData(data, ['#90ee90' if x == mid else '#ADD8E6' for x in range(len(data))])
        time.sleep(timeTick)

        if data[mid] == item:
            drawData(data, ['#010445' if x == mid else '#ADD8E6' for x in range(len(data))])
            time.sleep(timeTick)
            isfound = True
            break

        elif data[mid] < item:
            drawData(data, ['#ADD8E6' if x > high or x < mid else '#FFFF00' for x in range(len(data))])
            time.sleep(timeTick)
            low = mid + 1

        else:
            drawData(data, ['#ADD8E6' if x < low or x > mid else '#FFFF00' for x in range(len(data))])
            time.sleep(timeTick)
            high = mid - 1

    if isfound == False:
        drawData(data, ['#DC143C' for x in range(len(data))])
