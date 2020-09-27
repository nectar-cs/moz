import os

from nectwiz import entrypoint
from nectwiz.model.base.wiz_model import models_man
from nectwiz.core.core import utils
from overrides.access_points import IceCreamAccessPoints

if __name__ == '__main__':
  root_dir = os.path.dirname(os.path.abspath(__file__))
  yamls = utils.yamls_in_dir(f'{root_dir}/configs')

  models_man.add_descriptors(yamls)
  models_man.add_classes([
    IceCreamAccessPoints
  ])

  entrypoint.start()
