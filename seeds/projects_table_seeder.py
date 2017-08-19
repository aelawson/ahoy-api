from orator.seeds import Seeder
from orator.orm import Factory

factory = Factory()

@factory.define(Project)
def projects_factory(faker):
    return {
        'project_id': faker.uuid4(),
        'team_id': faker.uuid4(),
        'project_name': faker.word(),
        'repo_url': faker.uri()
    }

class ProjectsTableSeeder(Seeder):

    factory = factory

    def run(self):
        """
        Run the database seeds.
        """
        self.factory(Project, 5).create()
