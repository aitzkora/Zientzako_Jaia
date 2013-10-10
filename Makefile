#Purge implicites rules 
.SUFFIXES:
.SUFFIXES: .pdf .tex

# Tools 
TEX = pdflatex 
BIBMAKE = bibtex

all :: init_python.pdf tp.pdf

init_python.pdf : init_python.tex 
	$(TEX) $<	

tp.pdf : tp.tex 
	$(TEX) $<	

# Clean the directory
clean::clean_pdf clean_aux

clean_pdf: 
	@echo Cleaning pdf File... 
	@rm -f init_python.pdf 
	@rm -f tp.pdf
clean_aux:
	@echo Cleaning Auxiliary files... 
	@rm -f *.nav *.out *.toc *.bbl gdb.out  
	@rm -f *.aux *.toc  *.log  *.snm
	@rm -fr __pycache__ *.pyc 
