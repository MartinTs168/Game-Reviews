from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand
from django.db.models import Q

UserModel = get_user_model()


class Command(BaseCommand):
    help = "Creates initial superuser, Employee group and a staff user"

    def handle(self, *args, **options):
        if not UserModel.objects.filter(
                Q(username='admin') & Q(is_superuser=True)
        ):
            admin_password = settings.DJANGO_ADMIN_PASSWORD
            if not admin_password:
                admin_password = input("Enter password for superuser 'admin': ")

            UserModel.objects.create_superuser(
                username='admin',
                email='admin@admin.com',
                password=admin_password
            )

            self.stdout.write(self.style.SUCCESS("Superuser 'admin' created successfully!"))
        else:
            self.stdout.write("Superuser 'admin' already exists. Skipping step")

        employee_group, created = Group.objects.get_or_create(name='Employee')
        if created:
            permissions = Permission.objects.filter(
                content_type__app_label__in=('games', 'tags', 'reviews',),
                codename__in=(
                    'add_game', 'change_game', 'delete_game',
                    'add_tag', 'change_tag', 'delete_tag',
                    'delete_review',
                )
            )

            employee_group.permissions.add(*permissions)
            self.stdout.write(self.style.SUCCESS("'Employee' group created successfully!"))

        else:
            self.stdout.write("'Employee' group already exists. Skipping step")

        if not UserModel.objects.filter(
                Q(username='default_employee') &
                Q(groups__name='Employee') &
                Q(is_staff=True)
        ):
            employee_password = settings.DJANGO_DEFAULT_EMPLOYEE_PASSWORD
            if not employee_password:
                employee_password = input("Enter password for employee user 'default_employee': ")

            employee = UserModel.objects.create_user(
                username='default_employee',
                email='default_employee@mail.com',
                password=employee_password,
                is_staff=True,
            )
            employee.groups.add(employee_group)
            self.stdout.write(self.style.SUCCESS("Employee user 'default_employee' created successfully!"))
        else:
            self.stdout.write("Employee user 'default_employee' already exists. Skipping step")
