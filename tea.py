from web3 import Web3
import json
from datetime import datetime, timedelta
import random
import time

RPC_URL = "https://tea-sepolia.g.alchemy.com/public"
w3 = Web3(Web3.HTTPProvider(RPC_URL))

def load_wallet():
    with open('wallet.txt', 'r') as file:
        line = file.readline().strip()
        parts = line.split(',')
        if len(parts) < 2:
            raise ValueError("wallet.txt dosyasında yeterli bilgi yok. Lütfen adres ve özel anahtarı virgül ile ayırarak ekleyin.")
        address = parts[0].strip()
        private_key = parts[1].strip()
    return address, private_key

def create_tx_data(amount_out_min, to_address, deadline, path):
    tx_data = (
        "0x7ff36ab5"
        + f"{amount_out_min:064x}"
        + "0000000000000000000000000000000000000000000000000000000000000080"
        + f"{to_address[2:].zfill(64)}"
        + f"{deadline:064x}"
        + f"{len(path):064x}"
        + ''.join([addr[2:].zfill(64) for addr in path])
    )
    return tx_data

def create_tx_data2(amount_in, amount_out_min, to_address, deadline, path):
    tx_data2 = (
        "0x18cbafe5"
        + f"{amount_in:064x}"
        + f"{amount_out_min:064x}"
        + "00000000000000000000000000000000000000000000000000000000000000a0"
        + f"{to_address[2:].zfill(64)}"
        + f"{deadline:064x}"
        + f"{len(path):064x}"
        + ''.join([addr[2:].zfill(64) for addr in path])
    )
    return tx_data2

def tea_DAUN_swap():
    print("--------------------------------")
    print("TEA --> DAUN Swap başlatılıyor.")
    
    address, private_key = load_wallet()
    
    amount_in = w3.to_wei(random.uniform(0.001, 0.005), 'ether')
    amount_out_min = w3.to_wei(0.0005, 'ether')
    path = [
        "0x7752dbd604a5c43521408ee80486853dceb4cceb",
        "0xb1885A41876ff1BcB107a80A352A800b3D394f6F"
    ]
    to_address = address

    deadline = int((datetime.now() + timedelta(minutes=20)).timestamp())

    tx_data = create_tx_data(amount_out_min, to_address, deadline, path)

    transaction = {
        'to': '0xE15efbaA098AA81BaB70c471FeA760684dc776ae',
        'data': tx_data,
        'value': amount_in,
        'gas': 300000,
        'gasPrice': w3.to_wei('0.002000292', 'gwei'),
        'nonce': w3.eth.get_transaction_count(address),
        'chainId': 10218
    }

    signed_tx = w3.eth.account.sign_transaction(transaction, private_key)
    txn_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    if txn_receipt.status == 1:
        print("TEA --> DAUN Swap başarılı.")
    else:
        print("TEA --> DAUN Swap başarısız.")
    
    time.sleep(random.randint(2, 5))

def tea_HBRL_swap():
    print("--------------------------------")
    print("TEA --> HBRL Swap başlatılıyor.")
    
    address, private_key = load_wallet()
    
    amount_in = w3.to_wei(random.uniform(0.001, 0.005), 'ether')
    amount_out_min = w3.to_wei(0.0005, 'ether')
    path = [
        "0x7752dBd604a5C43521408ee80486853dCEb4cceB",
        "0x7d7D20Ea5afb64Fc7beC15ba4670FF08B5E838b6"
    ]
    to_address = address


    deadline = int((datetime.now() + timedelta(minutes=20)).timestamp())

    tx_data = create_tx_data(amount_out_min, to_address, deadline, path)

    transaction = {
        'to': '0xE15efbaA098AA81BaB70c471FeA760684dc776ae',
        'data': tx_data,
        'value': amount_in,
        'gas': 300000,
        'gasPrice': w3.to_wei('0.002000292', 'gwei'),
        'nonce': w3.eth.get_transaction_count(address),
        'chainId': 10218
    }

    signed_tx = w3.eth.account.sign_transaction(transaction, private_key)
    txn_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    if txn_receipt.status == 1:
        print("TEA --> HBRL Swap başarılı.")
    else:
        print("TEA --> HBRL Swap başarısız.")
       
    time.sleep(random.randint(2, 5))

def hbrl_tea_swap():
    print("--------------------------------")
    print("HBRL --> TEA Swap başlatılıyor.")
    
    address, private_key = load_wallet()
    
    amount_in = w3.to_wei(random.uniform(0.0001, 0.0005), 'ether')
    amount_out_min = w3.to_wei(0.00005, 'ether')
    path = [
        "0x7d7D20Ea5afb64Fc7beC15ba4670FF08B5E838b6",
        "0x7752dBd604a5C43521408ee80486853dCEb4cceB"
    ]
    to_address = address


    deadline = int((datetime.now() + timedelta(minutes=20)).timestamp())

    tx_data2 = create_tx_data2(amount_in, amount_out_min, to_address, deadline, path)

    transaction = {
        'to': '0xE15efbaA098AA81BaB70c471FeA760684dc776ae',
        'data': tx_data2,
        'value': 0,
        'gas': 300000,
        'gasPrice': w3.to_wei('0.002000292', 'gwei'),
        'nonce': w3.eth.get_transaction_count(address),
        'chainId': 10218
    }

    signed_tx = w3.eth.account.sign_transaction(transaction, private_key)
    txn_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    if txn_receipt.status == 1:
        print("HBRL --> TEA Swap başarılı.")
    else:
        print("HBRL --> TEA Swap başarısız.")

    time.sleep(random.randint(2, 5))

def daun_tea_swap():
    print("--------------------------------")
    print("DAUN --> TEA Swap başlatılıyor.")
    
    address, private_key = load_wallet()
    
    amount_in = w3.to_wei(random.uniform(0.0001, 0.0005), 'ether')
    amount_out_min = w3.to_wei(0.00005, 'ether')
    path = [
        "0xb1885A41876ff1BcB107a80A352A800b3D394f6F",
        "0x7752dBd604a5C43521408ee80486853dCEb4cceB"
    ]
    to_address = address


    deadline = int((datetime.now() + timedelta(minutes=20)).timestamp())

    tx_data2 = create_tx_data2(amount_in, amount_out_min, to_address, deadline, path)

    transaction = {
        'to': '0xE15efbaA098AA81BaB70c471FeA760684dc776ae',
        'data': tx_data2,
        'value': 0,
        'gas': 300000,
        'gasPrice': w3.to_wei('0.002000292', 'gwei'),
        'nonce': w3.eth.get_transaction_count(address),
        'chainId': 10218
    }

    signed_tx = w3.eth.account.sign_transaction(transaction, private_key)
    txn_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    if txn_receipt.status == 1:
        print("DAUN --> TEA Swap başarılı.")
    else:
        print("DAUN --> TEA Swap başarısız.")
    
    time.sleep(random.randint(2, 5))       

def main():
    tea_DAUN_swap()
    tea_HBRL_swap()
    hbrl_tea_swap()
    daun_tea_swap()

if __name__ == "__main__":
    main()
