SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)\" $(SPHINXOPTS) $(O)

install:
	python -m ensurepip --upgrade
	python -m pip install -r requirements.txt

html: install
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)\" $(SPHINXOPTS) $(O)

.PHONY: help Makefile install html

%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)\" $(SPHINXOPTS) $(O)