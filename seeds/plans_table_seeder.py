from orator.seeds import Seeder

class PlansTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('plans').insert({
            'team_id': 1
        })
        self.db.table('plans').insert({
            'team_id': 2
        })
        self.db.table('plans').insert({
            'team_id': 3
        })
