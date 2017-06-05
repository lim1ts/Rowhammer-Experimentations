#!/bin/bash

set -eu

mkdir -p out

cflags="-Wall -Werror -O2 -static"
g++ $cflags privesc2.cc -o out/init

g++ $cflags -g -O0 privescNoRoot.cc -o testnoroot
