SIZE=1000
####
COV1=$1 ; P1=0.9 ; COV2=$2 ; P2=0.5
echo "=${COV1}=${COV2}="
echo "generating tp...${P1} ${P2}"
python binomial_sim.py ${COV1} ${P1} ${COV2} ${P2} ${SIZE} > tp.txt
P1=0.5 ;  P2=0.5
echo "generating tn...${P1} ${P2}"
python binomial_sim.py ${COV1} ${P1} ${COV2} ${P2} ${SIZE} > tn.txt
####
echo "fisher on tp..."
python fisher.py < tp.txt > fisher_of_tp_${COV1}_${COV2}.txt
echo "fisher on tn..."
python fisher.py < tn.txt > fisher_of_tn_${COV1}_${COV2}.txt
echo "beta_diff on tp"
awk '{print $1+1,$2+1,$3+1,$4+1}' tp.txt | ocaml str.cma beta_diff.ml > beta_of_tp_${COV1}_${COV2}.txt
echo "beta_diff on tn"
awk '{print $1+1,$2+1,$3+1,$4+1}' tn.txt | ocaml str.cma beta_diff.ml > beta_of_tn_${COV1}_${COV2}.txt
#######
python compute_power.py fisher_of_tp_${COV1}_${COV2}.txt fisher_of_tn_${COV1}_${COV2}.txt > fisher.roc.${COV1}_${COV2}.txt
python compute_power_beta.py beta_of_tp_${COV1}_${COV2}.txt beta_of_tn_${COV1}_${COV2}.txt > beta.roc.${COV1}_${COV2}.txt
paste fisher.roc.${COV1}_${COV2}.txt beta.roc.${COV1}_${COV2}.txt > roc_${COV1}_${COV2}.txt
cat fisher_of_tp_${COV1}_${COV2}.txt fisher_of_tn_${COV1}_${COV2}.txt > fisher_${COV1}_${COV2}.txt 
cat beta_of_tp_${COV1}_${COV2}.txt beta_of_tn_${COV1}_${COV2}.txt > beta_${COV1}_${COV2}.txt 
paste fisher_${COV1}_${COV2}.txt beta_${COV1}_${COV2}.txt > fisher_beta_${COV1}_${COV2}.txt
#plot with plot_roc.py 
#######
