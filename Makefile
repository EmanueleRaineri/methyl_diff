methyl_diff_static: methyl_diff.c
	gcc -Wall -static -O3 -o methyl_diff $< -lm

methyl_diff: methyl_diff.c
	gcc -Wall  -O3 -o methyl_diff $< -lm

beta_diff : beta_diff.ml
	ocamlopt.opt -ccopt -static str.cmxa beta_diff.ml -o beta_diff

beta_paper.ps : beta_paper.dvi
	dvips -o beta_paper.ps beta_paper.dvi

beta_paper.dvi : beta_paper.tex beta_paper.bib fig1.eps fig2.eps fig3.eps fig4.eps
	latex beta_paper.tex
	bibtex beta_paper
	latex beta_paper.tex
	latex beta_paper.tex

beta_paper.pdf : beta_paper.ps
	ps2pdf $< $@

data/G199.G202.beta.fisher.zscore:
	awk '{print $$2}' G199.G202.zscore | paste G199.G202 G199.G202.beta_diff G199.G202.fisher - > $@ 

data/roc_5_5.txt : cmp_power.sh methyl_diff
	./cmp_power.sh 5 5

data/roc_10_10.txt : cmp_power.sh methyl_diff
	./cmp_power.sh 10 10

data/roc_40_40.txt : cmp_power.sh methyl_diff
	./cmp_power.sh 40 40 

fig1.eps : plot_fig1.py data/G199.G202.beta.fisher.zscore
	python plot_fig1.py

fig2.eps : plot_fig2.py data/roc_5_5.txt data/roc_10_10.txt data/roc_40_40.txt 
	python plot_fig2.py

fig3.eps: plot_fig3.py data/fisher_of_p_10_10.txt data/fisher_of_n_10_10.txt 
	python plot_fig3.py

fig4.eps: plot_fig4.py
	python plot_fig4.py

clean:
	rm -f beta_paper.ps beta_paper.pdf beta_paper.dvi data/* beta_paper.aux beta_paper.bbl beta_paper.blg beta_paper.log 
