# -:- coding:utf8 -:-
import os
import shutil


def main():
    name = "power"
    target_path = "d:\\tmp\\{0}".format(name)
    old_path = "d:\\tmp\\{0}_old".format(name)
    diff_path = "d:\\tmp\\{0}_diff".format(name)

    os.mkdir(diff_path)
    knapsack = set(os.listdir(target_path))
    for filename in os.listdir(old_path):
        if filename not in knapsack:
            shutil.move(os.path.join(old_path, filename), os.path.join(diff_path, filename))


if __name__ == '__main__':
    main()
