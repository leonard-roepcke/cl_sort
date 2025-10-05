import time

def main():
    print("start")
    arr = [0, 4, 2, 3, 1]
    iterations = 0
    i1 = 0

    algrorithm = chose_sort()

    while sorted(arr) != arr:
        print(arr)
        time.sleep(0)
        if algrorithm == 1:
            arr = random_sort(arr)
        elif algrorithm == 2:
            arr = swap_sort(arr, i1)
            i1 += 1
        elif algrorithm == 3:
            arr = inhouse_sort(arr)
        
        
        iterations += 1

    print(arr)
    print(f"Sorted in {iterations} iterations")
        
def chose_sort():
    while True:
        algrorithm = input("Choose sorting algorithm (1:random_sort, 2:swap_sort 3:inhouse_sort): ")
        try:
            if 1<=int(algrorithm)<=3:
                return int(algrorithm)
        except:
            pass

def random_sort(arr):
    import random
    arr_copy = arr[:]
    random.shuffle(arr_copy)
    return arr_copy

def swap_sort(arr, i1):
    arr_copy = arr[:]
    i_pos = i1 % (len(arr_copy) - 1)
    if arr_copy[i_pos] > arr_copy[i_pos + 1]:
        arr_copy[i_pos], arr_copy[i_pos + 1] = arr_copy[i_pos + 1], arr_copy[i_pos]
    
    for i in range(len(arr_copy)):
        if i == i_pos:
            print(" X ", end="")
        elif i == i_pos + 1:
            print(" 0 ", end="")
        else:
            print("   ", end="")
    return arr_copy

def inhouse_sort(arr):
    return sorted(arr)
    


if __name__ == "__main__":
    main()
