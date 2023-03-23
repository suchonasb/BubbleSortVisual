import time


# Linear search algorithm

def Linear_Search(data, drawData, timeTick, item):
    n = len(data)
    isfound = False
    for i in range(n):
        drawData(data, ['#90ee90' if x == i else '#ADD8E6' for x in range(len(data))])
        time.sleep(timeTick)

        if (data[i] == item):
            drawData(data, ['#010445' if x == i else '#ADD8E6' for x in range(len(data))])
            isfound = True
            break

    if(isfound == False):
        drawData(data, ['#DC143C' for x in range(len(data))])

