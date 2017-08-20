from orator.migrations import Migration

class CreateTableReleases(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('releases') as table:
            table.increments('release_id').unsigned()
            table.integer('team_id').unsigned()
            table.integer('project_id').unsigned()
            table.timestamps()
            # Keys
            table.foreign('team_id')\
                .references('team_id')\
                .on('teams')\
                .on_delete('cascade')
            table.foreign('project_id')\
                .references('project_id')\
                .on('projects')\
                .on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('releases')
