# from threading import Thread
#
#
# def work(n):
#     print("%s is working " % n)
#
#
# if __name__ == "__main__":
#     t = Thread(target=work, args=("a",))
#     t.start()
#     t.run()
#     print("主")
# import threading
# lock = threading.Lock()
# class Foo(object):
#     __instance = None
#
#     def __new__(cls,*args,**kwargs):
#         if not cls.__instance:
#             with lock:
#                 if not cls.__instance:
#                     obj = super(Foo,cls).__new__(cls,*args,**kwargs)
#                     cls.__instance = obj
#         return cls.__instance
# a = Foo()
# b = Foo()
# print(a,b)
# import threading
# lock = threading.Lock()
#
# class Singleton(type):
#
#     def __call__(cls, *args, **kwargs):
#         if not hasattr(cls,'__instance'):
#             with lock:
#                 if not hasattr(cls,'__instance'):
#                     obj = cls.__new__(cls,*args,**kwargs)
#                     obj.__init__(*args,**kwargs)
#                     setattr(cls,'__instance',obj)
#         return getattr(cls,'__instance')
#
# class Foo(object,metaclass=Singleton):
#     def __init__(self):
#         self.name = 'xxx'
#
# a = Foo('1')
# d = Foo('2')
# print(a.name,d.name)

import threading
lock = threading.Lock()

class Foo(object):
    __instance = None
    def __init__(self):
        pass

    @classmethod
    def get_instance(cls,*args,**kwargs):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    obj = cls(*args,**kwargs)
                    cls.__instance = obj
        return cls.__instance

a = Foo.get_instance()



