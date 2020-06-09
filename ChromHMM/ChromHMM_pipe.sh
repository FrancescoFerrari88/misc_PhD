### ChromHMM pipeline to be run after DNA-mapping or ChIP-seq snakemake workflows ###

### RUN THIS FILE FROM INSIDE THE OUTPUT FOLDER OF THE SNAKEMAKE PIPELINES

### requisites: create a folder called "ChromHMM" inside the output directory of the snakemake workflows; in "ChromsHMM" create a file called "cellmarkfiletable.tsv" of the form:
### cell_type	mark1	bam_file_name_mark2.bam
### cell_type	mark2	bam_file_name_mark2.bam
### ...
### additional files (e.g chrlengthfile) can be found in /home/ferrari/.conda/envs/ferrari_env/share/chromhmm-1.14-/ NB: 1. CHECK IF CHROMOSOME NAMES IN BAM FILES CORRESPOND TO CHROMOSOMES NAMES IN chrlengthfile 2. Check if files in the COORD folder (used for OverlapErichment) report chromosomes as in bam files

# arguments to provide to the script

organism_assembly=$1
num_states=$2
celltable=$(realpath $3)
outdir=$(realpath $4)
indir=$(realpath $5)

# Create ChromHMM folder
mkdir ChromHMM 

# Create symbolic link of chromosome sizes file into ChromHMM folder
ln -s -t $outdir ~/anaconda3/envs/Chrom-Seg/share/chromhmm-1.15-0/ChromHMM/CHROMSIZES/$organism_assembly".txt"

# Create "cellmarkfiletable.tsv"
for i in filtered_bam/*.bam; do echo $(basename $i) | awk -F "_" 'BEGIN { OFS = "\t" } { print $2,$3,$i }' >> ChromHMM/cellmarkfiletable.tsv ; done 

# Run BinarizeBam

java -mx4000M -jar /home/ferrari/.conda/envs/ferrari_env/share/chromhmm-1.14-/ChromHMM.jar BinarizeBam $outdir/$organism_assembly".txt" $indir $celltable $outdir/output_BinarizeBam/

# Run LearnModel
java -mx4000M -jar /home/ferrari/.conda/envs/ferrari_env/share/chromhmm-1.14-/ChromHMM.jar LearnModel -p 8 $outdir/output_BinarizeBam/ $outdir/output_LearnModel_$num_states/ $num_states $organism_assembly 
