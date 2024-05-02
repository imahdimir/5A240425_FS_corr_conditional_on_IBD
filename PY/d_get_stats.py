"""

"""

import pandas as pd
import sys
from pathlib import Path

sys.path.append(Path.cwd().as_posix())

from prj.lib import f , v , d , fp , BINS

##
def make_all_combinations() :
    """  """

    ##
    gt = {
            (0 , fp.dsg_0 , v.dsg) : None ,
            (1 , fp.dsg_1 , v.dsg) : None ,
            (2 , fp.dsg_2 , v.dsg) : None ,
            (0 , fp.hc_0 , v.hc)   : None ,
            (1 , fp.hc_1 , v.hc)   : None ,
            (2 , fp.hc_2 , v.hc)   : None ,
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

    for cn in [1] :
        df3[cn] = df3.apply(lambda r : format_file_path(r , cn) , axis = 1)

    ##
    return df3

##
def get_corr_stats(ibd , ipat , gt , info) :
    """  """

    def _test() :
        pass

        ##
        ibd = 0
        ipat = fp.dsg_0
        gt = 'DSG'
        info = 30

    ##
    fn = ipat.format(info = info)
    df0 = pd.read_parquet(fn)
    df0.columns = [v.corr]

    ##
    df = df0[[v.corr]].describe()

    ##
    df.loc[v.n_na] = df0[[v.corr]].isna().sum()

    ##
    df = df.T

    ##
    df = df.rename(columns = {
            'count' : v.n_snps ,
            '50%'   : v.median
            })

    ##
    df[v.gt] = gt
    df[v.info] = info
    df[v.ibd] = ibd

    ##
    reord = {
            v.gt     : None ,
            v.info   : None ,
            v.ibd    : None ,
            v.mean   : None ,
            v.std    : None ,
            v.min    : None ,
            v.q1     : None ,
            v.median : None ,
            v.q3     : None ,
            v.max    : None ,
            v.n_na   : None ,
            v.n_snps : None ,
            }

    df = df[reord.keys()]

    ##
    df = df.convert_dtypes()

    ##
    return df

##
def main() :
    pass

    ##
    df3 = make_all_combinations()

    ##
    df = pd.DataFrame()

    for pr , gt , ip , iscore in df3.itertuples(index = False) :
        print(pr , gt , ip , iscore)
        _df = get_corr_stats(pr , gt , ip , iscore)
        df = pd.concat([df , _df])

        # break

    ##
    df.to_excel(f.corrs , index = False)

    ##
