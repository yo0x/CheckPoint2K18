#!/bin/bash

for file in /home/y6x/Documents/check/programm/archives/*
do
   #echo $file
   #zipnote $file |grep "^[^@]" >> 1final.txt
   ./rar v $file >> lfinalrar.txt
done
