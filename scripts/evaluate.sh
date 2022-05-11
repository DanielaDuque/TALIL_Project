#!/bin/sh

# Generates useful files from just a CRF template

echo "Generating files from template_$1:"

echo "Data Scrip $2:"

mkdir decoupage$2

echo "Training using wapiti and atis.train set..."
wapiti train -p template_$1.txt -t 4 ../../data/decoupage$2.train decoupage$2/atis$2_$1.crfmodel

echo "Generating readable file..."
wapiti dump decoupage$2/atis$2_$1.crfmodel decoupage$2/model$2_$1.txt

echo "Tagging the model using the CRF tagger..."
wapiti label -m decoupage$2/atis$2_$1.crfmodel ../../data/decoupage$2.test > decoupage$2/predictions$2_$1

echo "Saving results in a readable file..."
result=$(cat decoupage$2/predictions$2_$1 | ../../scripts/evaluation.pl)
echo "$result" > decoupage$2/result$2_$1.txt

echo "Finist template $2."



