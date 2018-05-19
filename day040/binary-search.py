from random import randint


def binary_search(val_list, key):
    start = 0
    end = len(val_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if val_list[mid] == key:
            return mid
        elif val_list[mid] > key:
            end = mid - 1
        elif val_list[mid] < key:
            start = mid + 1
    return -1


def main():
    list1 = [x for x in range(100)]
    list1.sort()
    print(list1)
    print(binary_search(list1, 0))


if __name__ == '__main__':
    main()
