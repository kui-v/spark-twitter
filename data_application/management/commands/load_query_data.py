from csv import DictReader

from django.core.management import BaseCommand

from data_application.models import Topic


VACCINES_NAMES = [
    'Canine Parvo',
    'Canine Distemper',
    'Canine Rabies',
    'Canine Leptospira',
    'Feline Herpes Virus 1',
    'Feline Rabies',
    'Feline Leukemia'
]

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the topic data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from metadata files in the sqllite_metadata folder"

    def handle(self, *args, **options):
        if Topic.objects.exists():
            print('Query data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return

        '''
        print("Creating vaccine data")
        for vaccine_name in VACCINES_NAMES:
            vac = Vaccine(name=vaccine_name)
            vac.save()
        '''
        
        print("Loading topics data")
        
        for row in DictReader(open('./sqllite_metadata/topics_data.csv')):
            topic = Topic()
            topic.name = row['Topic']

            topic.save()
        '''
        for row in DictReader(open('./sqllite_metadata/questions_data.csv')):
            question = Question()
            question.question = row['Question']'''
        
