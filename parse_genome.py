


def read_genome():
    myfile = input("Enter a file name and directory:")
    try:
        f = open(myfile)
    except IOError:
        print("File doesn't exist!")
    genome = ''
    # Gets rid of triling empy spaces.
    with open(myfile, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

