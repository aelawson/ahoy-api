from orator.seeds import Seeder

from seeds.teams_table_seeder import TeamsTableSeeder
from seeds.plans_table_seeder import PlansTableSeeder
from seeds.releases_table_seeder import ReleasesTableSeeder
from seeds.stages_table_seeder import StagesTableSeeder

class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(StagesTableSeeder)
        self.call(TeamsTableSeeder)
        self.call(PlansTableSeeder)
        self.call(ReleasesTableSeeder)
