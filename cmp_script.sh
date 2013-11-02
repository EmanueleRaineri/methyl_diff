#script for comparing

python binomial_sim.py 10 0.9 10 0.1 10 > binomial_counts.txt
awk '{print $1+1,$2+1,$3+1,$4+1}' binomial_counts.txt | ocaml str.cma beta_diff.ml
python fisher.py < binomial_counts.txt

