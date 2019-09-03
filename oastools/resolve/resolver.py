""" resolver

:Author: Bilal Shaikh < bilalshaikh42@gmail.com >
:Date: 2019-08-30
:Copyright: 2019, Bilal Shaikh
:License: MIT
"""
import copy
import oastools.parse as parse
import os

cache = {}


def main():
    pass

# TODO make this function decide if to resolve internal sections
#!BUG The option for reftype else send back whole file rather than part


def __get_object_from_path(spec, path):
    objs = path.split('/')
    obj = spec
    for path in objs:
        obj = obj[path]
    return obj


def resolve(path):
    rootpath = "./oastools/resolve/fixtures/spec/"
    refType = path.find("#")
    if (refType == -1):  # remote file
        path = os.path.join(rootpath, path)
        ref = parse.OpenApiParser(path).spec
        return ref
    elif(refType == 0):  # local refrence
        return path
    else:  # remote file with section specified
        print(path)
        path = path[0:refType]
        section = path[refType+1:]
        path = os.path.join(rootpath, path)
        print(path)
        fullRef = parse.OpenApiParser(path).spec
        ref = __get_object_from_path(fullRef, section)
        return ref


def traverse(spec, callback=resolve):
    if (isinstance(spec, dict)):
        for key in spec.keys():
            if key == "$ref":
                refSpec = callback(spec[key])
                spec = traverse(refSpec)
            else:
                spec[key] = traverse(spec[key])
        return spec
    if(isinstance(spec, list)):
        new_list = []
        for item in spec:
            new_list.append(traverse(item))
        return new_list
    else:
        return spec


class Resolver(object):
    def __init__(self, openapi_spec, path=None):
        self.spec = copy.deepcopy(openapi_spec)
        self.cache = {}
        self.path = path


if __name__ == "__main__":
    main()
