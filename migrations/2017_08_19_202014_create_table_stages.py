from orator.migrations import Migration

class CreateTableStages(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('stages') as table:
            table.increments('id').unsigned()
            table.string('name', 50)
            table.small_integer('order').unsigned()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('stages')
