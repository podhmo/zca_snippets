# -*- coding:utf-8 -*-
import pkg_resources
from zope.interface.interface import Method

def import_symbol(symbol): #todo cache
    return pkg_resources.EntryPoint.parse("x=%s" % symbol).load(False)

class _positional(object):
    def __repr__(self):
        return "<_P>"
positional = _positional()

class InfoDetector(object):
    def maybe_dotted(self, s):
        return import_symbol(s)

    def module_path(self, obj):
        return obj.__module__

    def object_name(self, obj):
        return obj.__name__ 

    def implements_name(self, iface, name):
        if name:
            return name
        else:
            if iface.__name__.startswith("I"):
                return iface.__name__[1:]
            raise Exception("NoName")

    def parse_methods(self, iface):
        for name, desc in iface.namesAndDescriptions(True):
            if isinstance(desc, Method):
                args = [(k, desc._optional.get(k, positional)) for k in desc.positional]
                yield({"name": name, "positional":args, "args": desc.varargs, "kwargs": desc.kwargs, "doc":desc.__doc__})

    def parse_attributes(self, iface):
        for name, desc in iface.namesAndDescriptions(True):
            if not isinstance(desc, Method):
                yield({"name": name, "doc": desc.__doc__})

