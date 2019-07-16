# read srr access number file 
# SRR00000
#  wget ftp://ftp.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR191/SRR1916152/SRR1916152.sra
# read read access file 
# for each line :
#   generate wget cmd 

import sys
# print(sys.argv)
acc_file = sys.argv[1]
with open(acc_file,'r')as read_acc_file:
    for line in read_acc_file:
        line = line.strip()
        cmd_str = 'wget ftp://ftp.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/{}/{}/{}.sra'.format(line[0:6],line,line)
        print(cmd_str)
