all: clean git-intro bash-tutorial

git-intro:
	pandoc -o git-intro.md git-intro.rst
	Rscript -e "library(knitr); knit2html('git-intro.md')"

# change wget 
# fix tables
# number sections
# remove section on looking at ``sudo`` man page
bash-tutorial:
	pandoc -N -o bash.md bash.rst
	Rscript -e "library(knitr); knit2html('bash.md')"

clean:
	-rm bash.html bash.md 
	-rm git-intro.html git-intro.md
