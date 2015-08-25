all: clean git-intro bash-tutorial

git-intro:
	pandoc -o git-intro.Rmd git-intro.rst
	Rscript -e "library(knitr); knit2html('git-intro.Rmd')"

bash-tutorial:
	sed -e '/^\*\ :ref/d' bash-advanced.rst > bash-advanced-clean.rst
	pandoc -o bash-advanced.Rmd bash-advanced-clean.rst
	rm bash-advanced-clean.rst
	Rscript -e "library(knitr); knit2html('bash-advanced.Rmd')"

clean:
	-rm bash-advanced.html bash-advanced.md bash-advanced.Rmd 
	-rm git-intro.html git-intro.md git-intro.Rmd 
