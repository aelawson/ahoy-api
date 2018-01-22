from orator.seeds import Seeder

class StagesTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('stages').insert({
            'name': 'Develop',
            'order': 1
        })
        self.db.table('stages').insert({
            'name': 'Staging',
            'order': 2
        })
        self.db.table('stages').insert({
            'name': 'Production',
            'order': 3
        })
