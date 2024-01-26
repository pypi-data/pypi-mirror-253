# coding: UTF-8
import sys
bstack11ll1_opy_ = sys.version_info [0] == 2
bstackl_opy_ = 2048
bstack1ll111l_opy_ = 7
def bstack1lll1l1_opy_ (bstack1l111_opy_):
    global bstack1111l1_opy_
    bstack1l1ll11_opy_ = ord (bstack1l111_opy_ [-1])
    bstack1l111ll_opy_ = bstack1l111_opy_ [:-1]
    bstack1l1ll1_opy_ = bstack1l1ll11_opy_ % len (bstack1l111ll_opy_)
    bstack11l1l1l_opy_ = bstack1l111ll_opy_ [:bstack1l1ll1_opy_] + bstack1l111ll_opy_ [bstack1l1ll1_opy_:]
    if bstack11ll1_opy_:
        bstack111ll11_opy_ = unicode () .join ([unichr (ord (char) - bstackl_opy_ - (bstack11l1lll_opy_ + bstack1l1ll11_opy_) % bstack1ll111l_opy_) for bstack11l1lll_opy_, char in enumerate (bstack11l1l1l_opy_)])
    else:
        bstack111ll11_opy_ = str () .join ([chr (ord (char) - bstackl_opy_ - (bstack11l1lll_opy_ + bstack1l1ll11_opy_) % bstack1ll111l_opy_) for bstack11l1lll_opy_, char in enumerate (bstack11l1l1l_opy_)])
    return eval (bstack111ll11_opy_)
