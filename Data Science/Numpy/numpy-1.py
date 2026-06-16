import numpy as np
from scipy import stats


arr = np.array([1, 2, 3, 4, 5])
#print(arr)

#print(arr+5)

mean = np.mean(arr)
#print(mean)


multiDimarray = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]])
print(multiDimarray,"\n\n\n")

MDarray1= np.array([[1,2,3],[4,5,6],[7,8,9]])

print(MDarray1, "\n")


MDarray2= np.array([[11,12,3],[4,35,6],[74,82,19]])
print(MDarray2, "\n")

MDarray3 = MDarray1 + MDarray2
print(MDarray3, "\n")

mean = np.mean(MDarray3)
print(mean,"\n")

median = np.median(MDarray3)
print(median,"\n")

#mode = stats.mode(MDarray3)
#print("mode: ",mode,"\n")

arr2 = np.array([1, 2, 3, 3, 2, 2, 2, 2, 3, 3, 5, 5, 5, 5, 5, 5, ])
mode = stats.mode(arr2)
print("mode: ",mode,"\n")


print(arr2[::2])

print(arr2.dtype)

print("same") if arr.dtype == arr2.dtype else print("different")

arrTOmatrix = arr2.reshape(4,4)
print(arrTOmatrix)

print(arr2.size)



arr = np.array([1, 2, 3, 4, 5])


