module load sratoolkit
# usage: ./pipe_download_dataset outdir sample_sheet 
# samples sheet has the form:
# RSSXXXXX Name_of_sample_1
# RSSXXXXX Name_of_sample_2
# ---

#variables (provide absolute paths)
outdir=$(realpath $1)
samples_sheet=$(realpath $2)

#create fastq_files directory inside output directory
mkdir $outdir"/fastq_files"

#download sra files (found in /home/ferrari/ncbi/public/sra/)
for i in $(cut -d ' ' -f 1 $samples_sheet); do prefetch -v $i; done

#generate fastq files to store in output directory
for i in $(cut -d ' ' -f1 $samples_sheet); do fastq-dump --outdir $outdir --split-files "/home/ferrari/ncbi/public/sra/"$i".sra"; done

#rename files
/data/manke/group/ferrari/coding_projects/Download_datasets/Rename_fastq_files.py $outdir $samples_sheet

#move renamed files in fastq_files directory
mv $outdir/*.fastq $outdir/fastq_files/

#compress files in fastq.gz format
for i in $outdir/fastq_files/*.fastq; do echo "gzipping $i"; gzip $i; done



