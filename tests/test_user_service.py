import unittest
from src.services.users import get_user_service
from src.schema.users import AddUserSchema


class TestUserService(unittest.TestCase):
    user_service = get_user_service()
    def test_user_create(self, ):
        new_user_object = AddUserSchema(
            username="tester",
            email="test@gmail.com",
            password="test"
        )
        userid = self.user_service.create(new_user_object)
        user_object = self.user_service.get(userid)

        self.assertEqual(user_object.email, new_user_object.email)  
        self.assertEqual(user_object.name, new_user_object.username)
        self.user_service.delete(userid)
    