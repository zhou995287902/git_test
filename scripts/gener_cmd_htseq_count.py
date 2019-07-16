# read srr access number file 
# SRR00000
# htseq-count -f bam -r pos ../read_aln/3b_strain2#3.sort.bam ../../reference_seq/Saccharomyces_cerevisiae.R64-1-1.97.gtf > 3b_strain2#3.count.tab
# read read access file 
# for each line :
#   generate wget cmd 

import sys
# print(sys.argv)
acc_file = sys.argv[3]
bam_dir = sys.argv[1]
ref_seq = sys.argv[2]
with open(acc_file,'r')as read_acc_file:
    for line in read_acc_file:
        line = line.strip().split('\t')
        cmd_str = 'htseq-count -f bam -r pos {bam_dir}/{sample_real_name}.sort.bam {ref_seq} > {sample_real_name}.count.tab'.format(bam_dir = bam_dir ,ref_seq = ref_seq, sample_real_name = line[1])
        print(cmd_str)
