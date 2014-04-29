# -*- coding:utf-8 -*-
import sys
import argparse
from zca_snippets.detector import InfoDetector
from zope.interface.interface import InterfaceClass

class ZCAListing(object):
    def __init__(self, io, detector):
        self.io = io
        self.detector = detector

    def dump_interfaces(self, module):
        for k, v in module.__dict__.items():
            if isinstance(v, InterfaceClass):
                module = self.detector.module_path(v)
                ifacename = self.detector.object_name(v)
                self.io.write("{}:{}\n".format(module, ifacename))

def main():
    parser = argparse.ArgumentParser(description="-")
    parser.add_argument("program")
    parser.add_argument("module")
    args = parser.parse_args(sys.argv)

    detector = InfoDetector()
    module = detector.maybe_dotted(args.module)
    listing = ZCAListing(sys.stdout, detector)
    listing.dump_interfaces(module)
