#!/bin/bash

screenfetch -N -n > ~/.dominae/txt/screenfetch.txt
sed -i -e 's/^/**/' ~/.dominae/txt/screenfetch.txt
sed -i -e 's/:/**:/' ~/.dominae/txt/screenfetch.txt
sed -i -e 's/@/**@/g' ~/.dominae/txt/screenfetch.txt
sed -i -e 's/**@ /@ /g' ~/.dominae/txt/screenfetch.txt
#sed -i -e 's/**@**/@/g' ~/.dominae/txt/screenfetch.txt
