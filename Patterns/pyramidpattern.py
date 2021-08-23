    #     *
    #    * *
    #   * * *
    #  * * * *
    # * * * * *

n=int(input("enter the number of levels:"))
def triangle(n):
    for i in range(1,n):
        print(" "*(n- i),end="")
        for j in range(0,i):
            print("*",end=" ")
        print()
triangle(n)

# def triangle(n):
#
#     # print(k)
#     for i in range(0, n):
#         for r in range(0, n-i):
#             print(end=" ")
#         for j in range(0, i + 5):   #0,1,2
#             print("* ", end="")
#         print("\r")
# triangle(10)

