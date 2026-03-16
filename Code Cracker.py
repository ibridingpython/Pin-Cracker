from random import choice
from itertools import product 
import time 

#? itertools is to make sure that it'll try each combination once
#? making the brute force extremely effective

#* A simulation of pin cracking program.

prompt = ("Welcome to pin cracker!")
prompt += ("\nPlease insert the length of the pin: ")

digits = list(range(10))
attempts = 0
bruting = True

while bruting == True:
    password = input(prompt)
    password = int(password)
    
    generated_pin = []
    
    for i in range(password):
        value = choice(digits)
        generated_pin.append(value)
        
    print(f"{len(generated_pin)} digits pin has been succesfully generated.")
    print(f"Program will now attempt to brute force.")
    
        #! countdown
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
            
    print("Starting attack...")
    print()
    start_time = time.time() #! time
    bruting = False
    
    
    

for attack_pin in product(digits, repeat=password):
        
        attempts += 1
        
        elapsed_time = time.time() - start_time
        attempts_per_second = attempts / elapsed_time
        
        if attempts % 1000000 == 0:
            print(f"Attempts so far: {attempts}")
            print(f"Current guess:", "".join(str(x) for x in attack_pin))
            print("Attempts per second:", f"{attempts_per_second:.1f}")
            print()
        
            
        if list(attack_pin) == generated_pin:
            
            print("Attack successfully executed.")
            print("> The pin is:", "".join(str(x) for x in attack_pin))
            print("> Attempts taken:", attempts)
            print("> Attempts per second:", f"{attempts_per_second:.2f}")
            print("> Time taken:", f"{elapsed_time:.1f}")
            print("===Made By Ibad===")
            print()

            break
