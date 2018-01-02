import binascii
import os

import six

if __name__ == '__main__':
    mapping = {}

    with open('crc.txt', 'wb') as f:
        for target in ["d:\\git\\dfis-portal-vue", "d:\\git\\dfis-portal", "d:\\git\\aframe", "d:\\git\\aframe-extras",
                       "d:\\git\\aframe-neg-rotate-component"]:
            for current, _, files in os.walk(target):
                # for current, _, files in os.walk("."):
                for x in files:
                    full_path = os.path.join(current, x)
                    crc32 = binascii.crc32(full_path) & 0xFFFFFFFF
                    mapping.setdefault(crc32, 0)
                    mapping[crc32] += 1
                    line = "{0} {1}".format(crc32, full_path)
                    f.write(line + '\n')
                    print(line)

    print("collision detection")
    for key, value in six.iteritems(mapping):
        if value >= 2:
            print("key {0}".format(key))
