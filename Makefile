all: 11 22 33 44 55 66 clean

11:
	pdflatex lec1.tex
	pdflatex lec1.tex
	pdflatex lec1.tex

22:
	pdflatex lec2.tex
	pdflatex lec2.tex
	pdflatex lec2.tex

33:
	pdflatex lec3.tex
	pdflatex lec3.tex
	pdflatex lec3.tex

44:
	pdflatex lec4.tex
	pdflatex lec4.tex
	pdflatex lec4.tex

55:
	pdflatex lec5.tex
	pdflatex lec5.tex
	pdflatex lec5.tex

66:
	pdflatex lec6.tex
	pdflatex lec6.tex
	pdflatex lec6.tex

clean:
	-@$(RM) *.log *.aux
