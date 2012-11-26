#!/usr/bin/env python3

class Cfg (dict) :

    def __getattr__ (self, name):
        return self.__getitem__(name)

    def __setattr__ (self, name, value):
        return self.__setitem__(name, value)

    def __str__ (self):
        return "Configuration:\n\t" + \
               "\n\t".join("{0} : {1}".format(k,v) for (k,v) in self.items())

