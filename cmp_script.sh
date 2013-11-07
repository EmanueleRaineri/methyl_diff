#script for comparing
SIZE=1000  
for TYPE in "hh" "lh" "ll"; do
    echo ${TYPE};
    if [ ${TYPE} = hh ]
    then
    COV1=40 ; P1=0.9 ; COV2=40 ; P2=0.5
    elif [ ${TYPE} = lh ]
    then
    COV1=5 ; P1=0.9 ; COV2=40 ; P2=0.5
    elif [ ${TYPE} = ll ]
    then
    COV1=5 ; P1=0.9 ; COV2=5 ; P2=0.5
    fi;
    BCOUNTS=${TYPE}_binomial_counts.txt;
    BERES=${TYPE}_results_beta.txt;
    FIRES=${TYPE}_results_fisher.txt;
    CMPRES=${TYPE}_cmp_results.txt;
    python binomial_sim.py ${COV1} ${P1} ${COV2} ${P2} ${SIZE} > ${BCOUNTS};
    awk '{print $1+1,$2+1,$3+1,$4+1}' ${BCOUNTS} | ocaml str.cma beta_diff.ml > ${BERES};
    echo "#####";
    python fisher.py < ${BCOUNTS} > ${FIRES}; 
    paste ${BERES} ${FIRES} > ${CMPRES};
    python plot_cmp.py ${CMPRES}; 
done
