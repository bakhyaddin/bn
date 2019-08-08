x = [-1, 3, 8, 2, 9, 5]
y = [4, 1, 2, 10, 5, 20]
z = 24

def finding_it(x,y):
    output = []
    result = 0
    for cx in x:
        for cy in y:
            result = cx + cy
            output.append(result)
    return output

#print(finding_it(x,y))

def the_result(output, z):
    difference = []
    index = 0
    for x in range(len(output)):
        difference.append(abs(output[index] - z))
        index +=1
    #print(min(difference))
    new_index = difference.index(min(difference))
    print(output[new_index])

def main():
    output = finding_it(x,y)
    the_result(output, z)

main()


def two_dimentional_list(x,y):
    rows = 6
    colums = 6
    the_list = [[0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0]]
    for cx in range(rows):
        for cy in range(colums):
            result = x[cx] + y[cy]
            the_list[cx][cy] = result

    for ch in the_list:
        print(ch)

#two_dimentional_list(x,y)