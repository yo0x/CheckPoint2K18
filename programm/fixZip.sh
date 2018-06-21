#!/bin/bash

a=0
ext="z"
for file in /home/y6x/Documents/check/programm/archives2/*
do

  mv "$file" "/home/y6x/Documents/check/programm/archives2/stam.z$a"
  (( a++ ))
done
