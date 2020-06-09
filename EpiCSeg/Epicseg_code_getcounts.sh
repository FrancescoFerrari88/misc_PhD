Rscript /data/manke/group/ferrari/bin/epicseg.R getcounts -r /data/manke/group/ferrari/PhD_project/reference_datasets/mESC_Epigenome_Chronis_dataset/output_DNA-mapping_snakepipe/EpiCSeg/count_matrix_final -m H3K4me3:/data/manke/group/ferrari/PhD_project/reference_datasets/mESC_Epigenome_Chronis_dataset/output_DNA-mapping_snakepipe/filtered_bam/Chronis_mESC_H3K4me3_ChIP-Seq.filtered.bam -m H3K4me2:/data/manke/group/ferrari/PhD_project/reference_datasets/mESC_Epigenome_Chronis_dataset/output_DNA-mapping_snakepipe/filtered_bam/Chronis_mESC_H3K4me2_ChIP-Seq.filtered.bam -m H3K4me1:/data/manke/group/ferrari/PhD_project/reference_datasets/mESC_Epigenome_Chronis_dataset/output_DNA-mapping_snakepipe/filtered_bam/Chronis_mESC_H3K4me1_ChIP-Seq.filtered.bam -m H3K36me3:/data/manke/group/ferrari/PhD_project/reference_datasets/mESC_Epigenome_Chronis_dataset/output_DNA-mapping_snakepipe/filtered_bam/Chronis_mESC_H3K36me3_ChIP-Seq.filtered.bam -m H3K27ac:/data/manke/group/ferrari/PhD_project/reference_datasets/mESC_Epigenome_Chronis_dataset/output_DNA-mapping_snakepipe/filtered_bam/Chronis_mESC_H3K27ac_ChIP-Seq.filtered.bam -m H3K79me2:/data/manke/group/ferrari/PhD_project/reference_datasets/mESC_Epigenome_Chronis_dataset/output_DNA-mapping_snakepipe/filtered_bam/Chronis_mESC_H3K79me2_ChIP-Seq.filtered.bam -m H3K9ac:/data/manke/group/ferrari/PhD_project/reference_datasets/mESC_Epigenome_Chronis_dataset/output_DNA-mapping_snakepipe/filtered_bam/Chronis_mESC_H3K9ac_ChIP-Seq.filtered.bam -m H3K27me3:/data/manke/group/ferrari/PhD_project/reference_datasets/mESC_Epigenome_Chronis_dataset/output_DNA-mapping_snakepipe/filtered_bam/Chronis_mESC_H3K27me3_ChIP-Seq.filtered.bam -m H3K9me3:/data/manke/group/ferrari/PhD_project/reference_datasets/mESC_Epigenome_Chronis_dataset/output_DNA-mapping_snakepipe/filtered_bam/Chronis_mESC_H3K9me3_ChIP-Seq.filtered.bam -t /data/manke/group/ferrari/PhD_project/reference_datasets/mESC_Epigenome_Chronis_dataset/output_DNA-mapping_snakepipe/EpiCSeg/counts --mapq 10 -p FALSE -s 100 -n 8