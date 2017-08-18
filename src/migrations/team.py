from orator import Migration

class CreateTableTeams(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('teams') as table:
            table.increments('id')
            table.small_integer('team_id').unsigned()
            table.string('team_name', 100)

    def down(self):
        """
        Rollback the migrations.
        """
        self.schema.drop('teams')
