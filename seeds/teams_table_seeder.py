from orator.seeds import Seeder

class TeamsTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('teams').insert({
            'name': 'Front-End'
        })
        self.db.table('teams').insert({
            'name': 'Back-End'
        })
        self.db.table('teams').insert({
            'name': 'Dev-Ops'
        })
