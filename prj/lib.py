import numpy as np
from pathlib import Path

PROJ = '2544_FS_corr_conditional_on_IBD'

BINS = np.arange(.3 , 1 , .01)

class Dir :
    f = '/var/genetics/ws/mahdimir/LC/PRJ_FILES_TEMP/2544_FS_corr_conditional_on_IBD'
    f = Path(f)

    inp = f / 'inp'
    med = f / 'med'
    out = f / 'out'

    dsg_i = inp / 'dsg_i'
    hc_i = inp / 'hc_i'
    ibd_c = inp / 'ibd_c'
    flt_snps = inp / 'flt_snps'
    ibd_segs = inp / 'ibd_segs'

    ibd_c_flt = med / 'ibd_c_flt'
    sibs_snps = med / 'sibs_snps'
    ibd_segs_cord = med / 'ibd_segs_cord'
    all_snps_ibd = med / 'all_snps_ibd'
    sibs_ibd = med / 'sibs_ibd'
    # sibs pairs ibd state for each snp by info score
    sibs_ibd_i = med / 'sibs_ibd_i'

    dsg_0 = out / 'dsg_0'
    dsg_1 = out / 'dsg_1'
    dsg_2 = out / 'dsg_2'
    hc_0 = out / 'hc_0'
    hc_1 = out / 'hc_1'
    hc_2 = out / 'hc_2'

d = Dir()

class FilePattern :
    flt_snps = d.flt_snps / 'c{chr}.txt'
    flt_snps = flt_snps.as_posix()

    sibs_snps = d.sibs_snps / 'c{chr}.prq'
    sibs_snps = sibs_snps.as_posix()

    ibd_segs = d.ibd_segs / 'v2chr_{chr}.ibd.segments'
    ibd_segs = ibd_segs.as_posix()

    ibd_segs_cord = d.ibd_segs_cord / 'c{chr}.prq'
    ibd_segs_cord = ibd_segs_cord.as_posix()

    all_snps_ibd = d.all_snps_ibd / 'c{chr}.prq'
    all_snps_ibd = all_snps_ibd.as_posix()

    sibs_ibd = d.sibs_ibd / 'c{chr}.prq'
    sibs_ibd = sibs_ibd.as_posix()

    sibs_ibd_i = d.sibs_ibd_i / 'i{info}.prq'
    sibs_ibd_i = sibs_ibd_i.as_posix()

    dsg_i = d.dsg_i / 'i{info}.prq'
    dsg_i = dsg_i.as_posix()

    hc_i = d.hc_i / 'i{info}.prq'
    hc_i = hc_i.as_posix()

    dsg_0 = d.dsg_0 / 'i{info}.prq'
    dsg_0 = dsg_0.as_posix()

    dsg_1 = d.dsg_1 / 'i{info}.prq'
    dsg_1 = dsg_1.as_posix()

    dsg_2 = d.dsg_2 / 'i{info}.prq'
    dsg_2 = dsg_2.as_posix()

    hc_0 = d.hc_0 / 'i{info}.prq'
    hc_0 = hc_0.as_posix()

    hc_1 = d.hc_1 / 'i{info}.prq'
    hc_1 = hc_1.as_posix()

    hc_2 = d.hc_2 / 'i{info}.prq'
    hc_2 = hc_2.as_posix()

fp = FilePattern()

class Files :
    all_ibd = d.med / 'all_ibd.prq'
    rel = '/disk/genetics/ukb/alextisyoung/haplotypes/relatives/bedfiles/hap.kin0'
    sibs = d.med / 'sibs.prq'
    flt_snps = d.inp / 'all_flt_snps.prq'
    corrs = d.out / 'corrs.xlsx'

f = Files()

class Vars :
    maf_n = '5'
    info_n = '7'
    rsid_n = '1'
    rsid_n_int = 1
    coor_n = '2'
    coor_n_int = 2
    inf_type = 'InfType'
    fs = 'FS'

    sib1 = 'sib1'
    sib2 = 'sib2'

    msk = 'msk'
    ms1 = 'ms1'
    chr = 'Chr'

    id1 = 'ID1'
    id2 = 'ID2'

    rsid = 'rsid'
    coor = 'coordinate'
    ibd_t = 'IBDType'
    strt_co = 'start_coordinate'
    strt_snp = 'startSNP'
    stop_co = 'stop_coordinate'
    stop_snp = 'stopSNP'

    iid = 'IID'

    info_score = 'info_score'

    corr = 'corr'
    n_na = 'n_na'
    n_snps = 'n_snps'
    median = 'median'
    gt = 'genotype'
    info = 'info_score'
    ibd = 'IBD State'
    mean = 'mean'
    std = 'std'
    min = 'min'
    q1 = '25%'
    q3 = '75%'
    max = 'max'
    dsg = 'Dosages'
    hc = 'Hard Calls'

v = Vars()
