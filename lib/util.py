

def is_number(s):
    try:
        int(s)
        return True

    except ValueError:

        try:
            float(s)
            return True

        except ValueError:
                return False

def sigmoid(bool):
    if bool:
        return 1
    else:
        return 0

def file_to_list( filename ):

    target_list = []

    with open(filename) as cols_file:
        for line in cols_file:

            target_list = line.replace(' ','').rstrip().split(',')

    return target_list
