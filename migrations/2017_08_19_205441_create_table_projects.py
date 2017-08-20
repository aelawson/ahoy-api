from orator.migrations import Migration


class CreateTableProjects(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('projects') as table:
            table.increments('project_id').unsigned()
            table.integer('team_id').unsigned()
            table.string('project_name', 100)
            table.string('repo_url', 255)
            table.timestamps()
            # Keys
            table.foreign('team_id')\
                .references('team_id')\
                .on('teams')\
                .on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('projects')
