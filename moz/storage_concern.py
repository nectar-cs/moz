from k8_kat.res.pvc.kat_pvc import KatPvc
from moz.mosaic_concern import MosaicConcern
from wiz.model.part import Part
from wiz.model.step import Step


class SetPvcNamePart(Part):

  def list_pvcs(self):
    KatPvc.q()

class SetPvcNameStep(Step):

  def commit(self):
    pass

class StorageConcern(MosaicConcern):

  @classmethod
  def step(cls, name) -> Step:
    pass

  def __init__(self):
    pass

  def next_step(self, crt_step):
    if crt_step == '':
      pass


