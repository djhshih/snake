#!/usr/bin/env python3

import pandas as pd

pair_annot = pd.read_csv("pair_annotation.tsv", sep="\t")
pair_annot.index = pair_annot["case_id"]
samples = list(pair_annot.index)

sample_annot = pd.read_csv("sample_annotation.tsv", sep="\t")
sample_annot.index = sample_annot["sample_id"]

def sex(sample_id):
    """Get biological sex of patient from whom the sample was taken"""
    return sample_annot.loc[sample_id, "sex"]

def bam_path(sample_id):
    """Get bam file path of sample"""
    return sample_annot.loc[sample_id, "clean_bam_file_capture"]

def control_id(case_id):
    """Get the control sample of a case-control pair"""
    return pair_annot.loc[case_id, 'control_id']

def replace_fext(fname, ext):
    return fname[:-len(ext)] + ext


import os, os.path
root_dir = 'bam'
if not os.path.exists(root_dir): os.makedirs(root_dir)
for sample in set(pair_annot.stack()):
    source = sample_annot.loc[sample, "clean_bam_file_capture"]
    target = "{0}/{1}.bam".format(root_dir, sample)
    print("{0} -> {1}".format(source, target))
    if not os.path.exists(target):
        os.symlink(source, target)
        os.symlink(replace_fext(source, "bai"), replace_fext(target, "bai"))

