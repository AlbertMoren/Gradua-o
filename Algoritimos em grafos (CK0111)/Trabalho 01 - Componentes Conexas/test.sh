#!/bin/bash

for i in {0..118}
do
    cat instancias/$i.in | ./programa.py > minhaSaida/saida_$i.txt
    diff -s minhaSaida/saida_$i.txt solucoes/$i.out
done

