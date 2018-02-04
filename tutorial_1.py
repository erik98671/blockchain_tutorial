import hashlib
import time

class Block:
    def __init__(self, index, previousHash, timestamp, data, currentHash):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data
        self.currentHash = currentHash

def getGenesisBlock():
    return Block(0, '0', '1517671763.270221', 'My very first block :)', '0q23nfa0se8fhPH234hnjldapjfasdfansdf23')

def calculateHash(index, previousHash, timestamp, data):
    value = str(index) + str(previousHash) + str(timestamp) + str(data)
    sha = hashlib.sha256(value.encode('utf-8'))
    return str(sha.hexdigest())

def calculateHashForBlock(block):
    return calculateHash(block.index, block.previousHash, block.timestamp, block.data)

def getLatestBlock():
    return blockchain[len(blockchain)-1]

def generateNextBlock(blockData):
    previousBlock = getLatestBlock()
    previousHash = previousBlock.currentHash
    nextIndex = previousBlock.index + 1
    nextTimestamp = time.time()
    nextHash = calculateHash(nextIndex, previousHash, nextTimestamp, blockData)
    return Block(nextIndex, previousHash, nextTimestamp, blockData, nextHash)

def isSameBlock(block1, block2):
    if block1.index != block2.index:
        return False
    elif block1.previousHash != block2.previousHash:
        return False
    elif block1.timestamp != block2.timestamp:
        return False
    elif block1.data != block2.data:
        return False
    elif block1.currentHash != block2.currentHash:
        return False
    return True

def isValidNewBlock(newBlock, previousBlock):
    if previousBlock.index + 1 != newBlock.index:
        print('Indices Do Not Match Up')
        return False
    elif previousBlock.currentHash != newBlock.previousHash:
        print('Previous hash does not match')
        return False
    elif calculateHashForBlock(newBlock) != newBlock.currentHash:
        print('Hash is invalid')
        return False
    else:
        print('The new block is valid.')
    return True

def isValidChain(bcToValidate):
    if not isSameBlock(bcToValidate[0], getGenesisBlock()):
        print('Genesis Block Incorrect')
        return False
    else:
        print('The chain is valid.')
    
    tempBlocks = [bcToValidate[0]]
    for i in range(1, len(bcToValidate)):
        if isValidNewBlock(bcToValidate[i], tempBlocks[i-1]):
            tempBlocks.append(bcToValidate[i])
        else:
            return False
    return True

# Create the blockchain as an array and add the Genesis Block.
blockchain = [getGenesisBlock()]

# This returns 'The chain is valid.' if the chain is valid.
# isValidChain(blockchain)

# This returns 'The new block is valid.' if the new block is valid.
# isValidNewBlock(generateNextBlock('Hello world!'), blockchain[0])

# If the old block and the new block are the same, this returns 'True'.
# print('The blocks are the same: ' + str(isSameBlock(blockchain[0], generateNextBlock('Hello world!'))))
