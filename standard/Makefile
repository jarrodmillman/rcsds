git-intro:
	pandoc -o git-intro.Rmd git-intro.rst
	Rscript -e "library(knitr); knit2html('git-intro.Rmd')"

bash-tutorial:
	pandoc -o bash-advanced.Rmd bash-advanced.rst
	Rscript -e "library(knitr); knit2html('bash-advanced.Rmd')"

clean:
	-rm bash-advanced.html bash-advanced.md bash-advanced.Rmd 
	-rm git-intro.html git-intro.md git-intro.Rmd 
