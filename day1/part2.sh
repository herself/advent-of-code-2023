#!/bin/bash

echo 0 > sum
cat "${1:?}" | \
while read line; do
  nums=$(echo "$line" | sed 's/one/o1e/g;s/two/t2o/g;s/three/t3e/g;s/four/f4r/g;s/five/f5e/g;s/six/s6x/g;s/seven/s7n/g;s/eight/e8t/g;s/nine/n9e/g')
  short=$(echo "$nums" | sed 's/[a-z]//g;s/\([0-9]\).*\([0-9]\)/\1\2/;s/^\([0-9]\)$/\1\1/')
  echo "> $line -> $nums -> $short" #| rg [A-Z]
  sum=$(cat sum)
  echo "$sum + $short" | bc > sum
done
cat sum
