def selection_sort(arr):
    n = len(arr)
    
    # Traverse through all elements of the array
    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage of Selection Sort
N = int(input("enter the no. of elements to input: "))

arr=[]
for i in range(N):
    ele = int(input("enter the elemnts: "))
    arr.append(ele)
print("Original array:", arr)

selection_sort(arr)
print("Sorted array:", arr)