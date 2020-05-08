# ###### Square Pattern #############
#
# for i in range(4):
#     for j in range(4):
#         print("# ", end="")
#     print()
#
#
# ###### Triangle Pattern #############
#
# for i in range(5):
#     for j in range(i):
#         print("# ", end="")
#     print()

###########Number Pattern###########
# 1234
# 234
# 34
# 4

#for i in range(4):

    # for j in range(4-i):
    #     print(i+j+1, end="")
    # print()


###########Character Pattern###########
# APQR
# ABPQ
# ABCP
# ABCD

str1 = "ABCD"
str2 = "PQR"
for i in range(4):
    for k in range(i + 1):
        print(str1[k], end="")
    for j in range(i, 3):
        print(str2[j], end="")
    print()