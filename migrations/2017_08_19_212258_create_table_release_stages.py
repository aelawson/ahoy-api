from orator.migrations import Migration


class CreateTableReleaseStages(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('release_stages') as table:
            table.increments('id')
            table.small_integer('release_id').unsigned()
            table.small_integer('stage_id').unsigned()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('release_stages')
