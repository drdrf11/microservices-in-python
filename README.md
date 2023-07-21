# microservices-in-python
Microservices in Python

- edit readme, $git pull, $set up virtual env -- #1
- add to .bashrc via $vim, run $source .bashrc, finds python version ($python --version)
- created files and folder in working directory -- #2 -- $touch <name> or $mkdir <name>
- created roughed-in Makefile contents in codespace editor (every actual command still commented-out)
- tested make ($make install, $make format, $make all)
- actually added files to repository:
  - showed $git status, used $git add *, $git commit -m 'adding initial devops structure', $git push
- filled in requirements.txt with package names (wikipedia, pytest, ...)
- fleshed out Makefile install clause (pip install --upgrade pip && pip install -r requirements.txt),
  tested same, ran $pip freeze | less, added version numbers to required packages requirements, tested
- $git add *, commit, push again
- created devops.yml file

1. Create a Python Virtual Environment 'python3 -m venv ~/.venv' or 'virtualenv ~/.venv'
2. Create empty files: Makefile, requirements.txt, main.py, Dockerfile, mylib/, mylib/__init__.py, mylib/logic.py, main.py
