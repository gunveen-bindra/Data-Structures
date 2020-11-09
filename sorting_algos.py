#bubble sort
def bubble_sort():
    list = [12,56,28,46,89,64,18]
    print(list)
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]        
    return list

#insertion sort
def insertion_sort():
    list = [12,56,28,46,89,51,18]
    
    print(list)
    for i in range(len(list)):
        val = list[i]
        j = i-1
        while j >= 0 and val < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = val
    return list

#selection sort
def selection_sort():
    list = [12,56,28,46,89,51,18]

    print(list)
    for i in range(len(list)):
        min_val_index = i
        for j in range(i+1, len(list)):
            if list[min_val_index] > list[j]:
                min_val_index = j
        list[i], list[min_val_index] = list[min_val_index], list[i]
    return list


    

a = input("Enter 1 to perform bubble sort \nEnter 2 to perform insertion sort \nEnter 3 to perform selection sort:")
if a=='1':
    print("bubble sort: ",bubble_sort())
elif a=='2':
    print("insertion sort: ", insertion_sort())
elif a=='3':
    print("selection sort: ", selection_sort())
else:
    print("invalid input")
