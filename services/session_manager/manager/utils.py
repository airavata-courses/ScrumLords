# Some utility functions
def make_keys_to_dot(d):
    def expand(key, value):
        if isinstance(value, dict):
            return [(key + "." + k, v) for k, v in make_keys_to_dot(value).items()]
        else:
            return [(key, value)]

    items = [item for k, v in d.items() for item in expand(k, v)]
    return dict(items)


def is_generator_empty(generator):
    try:
        item = next(generator)

        def my_generator():
            yield item
            yield from generator

        return my_generator(), False
    except StopIteration:
        return (_ for _ in []), True
