import sys

def diamond(a,b):
    while b < a:
        print(" "*(a-b), "*"*(2*b+1))
        return diamond(a,b+1)

def reverse_diamond(c,d):
    while d >= 0:
        print(" "*(c-d), "*"*(2*d+1))
        return reverse_diamond(c,d-1)

#diamond(int(sys.argv[1]),0)
diamond_size = int(input())
diamond(diamond_size,0)
#reverse_diamond(int(sys.argv[1]),int(sys.argv[1])-2)
reverse_diamond(diamond_size,diamond_size-2)