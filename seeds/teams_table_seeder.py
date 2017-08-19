from orator.seeds import Seeder
from orator.orm import Factory

factory = Factory()

@factory.define(Team)
def users_factory(faker):
    return {
        'team_id': faker.uuid4(),
        'team_name': faker.word()
    }

class TeamsTableSeeder(Seeder):

    factory = factory

    def run(self):
        """
        Run the database seeds.
        """
        self.factory(Team, 5).create()
