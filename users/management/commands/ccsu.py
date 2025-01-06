# from django.core.management import BaseCommand
#
# from users.models import User
#
#
# class Command(BaseCommand):
#
#     def handle(self, *args, **options):
#         user = User.objects.create(
#             username='admin@web.bm',
#             first_name='Admin',
#             last_name='Adminov',
#             is_staff=True,
#             is_superuser=True,
#             is_active=True,
#             role='admin'
#         )
#
#         user.set_password('qwerty')
#         user.save()
#         print('Admin created')
#
#         moderator = User.objects.create(
#             username='master@web.bm',
#             first_name='Master',
#             last_name='Masterov',
#             role='master',
#             is_staff=True,
#             is_superuser=False,
#             is_active=True
#         )
#
#         moderator.set_password('qwerty')
#         moderator.save()
#         print('Master created')
#
#         user = User.objects.create(
#             username='operator@web.bm',
#             first_name='Operator',
#             last_name='Operatov',
#             role='Operator',
#             is_staff=False,
#             is_superuser=False,
#             is_active=True
#         )
#
#         user.set_password('qwerty')
#         user.save()
#         print('Operator created')


from django.core.management import BaseCommand
from users.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        # Создание администратора
        user = User.objects.create(
            username='admin@web.bm',
            first_name='Admin',
            last_name='Adminov',
            is_staff=True,
            is_superuser=True,
            is_active=True,
            role='admin'
        )
        user.set_password('qwerty')
        user.save()
        print('Admin created')

        # Создание модератора
        moderator = User.objects.create(
            username='master@web.bm',
            first_name='Master',
            last_name='Masterov',
            role='master',
            is_staff=True,
            is_superuser=False,
            is_active=True
        )
        moderator.set_password('qwerty')
        moderator.save()
        print('Master created')

        # Создание оператора
        operator = User.objects.create(
            username='operator@web.bm',
            first_name='Operator',
            last_name='Operatov',
            role='operator',  # Обратите внимание на правильный регистр роли
            is_staff=False,
            is_superuser=False,
            is_active=True
        )
        operator.set_password('qwerty')
        operator.save()
        print('Operator created')
