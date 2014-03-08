BDD Lexer
=========

A simple BDD Lexer for [pygments](http://pygments.org/)

### How to use it?

Install pygments, copy bdd.py to $PYGMENTS_HOME/pygments/lexers

Run:
```text
cd $PYGMENTS_HOME
make mapfiles
```

Test:
```text
./pygmentize -O full -f html -o /tmp/example.html $BDD_LEXER_HOME/bdd-test.story
```
