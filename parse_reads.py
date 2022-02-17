#This code is used to parse fastq files

def parse_reads():
    sequences = []
    qualities = []
    myfile = input("Enter a file name and directory:")
    try:
        f = open(myfile)
    except IOError:
        print("File doesn't exist!")
    with open(myfile, ) as fh:
        while True:
            fh.readline()
            seq = fh.readline().rstrip()
            qual = fh.readline().rstrip()
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
        return sequences
print(parse_reads())

