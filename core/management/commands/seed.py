from django.core.management.base import BaseCommand
from core.models import City, Region, Suburb

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "seed database (MODE_REFRESH: Recreate data, \
    MODE_CLEAR: Clear all data and do not create any object)"

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done!')


def clear_data():
    Region.objects.all().delete()


def create_region():
    regionNames = ["Canterbury", "Wellington", "Auckland"]
    for regionName in regionNames:
        region = Region(
            region=regionName
        )
        region.save()


def create_cities():
    cityNames = [
        ('Canterbury', 'Christchurch'),
        ('Canterbury', 'Ashburton'),
        ('Wellington', 'Wellington city'),
        ('Wellington', 'Lower Hutt'),
        ('Auckland', 'Auckland city'),
        ('Auckland', 'North Shore'),
    ]
    for cityName in cityNames:
        region = Region.objects.get(region=cityName[0])
        city = City(
            region=region,
            city=cityName[1]
        )
        city.save()


def create_suburbs():
    suburbNames = [
        ('Christchurch', 'Addinton'),
        ('Christchurch', 'Hornby'),
        ('Ashburton', 'Ashburton'),
        ('Ashburton', 'Eiffelton'),
        ('Wellington city', 'Aro Valley'),
        ('Wellington city', 'Brooklyn'),
        ('Lower Hutt', 'Petone'),
        ('Lower Hutt', 'Waterloo'),
        ('Auckland city', 'Avondale'),
        ('Auckland city', 'Ellerslie'),
        ('North Shore', 'Beach Haven'),
        ('North Shore', 'Albany'),
    ]
    for suburbName in suburbNames:
        city = City.objects.get(city=suburbName[0])
        suburb = Suburb(
            city=city,
            suburb=suburbName[1]
        )
        suburb.save()


def run_seed(self, mode):
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    create_region()
    create_cities()
    create_suburbs()
