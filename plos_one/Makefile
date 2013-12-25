cover_letter.pdf: cover_letter.tex
	latex cover_letter.tex
	dvipdf cover_letter.dvi $@

beta_paper_plos.tex: ../beta_paper.tex
	python fill_plos_template.py > $@

beta_paper_plos.pdf: beta_paper_plos.ps
	ps2pdf $^

fig1.eps fig2.eps fig3.eps fig4.eps:
	cp ../fig1.eps ../fig2.eps ../fig3.eps ../fig4.eps .

beta_paper_plos.ps: beta_paper_plos.dvi fig1.eps fig2.eps fig3.eps fig4.eps
	dvips -o $@ $<

beta_paper_plos.dvi : beta_paper_plos.tex ../beta_paper.bib
	latex beta_paper_plos.tex
	bibtex beta_paper_plos
	latex beta_paper_plos.tex
	latex beta_paper_plos.tex

clean:
	rm -f beta_paper_plos.dvi beta_paper_plos.tex beta_paper_plos.ps beta_paper_plos.pdf
