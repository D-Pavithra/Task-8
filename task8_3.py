class calculate:
    def area (a, side):
        if len(side) == 2:
            return side[0]*side[1]
        elif len(Side) == 1:
            pi = 3.141
            return pi*side[0]**2
        else:
            return None
    def perimeter(a, side):
        if len(side)==2:
            return 2*(side[0]+side[1])
        elif len(side)==1:
            pi = 3.141
            return 2*pi*side[0]
        else:
            return None
list1 = [10, 501, 22, 37, 100, 999, 87, 351]
for value in list1:
    area = calculate.area([value])
    perimeter = calculate.perimeter([value])
    print (area)
    print (perimeter)