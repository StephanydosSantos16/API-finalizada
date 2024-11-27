class UserService:
    @staticmethod
    def can_manage_users(user):
        return user['is_admin']

    @staticmethod
    def can_manage_product(product, user):
        return product.user_id == user['id']
