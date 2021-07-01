"""Console client."""
import os
import sys
import json
from optparse import OptionParser  # pylint: disable=deprecated-module
from PyPDF2 import PdfFileReader, PdfFileWriter

COPYRIGHTS = 'Copyrights by Vitaly Bogomolov 2021'
VERSION = '1.0'

OPTS = None
PARSER = OptionParser(
  usage='Usage: %prog toc.json\n\nvizit https://github.com/vb64/pdftoc for more info.',
  version="%prog version {}".format(VERSION)
)
FOLDER = '{f}'


class Bookmark:
    """One pdf bookmark."""

    def __init__(self, title, page_number, parent):
        """Creat new bookmark."""
        self.title = title
        self.page_number = page_number
        self.parent = parent
        self.obj = None

    def add(self, merger):
        """Add bookmark to pdf."""
        parent = None
        if self.parent:
            parent = self.parent.obj

        self.obj = merger.addBookmark(self.title, self.page_number, parent=parent)
        return self.obj


class Bookmarks:
    """Pdf bookmarks list."""

    items = []

    def add(self, title, page_number, parent):
        """Create and return new bookmark."""
        self.items.append(Bookmark(title, page_number, parent))
        return self.items[-1]

    def link(self, merger):
        """Make bookmarks in pdf."""
        for i in self.items:
            i.add(merger)


def make(merger, toc, default_folder, parent, bookmarks):
    """Join several pdf files to target."""
    for title, pdf, childs in toc:
        if pdf.startswith(FOLDER):
            pdf = os.path.join(
              default_folder,
              pdf.replace(FOLDER, '')
            )
        new_parent = bookmarks.add(title, merger.getNumPages(), parent)
        if pdf:
            print(pdf)
            merger.appendPagesFromReader(PdfFileReader(open(pdf, 'rb')))  # pylint: disable=consider-using-with

        if childs:
            make(merger, childs, default_folder, new_parent, bookmarks)

    return 0


def main(argv, _options):
    """Entry point."""
    print("Pdf merge tool. {}".format(COPYRIGHTS))
    if len(argv) < 1:
        PARSER.print_usage()
        return 1

    bookmarks = Bookmarks()
    data = json.loads(open(argv[0], encoding='utf-8').read())  # pylint: disable=consider-using-with
    merger = PdfFileWriter()
    make(merger, data["toc"], data["folder"], None, bookmarks)
    bookmarks.link(merger)

    os.makedirs(os.path.dirname(data["target"]), exist_ok=True)
    with open(data["target"], "wb") as output:
        merger.write(output)

    return 0


if __name__ == '__main__':  # pragma: no cover
    OPTS, ARGS = PARSER.parse_args()
    sys.exit(main(ARGS, OPTS))
