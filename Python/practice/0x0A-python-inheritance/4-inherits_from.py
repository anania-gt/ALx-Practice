def inherits_from(obj, a_class):
    return isinstance(obj,a_class) and a_class is not type(obj)

class BaseClass:
    pass

class SubClass(BaseClass):
    pass

class AnotherSubClass(SubClass):
    pass

base_instance = BaseClass()
sub_instance = SubClass()
another_sub_instance = AnotherSubClass()
print(inherits_from(sub_instance, BaseClass))           # Output: True
print(inherits_from(another_sub_instance, BaseClass))   # Output: True
print(inherits_from(base_instance, BaseClass))          # Output: False
print(inherits_from(sub_instance, SubClass))            # Output: False
print(inherits_from(another_sub_instance, SubClass))    # Output: True
print(inherits_from(base_instance, SubClass))           # Output: False
print(inherits_from(another_sub_instance, AnotherSubClass)) # Output: False