#!/usr/bin/env Rscript

library("data.table")
library("dplyr")
library("plinkFile")
library("genio")
library("ggplot2")
library("glue")
library('readxl')


gtype_name = 'Dosages'
info_score = 30
ibd = 0
ifp = '/Users/mahdi/Library/CloudStorage/Dropbox/out/dsg_0/i%d.xlsx'

fp <- sprintf(ifp, info_score)
print(fp)

df <- read_excel(fp, col_names = T)

names(df) = c('snp', 'corr')
df <- na.omit(df)

n_snps <- nrow(df)
dn = info_score / 100

ggplot(data.frame(df), aes(x = corr)) +
  geom_histogram(binwidth = 0.02, fill = "#56B4E9", colour = "#56B4E9", alpha = 0.5) +
  labs(title = glue('{gtype_name}, SNPs with INFO = {dn} - {dn+0.01} & IBD = {ibd}, (n = {n_snps})'),
       x = "Genotype Correlation",
       y = "Count") +
  geom_vline(xintercept=ibd / 2, linetype="dotted") +
  geom_vline(xintercept=mean(df$corr), linetype="dashed", color = 'red') +
  theme_classic() +
  theme(legend.position="none")

op = '/Users/mahdi/Library/CloudStorage/Dropbox/out/dsg_0_plots/i%d.png'
fpo = sprintf(op, info_score)
print(fpo)

ggsave(fpo)


plot_corr <- function(gt, info, ibd, ifp, op) 
{
  
  fp <- sprintf(toString(ifp), info)
  print(fp)
  
  df <- read_excel(fp, col_names = T)
  
  names(df) = c('snp', 'corr')
  df <- na.omit(df)
  
  n_snps <- nrow(df)
  dn = info / 100
  
  ggplot(data.frame(df), aes(x = corr)) +
    geom_histogram(binwidth = 0.02, fill = "#56B4E9", colour = "#56B4E9", alpha = 0.5) +
    labs(title = glue('{gt}, SNPs with INFO = {dn} - {dn+0.01} & IBD = {ibd}, (n = {n_snps})'),
         x = "Genotype Correlation",
         y = "Count") +
    
    geom_vline(xintercept=ibd / 2, linetype="dotted") +
    geom_vline(xintercept=mean(df$corr), linetype="dashed", color = 'red') +
    
    theme_classic() +
    theme(legend.position="none")
  
  fpo = sprintf(toString(op), info)
  print(fpo)
  
  ggsave(fpo)
}


out_pre <- '/Users/mahdi/Library/CloudStorage/Dropbox/out'


dsg_0 <- glue({out_pre}, '/dsg_0/i%d.xlsx')
dsg_1 <- glue({out_pre}, '/dsg_1/i%d.xlsx')
dsg_2 <- glue({out_pre}, '/dsg_2/i%d.xlsx')

hc_0 <- glue({out_pre}, '/hc_0/i%d.xlsx')
hc_1 <- glue({out_pre}, '/hc_1/i%d.xlsx')
hc_2 <- glue({out_pre}, '/hc_2/i%d.xlsx')

o_dsg_0 <- glue({out_pre}, '/dsg_0_plots/i%d.png')
o_dsg_1 <- glue({out_pre}, '/dsg_1_plots/i%d.png')
o_dsg_2 <- glue({out_pre}, '/dsg_2_plots/i%d.png')

o_hc_0 <- glue({out_pre}, '/hc_0_plots/i%d.png')
o_hc_1 <- glue({out_pre}, '/hc_1_plots/i%d.png')
o_hc_2 <- glue({out_pre}, '/hc_2_plots/i%d.png')

dsg <- 'Dosages'
hc <- 'Hard Calls'

info <- seq(30, 99, 1)

prd1 <- expand.grid(dsg, 0, dsg_0, o_dsg_0, info)
prd <- prd1

prd1 <- expand.grid(dsg, 1, dsg_1, o_dsg_1, info)
prd <- rbind(prd, prd1)

prd1 <- expand.grid(dsg, 2, dsg_2, o_dsg_2, info)
prd <- rbind(prd, prd1)

prd1 <- expand.grid(hc , 0, hc_0, o_hc_0, info)
prd <- rbind(prd, prd1)

prd1 <- expand.grid(hc , 1, hc_1, o_hc_1, info)
prd <- rbind(prd, prd1)

prd1 <- expand.grid(hc , 2, hc_2, o_hc_2, info)
prd <- rbind(prd, prd1)


x <- 1
gt = prd[x, 'Var1']
ibd = prd[x, 'Var2']
info = prd[x, 'Var5']
ifp = prd[x, 'Var3']
op = prd[x, 'Var4']

plot_corr(gt, info, ibd, ifp, op)

for (x in 1:nrow(prd))
{
  print(x)
  
  gt = prd[x, 'Var1']
  ibd = prd[x, 'Var2']
  ifp = prd[x, 'Var3']
  op = prd[x, 'Var4']
  info = prd[x, 'Var5']
  
  plot_corr(gt, info, ibd, ifp, op)
  
}