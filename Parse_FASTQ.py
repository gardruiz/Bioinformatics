def read_FASTQ():
    clean_reads = []
    cleaner_reads = []
    myfile = input("Enter a file name and directory:")
    try:
        f = open(myfile)
    except IOError:
        print("File doesn't exist!")
    reads = []
    # Gets rid of triling empy spaces.
    with open(myfile, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '@' and not line[1] == 'I'and not line[0]== '+':
                reads.append( line.rstrip())
        for read in reads:
            if '@' and 'B' and '+' and ':' not in read:
                clean_reads.append(read)

        for read in clean_reads:
            if 'G' and 'D' not in read:
                cleaner_reads.append(read)
    return cleaner_reads




