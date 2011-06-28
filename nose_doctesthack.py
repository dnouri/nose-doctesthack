import pdb
import sys
from doctest import DocTestCase

from nose.plugins.base import Plugin

class Pdb(Plugin):
    enabled = False

    def options(self, parser, env):
        """Register commandline options.
        """
        parser.add_option(
            "-D", "--doctesthack", action="store_true", dest="enable",
            default=env.get('NOSE_PDB_DOCTESTHACK', False),
            help="An alternative to --pdb-failures that works better with doctests")

    def configure(self, options, conf):
        self.enabled = options.enable

    def addError(self, test, err, capt):
        if self.enabled:
            self.debug(test, err)

    def addFailure(self, test, err, capt, tbinfo):
        if self.enabled:
            self.debug(test, err)

    def debug(self, test, err):
        if isinstance(test, DocTestCase):
            try:
                test.debug()
            except Exception as exc:
                err = exc.exc_info
        ec, ev, tb = err
        stdout = sys.stdout
        sys.stdout = sys.__stdout__
        try:
            pdb.post_mortem(tb)
        finally:
            sys.stdout = stdout
