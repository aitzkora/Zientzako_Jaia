#Purge implicites rules 
.SUFFIXES:
.SUFFIXES: .pdf .tex

# Tools 
TEX = pdflatex 
BIBMAKE = bibtex

init_python.pdf : init_python.tex 
	$(TEX) $<	

tp_cesar.pdf : tp_cesar.tex 
	$(TEX) $<	

# Clean the directory
clean::clean_pdf clean_aux

clean_pdf: 
	@echo Cleaning pdf File... 
	@rm -f init_python.pdf
	@rm -f tp_cesar.pdf
clean_aux:
	@echo Cleaning Auxiliary files... 
	@rm -f *.nav *.out *.toc *.bbl gdb.out  
	@rm -f *.aux *.toc  *.log  *.snm
