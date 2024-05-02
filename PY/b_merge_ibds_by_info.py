"""

    """

import pandas as pd
import sys
from pathlib import Path

sys.path.append(Path.cwd().as_posix())

from prj.lib import f , v , d , fp , BINS

##
def ret_all_snps_in_info_range(info_range_start) :
    """ """

    ##
    dfs = pd.read_parquet(f.flt_snps)

    ##
    sc = info_range_start
    msk = dfs[v.info_n].ge(sc)
    msk &= dfs[v.info_n].lt(sc + .01)

    df = dfs[msk]

    ##
    return df

##
def merge_snps_ibd_by_info(info_score) :
    """ """

    ##
    def _test() :
        pass

        ##
        info_score = .7

    ##
    fn = fp.sibs_ibd.format(chr = 1)
    df = pd.read_parquet(fn)

    ##
    dfi = ret_all_snps_in_info_range(info_score)

    c2k0 = [v.sib1 , v.sib2] + list(dfi[v.rsid_n])

    ##
    c2k = df.columns.intersection(c2k0)

    df = df[c2k]

    ##
    for _i in range(2 , 22 + 1) :
        print(_i)

        _p = fp.sibs_ibd.format(chr = _i)
        print(_p)

        _df = pd.read_parquet(_p)

        c2k = _df.columns.intersection(c2k0)

        _df = _df[c2k]

        _idc = [v.sib1 , v.sib2]
        assert df.columns.intersection(_df.columns).difference(_idc).empty

        df = pd.merge(df , _df , how = 'left' , on = _idc)

        print(df.shape)

    ##
    _p = fp.sibs_ibd_i.format(info = int(info_score * 100))
    df.to_parquet(_p , index = False)

##
def merge_snps_ibd_by_info_4_all_info_scores() :
    for isc in BINS :
        print(isc)
        merge_snps_ibd_by_info(isc)

##
def main() :
    pass

    ##
    merge_snps_ibd_by_info_4_all_info_scores()

    ##

    ##

##
def _test() :
    pass

    ##

    ##

    ##

    ##

    ##

    ##
