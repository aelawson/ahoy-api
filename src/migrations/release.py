from orator import Migration

class CreateTableReleases(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('releases') as table:
            table.increments('id')
            table.small_integer('team_id').unsigned()
            table.small_integer('release_id').unsigned()

    def down(self):
        """
        Rollback the migration.
        """
        self.schema.drop('releases')
