# Snake workflows #

## Demo ##

1. Install `snakemake` and tools that are used within `shell` blocks in `wes_copy_number.snake`.
2. Create a work directory, e.g. `work`.
3. Copy `demo/sample_annotation.tsv` and `demo/pair_annotation.tsv` to `work`. Edit them to specify paths to input files.
4. Run `prepare.py` from within the directory to set up symlinks to the input files.
5. Run `snakemake` locally using `demo/run.sh` or submit jobs to a cluster using
	 `demo/submit.sh`.

