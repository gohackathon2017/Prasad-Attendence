class Phase2DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'Phase2':
            return 'phase2'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'Phase2':
            return 'phase2'
        return 'default'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'Phase2':
            return db == 'phase2'
        return db == 'default'
