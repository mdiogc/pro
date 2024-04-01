# **********************
# ORDENANDO CON BURBUJAS
# **********************


def bubble(items: list) -> list:
    sorted_items = items[:]
    number = len(sorted_items)
    for numbers in range(number):
         for index in range(number-numbers-1):
              if sorted_items[index] > sorted_items[index+1]:
                  sorted_items[index], sorted_items[index+1] = sorted_items[index+1], sorted_items[index]

    return sorted_items
