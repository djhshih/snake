import pandas as pd

pair_annot = pd.read_csv("pair_annotation.tsv", sep="\t")
pair_annot.index = pair_annot["first_id"]
samples = list(pair_annot.index)

sample_annot = pd.read_csv("sample_annotation.tsv", sep="\t")
sample_annot.index = sample_annot["sample_id"]

def sex(sample_id):
    """Get biological sex of patient from whom the sample was taken"""
    return sample_annot.loc[sample_id, "sex"]

def bam_path(sample_id):
    """Get bam file path of sample"""
    return sample_annot.loc[sample_id, "clean_bam_file_capture"]

def second_id(first_id):
    """Get the second sample of a pair"""
    return pair_annot.loc[first_id, 'second_id']

def replace_fext(fname, ext):
    return fname[:-len(ext)] + ext


import os, os.path
os.makedirs('bam')
for sample in set(pair_annot.stack()):
    source = sample_annot.loc[sample, "clean_bam_file_capture"]
    target = "bam/{0}.bam".format(sample)
    if not os.path.exists(target):
        os.symlink(source, target)
        os.symlink(replace_fext(source, "bai"), replace_fext(target, "bai"))

