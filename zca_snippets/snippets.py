# -*- coding:utf-8 -*-
import itertools as it
import sys
import argparse
from zca_snippets.detector import InfoDetector, positional
import json #xxx:

class ZCASnippets(object):
    def __init__(self, io, detector, verbose=True, base_depends=True):
        self.io = io
        self.detector = detector
        self.verbose = verbose
        self.base_depends = base_depends

    def out(self, s):
        self.io.write(s)
        self.io.write("\n")

    def dump_snippets(self, iface, clsname):
        module = self.detector.module_path(iface)
        ifacename = self.detector.object_name(iface)
        if self.verbose:
            if self.base_depends:
                self.out("from zope.interface import implementer")
            self.out("from {module} import {name}".format(
                module=module,
                name=ifacename))
            self.out("")


        self.out("## see: {module}:{name}".format(module=module, name=ifacename))
        self.out("@implementer({name})".format(name=self.detector.object_name(iface)))
        self.out("class {clsname}(object):".format(clsname=self.detector.implements_name(iface, clsname)))
        for attr in self.detector.parse_attributes(iface):
            self.out("""\
    @property
    def {attr[name]}(self):
        pass
""".format(attr=attr))
        for method in self.detector.parse_methods(iface):
            required = (k for k,v in method["positional"] if v is positional)
            optionals = ("=".join((k, json.dumps(v))) for k, v in method["positional"] if not v is positional)
            args = ", ".join(it.chain(required, optionals))
            self.out("""\
    def {method[name]}(self, {args}{varargs}{kwargs}):
        pass
""".format(method=method, 
                       args=args, 
                       varargs="" if method["args"] is None else ", *{}".format(method["args"]), 
                       kwargs="" if method["kwargs"] is None else ", **{}".format(method["kwargs"])
                   ))



def main():
    parser = argparse.ArgumentParser(description="-")
    parser.add_argument("--quiet", "-q", action="store_true")
    parser.add_argument("--base", "-b", action="store_true")
    parser.add_argument("program")
    parser.add_argument("iface")
    parser.add_argument("name", nargs="?")
    parser.set_defaults(quiet=False, base=False)
    args = parser.parse_args(sys.argv)
    verbose = not args.quiet

    detector = InfoDetector()
    iface = detector.maybe_dotted(args.iface)
    snippets = ZCASnippets(sys.stdout, detector, verbose=verbose, base_depends=args.base)
    snippets.dump_snippets(iface, args.name)
