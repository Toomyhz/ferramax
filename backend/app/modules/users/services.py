import app.modules.users.repository as user_repository

def assign_role_to_user(user_id, role_id):
    user = user_repository.get_user_by_id(user_id)
    if not user:
        raise ValueError("Usuario no encontrado")
    role = user_repository.get_role_by_id(role_id)
    if not role:
        raise ValueError("Rol no encontrado")
    if role in user.roles:
        raise ValueError("El usuario ya tiene ese rol")
    return user_repository.assign_role(user, role)