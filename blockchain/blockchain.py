import hashlib
import os
import sys
import uuid
import shutil
from itertools import cycle


def blockchain():
    chainfile_f = "test.chain"
    if os.path.isfile(chainfile_f):
        os.remove(chainfile_f)
    chainfile = open(chainfile_f, "a")
    testdir = "test_data"
    stop = 0
    hash1 = "6666"
    chainnum = -1
    previous = "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e"
    files = os.listdir(testdir)
    for file1 in files:
        hash1 = ""
        multiplier = -1
        file1 = testdir + "/" + file1
        myfile = open(file1, "r")
        string = myfile.read()
        while str(hash1)[0:4] != "0000":
            multiplier = multiplier + 1
            data = str(chainnum) + str(multiplier) + string + previous
            hash1 = hashlib.sha512(data.encode('utf-8')).hexdigest()
        previous = hash1
        chainnum = chainnum + 1
        chainfile.write(str(chainnum) + ";" + hash1 + "\n")
        myfile.close
    chainfile.close


def create_test_data(num):
    directory = "test_data"
    shutil.rmtree(directory)
    os.makedirs(directory)
    for n in range(1, num + 1):
        file = open(directory + "/" + str(n), "w+")
        file.write(str(uuid.uuid4()) + "\n" + str(uuid.uuid4()) + "\n")
        file.close


def test_chain():
    chainfile_f = "test.chain"
    if not os.path.isfile(chainfile_f):
        print("No chain file.\nGenerate it first")
        sys.exit(1)
    testdir = "test_data"
    chainfile = open(chainfile_f, "r")
    files = os.listdir(testdir)
    f_count = 0
    chainnum = -1
    previous = "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e"
    for line in chainfile:
        hash1 = "6666"
        multiplier = -1
        f_count += 1
        file1 = testdir + "/" + files[f_count]
        myfile = open(file1, "r")
        string = myfile.read()
        while str(hash1)[0:4] != "0000":
            multiplier = multiplier + 1
            data = str(chainnum) + str(multiplier) + string + previous
            hash1 = hashlib.sha512(data.encode('utf-8')).hexdigest()
        previous = hash1
        chainnum = chainnum + 1
        line1 = str(chainnum) + ";" + hash1 + "\n"
        if line != line1:
            return "Broken on file \"" + files[f_count - 1] + "\""
        myfile.close
    return "All is fine"


def main():
    try:
        int(sys.argv[1])
    except:
        print(
            "Hey YOU!!!!!: test_file_num must be a number!!!!\nuse this: python3 blockchain.py test_file_num [new]\n[new] needed for new test data creation")
        sys.exit(1)
    num = int(sys.argv[1])
    if sys.argv[2] == "new":
        create_test_data(num)
    blockchain()
    print(test_chain())


if __name__ == "__main__":
    main()
