# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, ignore_case=False):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self._items = iter(items)
        self._used_items = set()
        self._ignore_case = ignore_case

    def __next__(self):
        result = None

        while result is None:
            it = next(self._items)

            if isinstance(it, str) and self._ignore_case:
                key = it.lower()
            else:
                key = it

            if key in self._used_items:
                continue

            self._used_items.add(key)
            result = it

        return result

    def __iter__(self):
        return self
