#!/bin/bash

sed 's/[a-z]//g;s/\([0-9]\).*\([0-9]\)/\1\2/;s/^\([0-9]\)$/\1\1/' "${1:?}" | awk '{s+=$1} END {print s}'
