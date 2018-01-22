from orator.migrations import Migration

class CreateTableTeams(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('teams') as table:
            table.increments('id').unsigned()
            table.string('name', 100)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('teams')
