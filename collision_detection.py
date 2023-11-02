def check_collision(object1, object2):
    if object1.colliderect(object2):
        return True
    else:
        return False