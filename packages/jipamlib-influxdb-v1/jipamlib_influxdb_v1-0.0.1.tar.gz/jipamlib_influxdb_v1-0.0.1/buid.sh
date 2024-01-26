#!/bin/bash
rm -f dist/*
python3 -m build
python3 -m twine upload  dist/*
echo "NO OLVIDAR"
echo "git add . && git commit -am 'Comentarios' && git push"
echo ""
git add . && git commit -am 'Comentarios' && git push
