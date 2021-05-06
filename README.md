# PhyloSeqReorder
# Language: Python
# Input: TXT (keyword-value pairs)
# Output: CSV
# Tested with: PluMA 1.1, Python 3.6
# Dependency:

PluMA plugin that takes a PhyloSeq-compatible OTU table and
reorders samples in accordance with its corresponding metadata.

The plugin accepts as input a tab-delimited parameter file
of keyword-value pairs:
OTU: OTU table
META: Metadata

The plugin produces as output the same OTU table, with columns
(samples) moved around.  The order they appear will now be the 
same as they appear in the metadata file.
