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
            class_name = dir(getattr(module_code, name.split('.')[-1]))[0]
            clazz = self.load_clazz(name + '.' + class_name)
            moduleClasses.append(clazz)

        return moduleClasses

    def load_clazz(self, name):
        components = name.split('.')
        mod = __import__(components[0])
        for comp in components[1:]:
            mod = getattr(mod, comp)
        return mod

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Connection(object):
    __metaclass__ = Singleton
    # TODO get proxy settings from environment
    proxyDict = {}

    def get(self, url):
        try:
            return requests.get(url,headers={},proxies=self.proxyDict)
        except:
            print('url error: ',url)
            return None
        

