def func(x):
    return x**2


def calc_rect_area(width, height):
    return width * height


def frange(start, end, step=1):
    result = []
    current = start

    while current <= end:
        print(current)
        result.append(current)
        current += step
    return result


def total_area(start, end, step):
    


print(frange(0, 2, 0.5))
