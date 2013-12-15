COMP=pdftex
methyl_diff: methyl_diff.c
	gcc -Wall -static -O3 -o methyl_diff $< -lm

beta_paper.ps : beta_paper.dvi
	dvips -o beta_paper.ps beta_paper.dvi

beta_paper.dvi : beta_paper.tex beta_paper.bib fig1.eps fig2.eps fig3.eps fig4.eps
	latex beta_paper.tex
	bibtex beta_paper
	latex beta_paper.tex
	latex beta_paper.tex

beta_paper.pdf : beta_paper.ps
	ps2pdf $< $@


roc_5_5.txt :
	./cmp_power.sh

fig1.eps : plot_fig1.py G199.G202.beta.fisher.zscore
	python plot_fig1.py
	#convert fig1.ps fig1.eps

fig2.eps : roc_5_5.txt roc_10_10.txt roc_40_40.txt 
	python plot_fig2.py

fig3.eps: plot_fig3.py fisher_of_tp_10_10.txt fisher_of_tn_10_10.txt 
	python plot_fig3.py

fig4.eps:
	python plot_fig4.py

clean:
	rm -f beta_paper.ps beta_paper.dvi 
