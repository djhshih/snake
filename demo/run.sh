snakemake \
	--snakefile ../wes_copy_number.snake \
	--configfile ../wes_copy_number.yaml \
	--latency-wait 30 \
	-j 100 \
	--rerun-incomplete
