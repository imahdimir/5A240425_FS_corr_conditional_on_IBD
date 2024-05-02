#!/usr/bin/env Rscript

library("ggplot2")
library("glue")
library('readxl')


dta_fn <- '/Users/mahdi/Library/CloudStorage/Dropbox/out/corrs.xlsx'

dta <- read_excel(dta_fn)

colnames(dta)[2] <- 'Info'
colnames(dta)[3] <- 'IBD'

dta$se = dta$std / sqrt(dta$n_snps)
dta$Info = dta$Info / 100


# plot correlations
ggplot(dta, aes(x = Info, y = mean, color=genotype, shape=factor(IBD))) +
  geom_point() +
  geom_errorbar(aes(ymin=mean-1.96*se, ymax=mean+1.96*se), width=.01) +
  geom_line() +
  geom_hline(yintercept=c(0, 0.5, 1), linetype="dashed") +
  theme_classic() +
  labs(x = "INFO Score", y = "Mean Genotype Correlation")



ofn <- '/Users/mahdi/Library/CloudStorage/Dropbox/out/mean_gt_by_ibd.png'

ggsave(ofn)


for (ibd in 0:2)
{
  
  print(ibd)
  
  df <- dta %>% filter(IBD == ibd)
  
  # plot correlations
  ggplot(df, aes(x = Info, y = mean, color=genotype)) +
    geom_point() +
    geom_errorbar(aes(ymin=mean-1.96*se, ymax=mean+1.96*se), width=.01) +
    geom_line() +
    geom_hline(yintercept=ibd / 2, linetype="dashed") +
    theme_classic() +
    labs(x = "INFO Score", y = "Mean Genotype Correlation")
  
  
  ofn <- glue('/Users/mahdi/Library/CloudStorage/Dropbox/out/mean_gt_by_ibd_', ibd, '.png')
  print(ofn)
  ggsave(ofn)
  
}