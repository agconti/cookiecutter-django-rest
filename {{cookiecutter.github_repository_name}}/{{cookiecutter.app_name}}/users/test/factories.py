import factory
from faker import Faker

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'users.User'
        django_get_or_create = ('username',)

    username = factory.Sequence(lambda n: 'testuser{}'.format(n))
    password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    email = fake.email()
    first_name = fake.first_name()
    last_name = fake.last_name()
    is_active = True
    is_staff = False
