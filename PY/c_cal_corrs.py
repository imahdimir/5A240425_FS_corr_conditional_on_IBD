"""

    """

import pandas as pd
import sys
from pathlib import Path

sys.path.append(Path.cwd().as_posix())

from prj.lib import f , v , d , fp , BINS

##
def save_corr_4_specific_info_score_n_gt_n_ibd(gt_fp , ibd , op , info) :
    """  """

    def _test() :
        pass

        ##
        gt_fp = fp.dsg_i
        ibd = 0
        op = fp.dsg_0
        info = 70

    ##
    fn = fp.sibs_ibd_i.format(info = info)

    df = pd.read_parquet(fn)

    ##
    fn = gt_fp.format(info = info)

    df2 = pd.read_parquet(fn)

    ##
    msk1 = df[v.sib1].isin(df2[v.iid])
    msk2 = df[v.sib2].isin(df2[v.iid])

    msk = msk1 & msk2

    ##
    df = df[msk]

    ##
    df_s1 = df[[v.sib1]]
    df_s2 = df[[v.sib2]]

    ##
    df_s1 = df_s1.merge(df2 , left_on = v.sib1 , right_on = v.iid)
    df_s2 = df_s2.merge(df2 , left_on = v.sib2 , right_on = v.iid)

    ##
    df_s1 = df_s1.drop(columns = v.iid)
    df_s2 = df_s2.drop(columns = v.iid)

    ##
    df = df.set_index([v.sib1 , v.sib2])

    df_s1 = df_s1.set_index(v.sib1)
    df_s2 = df_s2.set_index(v.sib2)

    ##
    df_s1 = df_s1[df.columns]
    df_s2 = df_s2[df.columns]

    ##
    df = df.reset_index(drop = True)

    ##
    df_s1 = df_s1.reset_index(drop = True)
    df_s2 = df_s2.reset_index(drop = True)

    ##
    msk = df.eq(ibd)

    ##
    df_s1 = df_s1[msk]

    ##
    df_s2 = df_s2[msk]

    ##
    df_cors = df_s1.corrwith(df_s2 , method = 'pearson')
    df_cors = df_cors.to_frame()

    ##
    fn = op.format(info = info)
    df_cors.to_parquet(fn)
    print(fn)

##
def make_all_combinations() :
    """  """

    ##
    gt = {
            (fp.dsg_i , 0 , fp.dsg_0) : None ,
            (fp.dsg_i , 1 , fp.dsg_1) : None ,
            (fp.dsg_i , 2 , fp.dsg_2) : None ,
            (fp.hc_i , 0 , fp.hc_0)   : None ,
            (fp.hc_i , 1 , fp.hc_1)   : None ,
            (fp.hc_i , 2 , fp.hc_2)   : None ,
            }

    gt = {k : v for k , v in zip(range(len(gt)) , gt.keys())}

    df1 = pd.DataFrame.from_dict(data = gt , orient = 'index')

    ##
    df2 = pd.DataFrame(data = BINS , columns = [v.info_score])
    df2 = df2 * 100
    df2 = df2.astype(int)

    ##
    df3 = pd.merge(df1 , df2 , how = 'cross')

    ##
    def format_file_path(row , cn) :
        return row[cn].format(info = row[v.info_score])

    for cn in [0 , 2] :
        df3[cn] = df3.apply(lambda r : format_file_path(r , cn) , axis = 1)

    ##
    return df3

##
def convert_parquet_to_excel(op , info) :
    """  """

    ##
    def _test() :
        pass

        ##
        op = fp.dsg_0
        info = 30

    ##
    fn = op.format(info = info)

    ##
    df = pd.read_parquet(fn)

    ##
    fn = Path(fn).with_suffix('.xlsx')

    ##
    df.to_excel(fn)

    ##
    print(fn)

##
def main() :
    pass

    ##
    df = make_all_combinations()

    ##
    for gpf , ibd , op , info in df.itertuples(index = False) :
        print(gpf , ibd , op , info)
        save_corr_4_specific_info_score_n_gt_n_ibd(gpf , ibd , op , info)

    ##
    for gpf , ibd , op , info in df.itertuples(index = False) :
        print(op , info)
        convert_parquet_to_excel(op , info)

    ##

    ##

    ##

##
def _test() :
    pass

    ##
    fn = '/Users/mmir/Library/CloudStorage/Dropbox/flt_snps.prq'

    df = pd.read_parquet(fn)

    ##

    ##

    ##
