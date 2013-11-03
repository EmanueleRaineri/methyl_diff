#script for comparing
SIZE=1000
COV1=40
P1=0.9
COV2=40
P2=0.5
python binomial_sim.py ${COV1} ${P1} ${COV2} ${P2} ${SIZE} > binomial_counts.txt
awk '{print $1+1,$2+1,$3+1,$4+1}' binomial_counts.txt | ocaml str.cma beta_diff.ml > results_beta.txt
echo "#####"
python fisher.py < binomial_counts.txt > results_fisher.txt
paste results_beta.txt results_fisher.txt > cmp_results.txt

