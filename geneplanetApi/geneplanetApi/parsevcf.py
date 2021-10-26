#!/usr/bin/env python

import io
import os
import pandas as pd
import settings

def read_vcf(path):
    with open(path, 'r') as f:
        lines = [l for l in f if not l.startswith('##')]
    return pd.read_csv(
        io.StringIO(''.join(lines)),
        header=0,
        names=['CHROM', 'POS', 'ID', 'REF', 'ALT', 'FORMAT'],
        sep='\t',
    )


df = read_vcf(os.path.join(settings.BASE_DIR, "first1k.vcf"))
db_url = 'sqlite:///db.sqlite3'
df.to_sql('geneplanetApi_genotype',
            db_url)