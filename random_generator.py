from random import randint

def random_pass(length:int) -> str:
    alp = "1234567890qwertyuiop[]asdfghjkl;zxcvbnm,./QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+"
    result_str = ""
    for letter in range(length):
        result_str += alp[randint(0, len(alp)-1)]
    return result_str