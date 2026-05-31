import copy
import threading

class StrictSingleton:
    __instance = {} # For name mangling
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            with cls._lock:
                if cls not in cls.__instance:
                    cls.__instance[cls] = super().__new__(cls)
        return cls.__instance[cls]

    def __copy__(self):
        raise TypeError("Cloning a singleton instance is forbidden.")

    def __deepcopy__(self, memo):
        raise TypeError("Cloning a singleton instance is forbidden.")

    def __reduce__(self):
        raise TypeError("Pickling a singleton instance is forbidden.")

    def __reduce_ex__(self, protocol):
        raise TypeError("Pickling a singleton instance is forbidden.")

    def __getnewargs__(self):
        raise TypeError("Cannot create new singleton instance.")

    def __getnewargs_ex__(self):
        raise TypeError("Cannot create new singleton instance.")
      
