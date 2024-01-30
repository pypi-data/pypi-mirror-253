from random import randint

# ========================================
  #SHADOW ALGORITHM
  #© 2023 Rohan Date & Shailesh Date 
  
  # Algorithm uses LFSR to generate one 
  # or more seeds, which in turn are 
  # concatenated to scramble the 
  # numbers further.

  # state is fixed to 128 bits

# ========================================

def get_taps(thingToXor : int, taps : list[int]) -> int:
    copy = thingToXor
    if len(taps) > 1:
        for i in taps:
            copy ^= thingToXor >> i
    else:
        copy ^= thingToXor >> taps[0]
    return copy

def scrng(numsToGen :int | None = 1, lenOfSeed :int | None = 100, strength : tuple[int, list[int]] | None = (127, [1, 2, 7])) -> list: 

    outputLen = 5000
    seedLen = lenOfSeed
    myBits = strength[0]
    someList = []
    state = (1 << myBits) | 1
    numCnt = 1
    concatVar = ""
    seedList = []
    taps = strength[1]
    while True:

            # tap and shift bits (LFSR part)
            newbit = (state ^ get_taps(state, taps )) & 1
            state = (state >> 1) | (newbit << myBits)

            # append int representation of the binary
            #  - this helps to get rid of the 0b representation
            #  - this automatically generates a set of values which when concatenated together become a random set of 
            #    numbers that are between 0-9

            concatVar += str(state)

            # generate the first x set of digits (defined by outputLen)
            numCnt += 1
            if numCnt >= outputLen: 
                break

    someList.extend(concatVar)
    myListLen = len(someList)

        # generate the final list of random numbers that has length numsToGen
    for i in range(numsToGen):

            # generate a rnd number based on list length
            #  - check to make sure random number + seedLen does not go beyond list
            someRndInt = randint(1, myListLen)
            while ((myListLen - someRndInt) < seedLen):
                someRndInt = randint(1, outputLen)

            # extract seed numbers from list
            myBegin = someRndInt
            myEnd = someRndInt + lenOfSeed
            newSeed = someList[myBegin:myEnd]
            # join the collected numbers
            myJoinedNewSeed = ''.join(newSeed)
            seedList.append(myJoinedNewSeed)
    return seedList
