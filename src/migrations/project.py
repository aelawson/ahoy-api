from orator import Migration

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

    def down(self):
        """
        Rollback the migration.
        """
        self.schema.drop('releases')
