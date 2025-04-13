from web3 import Web3
import json
from datetime import datetime
import time 
import random

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

def deposit_tea_token(gas_price=350):
    print("--------------------------------")
    print("deposit işlemi başlatılıyor.")
    address, private_key = load_wallet()

    amount_in = w3.to_wei(random.uniform(0.001, 0.005), 'ether')

    tx_data = (
        "0xd0e30db0" 
    )

    transaction = {
        'to': '0xD0501e868AEC9973E118B975E00E1d078c88D263',
        'value': amount_in,
        'gas': 200000,
        'gasPrice': w3.to_wei(str(gas_price), 'gwei'),
        'nonce': w3.eth.get_transaction_count(address),
        'chainId': 10218,
        'data': tx_data
    }

    signed_tx = w3.eth.account.sign_transaction(transaction, private_key)
    txn_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    if txn_receipt.status == 1:
        print(f" TEA başarıyla  deposit edildi.")
    else:
        print("İşlem başarısız oldu.")

    time.sleep(random.randint(3, 8))

def withdraw_tea_token(gas_price=350):
    print("--------------------------------")
    print("withdraw işlemi başlatılıyor.")

    address, private_key = load_wallet()

    amount_out_min = w3.to_wei(0.0005, 'ether')

    tx_data = (
        "0x2e1a7d4d" 
        + f"{amount_out_min:064x}"
    )

    transaction = {
        'to': '0xD0501e868AEC9973E118B975E00E1d078c88D263',
        'value': 0,
        'gas': 200000,
        'gasPrice': w3.to_wei(str(gas_price), 'gwei'),
        'nonce': w3.eth.get_transaction_count(address),
        'chainId': 10218,
        'data': tx_data
    }

    signed_tx = w3.eth.account.sign_transaction(transaction, private_key)
    txn_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    if txn_receipt.status == 1:
        print(f" TEA başarıyla  withdraw edildi.")
    else:
        print("İşlem başarısız oldu.")
    
    time.sleep(random.randint(3, 8))

def main():
    deposit_tea_token()
    withdraw_tea_token()

if __name__ == "__main__":
    main() 