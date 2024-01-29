import uos
import ubinascii
import uhashlib


def up_listfiles():
    def sha256(filename):
        JUNK = 256
        sha = uhashlib.sha256()
        with open(filename, "rb") as f:
            while True:
                data = f.read(JUNK)
                if len(data) == 0:
                    return ubinascii.hexlify(sha.digest())
                sha.update(data)

    def list_dir(path: str):
        "Recursive listdir"
        for filetuple in uos.ilistdir(path):
            filename = path + filetuple[0]
            filetype = filetuple[1]
            if filetype == 0x8000:
                # a file
                yield (filename, sha256(filename))
                continue
            if filetype == 0x4000:
                # a directory
                yield from list_dir(filename + "/")
                continue
            assert False, filename

    return list(list_dir(""))
