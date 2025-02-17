import random
class Data:
    @staticmethod
    def create_new_email_for_registration():
        return f'ADAkimova{random.randint(100,999)}@ya.ru'
    @staticmethod
    def create_new_password_for_registration():
        return f'Test!{random.randint(100,999)}'