from orator.seeds import Seeder

class ReleasesTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        # Front-End Team
        self.db.table('releases').insert({
            'plan_id': 1,
            'stage_id': 1,
            'repo_url': 'https://www.github.com/aelawson/ahoy'
        })
        self.db.table('releases').insert({
            'plan_id': 1,
            'stage_id': 2,
            'repo_url': 'https://www.github.com/aelawson/ahoy'
        })
        self.db.table('releases').insert({
            'plan_id': 1,
            'stage_id': 3,
            'repo_url': 'https://www.github.com/aelawson/ahoy'
        })
        # Back-End Team
        self.db.table('releases').insert({
            'plan_id': 2,
            'stage_id': 1,
            'repo_url': 'https://www.github.com/aelawson/ahoy_api'
        })
        self.db.table('releases').insert({
            'plan_id': 2,
            'stage_id': 2,
            'repo_url': 'https://www.github.com/aelawson/ahoy_api'
        })
        self.db.table('releases').insert({
            'plan_id': 2,
            'stage_id': 3,
            'repo_url': 'https://www.github.com/aelawson/ahoy_api'
        })
        # Dev-Ops Team
        self.db.table('releases').insert({
            'plan_id': 3,
            'stage_id': 1,
            'repo_url': 'https://www.github.com/aelawson/tic_tac_toe'
        })
        self.db.table('releases').insert({
            'plan_id': 3,
            'stage_id': 2,
            'repo_url': 'https://www.github.com/aelawson/tic_tac_toe'
        })
        self.db.table('releases').insert({
            'plan_id': 3,
            'stage_id': 3,
            'repo_url': 'https://www.github.com/aelawson/tic_tac_toe'
        })
