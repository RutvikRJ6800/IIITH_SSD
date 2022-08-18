#! bin/bash

# file path taken from argument
filePath=$1

noOfLines="$(wc -l < $filePath)"


if (( noOfLines % 2 == 0 ))
then
    lineToBePrint=$(($noOfLines/2))
else
    lineToBePrint=$(($noOfLines/2 + 1))    
fi


awk '{ if (NR==$lineToBePrint) print }' $filePath 
cat $filePath | awk NR==$lineToBePrint
