class ProcessId(object):
    Input, QSpace, Fit = range(3)


_registeredItems = {}


def getItemClass(itemName):
    return _registeredItems.get(itemName)


def registerItemClass(klass):
    global _registeredItems

    className = klass.XsocsClass
    if className in _registeredItems:
        raise AttributeError(
            "Failed to register item class {0}."
            "attribute is already registered."
            "".format(klass.__name__)
        )

    # TODO : some kind of checks on the klass
    _registeredItems[className] = klass


def ItemClassDef(XsocsClassName):
    def inner(cls):
        cls.XsocsClass = XsocsClassName
        registerItemClass(cls)
        return cls

    return inner
