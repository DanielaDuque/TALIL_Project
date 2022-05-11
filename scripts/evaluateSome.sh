#!/bin/sh

echo "Making the scripts."
../../scripts/evaluate.sh $1 1
../../scripts/evaluate.sh $1 2
../../scripts/evaluate.sh $1 3

echo "All done."
