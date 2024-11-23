""" Add new AI:s here """

from ai_contenders.full_random import full_random
from ai_contenders.random_attacker import random_attacker
from ai_contenders.full_defender import full_defender
from ai_contenders.non_aggressor import non_aggressor
from ai_contenders.counter_player import counter_player
from ai_contenders.mixtral_1 import mixtral_1
from ai_contenders.anti_random_attacker import anti_random_attacker

# All condenders are added here

ai_list = [
    full_random,
    random_attacker,
    full_defender,
    non_aggressor,
    counter_player,
    mixtral_1,
    anti_random_attacker,

]
