# -:- coding:utf8 -:-
from collections import OrderedDict
from functools import partial


def entity_update(src, dst, properties=None):
    """
    
    :param dict src: 
    :param dict dst: 
    :param list[str] properties: 
    :return: 
    """
    if properties is None:
        dst.update(src)
    elif properties:
        for prop in properties:
            if prop in src:
                dst[prop] = src[prop]
    return dst


def reside_project(items):
    result = []
    l_queue, r_queue = [], []
    l_update = partial(entity_update, properties=["cur_name"])
    r_update = partial(entity_update, properties=["prev_name"])
    for item in items:
        if item['prev_name'] and item['cur_name']:
            result.append(item)
        elif item['prev_name']:
            if r_queue:
                result.append(l_update(r_queue.pop(0), item))
            else:
                l_queue.append(item)
        elif item['cur_name']:
            if l_queue:
                result.append(r_update(l_queue.pop(0), item))
            else:
                l_queue.append(item)
    result.extend(l_queue)
    result.extend(r_queue)
    return result


def main():
    projects = OrderedDict()
    projects[0] = dict(prev_name="project1", cur_name="project1", parent_id=1)
    projects[1] = dict(prev_name="project2", cur_name="project2", parent_id=1)
    projects[3] = dict(prev_name="project3", cur_name=None, parent_id=1)
    projects[4] = dict(prev_name=None, cur_name="project4", parent_id=1)
    projects[5] = dict(prev_name=None, cur_name="project5", parent_id=1)
    projects[6] = dict(prev_name='project6', cur_name="project6", parent_id=2)
    projects[7] = dict(prev_name='project7', cur_name=None, parent_id=2)
    projects[8] = dict(prev_name=None, cur_name="project8", parent_id=3)
    projects[9] = dict(prev_name=None, cur_name="project8", parent_id=4)

    for item in projects.values():
        print(item)

    print
    for item in reside_project(projects.values()):
        print(item)


def project_sort():
    im = OrderedDict()
    im[u'中'] = '11'
    im[u'中2'] = '00'
    im[u'中4'] = '22'
    im[u'中2'] = '00011'
    im[u'中'] = '11222'

    for key in im:
        print im[key]


if __name__ == '__main__':
    main()
    project_sort()

    x = {'id': 12, 'name': 'benjamin'}
    y = {'id': 13, 'prev_name': 'wendy'}
    x.update(y)
    print x, y
    x = u'中国/中国2'
    segments = x.split('/')
    print(type(segments[0]))
    print x.startswith(u'中国/')
