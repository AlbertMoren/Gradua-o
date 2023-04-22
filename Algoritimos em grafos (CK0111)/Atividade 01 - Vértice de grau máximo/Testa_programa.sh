#!/bin/bash

for i in {0..118}
do
    cat instancias/$i.in | ./programa.py > minhaSaida/saida.txt
    cat minhaSaida/saida.txt
done