import os
import re
import sys
import json
import time
import shutil
import tempfile
import requests
import subprocess
from threading import Thread
from os.path import expanduser
from bstack_utils.constants import *
from requests.auth import HTTPBasicAuth
from bstack_utils.helper import bstack1llll11ll_opy_, bstack1ll1ll1lll_opy_
class bstack1111ll111_opy_:
  working_dir = os.getcwd()
  bstack1l111l1l1_opy_ = False
  config = {}
  binary_path = bstack1lll1l1_opy_ (u"ࠧࠨጲ")
  bstack111llll1l1_opy_ = bstack1lll1l1_opy_ (u"ࠨࠩጳ")
  bstack1llll111ll_opy_ = False
  bstack111llll1ll_opy_ = None
  bstack111l11l111_opy_ = {}
  bstack111ll11ll1_opy_ = 300
  bstack111ll1l1ll_opy_ = False
  logger = None
  bstack111ll111ll_opy_ = False
  bstack111lll1111_opy_ = bstack1lll1l1_opy_ (u"ࠩࠪጴ")
  bstack111l1ll1l1_opy_ = {
    bstack1lll1l1_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪጵ") : 1,
    bstack1lll1l1_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬጶ") : 2,
    bstack1lll1l1_opy_ (u"ࠬ࡫ࡤࡨࡧࠪጷ") : 3,
    bstack1lll1l1_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠭ጸ") : 4
  }
  def __init__(self) -> None: pass
  def bstack111lll1lll_opy_(self):
    bstack111ll1111l_opy_ = bstack1lll1l1_opy_ (u"ࠧࠨጹ")
    bstack111ll11lll_opy_ = sys.platform
    bstack111l1ll1ll_opy_ = bstack1lll1l1_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧጺ")
    if re.match(bstack1lll1l1_opy_ (u"ࠤࡧࡥࡷࡽࡩ࡯ࡾࡰࡥࡨࠦ࡯ࡴࠤጻ"), bstack111ll11lll_opy_) != None:
      bstack111ll1111l_opy_ = bstack11ll11l111_opy_ + bstack1lll1l1_opy_ (u"ࠥ࠳ࡵ࡫ࡲࡤࡻ࠰ࡳࡸࡾ࠮ࡻ࡫ࡳࠦጼ")
      self.bstack111lll1111_opy_ = bstack1lll1l1_opy_ (u"ࠫࡲࡧࡣࠨጽ")
    elif re.match(bstack1lll1l1_opy_ (u"ࠧࡳࡳࡸ࡫ࡱࢀࡲࡹࡹࡴࡾࡰ࡭ࡳ࡭ࡷࡽࡥࡼ࡫ࡼ࡯࡮ࡽࡤࡦࡧࡼ࡯࡮ࡽࡹ࡬ࡲࡨ࡫ࡼࡦ࡯ࡦࢀࡼ࡯࡮࠴࠴ࠥጾ"), bstack111ll11lll_opy_) != None:
      bstack111ll1111l_opy_ = bstack11ll11l111_opy_ + bstack1lll1l1_opy_ (u"ࠨ࠯ࡱࡧࡵࡧࡾ࠳ࡷࡪࡰ࠱ࡾ࡮ࡶࠢጿ")
      bstack111l1ll1ll_opy_ = bstack1lll1l1_opy_ (u"ࠢࡱࡧࡵࡧࡾ࠴ࡥࡹࡧࠥፀ")
      self.bstack111lll1111_opy_ = bstack1lll1l1_opy_ (u"ࠨࡹ࡬ࡲࠬፁ")
    else:
      bstack111ll1111l_opy_ = bstack11ll11l111_opy_ + bstack1lll1l1_opy_ (u"ࠤ࠲ࡴࡪࡸࡣࡺ࠯࡯࡭ࡳࡻࡸ࠯ࡼ࡬ࡴࠧፂ")
      self.bstack111lll1111_opy_ = bstack1lll1l1_opy_ (u"ࠪࡰ࡮ࡴࡵࡹࠩፃ")
    return bstack111ll1111l_opy_, bstack111l1ll1ll_opy_
  def bstack111l1lllll_opy_(self):
    try:
      bstack111ll1l1l1_opy_ = [os.path.join(expanduser(bstack1lll1l1_opy_ (u"ࠦࢃࠨፄ")), bstack1lll1l1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬፅ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack111ll1l1l1_opy_:
        if(self.bstack111l11lll1_opy_(path)):
          return path
      raise bstack1lll1l1_opy_ (u"ࠨࡕ࡯ࡣ࡯ࡦࡪࠦࡴࡰࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠥፆ")
    except Exception as e:
      self.logger.error(bstack1lll1l1_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡪ࡮ࡴࡤࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨࠤࡵࡧࡴࡩࠢࡩࡳࡷࠦࡰࡦࡴࡦࡽࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࠲ࠦࡻࡾࠤፇ").format(e))
  def bstack111l11lll1_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack111lll1ll1_opy_(self, bstack111ll1111l_opy_, bstack111l1ll1ll_opy_):
    try:
      bstack111ll1ll1l_opy_ = self.bstack111l1lllll_opy_()
      bstack111ll1llll_opy_ = os.path.join(bstack111ll1ll1l_opy_, bstack1lll1l1_opy_ (u"ࠨࡲࡨࡶࡨࡿ࠮ࡻ࡫ࡳࠫፈ"))
      bstack111l1l1111_opy_ = os.path.join(bstack111ll1ll1l_opy_, bstack111l1ll1ll_opy_)
      if os.path.exists(bstack111l1l1111_opy_):
        self.logger.info(bstack1lll1l1_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡨࡲࡹࡳࡪࠠࡪࡰࠣࡿࢂ࠲ࠠࡴ࡭࡬ࡴࡵ࡯࡮ࡨࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠦፉ").format(bstack111l1l1111_opy_))
        return bstack111l1l1111_opy_
      if os.path.exists(bstack111ll1llll_opy_):
        self.logger.info(bstack1lll1l1_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡽ࡭ࡵࠦࡦࡰࡷࡱࡨࠥ࡯࡮ࠡࡽࢀ࠰ࠥࡻ࡮ࡻ࡫ࡳࡴ࡮ࡴࡧࠣፊ").format(bstack111ll1llll_opy_))
        return self.bstack111l11l1ll_opy_(bstack111ll1llll_opy_, bstack111l1ll1ll_opy_)
      self.logger.info(bstack1lll1l1_opy_ (u"ࠦࡉࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡨࡵࡳࡲࠦࡻࡾࠤፋ").format(bstack111ll1111l_opy_))
      response = bstack1ll1ll1lll_opy_(bstack1lll1l1_opy_ (u"ࠬࡍࡅࡕࠩፌ"), bstack111ll1111l_opy_, {}, {})
      if response.status_code == 200:
        with open(bstack111ll1llll_opy_, bstack1lll1l1_opy_ (u"࠭ࡷࡣࠩፍ")) as file:
          file.write(response.content)
        self.logger.info(bstack111l1lll11_opy_ (u"ࠢࡅࡱࡺࡲࡱࡵࡡࡥࡧࡧࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡥࡳࡪࠠࡴࡣࡹࡩࡩࠦࡡࡵࠢࡾࡦ࡮ࡴࡡࡳࡻࡢࡾ࡮ࡶ࡟ࡱࡣࡷ࡬ࢂࠨፎ"))
        return self.bstack111l11l1ll_opy_(bstack111ll1llll_opy_, bstack111l1ll1ll_opy_)
      else:
        raise(bstack111l1lll11_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠦࡴࡩࡧࠣࡪ࡮ࡲࡥ࠯ࠢࡖࡸࡦࡺࡵࡴࠢࡦࡳࡩ࡫࠺ࠡࡽࡵࡩࡸࡶ࡯࡯ࡵࡨ࠲ࡸࡺࡡࡵࡷࡶࡣࡨࡵࡤࡦࡿࠥፏ"))
    except:
      self.logger.error(bstack1lll1l1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠨፐ"))
  def bstack111l11llll_opy_(self, bstack111ll1111l_opy_, bstack111l1ll1ll_opy_):
    try:
      bstack111l1l1111_opy_ = self.bstack111lll1ll1_opy_(bstack111ll1111l_opy_, bstack111l1ll1ll_opy_)
      bstack111ll11l1l_opy_ = self.bstack111ll1l11l_opy_(bstack111ll1111l_opy_, bstack111l1ll1ll_opy_, bstack111l1l1111_opy_)
      return bstack111l1l1111_opy_, bstack111ll11l1l_opy_
    except Exception as e:
      self.logger.error(bstack1lll1l1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡧࡦࡶࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡳࡥࡹ࡮ࠢፑ").format(e))
    return bstack111l1l1111_opy_, False
  def bstack111ll1l11l_opy_(self, bstack111ll1111l_opy_, bstack111l1ll1ll_opy_, bstack111l1l1111_opy_, bstack111l11l11l_opy_ = 0):
    if bstack111l11l11l_opy_ > 1:
      return False
    if bstack111l1l1111_opy_ == None or os.path.exists(bstack111l1l1111_opy_) == False:
      self.logger.warn(bstack1lll1l1_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡴࡦࡺࡨࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧ࠰ࠥࡸࡥࡵࡴࡼ࡭ࡳ࡭ࠠࡥࡱࡺࡲࡱࡵࡡࡥࠤፒ"))
      bstack111l1l1111_opy_ = self.bstack111lll1ll1_opy_(bstack111ll1111l_opy_, bstack111l1ll1ll_opy_)
      self.bstack111ll1l11l_opy_(bstack111ll1111l_opy_, bstack111l1ll1ll_opy_, bstack111l1l1111_opy_, bstack111l11l11l_opy_+1)
    bstack111l11l1l1_opy_ = bstack1lll1l1_opy_ (u"ࠧࡤ࠮ࠫࡂࡳࡩࡷࡩࡹ࡝࠱ࡦࡰ࡮ࠦ࡜ࡥ࠰࡟ࡨ࠰࠴࡜ࡥ࠭ࠥፓ")
    command = bstack1lll1l1_opy_ (u"࠭ࡻࡾࠢ࠰࠱ࡻ࡫ࡲࡴ࡫ࡲࡲࠬፔ").format(bstack111l1l1111_opy_)
    bstack111lll111l_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack111l11l1l1_opy_, bstack111lll111l_opy_) != None:
      return True
    else:
      self.logger.error(bstack1lll1l1_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡤࡪࡨࡧࡰࠦࡦࡢ࡫࡯ࡩࡩࠨፕ"))
      bstack111l1l1111_opy_ = self.bstack111lll1ll1_opy_(bstack111ll1111l_opy_, bstack111l1ll1ll_opy_)
      self.bstack111ll1l11l_opy_(bstack111ll1111l_opy_, bstack111l1ll1ll_opy_, bstack111l1l1111_opy_, bstack111l11l11l_opy_+1)
  def bstack111l11l1ll_opy_(self, bstack111ll1llll_opy_, bstack111l1ll1ll_opy_):
    try:
      working_dir = os.path.dirname(bstack111ll1llll_opy_)
      shutil.unpack_archive(bstack111ll1llll_opy_, working_dir)
      bstack111l1l1111_opy_ = os.path.join(working_dir, bstack111l1ll1ll_opy_)
      os.chmod(bstack111l1l1111_opy_, 0o755)
      return bstack111l1l1111_opy_
    except Exception as e:
      self.logger.error(bstack1lll1l1_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡺࡴࡺࡪࡲࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠤፖ"))
  def bstack111l1ll11l_opy_(self):
    try:
      percy = str(self.config.get(bstack1lll1l1_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨፗ"), bstack1lll1l1_opy_ (u"ࠥࡪࡦࡲࡳࡦࠤፘ"))).lower()
      if percy != bstack1lll1l1_opy_ (u"ࠦࡹࡸࡵࡦࠤፙ"):
        return False
      self.bstack1llll111ll_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack1lll1l1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡦࡨࡸࡪࡩࡴࠡࡲࡨࡶࡨࡿࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢፚ").format(e))
  def bstack111l1llll1_opy_(self):
    try:
      bstack111l1llll1_opy_ = str(self.config.get(bstack1lll1l1_opy_ (u"࠭ࡰࡦࡴࡦࡽࡈࡧࡰࡵࡷࡵࡩࡒࡵࡤࡦࠩ፛"), bstack1lll1l1_opy_ (u"ࠢࡢࡷࡷࡳࠧ፜"))).lower()
      return bstack111l1llll1_opy_
    except Exception as e:
      self.logger.error(bstack1lll1l1_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩ࡫ࡴࡦࡥࡷࠤࡵ࡫ࡲࡤࡻࠣࡧࡦࡶࡴࡶࡴࡨࠤࡲࡵࡤࡦ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤ፝").format(e))
  def init(self, bstack1l111l1l1_opy_, config, logger):
    self.bstack1l111l1l1_opy_ = bstack1l111l1l1_opy_
    self.config = config
    self.logger = logger
    if not self.bstack111l1ll11l_opy_():
      return
    self.bstack111l11l111_opy_ = config.get(bstack1lll1l1_opy_ (u"ࠩࡳࡩࡷࡩࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ፞"), {})
    self.bstack111ll1ll11_opy_ = config.get(bstack1lll1l1_opy_ (u"ࠪࡴࡪࡸࡣࡺࡅࡤࡴࡹࡻࡲࡦࡏࡲࡨࡪ࠭፟"), bstack1lll1l1_opy_ (u"ࠦࡦࡻࡴࡰࠤ፠"))
    try:
      bstack111ll1111l_opy_, bstack111l1ll1ll_opy_ = self.bstack111lll1lll_opy_()
      bstack111l1l1111_opy_, bstack111ll11l1l_opy_ = self.bstack111l11llll_opy_(bstack111ll1111l_opy_, bstack111l1ll1ll_opy_)
      if bstack111ll11l1l_opy_:
        self.binary_path = bstack111l1l1111_opy_
        thread = Thread(target=self.bstack111lll11ll_opy_)
        thread.start()
      else:
        self.bstack111ll111ll_opy_ = True
        self.logger.error(bstack1lll1l1_opy_ (u"ࠧࡏ࡮ࡷࡣ࡯࡭ࡩࠦࡰࡦࡴࡦࡽࠥࡶࡡࡵࡪࠣࡪࡴࡻ࡮ࡥࠢ࠰ࠤࢀࢃࠬࠡࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡔࡪࡸࡣࡺࠤ፡").format(bstack111l1l1111_opy_))
    except Exception as e:
      self.logger.error(bstack1lll1l1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡲࡨࡶࡨࡿࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢ።").format(e))
  def bstack111l11ll11_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack1lll1l1_opy_ (u"ࠧ࡭ࡱࡪࠫ፣"), bstack1lll1l1_opy_ (u"ࠨࡲࡨࡶࡨࡿ࠮࡭ࡱࡪࠫ፤"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack1lll1l1_opy_ (u"ࠤࡓࡹࡸ࡮ࡩ࡯ࡩࠣࡴࡪࡸࡣࡺࠢ࡯ࡳ࡬ࡹࠠࡢࡶࠣࡿࢂࠨ፥").format(logfile))
      self.bstack111llll1l1_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack1lll1l1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡦࡶࠣࡴࡪࡸࡣࡺࠢ࡯ࡳ࡬ࠦࡰࡢࡶ࡫࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦ፦").format(e))
  def bstack111lll11ll_opy_(self):
    bstack111lll1l11_opy_ = self.bstack111l1l1l11_opy_()
    if bstack111lll1l11_opy_ == None:
      self.bstack111ll111ll_opy_ = True
      self.logger.error(bstack1lll1l1_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡸࡴࡱࡥ࡯ࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨ࠱ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡲࡨࡶࡨࡿࠢ፧"))
      return False
    command_args = [bstack1lll1l1_opy_ (u"ࠧࡧࡰࡱ࠼ࡨࡼࡪࡩ࠺ࡴࡶࡤࡶࡹࠨ፨") if self.bstack1l111l1l1_opy_ else bstack1lll1l1_opy_ (u"࠭ࡥࡹࡧࡦ࠾ࡸࡺࡡࡳࡶࠪ፩")]
    bstack111ll111l1_opy_ = self.bstack111l111lll_opy_()
    if bstack111ll111l1_opy_ != None:
      command_args.append(bstack1lll1l1_opy_ (u"ࠢ࠮ࡥࠣࡿࢂࠨ፪").format(bstack111ll111l1_opy_))
    env = os.environ.copy()
    env[bstack1lll1l1_opy_ (u"ࠣࡒࡈࡖࡈ࡟࡟ࡕࡑࡎࡉࡓࠨ፫")] = bstack111lll1l11_opy_
    bstack111ll11l11_opy_ = [self.binary_path]
    self.bstack111l11ll11_opy_()
    self.bstack111llll1ll_opy_ = self.bstack111l1ll111_opy_(bstack111ll11l11_opy_ + command_args, env)
    self.logger.debug(bstack1lll1l1_opy_ (u"ࠤࡖࡸࡦࡸࡴࡪࡰࡪࠤࡍ࡫ࡡ࡭ࡶ࡫ࠤࡈ࡮ࡥࡤ࡭ࠥ፬"))
    bstack111l11l11l_opy_ = 0
    while self.bstack111llll1ll_opy_.poll() == None:
      bstack111lll11l1_opy_ = self.bstack111l1l1l1l_opy_()
      if bstack111lll11l1_opy_:
        self.logger.debug(bstack1lll1l1_opy_ (u"ࠥࡌࡪࡧ࡬ࡵࡪࠣࡇ࡭࡫ࡣ࡬ࠢࡶࡹࡨࡩࡥࡴࡵࡩࡹࡱࠨ፭"))
        self.bstack111ll1l1ll_opy_ = True
        return True
      bstack111l11l11l_opy_ += 1
      self.logger.debug(bstack1lll1l1_opy_ (u"ࠦࡍ࡫ࡡ࡭ࡶ࡫ࠤࡈ࡮ࡥࡤ࡭ࠣࡖࡪࡺࡲࡺࠢ࠰ࠤࢀࢃࠢ፮").format(bstack111l11l11l_opy_))
      time.sleep(2)
    self.logger.error(bstack1lll1l1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡱࡧࡵࡧࡾ࠲ࠠࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠦࡆࡢ࡫࡯ࡩࡩࠦࡡࡧࡶࡨࡶࠥࢁࡽࠡࡣࡷࡸࡪࡳࡰࡵࡵࠥ፯").format(bstack111l11l11l_opy_))
    self.bstack111ll111ll_opy_ = True
    return False
  def bstack111l1l1l1l_opy_(self, bstack111l11l11l_opy_ = 0):
    try:
      if bstack111l11l11l_opy_ > 10:
        return False
      bstack111l1l1lll_opy_ = os.environ.get(bstack1lll1l1_opy_ (u"࠭ࡐࡆࡔࡆ࡝ࡤ࡙ࡅࡓࡘࡈࡖࡤࡇࡄࡅࡔࡈࡗࡘ࠭፰"), bstack1lll1l1_opy_ (u"ࠧࡩࡶࡷࡴ࠿࠵࠯࡭ࡱࡦࡥࡱ࡮࡯ࡴࡶ࠽࠹࠸࠹࠸ࠨ፱"))
      bstack111l1lll1l_opy_ = bstack111l1l1lll_opy_ + bstack11ll111l11_opy_
      response = requests.get(bstack111l1lll1l_opy_)
      return True if response.json() else False
    except:
      return False
  def bstack111l1l1l11_opy_(self):
    bstack111l1l11ll_opy_ = bstack1lll1l1_opy_ (u"ࠨࡣࡳࡴࠬ፲") if self.bstack1l111l1l1_opy_ else bstack1lll1l1_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ፳")
    bstack11l11lllll_opy_ = bstack1lll1l1_opy_ (u"ࠥࡥࡵ࡯࠯ࡢࡲࡳࡣࡵ࡫ࡲࡤࡻ࠲࡫ࡪࡺ࡟ࡱࡴࡲ࡮ࡪࡩࡴࡠࡶࡲ࡯ࡪࡴ࠿࡯ࡣࡰࡩࡂࢁࡽࠧࡶࡼࡴࡪࡃࡻࡾࠤ፴").format(self.config[bstack1lll1l1_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩ፵")], bstack111l1l11ll_opy_)
    uri = bstack1llll11ll_opy_(bstack11l11lllll_opy_)
    try:
      response = bstack1ll1ll1lll_opy_(bstack1lll1l1_opy_ (u"ࠬࡍࡅࡕࠩ፶"), uri, {}, {bstack1lll1l1_opy_ (u"࠭ࡡࡶࡶ࡫ࠫ፷"): (self.config[bstack1lll1l1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ፸")], self.config[bstack1lll1l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ፹")])})
      if response.status_code == 200:
        bstack111lll1l1l_opy_ = response.json()
        if bstack1lll1l1_opy_ (u"ࠤࡷࡳࡰ࡫࡮ࠣ፺") in bstack111lll1l1l_opy_:
          return bstack111lll1l1l_opy_[bstack1lll1l1_opy_ (u"ࠥࡸࡴࡱࡥ࡯ࠤ፻")]
        else:
          raise bstack1lll1l1_opy_ (u"࡙ࠫࡵ࡫ࡦࡰࠣࡒࡴࡺࠠࡇࡱࡸࡲࡩࠦ࠭ࠡࡽࢀࠫ፼").format(bstack111lll1l1l_opy_)
      else:
        raise bstack1lll1l1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡨࡨࡸࡨ࡮ࠠࡱࡧࡵࡧࡾࠦࡴࡰ࡭ࡨࡲ࠱ࠦࡒࡦࡵࡳࡳࡳࡹࡥࠡࡵࡷࡥࡹࡻࡳࠡ࠯ࠣࡿࢂ࠲ࠠࡓࡧࡶࡴࡴࡴࡳࡦࠢࡅࡳࡩࡿࠠ࠮ࠢࡾࢁࠧ፽").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack1lll1l1_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡱࡧࡵࡧࡾࠦࡰࡳࡱ࡭ࡩࡨࡺࠢ፾").format(e))
  def bstack111l111lll_opy_(self):
    bstack111l1l1ll1_opy_ = os.path.join(tempfile.gettempdir(), bstack1lll1l1_opy_ (u"ࠢࡱࡧࡵࡧࡾࡉ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠥ፿"))
    try:
      if bstack1lll1l1_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩᎀ") not in self.bstack111l11l111_opy_:
        self.bstack111l11l111_opy_[bstack1lll1l1_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪᎁ")] = 2
      with open(bstack111l1l1ll1_opy_, bstack1lll1l1_opy_ (u"ࠪࡻࠬᎂ")) as fp:
        json.dump(self.bstack111l11l111_opy_, fp)
      return bstack111l1l1ll1_opy_
    except Exception as e:
      self.logger.error(bstack1lll1l1_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡤࡴࡨࡥࡹ࡫ࠠࡱࡧࡵࡧࡾࠦࡣࡰࡰࡩ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦᎃ").format(e))
  def bstack111l1ll111_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack111lll1111_opy_ == bstack1lll1l1_opy_ (u"ࠬࡽࡩ࡯ࠩᎄ"):
        bstack111ll11111_opy_ = [bstack1lll1l1_opy_ (u"࠭ࡣ࡮ࡦ࠱ࡩࡽ࡫ࠧᎅ"), bstack1lll1l1_opy_ (u"ࠧ࠰ࡥࠪᎆ")]
        cmd = bstack111ll11111_opy_ + cmd
      cmd = bstack1lll1l1_opy_ (u"ࠨࠢࠪᎇ").join(cmd)
      self.logger.debug(bstack1lll1l1_opy_ (u"ࠤࡕࡹࡳࡴࡩ࡯ࡩࠣࡿࢂࠨᎈ").format(cmd))
      with open(self.bstack111llll1l1_opy_, bstack1lll1l1_opy_ (u"ࠥࡥࠧᎉ")) as bstack111l11ll1l_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack111l11ll1l_opy_, text=True, stderr=bstack111l11ll1l_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack111ll111ll_opy_ = True
      self.logger.error(bstack1lll1l1_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡰࡦࡴࡦࡽࠥࡽࡩࡵࡪࠣࡧࡲࡪࠠ࠮ࠢࡾࢁ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯࠼ࠣࡿࢂࠨᎊ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack111ll1l1ll_opy_:
        self.logger.info(bstack1lll1l1_opy_ (u"࡙ࠧࡴࡰࡲࡳ࡭ࡳ࡭ࠠࡑࡧࡵࡧࡾࠨᎋ"))
        cmd = [self.binary_path, bstack1lll1l1_opy_ (u"ࠨࡥࡹࡧࡦ࠾ࡸࡺ࡯ࡱࠤᎌ")]
        self.bstack111l1ll111_opy_(cmd)
        self.bstack111ll1l1ll_opy_ = False
    except Exception as e:
      self.logger.error(bstack1lll1l1_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡵࡰࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡺ࡭ࡹ࡮ࠠࡤࡱࡰࡱࡦࡴࡤࠡ࠯ࠣࡿࢂ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࢀࢃࠢᎍ").format(cmd, e))
  def bstack1lllllllll_opy_(self):
    if not self.bstack1llll111ll_opy_:
      return
    try:
      bstack111llll11l_opy_ = 0
      while not self.bstack111ll1l1ll_opy_ and bstack111llll11l_opy_ < self.bstack111ll11ll1_opy_:
        if self.bstack111ll111ll_opy_:
          self.logger.info(bstack1lll1l1_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡴࡧࡷࡹࡵࠦࡦࡢ࡫࡯ࡩࡩࠨᎎ"))
          return
        time.sleep(1)
        bstack111llll11l_opy_ += 1
      os.environ[bstack1lll1l1_opy_ (u"ࠩࡓࡉࡗࡉ࡙ࡠࡄࡈࡗ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࠨᎏ")] = str(self.bstack111l1l11l1_opy_())
      self.logger.info(bstack1lll1l1_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡶࡩࡹࡻࡰࠡࡥࡲࡱࡵࡲࡥࡵࡧࡧࠦ᎐"))
    except Exception as e:
      self.logger.error(bstack1lll1l1_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡧࡷࡹࡵࠦࡰࡦࡴࡦࡽ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧ᎑").format(e))
  def bstack111l1l11l1_opy_(self):
    if self.bstack1l111l1l1_opy_:
      return
    try:
      bstack111ll1l111_opy_ = [platform[bstack1lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ᎒")].lower() for platform in self.config.get(bstack1lll1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ᎓"), [])]
      bstack111llll111_opy_ = sys.maxsize
      bstack111l1l111l_opy_ = bstack1lll1l1_opy_ (u"ࠧࠨ᎔")
      for browser in bstack111ll1l111_opy_:
        if browser in self.bstack111l1ll1l1_opy_:
          bstack111ll1lll1_opy_ = self.bstack111l1ll1l1_opy_[browser]
        if bstack111ll1lll1_opy_ < bstack111llll111_opy_:
          bstack111llll111_opy_ = bstack111ll1lll1_opy_
          bstack111l1l111l_opy_ = browser
      return bstack111l1l111l_opy_
    except Exception as e:
      self.logger.error(bstack1lll1l1_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡥࡩࡸࡺࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤ᎕").format(e))