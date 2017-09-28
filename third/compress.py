import tarfile
import zipfile


def unzip(filename):
    with open(filename, 'rb') as f:
        with tarfile.open(fileobj=f, mode='r:*') as r:
            for i in r:
                content = r.extractfile(i)
                print (content)


def unzip2(filename):
    with open(filename, 'rb') as f:
        with zipfile.ZipFile(f, mode='r') as r:
            for i in r.infolist():
                print (i.filename)
                if i.compress_type == 0:
                    continue
                content = r.read(i)
                print (content)


if __name__ == '__main__':
    unzip('compress.tar.gz')
    unzip('d:\\tmp\\tmp.tar')
    unzip2('d:\\tmp\\tmp.zip')
