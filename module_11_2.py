from pprint import pprint  # Импортируем модуль pprint


def introspection_info(obj):
    info = {
        'type': type(obj).__name__,
        'attributes': [],
        'methods': [],
        'module': getattr(obj, '__module__', 'builtins'),  # Используем getattr с значением по умолчанию
        'other_properties': {}
    }

    # Получаем все атрибуты и методы объекта
    for attr_name in dir(obj):
        attr_value = getattr(obj, attr_name)
        if callable(attr_value):
            info['methods'].append(attr_name)
        else:
            info['attributes'].append(attr_name)

    # Дополнительные свойства в зависимости от типа объекта
    if hasattr(obj, '__doc__'):
        info['other_properties']['doc'] = obj.__doc__
    if hasattr(obj, '__dict__'):
        info['other_properties']['instance_attributes'] = obj.__dict__

    return info


# Пример использования с собственным классом
class Person:
    """Пример класса Person с атрибутами и методами."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


# Создаем объект класса Person
person = Person("Alice", 30)

# Получаем информацию об объекте
person_info = introspection_info(person)
pprint(person_info)  # Используем pprint для красивого вывода

# Пример с числом
number_info = introspection_info(42)
pprint(number_info)  # Используем pprint для красивого вывода
