#This script creates a python dictionary from a fasta file.
#This script find ORFs inside the sequences of a multi-fasta file.
#Genomics data science course.
#Change myfile.fa for the proper file and directory.
import re

myfile = input("Enter a file name and directory:")
try:
    f=open(myfile)
except IOError:
    print("File doesn't exist!")

seqs = {}
for line in f:
    line=line.rstrip()
#Gets rid of triling empy spaces.

    if line[0]=='>':
        words=line.split()
        name=words[0][1:]
        seqs[name] = ''
    else:
        seqs[name] = seqs[name] + line
print("Number of entries:",len(seqs.keys()))
length_seqs = {key:len(seq)for key, seq in seqs.items()}

sorted_length_seqs = sorted(length_seqs.items(), key=lambda kv:kv[1])
print("Entries by length:",sorted_length_seqs)

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

