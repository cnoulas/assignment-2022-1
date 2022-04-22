import math
import hashlib
import sys


with open(sys.argv[1]) as uncompressed_file:
    nums = []
    for line in uncompressed_file:
        nums += [int(x) for x in line.split()]
    n = len(nums)
    max = nums[n-1]
    l = math.floor(math.log2(max/n))
    L = bytearray()
    U = bytearray()
    u = math.ceil(math.log2(max))-l

    for i in range(0, n):
        if nums[i] == 0:
            for v in range(0, l):
                L.extend(int(bin(0), 2).to_bytes(1, byteorder='big'))
        else:
            helpMe = math.floor(math.log(nums[i], 2)) + 1
            if helpMe < l:
                for h in range(helpMe, 0, -1):
                    a = bin(nums[i])[-h]
                    L.extend(int(a, 2).to_bytes(1, byteorder='big'))
            else:
                for j in range(l, 0, -1):
                    a = bin(nums[i])[-j]
                    L.extend(int(a, 2).to_bytes(1, byteorder='big'))

    b = bin(0)
    while (len(L) % 8) != 0:
        L.extend(int(b, 2).to_bytes(1, byteorder='big'))

    print('l ', l)
    print('L')
    counter = 0
    for i in range(0, len(L)):
        if counter < 7:
            print(L[i], end='')
            counter += 1
        else:
            print(L[i])
            counter = 0

    print('U')
    for i in range(0, n):
        helpMe2 = nums[i] >> l
        if i == 0:
            diff = helpMe2
        else:
            diff = (nums[i] >> l) - (nums[i - 1] >> l)
        for j in range(0, diff):
            U.extend(int(bin(0), 2).to_bytes(1, byteorder='big'))
        U.extend(int(bin(1), 2).to_bytes(1, byteorder='big'))
    counter = 0

    b = bin(0)
    while (len(U) % 8) != 0:
        U.extend(int(b, 2).to_bytes(1, byteorder='big'))

    for i in range(0, len(U)):
        if counter < 7:
            print(U[i], end='')
            counter += 1
        else:
            print(U[i])
            counter = 0
    m = hashlib.sha256()
    m.update(L)
    m.update(U)
    digest = m.hexdigest()
    print(digest)
