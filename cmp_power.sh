SIZE=1000
DATA=data
####
COV1=$1 ; P1=0.9 ; COV2=$2 ; P2=0.5
#
FISHERP=$DATA/fisher_of_p_${COV1}_${COV2}.txt
FISHERN=$DATA/fisher_of_n_${COV1}_${COV2}.txt
FISHER_ROC=$DATA/fisher.roc.${COV1}_${COV2}.txt
#
ZSCOREP=$DATA/zscore_of_p_${COV1}_${COV2}.txt
ZSCOREN=$DATA/zscore_of_n_${COV1}_${COV2}.txt
ZSCORE_ROC=$DATA/zscore.roc.${COV1}_${COV2}.txt
#
BETAP=$DATA/beta_of_p_${COV1}_${COV2}.txt
BETAN=$DATA/beta_of_n_${COV1}_${COV2}.txt
BETA_ROC=$DATA/beta.roc.${COV1}_${COV2}.txt
##########
echo "=${COV1}=${COV2}="
echo "generating p...${P1} ${P2}"
python binomial_sim.py ${COV1} ${P1} ${COV2} ${P2} ${SIZE} > $DATA/p.txt
P1=0.5 ;  P2=0.5
echo "generating n...${P1} ${P2}"
python binomial_sim.py ${COV1} ${P1} ${COV2} ${P2} ${SIZE} > $DATA/n.txt
####
echo "fisher on p..."
python fisher.py < $DATA/p.txt > $FISHERP 
echo "fisher on n..."
python fisher.py < $DATA/n.txt > $FISHERN
#######
echo "beta_diff on p"
awk '{print $1+1,$2+1,$3+1,$4+1}' $DATA/p.txt | ocaml str.cma beta_diff.ml > $BETAP 
echo "beta_diff on n"
awk '{print $1+1,$2+1,$3+1,$4+1}' $DATA/n.txt | ocaml str.cma beta_diff.ml > $BETAN 
#######
echo "Z score on p"
python zscore.py < $DATA/p.txt |awk '{print $2}' > $ZSCOREP 
python zscore.py < $DATA/n.txt |awk '{print $2}' > $ZSCOREN 
#######
echo "compute power"
#fisher
python compute_power.py $FISHERP $FISHERN > $FISHER_ROC 
#z score
python compute_power.py $ZSCOREP $ZSCOREN > $ZSCORE_ROC 
#beta
python compute_power_beta.py $BETAP $BETAN > $BETA_ROC 
#######
paste $FISHER_ROC $BETA_ROC $ZSCORE_ROC > $DATA/roc_${COV1}_${COV2}.txt
cat $FISHERP $FISHERN > $DATA/fisher_${COV1}_${COV2}.txt 
cat $BETAP $BETAN > $DATA/beta_${COV1}_${COV2}.txt 
cat $ZSCOREP $ZSCOREN  > $DATA/zscore_${COV1}_${COV2}.txt 
paste $DATA/fisher_${COV1}_${COV2}.txt $DATA/beta_${COV1}_${COV2}.txt $DATA/zscore_${COV1}_${COV2}.txt > $DATA/fisher_beta_zscore_${COV1}_${COV2}.txt
#######
