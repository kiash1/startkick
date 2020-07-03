#!/bin/bash

for filename in ./*/*/*/*/*/*/*/*/*.py; do
    [ -e "$filename" ] || continue
    echo "$filename"
    2to3-3.7 -w "$filename"
    git add .
    git commit -m "convert $filename from python2 to 3.7"
    # ... rest of the loop body
done