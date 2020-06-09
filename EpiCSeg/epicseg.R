#!/usr/lib64/R/bin/Rscript
cat('loading epicseg\n')
library(epicseg, lib.loc="/home/ferrari/R/x86_64-redhat-linux-gnu-library/3.4")
epicseg:::CLI(args=commandArgs(trailingOnly=TRUE), epicseg:::getProg())
