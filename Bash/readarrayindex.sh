#!/bin/bash

while read line; do
    arr=("${arr[@]}" "$line")
done

# Print the third array
echo "${arr[3]}"
