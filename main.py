import random
import time
from teadeposit import deposit_tea_token, withdraw_tea_token
from tea import tea_DAUN_swap, tea_HBRL_swap, hbrl_tea_swap, daun_tea_swap

def set_gas_price():
    try:
        gas_price = input("Gas price değerini girin (gwei olarak, örnek: 500): ")
        gas_price = int(gas_price)
        return gas_price
    except ValueError:
        print("Geçersiz bir değer girdiniz. Varsayılan değer: 500 gwei")
        return 500

def main():
    # Kullanıcıdan gas price değerini al
    gas_price = set_gas_price()
    print(f"Gas price {gas_price} gwei olarak ayarlandı.")
    
    # Kullanılacak fonksiyonları listele
    functions = [
        {"func": tea_DAUN_swap, "gas_price": gas_price},
        {"func": tea_HBRL_swap, "gas_price": gas_price},
        {"func": hbrl_tea_swap, "gas_price": gas_price},
        {"func": daun_tea_swap, "gas_price": gas_price},
        {"func": deposit_tea_token, "gas_price": gas_price},
        {"func": withdraw_tea_token, "gas_price": gas_price}
    ]
    
    # 120 kez rastgele bir fonksiyon çalıştır
    for i in range(1, 121):
        func_info = random.choice(functions)
        print(f"{i}. işlem: ")
        
        # Gas price değerini ilgili fonksiyona parametre olarak gönder
        try:
            if hasattr(func_info["func"], "__code__") and func_info["func"].__code__.co_argcount > 0:
                func_info["func"](func_info["gas_price"])
            else:
                # Bazı fonksiyonlar parametre almıyor olabilir, bu durumu kontrol et
                func_info["func"]()
        except TypeError:
            # Parametre almayan fonksiyonlar için
            func_info["func"]()

if __name__ == "__main__":
    main() 