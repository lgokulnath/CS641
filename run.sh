#!/bin/bash
python script.py | ssh student@172.27.26.188 -t 2>/dev/null | grep '[[:alpha:]]\{16\}' | tr -d '\t'  > out.txt