snakemake \
	--snakefile ../wes_copy_number.snake \
	--configfile ../wes_copy_number.yaml \
	--cluster-config ../wes_copy_number.cluster-uger.yaml \
	--drmaa " {cluster.opts}" \
	--latency-wait 30 \
	-j 100 \
	--rerun-incomplete
