#!/usr/bin/env python

import io
import os
import pandas as pd

def read_vcf(path):
    with open(path, 'r') as f:
        lines = [l for l in f if not l.startswith('##')]
    return pd.read_csv(
        io.StringIO(''.join(lines)),
        header=0,
        names=['chrom', 'pos', 'chrom_id', 'ref', 'alt', 'ch_format'],
        # sep='\t',
        delim_whitespace=True
    )


df = read_vcf(os.path.join(os.path.dirname(os.path.realpath(__file__)), "first1k.vcf"))
db_url = 'sqlite:///db.sqlite3'
df.to_sql('geneplanetApi_genotype',
            db_url,
            if_exists='replace',
            index=False)