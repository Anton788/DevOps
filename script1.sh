#!/usr/bin/env bash

git init
git remote add origin $1
git pull origin main
git checkout -b $2
git pull origin $2
git checkout main
git checkout -b $3
git pull origin $3
git checkout main
git diff --name-only $2 $3 -- > out.txt
