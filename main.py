import random
from teadeposit import deposit_tea_token, withdraw_tea_token
from tea import tea_DAUN_swap, tea_HBRL_swap, hbrl_tea_swap, daun_tea_swap

functions = [tea_DAUN_swap, tea_HBRL_swap, hbrl_tea_swap, daun_tea_swap, deposit_tea_token, withdraw_tea_token]

for i in range(1, 121):  
    func = random.choice(functions)  
    print("")
    print("--------------------------------")
    print(f"{i}. işlem: ")  
    func() 