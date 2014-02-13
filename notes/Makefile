SHELL=/bin/bash


clean:
	find . -name "*.aux" | xargs rm -f
	find . -name "*.log" | xargs rm -f
	find . -name "*.toc" | xargs rm -f

all:

pdf:
	echo $? | xargs -n 1 ./tex_to_pdf.sh
