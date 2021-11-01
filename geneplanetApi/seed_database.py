#!/usr/bin/env python

import io
import os
import pandas as pd

# Script that reads huge vcf file in parts and pushes chunks to database
def read_vcf(path):
    chunksize=100000
    header = 38

    df = pd.read_csv(
        path,
        header=header,
        names=['chrom', 'pos', 'chrom_id', 'ref', 'alt', 'ch_format'],
        delim_whitespace=True,
        chunksize=chunksize
    )
    i = 0;
    db_url = 'sqlite:///db.sqlite3'

    for chunk in df:
        chunk.to_sql(
            'geneplanetApi_genotype',
            db_url,
            if_exists='append',
            index=False
        )
        i += 1
        print("Done " + str(i*chunksize))
    

read_vcf(os.path.join(os.path.dirname(os.path.realpath(__file__)), "hg37variants1000g.vcf"))


