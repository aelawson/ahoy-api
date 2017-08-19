from orator.migrations import Migration


class CreateTablePlans(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('plans') as table:
            table.increments('id')
            table.small_integer('team_id').unsigned()
            table.small_integer('plan_id').unsigned()
            table.small_integer('project_id').unsigned()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('plans')
