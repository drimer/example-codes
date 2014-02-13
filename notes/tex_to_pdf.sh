#!/bin/bash


[[ $# == 0 ]] && exit 1

tex_file=$1
cur_dir=$(pwd)
cd $(dirname $tex_file)
pdflatex -shell-escape $(basename $tex_file)
cd $cur_dir
