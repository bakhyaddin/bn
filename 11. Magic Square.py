def size_rows_and_columns(values):
    size_rows=len(values)
    size_columns=len(values[0])
    return size_rows,size_columns


def get_sum_first_row(values,size_columns):
    sum_first_row=0
    for r in range(1):
        for c in range(size_columns):
            sum_first_row+=values[c][r]
    return sum_first_row


def get_sum_rows(values,size_rows,size_columns,sum_first_row):
    sum_rows=0
    for r in range(size_rows):
        for c in range(size_columns):
            sum_rows+=values[r][c]
        if sum_rows!=sum_first_row:
            return False
        sum_rows=0
    return True


def get_sum_columns(values,size_rows,size_columns,sum_first_row):
    sum_columns=0
    for c in range(size_columns):
        for r in range(size_rows):
            sum_columns+=values[r][c]
        if sum_columns!=sum_first_row:
            return False
        sum_columns=0
    return True


def equal_rows_and_columns(values,size_rows,size_columns,sum_first_row):
    if get_sum_rows(values,size_rows,size_columns,sum_first_row) and get_sum_columns(values,size_rows,size_columns,sum_first_row):
        return True
    else:
        return False


def get_sum_left_diogonals(values,size_rows,sum_first_row):
    sum_left_diogonals=0
    for d in range(size_rows):
        sum_left_diogonals+=values[d][d]
    if sum_left_diogonals!=sum_first_row:
        return False
    else:
        return True


def get_sum_right_diogonals(values,size_rows,sum_first_row):
    sum_right_diogonals=0
    d=size_rows-1
    for d in range(size_rows):
        sum_right_diogonals+=values[d][d]
        d=size_rows-1
    if sum_right_diogonals!=sum_first_row:
        return False
    else:
        return True


def equal_diogonals(values,size_rows,sum_first_row):
    if get_sum_left_diogonals(values,size_rows,sum_first_row) and get_sum_right_diogonals(values,size_rows,sum_first_row):
        return True
    else:
        return False


#why starting point of universe is not arbitrary

def main():
    values=[[1,1,1,1],  #value[0]
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,0]]


    size_rows,size_columns=size_rows_and_columns(values)
    sum_first_row=get_sum_first_row(values,size_columns)
    sum_left_diogonals=get_sum_left_diogonals(values,size_rows,sum_first_row)


    if equal_diogonals(values,size_rows,sum_first_row) and equal_rows_and_columns(values,size_rows,size_columns,sum_first_row):
        print('This is True')
    else:
        print('this is wrong')

        for x in values:
            print(x)
        
main()
