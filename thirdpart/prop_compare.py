import re


class PropertyPump(object):

    def __init__(self, src, paths):
        """
        
        :param dict src: 
        :param list[str] paths: 
        """
        self.__target = src
        self.__paths = paths

    RE_ARRAY_PROPERTY = re.compile('^\[\d+\]$')

    def build(self, target,  property_path, value):
        properties = property_path.split('.')
        while len(properties) > 1:
            name = properties.pop(0)
            is_array = False
            if name.endswith('[]'):
                name = name[:-2]
                is_array = True

            if name not in target:
                if is_array:
                    target[name] = []
                    target = target[name][0]
                else:
                    target[name] = {}
                    target = target[name]
            else:
                if is_array:
                    tmp = find(target[name], functools.partial(self.locate_object, params=params))

                    if tmp is None:
                        target[name].append({Rule.ID_KEY: self.get_ident(params)})
                        target = target[name][-1]
                    else:
                        target = tmp

                else:
                    target = target[name]

        prop = properties.pop()
        try:
            target[prop] = self.property_type(value)
            if self.precision:
                target[prop] = round(target[prop], self.precision)
        except ValueError:
            if self.default_value is not missing:
                target[prop] = self.default_value
            else:
                target[prop] = self.property_type()

    def _pretty_json_path(self, path):
        """
        pretty address.[0].path to address[0].path
        :param str path: 
        :return: 
        """
        segments = path.split('.')

        def builder(prev, cur):
            if re.match(cur):
                return "{0}[]".format(prev)
            return "{0}.{1}".format(prev, cur)

        segments = reduce(builder, segments)
        return segments

    def purge(self):
        pass

def compare_and_swap(src, dst, knapsack=None):
    """
    
    :param dict src: 
    :param dict dst: 
    :param set knapsack: 
    :return: dict
    """
    knapsack = knapsack or set()
    if set(src.keys()) <= set(dst.keys()):
        for key in src:
            item = dst[key]
            if isinstance(item, dict):
                src_item = src[key]
                object_id = id(src_item)
                if object_id in knapsack:
                    raise RuntimeError('recursive loop')
                knapsack.add(object_id)
                compare_and_swap(src_item, item, knapsack=knapsack)
            else:
                src[key] = item
    return src


def purge(dst, path):
    empty = dict()
    from jsonpath_rw import parse
    parser = parse(path)
    result = parser.find(dst)
    if not result:
        return None

    value = result[0].value
    print result[0].full_path
    segments = path.split('.')
    tmp = prev = result = {}
    while segments:
        empty = {}
        key = segments.pop(0)
        if key.startswith('['):
            key, value = prev.popitem()
            prev[key] = [empty]
        else:
            pass
        # prev = tmp
        if key.startswith('['):
            tmp[key] = [empty]
        else:
            tmp[key] = empty

        tmp = empty

    prev[key] = value
    return result


if __name__ == '__main__':
    b, a = {'name': 'wendy', 'sex': 'male', 'address': {'zip': '112'}}, {'name': 'benjamin', 'address': {'zip': '231'}}
    print (compare_and_swap(a, b))

    x = {'name': 'wendy', 'person': {}}
    x['person'].update(x)
    y = {'person': {}}
    y['person'].update(y)
    print(x, y)
    # print (compare_and_swap(y, x))

    segments = 'address.[0].zip'.split('.')


    def merge(x1, y1):
        if y1:
            print x1, y1
        return [x1, y1]


    tmp = reduce(merge, segments)

    from jsonpath_rw import parse

    parser = parse('address.zip')
    j = {'address': [{'zip': '123'}], 'name': 'benjamin'}
    print purge(j, 'address.[0].zip')
