from functools import wraps


def require_admin(func):
    @wraps(func)
    def wrapper(user_role, *args, **kwargs):
        if user_role != 'admin':
            print("❌ Access denied: Admins only!")
            return None
        print("✅ Access granted: Welcome, admin!")
        return func(*args, **kwargs)
    return wrapper


@require_admin
def delete_user(user_id):
    print(f"User with ID {user_id} has been deleted.")


# Testing the decorator
delete_user('admin', 123)  # Should allow access
delete_user('guest', 456)  # Should deny access