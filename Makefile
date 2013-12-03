methly_diff: methyl_diff.c
	gcc -Wall -static -O3 -o methyl_diff $< -lm

beta_paper.ps : beta_paper.dvi
	dvips -o beta_paper.ps beta_paper.dvi

beta_paper.dvi : beta_paper.tex beta_paper.bib fig1.eps fig2.eps fig3.eps
	latex beta_paper.tex
	bibtex beta_paper
	latex beta_paper.tex
	latex beta_paper.tex
	dvips -o beta_paper.ps beta_paper.dvi

fig1.eps : plot_fig1.py
	python plot_fig1.py

fig2.eps : plot_fig2.py
	python plot_fig2.eps


fig3.eps: plot_fig3.py
	python plot_fig3.py
