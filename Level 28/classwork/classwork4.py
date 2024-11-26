def check_alive(health):
    if health > 0:
        return True  # Alive
    elif health <= 0:
        return False