#!/bin/bash

while read p; do

  find /home/y6x/Documents/check/programm/archives/ -name "*.$p" -type f -delete

done < finalNumRAR.txt
