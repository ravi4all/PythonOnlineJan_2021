def player():
    health = 78
    return health

def enemy():
    health = 60
    return health

def game():
    p_health = player()
    e_health = enemy()
    print("Player Health : ",p_health)
    print("Enemy Health : ",e_health)

game()