# read srr access number file 
# SRR00000  EV_3
# hisat2 -x ../../reference_seq/yeast_ref -U ../../RNA_seq/SRR1916154.fastq | samtools view -bS - | samtools sort -@ 4 - -o 3b_strain2#3.sort.bam
# read read access file 
# for each line :
#   generate wget cmd 

import sys
# print(sys.argv)
ref = sys.argv[1]
fq_dir = sys.argv[2]
acc_file = sys.argv[3]
with open(acc_file,'r')as read_acc_file:
    for line in read_acc_file:
        line = line.strip().split('\t')
        cmd_str = 'hisat2 -x {ref} -U {fq_dir}/{srr_acc}.fastq | samtools view -bS - | samtools sort -@ 4 - -o {sample_real_name}.sort.bam\nsamtools index {sample_real_name}.sort.bam'.format(ref = ref,fq_dir = fq_dir,srr_acc = line[0],sample_real_name = line[1])
        print(cmd_str)
