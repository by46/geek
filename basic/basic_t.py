import pprint

import py

u = py.builtin._totext


def _compare_eq_dict(left, right):
    explanation = []
    common = set(left).intersection(set(right))
    # same = dict((k, left[k]) for k in common if left[k] == right[k])
    # if same and not verbose:
    #     explanation += [u('Omitting %s identical items, use -v to show') %
    #                     len(same)]
    # elif same:
    #     explanation += [u('Common items:')]
    #     explanation += pprint.pformat(same).splitlines()
    diff = set(k for k in common if left[k] != right[k])
    if diff:
        explanation += [u('Differing items:')]
        for k in diff:
            explanation += [py.io.saferepr({k: left[k]}) + ' != ' +
                            py.io.saferepr({k: right[k]})]
    extra_left = set(left) - set(right)
    if extra_left:
        explanation.append(u('Left contains more items:'))
        explanation.extend(pprint.pformat(
            dict((k, left[k]) for k in extra_left)).splitlines())
    extra_right = set(right) - set(left)
    if extra_right:
        explanation.append(u('Right contains more items:'))
        explanation.extend(pprint.pformat(
            dict((k, right[k]) for k in extra_right)).splitlines())
    return explanation


def compare():
    x = {"name": "benjamin", "address": ["address1"], "x": "benjamin", "x1": "benjamin",
         "x3": "benjamin"}
    y = {"name": "benjamin1", "address": ["address2"], "x": "benjamin", "x1": "benjamin", "x2": "benjamin",
         "x3": "benjamin"}
    # assert x == y
    print(_compare_eq_dict(x, y))

if __name__ == '__main__':
    compare()