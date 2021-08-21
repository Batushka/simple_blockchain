from blockchain.functions_and_classes import Block, create_genesis_block, next_block

# создаем блокчейн и первый блок
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# определяем количество блоков
# которые добавим после первого
num_of_blocks_to_add = 20

# добавим блоки в цепь
for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    # выводим логи создания блоков
    print("Block #{} has been added to the blockchain!".format(block_to_add.index))
    print("Hash: {}\n".format(block_to_add.hash))
