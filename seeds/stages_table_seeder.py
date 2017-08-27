from orator.seeds import Seeder

class StagesTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('stages').insert({
            'stage_name': 'Develop',
            'stage_order': 1
        })
        self.db.table('stages').insert({
            'stage_name': 'Staging',
            'stage_order': 2
        })
        self.db.table('stages').insert({
            'stage_name': 'Production',
            'stage_order': 3
        })
