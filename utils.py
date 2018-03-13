from pkgutil import walk_packages
import requests, modules, inspect


class ModuleLoader(object):

    def load(self, root_import_path, is_valid=lambda entity: not entity.startswith('_')):
        """Returns modules in ``root_import_path`` that satisfy the ``is_valid`` test

        :param root_import_path: An string name for importing (i.e. "myapp").
        :param is_valid: A callable that takes a variable and returns ``True``
                        if it is of interest to us."""

        moduleClasses = []

        for _, name, is_pkg in walk_packages(modules.__path__, modules.__name__ + '.'):
            if is_pkg: 
                continue
            module_code = __import__(name)
            for name, obj in inspect.getmembers(module_code):
                if inspect.isclass(obj):
                    print(name, obj)
                    moduleClasses.append(obj)
                    #for thing in contents:
                    #    if is_valid(thing):
                    #        moduleClasses.append((name, obj))

        return moduleClasses

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Connection(object):
    __metaclass__ = Singleton
    # TODO get proxy settings from environment
    proxyDict = {'http':'http://lupo:Mattone_Febbraio@proxy.eng.it:3128'
             ,'https':'http://lupo:Mattone_Febbraio@proxy.eng.it:3128'}
    def get(self, url):
        return requests.get(url,headers={},proxies=self.proxyDict)

