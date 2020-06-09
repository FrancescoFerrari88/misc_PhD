#!/usr/bin/python

import os
import sys

# variables
outdir=sys.argv[1]
samples_sheet=sys.argv[2]

#get abs_paths
outdir = os.path.abspath(outdir)
samples_sheet=os.path.abspath(samples_sheet)

# read in sample sheet
map_dic=dict()
with open(samples_sheet) as mapp:
    for line in mapp:
        lista=line.strip().split()
        map_dic[lista[0]] = lista[1]
print(map_dic)

# list files in directory
list_dir=os.listdir(outdir)
print(list_dir)
list_dir=[i for i in list_dir if i.startswith('SRR')]
print('\n{} SRR files were found in the output directory:\n{}\n\nProceed with renaming\n'.format(len(list_dir),list_dir))

# rename
single_paired={}
for i in list_dir:
    sample = i.split('.')[-2].split('_')[-2]
    read = i.split('.')[-2].split('_')[-1]
    if not sample in single_paired:
        single_paired[sample]=[read]
    else:
        single_paired[sample].append(read)

for i in list_dir:
    sample = i.split('.')[-2].split('_')[-2]
    read = i.split('.')[-2].split('_')[-1]
    if len(single_paired[sample]) == 2:
        print("{}, read {}".format(sample, read))
        if read == '1':
            if sample in map_dic:
                os.rename(os.path.join(outdir,i), os.path.join(outdir,'{}_R1.fastq'.format(map_dic[sample])))
                print('{} --> {}_R1.fastq'.format(sample,map_dic[sample]))
            else:
                print('sample {} could not be renamed because missing from samples sheet'.format(i))

        elif read == '2':
            if sample in map_dic:
                os.rename(os.path.join(outdir,i), os.path.join(outdir,'{}_R2.fastq'.format(map_dic[sample])))
                print('{} --> {}_R2.fastq'.format(sample,map_dic[sample]))
            else:
                print('sample {} could not be renamed because missing from samples sheet'.format(sample))
    
        else:
            print('Something is wrong. Check if samples names are properly formatted ')
            break
    elif len(single_paired[sample]) == 1:
        if sample in map_dic:
            os.rename(os.path.join(outdir,i),os.path.join(outdir,'{}.fastq'.format(map_dic[sample])))
            print('{} --> {}.fastq').format(sample,map_dic[sample])
        else:
            print('sample {} could not be renamed because missing from samples sheet'.format(i))




