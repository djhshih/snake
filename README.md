# Snake workflows #

## Usage ##

1. Install `snakemake` and tools that are used within `shell` blocks in `wes_copy_number.snake`.
2. Edit `demo/sample_annotation.tsv` and `demo/pair_annotation.tsv` to specify paths to input files.
3. Create a work directory. Copy `sample_annotation.tsv` and
	 `pair_annotation.tsv` there. Run `prepare.py` from within the directory to
   set up symlinks to the input files.
4. Run `snakemake` locally using `demo/run.sh` or submit jobs to a cluster using
	 `demo/submit.sh`.

