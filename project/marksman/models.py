import logging
from marksman.db import DbModelz


logger = logging.getLogger(__name__)


class Models:
    def __init__(self, db_modelz: DbModelz, pks_fn: dict, values_fn: dict):
        self.db_modelz = db_modelz
        pks = {}
        for k, v in pks_fn.items():
            pks[k] = v()
        self.pks = pks  # dict of pk and value
        self.values_fn = values_fn  # dict of value_field_name : func

    def read(self):
        return self.db_modelz.exists(**self.pks)

    def create(self):
        calculated = []
        for _, v in self.pks.items():
            calculated.append(v)
        for _, fn in self.values_fn.items():
            val = fn()
            if not val:
                logger.warning('You cant keep this field empty!')
                val = fn()
                if not val:
                    logger.warning(
                        'Quitting... As you are keeping this field empty')
                    return
            calculated.append(val)
        self.db_modelz.insert(tuple(calculated))

    def update(self):
        calculated = {}
        for k, v in self.values_fn.items():
            calculated[k] = v()
        if any(calculated.values()):
            self.db_modelz.update(calculated, **self.pks)
        else:
            logger.warning('You left all values empty > Not updating anything')

    def delete(self):
        self.db_modelz.delete(**self.pks)

