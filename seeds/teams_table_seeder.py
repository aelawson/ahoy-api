from orator.seeds import Seeder

class TeamsTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('teams').insert({
            'team_name': 'Front-End'
        })
        self.db.table('teams').insert({
            'team_name': 'Back-End'
        })
        self.db.table('teams').insert({
            'team_name': 'Dev-Ops'
        })
