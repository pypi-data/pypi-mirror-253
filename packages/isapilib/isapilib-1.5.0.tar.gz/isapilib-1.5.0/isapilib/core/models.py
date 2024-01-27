from django.db import models

from isapilib.utilities import execute_query


class BaseModel(models.Model):

    def get_triggers(self, disabled=0, using='default'):
        tb_name = self._meta.db_table
        return execute_query('SELECT name FROM sys.triggers WHERE parent_id = OBJECT_ID(%s) AND is_disabled = %s',
                             [tb_name, disabled], using=using)

    def enable_trigger(self, name, using='default'):
        try:
            tb_name = self._meta.db_table
            execute_query(f'ENABLE TRIGGER [{name}] ON [{tb_name}]', using=using)
        except Exception:
            pass

    def disable_trigger(self, name, using='default'):
        try:
            tb_name = self._meta.db_table
            execute_query(f'DISABLE TRIGGER [{name}] ON [{tb_name}]', using=using)
        except Exception:
            pass

    def save(self, *args, **kwargs):
        check_triggers = kwargs.pop('triggers', True)
        using = kwargs.get('using', 'default')
        triggers = None
        if not check_triggers:
            triggers = self.get_triggers(using=using)
            for tgr in triggers:
                self.disable_trigger(tgr[0], using=using)

        try:
            return super().save(*args, **kwargs)
        except Exception as e:
            raise e
        finally:
            if not check_triggers:
                for tgr in triggers:
                    self.enable_trigger(tgr[0], using=using)

    class Meta:
        abstract = True
