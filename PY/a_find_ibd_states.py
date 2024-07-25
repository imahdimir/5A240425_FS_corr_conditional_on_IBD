"""

    """

import pandas as pd
import sys
from pathlib import Path

sys.path.append(Path.cwd().as_posix())

from prj.lib import f , v , d , fp

##
def make_sibs_prq() :
    """ """

    ##
    dfr = pd.read_csv(f.rel , sep = '\s')

    ##
    msk = dfr[v.inf_type].eq(v.fs)
    dfr = dfr[msk]

    ##
    dfr[[v.sib1 , v.sib2]] = dfr[[v.id1 , v.id2]].astype(str)

    ##
    dfr = dfr[[v.sib1 , v.sib2]]

    ##
    dfr.to_parquet(f.sibs , index = False)

##
def make_chr_sibs_snps_prq(dfs , chr_num) :
    """ """

    ##
    fn = fp.flt_snps.format(chr = chr_num)

    df1 = pd.read_csv(fn , sep = '\s' , header = None)

    ##
    df1[[v.rsid , v.coor]] = df1[[v.rsid_n_int , v.coor_n_int]]

    ##
    df1 = df1[[v.rsid , v.coor]]

    ##
    df = pd.merge(dfs , df1 , how = 'cross')

    ##
    fn = fp.sibs_snps.format(chr = chr_num)
    df.to_parquet(fn , index = False)
    print(fn)

##
def make_all_sibs_snps_prq() :
    """ """

    ##
    dfs = pd.read_parquet(f.sibs)

    ##
    for cn in range(1 , 22 + 1) :
        print(cn)

        make_chr_sibs_snps_prq(dfs , cn)

##
def make_chr_ibd_segs_cord_prq(chr_num) :
    """ """

    ##
    def _test() :
        pass

        ##
        chr_num = 22

    ##
    fn = fp.ibd_segs.format(chr = chr_num)

    ##
    df = pd.read_csv(fn , sep = '\s')

    ##
    df[[v.sib1 , v.sib2]] = df[[v.id1 , v.id2]].astype(str)

    ##
    dfa = df[[v.sib1 , v.sib2 , v.strt_co , v.strt_snp , v.ibd_t]]
    dfb = df[[v.sib1 , v.sib2 , v.stop_co , v.stop_snp , v.ibd_t]]

    dfa = dfa.rename(columns = {
            v.strt_co  : v.coor ,
            v.strt_snp : v.rsid
            })
    dfb = dfb.rename(columns = {
            v.stop_co  : v.coor ,
            v.stop_snp : v.rsid
            })

    ##
    dfc = pd.concat([dfa , dfb])

    ##
    fn = fp.ibd_segs_cord.format(chr = chr_num)
    dfc.to_parquet(fn , index = False)
    print(fn)

##
def make_all_chr_ibd_segs_cord_prq() :
    """ """

    ##
    for cn in range(1 , 22 + 1) :
        print(cn)

        make_chr_ibd_segs_cord_prq(cn)

def make_chr_all_snps_ibd_prq(chr_num) :
    """ """

    ##
    fn = fp.sibs_snps.format(chr = chr_num)

    dfa = pd.read_parquet(fn)

    ##
    fn = fp.ibd_segs_cord.format(chr = chr_num)

    dfb = pd.read_parquet(fn)

    ##
    dfa = pd.concat([dfa , dfb])

    ##
    dfa = dfa.sort_values([v.coor])

    ##
    dfc = dfa.copy()

    ##
    dfc[v.ibd_t] = dfc.groupby([v.sib1 , v.sib2])[v.ibd_t].ffill()

    ##
    dfc[v.ibd_t] = dfc.groupby([v.sib1 , v.sib2])[v.ibd_t].bfill()

    ##
    fn = fp.all_snps_ibd.format(chr = chr_num)
    dfc.to_parquet(fn , index = False)
    print(fn)

##
def make_all_chr_all_snps_ibd_prq() :
    """ """

    ##
    for cn in range(1 , 22 + 1) :
        print(cn)

        make_chr_all_snps_ibd_prq(cn)

##
def pivot_one_chr_sibs_ibd(chr_num) :
    """ """

    ##
    fn = fp.all_snps_ibd.format(chr = chr_num)

    df = pd.read_parquet(fn)

    ##
    df1 = df.pivot_table(index = [v.sib1 , v.sib2] ,
                         columns = v.rsid ,
                         values = v.ibd_t)

    ##
    df1 = df1.reset_index()

    ##
    fn = fp.sibs_ibd.format(chr = chr_num)
    df1.to_parquet(fn , index = False)
    print(fn)

    ##

def pivot_all_chr_sibs_ibd() :
    """ """
    for cn in range(1 , 22 + 1) :
        print(cn)

        pivot_one_chr_sibs_ibd(cn)

##
def main() :
    pass

    ##
    make_sibs_prq()

    ##
    make_all_sibs_snps_prq()

    ##
    make_all_chr_ibd_segs_cord_prq()

    ##
    make_all_chr_all_snps_ibd_prq()

    ##
    pivot_all_chr_sibs_ibd()

##
def _test() :
    pass

    ##
    fn = '/disk/genetics/ukb/mahdimir/PRJ_FILES_ARCH/1144_plot_all_70_bins/med/dsg_i/i30.prq'

    df = pd.read_parquet(fn)

    ##
    fn = '/var/genetics/ws/mahdimir/DB/v2chr_22.ibd'

    df = pd.read_csv(fn , sep = '\s')

    ##
    fn  # write a function d

    ##
    df = ret_all_snps_in_info_range(.7)

    ##
    df = pd.read_parquet(f.all_flt_snps)

    ##
    from bgen_reader import open_bgen

    fn = '/disk/genetics/ukb/mahdimir/PRJ_FILES_ARCH/1144_plot_all_70_bins/inp/plink_out/c22.bgen'

    bgn = open_bgen(fn)

    ##
    rs = list(bgn.rsids)

    ##
    fn = '/disk/genetics/ukb/mahdimir/PRJ_FILES_ARCH/1144_plot_all_70_bins/inp/flt_snps/c22.txt'

    df = pd.read_csv(fn , sep = '\s' , header = None)

    ##
    fn = '/var/genetics/ws/mahdimir/LC/PRJ_FILES_TEMP/2544_FS_corr_conditional_on_IBD/inp/flt_snps/c1.txt'

    df = pd.read_csv(fn , sep = '\s' , header = None)

    ##
    df[v.chr] = 1

    ##
    df = df[[v.rsid_n , v.coor_n]]

    ##

    dfs = pd.read_parquet(f.sibs)

    ##
    fn = '/disk/genetics/ukb/mahdimir/PRJ_FILES_ARCH/1144_plot_all_70_bins/inp/flt_snps/c22.txt'

    df1 = pd.read_csv(fn , sep = '\s' , header = None)

    ##
    df1[[v.rsid , v.coor]] = df1[[v.rsid_n_int , v.coor_n_int]]

    ##
    df1 = df1[[v.rsid , v.coor]]

    ##
    df = pd.merge(dfs , df1 , how = 'cross')

    ##
    dfv = df.head()

    ##
    df.to_parquet()

    ##
