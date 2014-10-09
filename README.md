DBDS
====

-
This is an integrative pipeline (Python) that using Druids (DRUIDS—Detection of regions with unexpected internal deviation from stationarity, http://dx.doi.org/10.1002/jez.b.21032) to calculate and detect conservative sites in phylogenetic data set.
Currently, the pipeline contains two steps.

Step 1: Batch execute pyDruids.py and store analysis results in designated folder
		Usage: python DBDS_Step1.py -s example.nex

Example: python DBDS_Step1.py -s Tang_COI_657.nex

Step 2: Calculate the conservative sites and generate non-stationary sites statistical report
		Usage: python DBDS_Step2.py -f folder_name -sl sequence_length -cp consensus_percentage

Example: python DBDS_Step2.py -f Tang_COI_657 -sl 2000 -cp 50


Ongoing tasks:

1) Data set matrix manipulation: according to the analysis results, this script is planning to edit matrix content for further analysis and examination.

2) Interoperability with otherphylogenetic analysis software.

