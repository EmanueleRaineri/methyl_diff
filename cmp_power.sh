SIZE=1000
DATA=data
####
COV1=$1 ; P1=0.9 ; COV2=$2 ; P2=0.5
#
POS=$DATA/p_${COV1}_${COV2}.txt
NEG=$DATA/n_${COV1}_${COV2}.txt
#
FISHERP=$DATA/fisher_of_p_${COV1}_${COV2}.txt
FISHERN=$DATA/fisher_of_n_${COV1}_${COV2}.txt
FISHER_ROC=$DATA/fisher.roc.${COV1}_${COV2}.txt
FISHER_LOG=$DATA/fisher.log.${COV1}_${COV2}.txt
#
ZSCOREP=$DATA/zscore_of_p_${COV1}_${COV2}.txt
ZSCOREN=$DATA/zscore_of_n_${COV1}_${COV2}.txt
ZSCORE_ROC=$DATA/zscore.roc.${COV1}_${COV2}.txt
ZSCORE_LOG=$DATA/zscore.log.${COV1}_${COV2}.txt
#
BETAP=$DATA/beta_of_p_${COV1}_${COV2}.txt
BETAN=$DATA/beta_of_n_${COV1}_${COV2}.txt
BETA_ROC=$DATA/beta.roc.${COV1}_${COV2}.txt
BETA_LOG=$DATA/beta.log.${COV1}_${COV2}.txt
##########
echo "=${COV1}=${COV2}="
echo "generating p...${P1} ${P2}"
python binomial_sim.py ${COV1} ${P1} ${COV2} ${P2} ${SIZE} > $POS
P1=0.5 ;  P2=0.5
echo "generating n...${P1} ${P2}"
python binomial_sim.py ${COV1} ${P1} ${COV2} ${P2} ${SIZE} > $NEG 
####
echo "fisher on p..."
python fisher.py < $POS > $FISHERP 
echo "fisher on n..."
python fisher.py < $NEG > $FISHERN
#######
echo "beta_diff on p"
awk '{print $1+1,$2+1,$3+1,$4+1}' $POS | ./methyl_diff > $BETAP 
echo "beta_diff on n"
awk '{print $1+1,$2+1,$3+1,$4+1}' $NEG | ./methyl_diff > $BETAN 
#######
echo "Z score on p"
python zscore.py < $POS  > $ZSCOREP 
python zscore.py < $NEG  > $ZSCOREN 
#######
echo "compute power"
#fisher
python compute_power_fisher.py $FISHERP $FISHERN > $FISHER_ROC 2> $FISHER_LOG
#z score
python compute_power_zscore.py $ZSCOREP $ZSCOREN > $ZSCORE_ROC 2> $ZSCORE_LOG
#beta
python compute_power_beta.py $BETAP $BETAN > $BETA_ROC  2> $BETA_LOG
#######
paste $FISHER_ROC $BETA_ROC $ZSCORE_ROC > $DATA/roc_${COV1}_${COV2}.txt
cat $FISHERP $FISHERN > $DATA/fisher_${COV1}_${COV2}.txt 
cat $BETAP $BETAN > $DATA/beta_${COV1}_${COV2}.txt 
cat $ZSCOREP $ZSCOREN  > $DATA/zscore_${COV1}_${COV2}.txt 
paste $DATA/fisher_${COV1}_${COV2}.txt $DATA/beta_${COV1}_${COV2}.txt $DATA/zscore_${COV1}_${COV2}.txt > $DATA/fisher_beta_zscore_${COV1}_${COV2}.txt
#######
