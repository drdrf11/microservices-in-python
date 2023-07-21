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
- created devops.yml file (go to Actions menu on github repo, follow "setup a workflow for yourself", add his content)
  (beware of version "numbers" -- use quotes '3.10' != 3.10 == 3.1)
- fleshed out make "lint" clause (pylint --disable=R,C *.py mylib/*.py) [I have already also fleshed out the format and test clauses]
  and tested it
- uncommented the "make lint" clause in devops.yml
- committed changes (git: add .github/, add *, commit, pull, push) - devops is automatically run (but commit? pull? push?)
- added 'build' (#build container) step to Makefile, started to create test file (test_logic.py)
- mod 'test' make step to ref a test file, and to check coverage
- add 'cli-fire.py' to generate doc file for wiki()

1. Create a Python Virtual Environment 'python3 -m venv ~/.venv' or 'virtualenv ~/.venv'
2. Create empty files: Makefile, requirements.txt, main.py, Dockerfile, mylib/, mylib/__init__.py, mylib/logic.py
3. Populate 'Makefile'
4. Set up Continuous Integration - check code for issues like lint errors
