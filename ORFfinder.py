#finds the ORF in the dictionary sequences.
def find_ORFs(DNA):
    ORFs = []
    if 'ATG' in DNA:
        for startMatch in re.finditer('ATG',DNA):
            remaining = DNA[startMatch.start():]
            for stopMatch in re.finditer('TAA|TGA|TAG',remaining):
                substring = remaining[:stopMatch.end()]
                if len(substring) % 3 == 0:
                    ORFs.append(substring)
                    break
    else:
        print("There are no ORFs in your sequence")
    ORFs.sort(key=len, reverse=True)
    print(ORFs)
    for ORF in ORFs:
        print(ORF,'ORF lenght',len(ORF))


for seq in seqs:
    DNA = seqs[seq]
    ORF = find_ORFs(DNA)
