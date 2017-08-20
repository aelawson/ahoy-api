from orator.migrations import Migration


class CreateTableReleaseStages(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('release_stages') as table:
            table.integer('release_id').unsigned()
            table.integer('stage_id').unsigned()
            table.timestamps()
            # Keys
            table.foreign('release_id')\
                .references('release_id')\
                .on('releases')\
                .on_delete('cascade')
            table.foreign('stage_id')\
                .references('stage_id')\
                .on('stages')\
                .on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('release_stages')
