#!/usr/bin/env python

import hashlib

DIFFICUTLY=6


# block1_transactions="HEADER:nonce{}----DATA:1#2#3#4"
block1_transactions="BL1#1#2#3#4"
block2_transactions="BL2#6#7#8#9"


def test_hash(hash, difficulty):

    difficulty_str = ''
    for i in range(difficulty):
        difficulty_str = '0' + difficulty_str

    print("Testing if hash starts with {}".format(difficulty_str))

    if hash.startswith(difficulty_str):
        # print("We a found a block !")
        return True


    # print("Keep looking for new block !")
    return False




def work_for_block(block_data, last_block_hash):
    nonce = 0



    block_hash = ''

    while True:

        block = "HEADER:nonce{}--last_block:{}----DATA:{}".format(nonce,
                                                                last_block_hash,
                                                                block_data)
        blocksha = hashlib.sha256()
        blocksha.update(str.encode(block))
        block_hash = blocksha.hexdigest()
        if test_hash(block_hash, DIFFICUTLY):
            print("We found block {} with nonce {} and difficulty {}".format(block_hash, nonce, DIFFICUTLY))
            break
        else:
            nonce += 1
            print("BLK: {} Nonce: {}".format(block_data[0:3], nonce))

    return block_hash




if __name__ == '__main__':

    block1 = work_for_block(block1_transactions, '0')
    block2 = work_for_block(block2_transactions, block1)


