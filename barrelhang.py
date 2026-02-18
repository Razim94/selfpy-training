import random

# BarrelHang - 7 Stages (can scale back to 6 if needed)

stage_1 = r"""
  \\ | | //
    \| |/
     ___
    |   |
    |___|
"""

stage_2 = r"""
   \ | | /
     \|/
     ___
    |   |
    |___|
"""

stage_3 = r"""
    \| |
     \|
     ___
    |   |
    |___|
"""

stage_4 = r"""
     \|
      |
     ___
    |   |
    |___|
"""

stage_5 = r"""

    !!!!!
     ___
    |   |
    |___|
    (falling!)
"""

stage_6 = r"""

     ___
    |   |
    |___|
    ~~~~~~~
   (splash incoming!)
"""

stage_7 = r"""

  ~~ ___~~~
  ~~/ X |~~~
  ~~|_#_/~~~~
  ~~~~~~~~~~
  
  
    SPLASH!
"""

# Game setup
attempts = random.randint(5,10)
print(f"You have {attempts} attempts to win I guess.")

print("Welcome to BarrelHang!")
print(r"""
  ____                      _ _   _
 |  _ \                    | | | | |
 | |_) | __ _ _ __ _ __ ___| | |_| | __ _ _ __   __ _
 |  _ < / _` | '__| '__/ _ \ |  _  |/ _` | '_ \ / _` |
 | |_) | (_| | |  | | |  __/ | | | | (_| | | | | (_| |
 |____/ \__,_|_|  |_|  \___|_|_| |_|\__,_|_| |_|\__, |
                                                  _| |
                                                 |___|
""")
