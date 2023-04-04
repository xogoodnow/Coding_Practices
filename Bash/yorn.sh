#!/bin/bash
read l
if [[ $l = "y" || $l = "Y" ]]; then
    echo "YES"
elif [[ $l = "n" || $l = "N" ]]; then
    echo "NO"
else
    echo "mimosa"
fi
