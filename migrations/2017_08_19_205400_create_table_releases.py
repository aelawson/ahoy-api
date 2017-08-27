from orator.migrations import Migration

class CreateTableReleases(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('releases') as table:
            table.increments('id').unsigned()
            table.integer('plan_id').unsigned()
            table.integer('stage_id').unsigned()
            table.string('repo_url', 255)
            table.timestamps()
            # Keys
            table.foreign('plan_id')\
                .references('id')\
                .on('plans')\
                .on_delete('cascade')
            table.foreign('stage_id')\
                .references('id')\
                .on('stages')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('releases')
