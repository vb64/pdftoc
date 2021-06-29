# PdfTOC utility

Merging several pdf files and generate hierarchy TOC for the resulting pdf. TOC and set of source pdf files are defining in JSON file.

Usage:
```bash
pdftoc toc.json
```

For example, to produce resulting `Merged report.pdf` file from `fixtures/example.pdf` with hierarchical TOC:

![Merged report.pdf](fixtures/example.jpg)

Use the following `toc.json` file:

```json
{
  "target": "Merged report.pdf",
  "folder": "fixtures",
  "toc": [
    ["Level 0", "", [
      ["Level 1", "{f}example.pdf", []],
      ["Level 1", "{f}example.pdf", [
        ["Level 2", "{f}example.pdf", []],
        ["Level 2", "{f}example.pdf", []]
      ]],
      ["Level 1", "{f}example.pdf", []]
    ]],
    ["Level 0", "{f}example.pdf", []]
  ]
}
```

Sequence "{f}" is optional placeholder. It will be replaced with the value of "folder" key ('fixtures' in the given example).

You can download the ready [win64 binary executable](https://github.com/vb64/pdftoc/releases/download/v.1.0/pdftoc.exe) or create your version from sources.

Download and install:

- [Python 3](https://www.python.org/downloads/release/python-3810/)
- GNU [Unix Utils](http://unxutils.sourceforge.net/) for makefile operation

Then

```bash
git clone git@github.com:vb64/pdftoc.git
cd pdftoc
make setup PYTHON_BIN=/path/to/python3/executable
make tests
make exe
```

`pdftoc.exe` will be created in `dist` subfolder.
