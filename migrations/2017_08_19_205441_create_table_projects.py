from orator.migrations import Migration


class CreateTableProjects(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('projects') as table:
            table.increments('id')
            table.small_integer('project_id').unsigned()
            table.small_integer('team_id').unsigned()
            table.string('project_name', 100)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('projects')
