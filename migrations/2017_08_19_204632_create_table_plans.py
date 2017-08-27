from orator.migrations import Migration

class CreateTablePlans(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('plans') as table:
            table.increments('id').unsigned()
            table.integer('team_id').unsigned()
            table.timestamps()
            # Keys
            table.foreign('team_id')\
                .references('id')\
                .on('teams')\
                .on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('plans')
