from __future__ import print_function

r = 6
c = 6
arr = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]

# for i in range (0,r-2):
#     for j in range(0,c-2):
#         for k in range(0,3):
#             if (k == 0):
#                 oneHourGlassSum += A[i][k] + A[i][k+1] + A[i][k+2]
#             elif (k == 1):
#                 oneHourGlassSum += A[i+1][k+1]
#             elif (k == 2):
#                 oneHourGlassSum += A[i+2][k] + A[i+2][k+1] + A[i+2][k+2]
#         hourGlassList.append(oneHourGlassSum)
#         print(oneHourGlassSum)
#         oneHourGlassSum = 0
#     print ('\n')

hourGlassList = []
oneHourGlassSum = 0
for i in range(0, r-2):
    for j in range(0, c-2):
        oneHourGlassSum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        hourGlassList.append(oneHourGlassSum)

print (max(hourGlassList))