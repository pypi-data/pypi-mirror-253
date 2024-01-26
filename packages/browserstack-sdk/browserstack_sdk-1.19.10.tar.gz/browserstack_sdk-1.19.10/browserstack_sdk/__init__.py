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
import atexit
import os
import signal
import sys
import yaml
import requests
import logging
import threading
import socket
import datetime
import string
import random
import json
import collections.abc
import re
import multiprocessing
import traceback
import copy
import tempfile
from packaging import version
from browserstack.local import Local
from urllib.parse import urlparse
from bstack_utils.constants import *
from bstack_utils.percy import *
from browserstack_sdk.bstack1l1l11l11_opy_ import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack1l111l111_opy_ import bstack1l111111_opy_
import time
import requests
def bstack11l1l1l1l_opy_():
  global CONFIG
  headers = {
        bstack1lll1l1_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩࡶ"): bstack1lll1l1_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧࡷ"),
      }
  proxies = bstack1ll1lll1l1_opy_(CONFIG, bstack1lll1l11ll_opy_)
  try:
    response = requests.get(bstack1lll1l11ll_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1llll11111_opy_ = response.json()[bstack1lll1l1_opy_ (u"ࠬ࡮ࡵࡣࡵࠪࡸ")]
      logger.debug(bstack1llll1l11l_opy_.format(response.json()))
      return bstack1llll11111_opy_
    else:
      logger.debug(bstack111ll1l11_opy_.format(bstack1lll1l1_opy_ (u"ࠨࡒࡦࡵࡳࡳࡳࡹࡥࠡࡌࡖࡓࡓࠦࡰࡢࡴࡶࡩࠥ࡫ࡲࡳࡱࡵࠤࠧࡹ")))
  except Exception as e:
    logger.debug(bstack111ll1l11_opy_.format(e))
def bstack1ll11l111l_opy_(hub_url):
  global CONFIG
  url = bstack1lll1l1_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤࡺ")+  hub_url + bstack1lll1l1_opy_ (u"ࠣ࠱ࡦ࡬ࡪࡩ࡫ࠣࡻ")
  headers = {
        bstack1lll1l1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨࡼ"): bstack1lll1l1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ࡽ"),
      }
  proxies = bstack1ll1lll1l1_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack11l1ll111_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack1lll11l1l_opy_.format(hub_url, e))
def bstack1ll1llll1l_opy_():
  try:
    global bstack111111ll_opy_
    bstack1llll11111_opy_ = bstack11l1l1l1l_opy_()
    bstack1ll1llll1_opy_ = []
    results = []
    for bstack1l1ll111_opy_ in bstack1llll11111_opy_:
      bstack1ll1llll1_opy_.append(bstack11lll1l1l_opy_(target=bstack1ll11l111l_opy_,args=(bstack1l1ll111_opy_,)))
    for t in bstack1ll1llll1_opy_:
      t.start()
    for t in bstack1ll1llll1_opy_:
      results.append(t.join())
    bstack1lll111lll_opy_ = {}
    for item in results:
      hub_url = item[bstack1lll1l1_opy_ (u"ࠫ࡭ࡻࡢࡠࡷࡵࡰࠬࡾ")]
      latency = item[bstack1lll1l1_opy_ (u"ࠬࡲࡡࡵࡧࡱࡧࡾ࠭ࡿ")]
      bstack1lll111lll_opy_[hub_url] = latency
    bstack1lllll111_opy_ = min(bstack1lll111lll_opy_, key= lambda x: bstack1lll111lll_opy_[x])
    bstack111111ll_opy_ = bstack1lllll111_opy_
    logger.debug(bstack1lllll11l_opy_.format(bstack1lllll111_opy_))
  except Exception as e:
    logger.debug(bstack1ll11ll1ll_opy_.format(e))
from bstack_utils.messages import *
from bstack_utils.config import Config
from bstack_utils.helper import bstack1ll1ll1lll_opy_, bstack1llll11ll_opy_, bstack1ll11111l_opy_, bstack11ll11111_opy_, \
  Notset, bstack1ll11lll1_opy_, \
  bstack1l1l11l1l_opy_, bstack1l1l11ll11_opy_, bstack1l1l1l1111_opy_, bstack1l1llll1l_opy_, bstack1lll1ll1_opy_, bstack1l1l11l111_opy_, \
  bstack1l1l1l1l1l_opy_, \
  bstack111ll111_opy_, bstack1ll1l11111_opy_, bstack11l1lllll_opy_, bstack1111lllll_opy_, \
  bstack1111l11l_opy_, bstack1l11l111l_opy_, bstack1l11lllll_opy_
from bstack_utils.bstack1ll1ll1l1l_opy_ import bstack11l1l111l_opy_
from bstack_utils.bstack11lllll1_opy_ import bstack11l111lll_opy_
from bstack_utils.bstack1ll111l1l_opy_ import bstack1l1l11ll_opy_, bstack1ll1111111_opy_
from bstack_utils.bstack1ll1l1l1ll_opy_ import bstack1l1ll11l_opy_
from bstack_utils.proxy import bstack1l1111l11_opy_, bstack1ll1lll1l1_opy_, bstack11lll1l11_opy_, bstack1lll1l11l1_opy_
import bstack_utils.bstack1ll1ll111_opy_ as bstack11111111l_opy_
from browserstack_sdk.bstack1ll1ll11_opy_ import *
from browserstack_sdk.bstack1l1llll11_opy_ import *
from bstack_utils.bstack1llllll11_opy_ import bstack1l1l111l11_opy_
bstack1llll111l_opy_ = bstack1lll1l1_opy_ (u"࠭ࠠࠡ࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࡠࡳࠦࠠࡪࡨࠫࡴࡦ࡭ࡥࠡ࠿ࡀࡁࠥࡼ࡯ࡪࡦࠣ࠴࠮ࠦࡻ࡝ࡰࠣࠤࠥࡺࡲࡺࡽ࡟ࡲࠥࡩ࡯࡯ࡵࡷࠤ࡫ࡹࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࡠࠬ࡬ࡳ࡝ࠩࠬ࠿ࡡࡴࠠࠡࠢࠣࠤ࡫ࡹ࠮ࡢࡲࡳࡩࡳࡪࡆࡪ࡮ࡨࡗࡾࡴࡣࠩࡤࡶࡸࡦࡩ࡫ࡠࡲࡤࡸ࡭࠲ࠠࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡲࡢ࡭ࡳࡪࡥࡹࠫࠣ࠯ࠥࠨ࠺ࠣࠢ࠮ࠤࡏ࡙ࡏࡏ࠰ࡶࡸࡷ࡯࡮ࡨ࡫ࡩࡽ࠭ࡐࡓࡐࡐ࠱ࡴࡦࡸࡳࡦࠪࠫࡥࡼࡧࡩࡵࠢࡱࡩࡼࡖࡡࡨࡧ࠵࠲ࡪࡼࡡ࡭ࡷࡤࡸࡪ࠮ࠢࠩࠫࠣࡁࡃࠦࡻࡾࠤ࠯ࠤࡡ࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡧࡦࡶࡖࡩࡸࡹࡩࡰࡰࡇࡩࡹࡧࡩ࡭ࡵࠥࢁࡡ࠭ࠩࠪࠫ࡞ࠦ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠢ࡞ࠫࠣ࠯ࠥࠨࠬ࡝࡞ࡱࠦ࠮ࡢ࡮ࠡࠢࠣࠤࢂࡩࡡࡵࡥ࡫ࠬࡪࡾࠩࡼ࡞ࡱࠤࠥࠦࠠࡾ࡞ࡱࠤࠥࢃ࡜࡯ࠢࠣ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴࠭ࢀ")
bstack1l1l1l1lll_opy_ = bstack1lll1l1_opy_ (u"ࠧ࡝ࡰ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࡡࡴࡣࡰࡰࡶࡸࠥࡨࡳࡵࡣࡦ࡯ࡤࡶࡡࡵࡪࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠹࡝࡝ࡰࡦࡳࡳࡹࡴࠡࡤࡶࡸࡦࡩ࡫ࡠࡥࡤࡴࡸࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠳ࡠࡠࡳࡩ࡯࡯ࡵࡷࠤࡵࡥࡩ࡯ࡦࡨࡼࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠳࡟࡟ࡲࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡸࡲࡩࡤࡧࠫ࠴࠱ࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠴ࠫ࡟ࡲࡨࡵ࡮ࡴࡶࠣ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫ࠡ࠿ࠣࡶࡪࡷࡵࡪࡴࡨࠬࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤࠬ࠿ࡡࡴࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮࠲ࡨ࡮ࡲࡰ࡯࡬ࡹࡲ࠴࡬ࡢࡷࡱࡧ࡭ࠦ࠽ࠡࡣࡶࡽࡳࡩࠠࠩ࡮ࡤࡹࡳࡩࡨࡐࡲࡷ࡭ࡴࡴࡳࠪࠢࡀࡂࠥࢁ࡜࡯࡮ࡨࡸࠥࡩࡡࡱࡵ࠾ࡠࡳࡺࡲࡺࠢࡾࡠࡳࡩࡡࡱࡵࠣࡁࠥࡐࡓࡐࡐ࠱ࡴࡦࡸࡳࡦࠪࡥࡷࡹࡧࡣ࡬ࡡࡦࡥࡵࡹࠩ࡝ࡰࠣࠤࢂࠦࡣࡢࡶࡦ࡬࠭࡫ࡸࠪࠢࡾࡠࡳࠦࠠࠡࠢࢀࡠࡳࠦࠠࡳࡧࡷࡹࡷࡴࠠࡢࡹࡤ࡭ࡹࠦࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮࠲ࡨ࡮ࡲࡰ࡯࡬ࡹࡲ࠴ࡣࡰࡰࡱࡩࡨࡺࠨࡼ࡞ࡱࠤࠥࠦࠠࡸࡵࡈࡲࡩࡶ࡯ࡪࡰࡷ࠾ࠥࡦࡷࡴࡵ࠽࠳࠴ࡩࡤࡱ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࡁࡦࡥࡵࡹ࠽ࠥࡽࡨࡲࡨࡵࡤࡦࡗࡕࡍࡈࡵ࡭ࡱࡱࡱࡩࡳࡺࠨࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡥࡤࡴࡸ࠯ࠩࡾࡢ࠯ࡠࡳࠦࠠࠡࠢ࠱࠲࠳ࡲࡡࡶࡰࡦ࡬ࡔࡶࡴࡪࡱࡱࡷࡡࡴࠠࠡࡿࠬࡠࡳࢃ࡜࡯࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࡠࡳ࠭ࢁ")
from ._version import __version__
bstack1ll1lll1_opy_ = None
CONFIG = {}
bstack1ll111llll_opy_ = {}
bstack1lll1ll1l1_opy_ = {}
bstack111l1llll_opy_ = None
bstack1ll11111ll_opy_ = None
bstack1lll111ll1_opy_ = None
bstack1lll1llll_opy_ = -1
bstack111111lll_opy_ = 0
bstack1l1l1ll11l_opy_ = bstack1ll1l111ll_opy_
bstack11ll11ll_opy_ = 1
bstack1l1l1lll1l_opy_ = False
bstack111l11ll1_opy_ = False
bstack1ll11l1l11_opy_ = bstack1lll1l1_opy_ (u"ࠨࠩࢂ")
bstack11l1lll11_opy_ = bstack1lll1l1_opy_ (u"ࠩࠪࢃ")
bstack1lll1111l_opy_ = False
bstack1l11ll111_opy_ = True
bstack1llllllll1_opy_ = bstack1lll1l1_opy_ (u"ࠪࠫࢄ")
bstack1l1ll1ll1_opy_ = []
bstack111111ll_opy_ = bstack1lll1l1_opy_ (u"ࠫࠬࢅ")
bstack1ll111l1ll_opy_ = False
bstack1ll1llll_opy_ = None
bstack1ll1l1lll1_opy_ = None
bstack1lll1ll11_opy_ = None
bstack11ll111l_opy_ = -1
bstack1ll111l11_opy_ = os.path.join(os.path.expanduser(bstack1lll1l1_opy_ (u"ࠬࢄࠧࢆ")), bstack1lll1l1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ࢇ"), bstack1lll1l1_opy_ (u"ࠧ࠯ࡴࡲࡦࡴࡺ࠭ࡳࡧࡳࡳࡷࡺ࠭ࡩࡧ࡯ࡴࡪࡸ࠮࡫ࡵࡲࡲࠬ࢈"))
bstack1l1l1l11l1_opy_ = 0
bstack1l1l1111l_opy_ = []
bstack1ll11l1ll1_opy_ = []
bstack111l111l1_opy_ = []
bstack1l1l1llll1_opy_ = []
bstack1lllllll1_opy_ = bstack1lll1l1_opy_ (u"ࠨࠩࢉ")
bstack1ll11l11ll_opy_ = bstack1lll1l1_opy_ (u"ࠩࠪࢊ")
bstack111lllll1_opy_ = False
bstack1llll1ll_opy_ = False
bstack1ll1l1lll_opy_ = {}
bstack11llll1l_opy_ = None
bstack1l11l1111_opy_ = None
bstack1l111l11_opy_ = None
bstack1llll1l1_opy_ = None
bstack1ll11l11l_opy_ = None
bstack1l1l11111_opy_ = None
bstack1l11111l1_opy_ = None
bstack1111lll1_opy_ = None
bstack111ll1l1l_opy_ = None
bstack1ll1l1111_opy_ = None
bstack1l1ll1l1l1_opy_ = None
bstack1l1ll11l11_opy_ = None
bstack1lll1l1l1_opy_ = None
bstack1llllll1ll_opy_ = None
bstack111l11l1_opy_ = None
bstack1lll111l11_opy_ = None
bstack11ll1l111_opy_ = None
bstack1ll111ll_opy_ = None
bstack1l1l1111l1_opy_ = None
bstack111lll111_opy_ = None
bstack1ll1111l11_opy_ = None
bstack1llll1llll_opy_ = bstack1lll1l1_opy_ (u"ࠥࠦࢋ")
logger = logging.getLogger(__name__)
logging.basicConfig(level=bstack1l1l1ll11l_opy_,
                    format=bstack1lll1l1_opy_ (u"ࠫࡡࡴࠥࠩࡣࡶࡧࡹ࡯࡭ࡦࠫࡶࠤࡠࠫࠨ࡯ࡣࡰࡩ࠮ࡹ࡝࡜ࠧࠫࡰࡪࡼࡥ࡭ࡰࡤࡱࡪ࠯ࡳ࡞ࠢ࠰ࠤࠪ࠮࡭ࡦࡵࡶࡥ࡬࡫ࠩࡴࠩࢌ"),
                    datefmt=bstack1lll1l1_opy_ (u"ࠬࠫࡈ࠻ࠧࡐ࠾࡙ࠪࠧࢍ"),
                    stream=sys.stdout)
bstack11l1l11l_opy_ = Config.bstack1lllll11l1_opy_()
percy = bstack1111ll111_opy_()
bstack1llll111ll_opy_ = bstack1l111111_opy_()
def bstack1l1l11l1_opy_():
  global CONFIG
  global bstack1l1l1ll11l_opy_
  if bstack1lll1l1_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨࢎ") in CONFIG:
    bstack1l1l1ll11l_opy_ = bstack111ll1lll_opy_[CONFIG[bstack1lll1l1_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩ࢏")]]
    logging.getLogger().setLevel(bstack1l1l1ll11l_opy_)
def bstack1ll1ll1l11_opy_():
  global CONFIG
  global bstack111lllll1_opy_
  global bstack11l1l11l_opy_
  bstack1l1ll1ll_opy_ = bstack1l1ll1l11l_opy_(CONFIG)
  if (bstack1lll1l1_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ࢐") in bstack1l1ll1ll_opy_ and str(bstack1l1ll1ll_opy_[bstack1lll1l1_opy_ (u"ࠩࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ࢑")]).lower() == bstack1lll1l1_opy_ (u"ࠪࡸࡷࡻࡥࠨ࢒")):
    bstack111lllll1_opy_ = True
  bstack11l1l11l_opy_.bstack1lll11111l_opy_(bstack1l1ll1ll_opy_.get(bstack1lll1l1_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨ࢓"), False))
def bstack1ll111111l_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack11llll1ll_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack11l11l11_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack1lll1l1_opy_ (u"ࠧ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡩ࡯࡯ࡨ࡬࡫࡫࡯࡬ࡦࠤ࢔") == args[i].lower() or bstack1lll1l1_opy_ (u"ࠨ࠭࠮ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡱࡪ࡮࡭ࠢ࢕") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack1llllllll1_opy_
      bstack1llllllll1_opy_ += bstack1lll1l1_opy_ (u"ࠧ࠮࠯ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡄࡱࡱࡪ࡮࡭ࡆࡪ࡮ࡨࠤࠬ࢖") + path
      return path
  return None
bstack1l1l111ll1_opy_ = re.compile(bstack1lll1l1_opy_ (u"ࡳࠤ࠱࠮ࡄࡢࠤࡼࠪ࠱࠮ࡄ࠯ࡽ࠯ࠬࡂࠦࢗ"))
def bstack1l11lll1_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack1l1l111ll1_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack1lll1l1_opy_ (u"ࠤࠧࡿࠧ࢘") + group + bstack1lll1l1_opy_ (u"ࠥࢁ࢙ࠧ"), os.environ.get(group))
  return value
def bstack1ll1l1l1l1_opy_():
  bstack11l1l111_opy_ = bstack11l11l11_opy_()
  if bstack11l1l111_opy_ and os.path.exists(os.path.abspath(bstack11l1l111_opy_)):
    fileName = bstack11l1l111_opy_
  if bstack1lll1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࡢࡊࡎࡒࡅࠨ࢚") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack1lll1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡕࡎࡇࡋࡊࡣࡋࡏࡌࡆ࢛ࠩ")])) and not bstack1lll1l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡒࡦࡳࡥࠨ࢜") in locals():
    fileName = os.environ[bstack1lll1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌࡥࡆࡊࡎࡈࠫ࢝")]
  if bstack1lll1l1_opy_ (u"ࠨࡨ࡬ࡰࡪࡔࡡ࡮ࡧࠪ࢞") in locals():
    bstack11l1_opy_ = os.path.abspath(fileName)
  else:
    bstack11l1_opy_ = bstack1lll1l1_opy_ (u"ࠩࠪ࢟")
  bstack11lllll1l_opy_ = os.getcwd()
  bstack1ll11llll_opy_ = bstack1lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭ࢠ")
  bstack111llll11_opy_ = bstack1lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡦࡳ࡬ࠨࢡ")
  while (not os.path.exists(bstack11l1_opy_)) and bstack11lllll1l_opy_ != bstack1lll1l1_opy_ (u"ࠧࠨࢢ"):
    bstack11l1_opy_ = os.path.join(bstack11lllll1l_opy_, bstack1ll11llll_opy_)
    if not os.path.exists(bstack11l1_opy_):
      bstack11l1_opy_ = os.path.join(bstack11lllll1l_opy_, bstack111llll11_opy_)
    if bstack11lllll1l_opy_ != os.path.dirname(bstack11lllll1l_opy_):
      bstack11lllll1l_opy_ = os.path.dirname(bstack11lllll1l_opy_)
    else:
      bstack11lllll1l_opy_ = bstack1lll1l1_opy_ (u"ࠨࠢࢣ")
  if not os.path.exists(bstack11l1_opy_):
    bstack1ll1ll1ll1_opy_(
      bstack11ll1l1l_opy_.format(os.getcwd()))
  try:
    with open(bstack11l1_opy_, bstack1lll1l1_opy_ (u"ࠧࡳࠩࢤ")) as stream:
      yaml.add_implicit_resolver(bstack1lll1l1_opy_ (u"ࠣࠣࡳࡥࡹ࡮ࡥࡹࠤࢥ"), bstack1l1l111ll1_opy_)
      yaml.add_constructor(bstack1lll1l1_opy_ (u"ࠤࠤࡴࡦࡺࡨࡦࡺࠥࢦ"), bstack1l11lll1_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      return config
  except:
    with open(bstack11l1_opy_, bstack1lll1l1_opy_ (u"ࠪࡶࠬࢧ")) as stream:
      try:
        config = yaml.safe_load(stream)
        return config
      except yaml.YAMLError as exc:
        bstack1ll1ll1ll1_opy_(bstack1lllll1111_opy_.format(str(exc)))
def bstack1l11l1lll_opy_(config):
  bstack11lll11ll_opy_ = bstack1ll1l1l1_opy_(config)
  for option in list(bstack11lll11ll_opy_):
    if option.lower() in bstack1ll1l1l11_opy_ and option != bstack1ll1l1l11_opy_[option.lower()]:
      bstack11lll11ll_opy_[bstack1ll1l1l11_opy_[option.lower()]] = bstack11lll11ll_opy_[option]
      del bstack11lll11ll_opy_[option]
  return config
def bstack1ll1l1ll_opy_():
  global bstack1lll1ll1l1_opy_
  for key, bstack11l1l1l11_opy_ in bstack11l1111l1_opy_.items():
    if isinstance(bstack11l1l1l11_opy_, list):
      for var in bstack11l1l1l11_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack1lll1ll1l1_opy_[key] = os.environ[var]
          break
    elif bstack11l1l1l11_opy_ in os.environ and os.environ[bstack11l1l1l11_opy_] and str(os.environ[bstack11l1l1l11_opy_]).strip():
      bstack1lll1ll1l1_opy_[key] = os.environ[bstack11l1l1l11_opy_]
  if bstack1lll1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ࢨ") in os.environ:
    bstack1lll1ll1l1_opy_[bstack1lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩࢩ")] = {}
    bstack1lll1ll1l1_opy_[bstack1lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪࢪ")][bstack1lll1l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩࢫ")] = os.environ[bstack1lll1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪࢬ")]
def bstack1lll1lll_opy_():
  global bstack1ll111llll_opy_
  global bstack1llllllll1_opy_
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) and bstack1lll1l1_opy_ (u"ࠩ࠰࠱ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬࢭ").lower() == val.lower():
      bstack1ll111llll_opy_[bstack1lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧࢮ")] = {}
      bstack1ll111llll_opy_[bstack1lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨࢯ")][bstack1lll1l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧࢰ")] = sys.argv[idx + 1]
      del sys.argv[idx:idx + 2]
      break
  for key, bstack1l1lllll1_opy_ in bstack1lll1l1l_opy_.items():
    if isinstance(bstack1l1lllll1_opy_, list):
      for idx, val in enumerate(sys.argv):
        for var in bstack1l1lllll1_opy_:
          if idx < len(sys.argv) and bstack1lll1l1_opy_ (u"࠭࠭࠮ࠩࢱ") + var.lower() == val.lower() and not key in bstack1ll111llll_opy_:
            bstack1ll111llll_opy_[key] = sys.argv[idx + 1]
            bstack1llllllll1_opy_ += bstack1lll1l1_opy_ (u"ࠧࠡ࠯࠰ࠫࢲ") + var + bstack1lll1l1_opy_ (u"ࠨࠢࠪࢳ") + sys.argv[idx + 1]
            del sys.argv[idx:idx + 2]
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx < len(sys.argv) and bstack1lll1l1_opy_ (u"ࠩ࠰࠱ࠬࢴ") + bstack1l1lllll1_opy_.lower() == val.lower() and not key in bstack1ll111llll_opy_:
          bstack1ll111llll_opy_[key] = sys.argv[idx + 1]
          bstack1llllllll1_opy_ += bstack1lll1l1_opy_ (u"ࠪࠤ࠲࠳ࠧࢵ") + bstack1l1lllll1_opy_ + bstack1lll1l1_opy_ (u"ࠫࠥ࠭ࢶ") + sys.argv[idx + 1]
          del sys.argv[idx:idx + 2]
def bstack1l1111111_opy_(config):
  bstack111ll1ll_opy_ = config.keys()
  for bstack11ll1ll11_opy_, bstack11l1l11ll_opy_ in bstack11l1ll1l_opy_.items():
    if bstack11l1l11ll_opy_ in bstack111ll1ll_opy_:
      config[bstack11ll1ll11_opy_] = config[bstack11l1l11ll_opy_]
      del config[bstack11l1l11ll_opy_]
  for bstack11ll1ll11_opy_, bstack11l1l11ll_opy_ in bstack11l1ll1l1_opy_.items():
    if isinstance(bstack11l1l11ll_opy_, list):
      for bstack11l11l1l1_opy_ in bstack11l1l11ll_opy_:
        if bstack11l11l1l1_opy_ in bstack111ll1ll_opy_:
          config[bstack11ll1ll11_opy_] = config[bstack11l11l1l1_opy_]
          del config[bstack11l11l1l1_opy_]
          break
    elif bstack11l1l11ll_opy_ in bstack111ll1ll_opy_:
      config[bstack11ll1ll11_opy_] = config[bstack11l1l11ll_opy_]
      del config[bstack11l1l11ll_opy_]
  for bstack11l11l1l1_opy_ in list(config):
    for bstack1l1111ll_opy_ in bstack1l11l1l1l_opy_:
      if bstack11l11l1l1_opy_.lower() == bstack1l1111ll_opy_.lower() and bstack11l11l1l1_opy_ != bstack1l1111ll_opy_:
        config[bstack1l1111ll_opy_] = config[bstack11l11l1l1_opy_]
        del config[bstack11l11l1l1_opy_]
  bstack1l1l1ll1l1_opy_ = []
  if bstack1lll1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨࢷ") in config:
    bstack1l1l1ll1l1_opy_ = config[bstack1lll1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩࢸ")]
  for platform in bstack1l1l1ll1l1_opy_:
    for bstack11l11l1l1_opy_ in list(platform):
      for bstack1l1111ll_opy_ in bstack1l11l1l1l_opy_:
        if bstack11l11l1l1_opy_.lower() == bstack1l1111ll_opy_.lower() and bstack11l11l1l1_opy_ != bstack1l1111ll_opy_:
          platform[bstack1l1111ll_opy_] = platform[bstack11l11l1l1_opy_]
          del platform[bstack11l11l1l1_opy_]
  for bstack11ll1ll11_opy_, bstack11l1l11ll_opy_ in bstack11l1ll1l1_opy_.items():
    for platform in bstack1l1l1ll1l1_opy_:
      if isinstance(bstack11l1l11ll_opy_, list):
        for bstack11l11l1l1_opy_ in bstack11l1l11ll_opy_:
          if bstack11l11l1l1_opy_ in platform:
            platform[bstack11ll1ll11_opy_] = platform[bstack11l11l1l1_opy_]
            del platform[bstack11l11l1l1_opy_]
            break
      elif bstack11l1l11ll_opy_ in platform:
        platform[bstack11ll1ll11_opy_] = platform[bstack11l1l11ll_opy_]
        del platform[bstack11l1l11ll_opy_]
  for bstack1llll1111l_opy_ in bstack111l1l1l1_opy_:
    if bstack1llll1111l_opy_ in config:
      if not bstack111l1l1l1_opy_[bstack1llll1111l_opy_] in config:
        config[bstack111l1l1l1_opy_[bstack1llll1111l_opy_]] = {}
      config[bstack111l1l1l1_opy_[bstack1llll1111l_opy_]].update(config[bstack1llll1111l_opy_])
      del config[bstack1llll1111l_opy_]
  for platform in bstack1l1l1ll1l1_opy_:
    for bstack1llll1111l_opy_ in bstack111l1l1l1_opy_:
      if bstack1llll1111l_opy_ in list(platform):
        if not bstack111l1l1l1_opy_[bstack1llll1111l_opy_] in platform:
          platform[bstack111l1l1l1_opy_[bstack1llll1111l_opy_]] = {}
        platform[bstack111l1l1l1_opy_[bstack1llll1111l_opy_]].update(platform[bstack1llll1111l_opy_])
        del platform[bstack1llll1111l_opy_]
  config = bstack1l11l1lll_opy_(config)
  return config
def bstack111l11lll_opy_(config):
  global bstack11l1lll11_opy_
  if bstack1lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫࢹ") in config and str(config[bstack1lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬࢺ")]).lower() != bstack1lll1l1_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨࢻ"):
    if not bstack1lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧࢼ") in config:
      config[bstack1lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨࢽ")] = {}
    if not bstack1lll1l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧࢾ") in config[bstack1lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪࢿ")]:
      bstack11llll1l1_opy_ = datetime.datetime.now()
      bstack111l1111l_opy_ = bstack11llll1l1_opy_.strftime(bstack1lll1l1_opy_ (u"ࠧࠦࡦࡢࠩࡧࡥࠥࡉࠧࡐࠫࣀ"))
      hostname = socket.gethostname()
      bstack11lllllll_opy_ = bstack1lll1l1_opy_ (u"ࠨࠩࣁ").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack1lll1l1_opy_ (u"ࠩࡾࢁࡤࢁࡽࡠࡽࢀࠫࣂ").format(bstack111l1111l_opy_, hostname, bstack11lllllll_opy_)
      config[bstack1lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧࣃ")][bstack1lll1l1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ࣄ")] = identifier
    bstack11l1lll11_opy_ = config[bstack1lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩࣅ")][bstack1lll1l1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨࣆ")]
  return config
def bstack11l11l111_opy_():
  bstack1ll11l1l_opy_ =  bstack1l1llll1l_opy_()[bstack1lll1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷ࠭ࣇ")]
  return bstack1ll11l1l_opy_ if bstack1ll11l1l_opy_ else -1
def bstack1ll1l1ll1l_opy_(bstack1ll11l1l_opy_):
  global CONFIG
  if not bstack1lll1l1_opy_ (u"ࠨࠦࡾࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࡿࠪࣈ") in CONFIG[bstack1lll1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫࣉ")]:
    return
  CONFIG[bstack1lll1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ࣊")] = CONFIG[bstack1lll1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭࣋")].replace(
    bstack1lll1l1_opy_ (u"ࠬࠪࡻࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࢃࠧ࣌"),
    str(bstack1ll11l1l_opy_)
  )
def bstack1111l111l_opy_():
  global CONFIG
  if not bstack1lll1l1_opy_ (u"࠭ࠤࡼࡆࡄࡘࡊࡥࡔࡊࡏࡈࢁࠬ࣍") in CONFIG[bstack1lll1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ࣎")]:
    return
  bstack11llll1l1_opy_ = datetime.datetime.now()
  bstack111l1111l_opy_ = bstack11llll1l1_opy_.strftime(bstack1lll1l1_opy_ (u"ࠨࠧࡧ࠱ࠪࡨ࠭ࠦࡊ࠽ࠩࡒ࣏࠭"))
  CONFIG[bstack1lll1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵ࣐ࠫ")] = CONFIG[bstack1lll1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶ࣑ࠬ")].replace(
    bstack1lll1l1_opy_ (u"ࠫࠩࢁࡄࡂࡖࡈࡣ࡙ࡏࡍࡆࡿ࣒ࠪ"),
    bstack111l1111l_opy_
  )
def bstack111l1l1l_opy_():
  global CONFIG
  if bstack1lll1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸ࣓ࠧ") in CONFIG and not bool(CONFIG[bstack1lll1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨࣔ")]):
    del CONFIG[bstack1lll1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩࣕ")]
    return
  if not bstack1lll1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࣖ") in CONFIG:
    CONFIG[bstack1lll1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫࣗ")] = bstack1lll1l1_opy_ (u"ࠪࠧࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭ࣘ")
  if bstack1lll1l1_opy_ (u"ࠫࠩࢁࡄࡂࡖࡈࡣ࡙ࡏࡍࡆࡿࠪࣙ") in CONFIG[bstack1lll1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧࣚ")]:
    bstack1111l111l_opy_()
    os.environ[bstack1lll1l1_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡥࡃࡐࡏࡅࡍࡓࡋࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪࣛ")] = CONFIG[bstack1lll1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩࣜ")]
  if not bstack1lll1l1_opy_ (u"ࠨࠦࡾࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࡿࠪࣝ") in CONFIG[bstack1lll1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫࣞ")]:
    return
  bstack1ll11l1l_opy_ = bstack1lll1l1_opy_ (u"ࠪࠫࣟ")
  bstack11llll11l_opy_ = bstack11l11l111_opy_()
  if bstack11llll11l_opy_ != -1:
    bstack1ll11l1l_opy_ = bstack1lll1l1_opy_ (u"ࠫࡈࡏࠠࠨ࣠") + str(bstack11llll11l_opy_)
  if bstack1ll11l1l_opy_ == bstack1lll1l1_opy_ (u"ࠬ࠭࣡"):
    bstack111llllll_opy_ = bstack111l11l1l_opy_(CONFIG[bstack1lll1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ࣢")])
    if bstack111llllll_opy_ != -1:
      bstack1ll11l1l_opy_ = str(bstack111llllll_opy_)
  if bstack1ll11l1l_opy_:
    bstack1ll1l1ll1l_opy_(bstack1ll11l1l_opy_)
    os.environ[bstack1lll1l1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑ࡟ࡄࡑࡐࡆࡎࡔࡅࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࣣࠫ")] = CONFIG[bstack1lll1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࣤ")]
def bstack1l1lll1lll_opy_(bstack11111ll11_opy_, bstack11ll1lll1_opy_, path):
  bstack11ll11ll1_opy_ = {
    bstack1lll1l1_opy_ (u"ࠩ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ࣥ"): bstack11ll1lll1_opy_
  }
  if os.path.exists(path):
    bstack1llll1ll1l_opy_ = json.load(open(path, bstack1lll1l1_opy_ (u"ࠪࡶࡧࣦ࠭")))
  else:
    bstack1llll1ll1l_opy_ = {}
  bstack1llll1ll1l_opy_[bstack11111ll11_opy_] = bstack11ll11ll1_opy_
  with open(path, bstack1lll1l1_opy_ (u"ࠦࡼ࠱ࠢࣧ")) as outfile:
    json.dump(bstack1llll1ll1l_opy_, outfile)
def bstack111l11l1l_opy_(bstack11111ll11_opy_):
  bstack11111ll11_opy_ = str(bstack11111ll11_opy_)
  bstack11l1llll1_opy_ = os.path.join(os.path.expanduser(bstack1lll1l1_opy_ (u"ࠬࢄࠧࣨ")), bstack1lll1l1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࣩ࠭"))
  try:
    if not os.path.exists(bstack11l1llll1_opy_):
      os.makedirs(bstack11l1llll1_opy_)
    file_path = os.path.join(os.path.expanduser(bstack1lll1l1_opy_ (u"ࠧࡿࠩ࣪")), bstack1lll1l1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ࣫"), bstack1lll1l1_opy_ (u"ࠩ࠱ࡦࡺ࡯࡬ࡥ࠯ࡱࡥࡲ࡫࠭ࡤࡣࡦ࡬ࡪ࠴ࡪࡴࡱࡱࠫ࣬"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack1lll1l1_opy_ (u"ࠪࡻ࣭ࠬ")):
        pass
      with open(file_path, bstack1lll1l1_opy_ (u"ࠦࡼ࠱࣮ࠢ")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack1lll1l1_opy_ (u"ࠬࡸ࣯ࠧ")) as bstack11111llll_opy_:
      bstack1llll1lll_opy_ = json.load(bstack11111llll_opy_)
    if bstack11111ll11_opy_ in bstack1llll1lll_opy_:
      bstack1ll1ll11l_opy_ = bstack1llll1lll_opy_[bstack11111ll11_opy_][bstack1lll1l1_opy_ (u"࠭ࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࣰࠪ")]
      bstack1l1lll1ll1_opy_ = int(bstack1ll1ll11l_opy_) + 1
      bstack1l1lll1lll_opy_(bstack11111ll11_opy_, bstack1l1lll1ll1_opy_, file_path)
      return bstack1l1lll1ll1_opy_
    else:
      bstack1l1lll1lll_opy_(bstack11111ll11_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack1lll1l11l_opy_.format(str(e)))
    return -1
def bstack1111l1l1_opy_(config):
  if not config[bstack1lll1l1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࣱࠩ")] or not config[bstack1lll1l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࣲࠫ")]:
    return True
  else:
    return False
def bstack11llllll1_opy_(config, index=0):
  global bstack1lll1111l_opy_
  bstack1ll111l1l1_opy_ = {}
  caps = bstack1l1lllll11_opy_ + bstack1l11l111_opy_
  if bstack1lll1111l_opy_:
    caps += bstack1ll1111ll_opy_
  for key in config:
    if key in caps + [bstack1lll1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬࣳ")]:
      continue
    bstack1ll111l1l1_opy_[key] = config[key]
  if bstack1lll1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ࣴ") in config:
    for bstack1llll111l1_opy_ in config[bstack1lll1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧࣵ")][index]:
      if bstack1llll111l1_opy_ in caps + [bstack1lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࣶࠪ"), bstack1lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧࣷ")]:
        continue
      bstack1ll111l1l1_opy_[bstack1llll111l1_opy_] = config[bstack1lll1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪࣸ")][index][bstack1llll111l1_opy_]
  bstack1ll111l1l1_opy_[bstack1lll1l1_opy_ (u"ࠨࡪࡲࡷࡹࡔࡡ࡮ࡧࣹࠪ")] = socket.gethostname()
  if bstack1lll1l1_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࣺࠪ") in bstack1ll111l1l1_opy_:
    del (bstack1ll111l1l1_opy_[bstack1lll1l1_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫࣻ")])
  return bstack1ll111l1l1_opy_
def bstack1llllll111_opy_(config):
  global bstack1lll1111l_opy_
  bstack1lll111ll_opy_ = {}
  caps = bstack1l11l111_opy_
  if bstack1lll1111l_opy_:
    caps += bstack1ll1111ll_opy_
  for key in caps:
    if key in config:
      bstack1lll111ll_opy_[key] = config[key]
  return bstack1lll111ll_opy_
def bstack1l1ll11ll1_opy_(bstack1ll111l1l1_opy_, bstack1lll111ll_opy_):
  bstack1ll11l1l1l_opy_ = {}
  for key in bstack1ll111l1l1_opy_.keys():
    if key in bstack11l1ll1l_opy_:
      bstack1ll11l1l1l_opy_[bstack11l1ll1l_opy_[key]] = bstack1ll111l1l1_opy_[key]
    else:
      bstack1ll11l1l1l_opy_[key] = bstack1ll111l1l1_opy_[key]
  for key in bstack1lll111ll_opy_:
    if key in bstack11l1ll1l_opy_:
      bstack1ll11l1l1l_opy_[bstack11l1ll1l_opy_[key]] = bstack1lll111ll_opy_[key]
    else:
      bstack1ll11l1l1l_opy_[key] = bstack1lll111ll_opy_[key]
  return bstack1ll11l1l1l_opy_
def bstack1l1llllll1_opy_(config, index=0):
  global bstack1lll1111l_opy_
  config = copy.deepcopy(config)
  caps = {}
  bstack1lll111ll_opy_ = bstack1llllll111_opy_(config)
  bstack1l1l1l1l11_opy_ = bstack1l11l111_opy_
  bstack1l1l1l1l11_opy_ += bstack1ll1l11l1l_opy_
  if bstack1lll1111l_opy_:
    bstack1l1l1l1l11_opy_ += bstack1ll1111ll_opy_
  if bstack1lll1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧࣼ") in config:
    if bstack1lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪࣽ") in config[bstack1lll1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩࣾ")][index]:
      caps[bstack1lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬࣿ")] = config[bstack1lll1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫऀ")][index][bstack1lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧँ")]
    if bstack1lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫं") in config[bstack1lll1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧः")][index]:
      caps[bstack1lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ऄ")] = str(config[bstack1lll1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩअ")][index][bstack1lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨआ")])
    bstack1ll11ll11l_opy_ = {}
    for bstack1ll1111l_opy_ in bstack1l1l1l1l11_opy_:
      if bstack1ll1111l_opy_ in config[bstack1lll1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫइ")][index]:
        if bstack1ll1111l_opy_ == bstack1lll1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫई"):
          try:
            bstack1ll11ll11l_opy_[bstack1ll1111l_opy_] = str(config[bstack1lll1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭उ")][index][bstack1ll1111l_opy_] * 1.0)
          except:
            bstack1ll11ll11l_opy_[bstack1ll1111l_opy_] = str(config[bstack1lll1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧऊ")][index][bstack1ll1111l_opy_])
        else:
          bstack1ll11ll11l_opy_[bstack1ll1111l_opy_] = config[bstack1lll1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨऋ")][index][bstack1ll1111l_opy_]
        del (config[bstack1lll1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩऌ")][index][bstack1ll1111l_opy_])
    bstack1lll111ll_opy_ = update(bstack1lll111ll_opy_, bstack1ll11ll11l_opy_)
  bstack1ll111l1l1_opy_ = bstack11llllll1_opy_(config, index)
  for bstack11l11l1l1_opy_ in bstack1l11l111_opy_ + [bstack1lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬऍ"), bstack1lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩऎ")]:
    if bstack11l11l1l1_opy_ in bstack1ll111l1l1_opy_:
      bstack1lll111ll_opy_[bstack11l11l1l1_opy_] = bstack1ll111l1l1_opy_[bstack11l11l1l1_opy_]
      del (bstack1ll111l1l1_opy_[bstack11l11l1l1_opy_])
  if bstack1ll11lll1_opy_(config):
    bstack1ll111l1l1_opy_[bstack1lll1l1_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩए")] = True
    caps.update(bstack1lll111ll_opy_)
    caps[bstack1lll1l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫऐ")] = bstack1ll111l1l1_opy_
  else:
    bstack1ll111l1l1_opy_[bstack1lll1l1_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫऑ")] = False
    caps.update(bstack1l1ll11ll1_opy_(bstack1ll111l1l1_opy_, bstack1lll111ll_opy_))
    if bstack1lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪऒ") in caps:
      caps[bstack1lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧओ")] = caps[bstack1lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬऔ")]
      del (caps[bstack1lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭क")])
    if bstack1lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪख") in caps:
      caps[bstack1lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬग")] = caps[bstack1lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬघ")]
      del (caps[bstack1lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ङ")])
  return caps
def bstack1lll11111_opy_():
  global bstack111111ll_opy_
  if bstack11llll1ll_opy_() <= version.parse(bstack1lll1l1_opy_ (u"࠭࠳࠯࠳࠶࠲࠵࠭च")):
    if bstack111111ll_opy_ != bstack1lll1l1_opy_ (u"ࠧࠨछ"):
      return bstack1lll1l1_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤज") + bstack111111ll_opy_ + bstack1lll1l1_opy_ (u"ࠤ࠽࠼࠵࠵ࡷࡥ࠱࡫ࡹࡧࠨझ")
    return bstack1l1lllll_opy_
  if bstack111111ll_opy_ != bstack1lll1l1_opy_ (u"ࠪࠫञ"):
    return bstack1lll1l1_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨट") + bstack111111ll_opy_ + bstack1lll1l1_opy_ (u"ࠧ࠵ࡷࡥ࠱࡫ࡹࡧࠨठ")
  return bstack111l1lll1_opy_
def bstack111l1lll_opy_(options):
  return hasattr(options, bstack1lll1l1_opy_ (u"࠭ࡳࡦࡶࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹࡿࠧड"))
def update(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = update(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack1l11llll1_opy_(options, bstack1ll11111l1_opy_):
  for bstack1ll1l11ll1_opy_ in bstack1ll11111l1_opy_:
    if bstack1ll1l11ll1_opy_ in [bstack1lll1l1_opy_ (u"ࠧࡢࡴࡪࡷࠬढ"), bstack1lll1l1_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬण")]:
      continue
    if bstack1ll1l11ll1_opy_ in options._experimental_options:
      options._experimental_options[bstack1ll1l11ll1_opy_] = update(options._experimental_options[bstack1ll1l11ll1_opy_],
                                                         bstack1ll11111l1_opy_[bstack1ll1l11ll1_opy_])
    else:
      options.add_experimental_option(bstack1ll1l11ll1_opy_, bstack1ll11111l1_opy_[bstack1ll1l11ll1_opy_])
  if bstack1lll1l1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧत") in bstack1ll11111l1_opy_:
    for arg in bstack1ll11111l1_opy_[bstack1lll1l1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨथ")]:
      options.add_argument(arg)
    del (bstack1ll11111l1_opy_[bstack1lll1l1_opy_ (u"ࠫࡦࡸࡧࡴࠩद")])
  if bstack1lll1l1_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩध") in bstack1ll11111l1_opy_:
    for ext in bstack1ll11111l1_opy_[bstack1lll1l1_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪन")]:
      options.add_extension(ext)
    del (bstack1ll11111l1_opy_[bstack1lll1l1_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫऩ")])
def bstack111111l1_opy_(options, bstack1ll1l111l1_opy_):
  if bstack1lll1l1_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧप") in bstack1ll1l111l1_opy_:
    for bstack1l1llll1l1_opy_ in bstack1ll1l111l1_opy_[bstack1lll1l1_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨफ")]:
      if bstack1l1llll1l1_opy_ in options._preferences:
        options._preferences[bstack1l1llll1l1_opy_] = update(options._preferences[bstack1l1llll1l1_opy_], bstack1ll1l111l1_opy_[bstack1lll1l1_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩब")][bstack1l1llll1l1_opy_])
      else:
        options.set_preference(bstack1l1llll1l1_opy_, bstack1ll1l111l1_opy_[bstack1lll1l1_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪभ")][bstack1l1llll1l1_opy_])
  if bstack1lll1l1_opy_ (u"ࠬࡧࡲࡨࡵࠪम") in bstack1ll1l111l1_opy_:
    for arg in bstack1ll1l111l1_opy_[bstack1lll1l1_opy_ (u"࠭ࡡࡳࡩࡶࠫय")]:
      options.add_argument(arg)
def bstack1lllll1l1l_opy_(options, bstack1111l1l1l_opy_):
  if bstack1lll1l1_opy_ (u"ࠧࡸࡧࡥࡺ࡮࡫ࡷࠨर") in bstack1111l1l1l_opy_:
    options.use_webview(bool(bstack1111l1l1l_opy_[bstack1lll1l1_opy_ (u"ࠨࡹࡨࡦࡻ࡯ࡥࡸࠩऱ")]))
  bstack1l11llll1_opy_(options, bstack1111l1l1l_opy_)
def bstack1l111lll_opy_(options, bstack11111l11l_opy_):
  for bstack1lll1111_opy_ in bstack11111l11l_opy_:
    if bstack1lll1111_opy_ in [bstack1lll1l1_opy_ (u"ࠩࡷࡩࡨ࡮࡮ࡰ࡮ࡲ࡫ࡾࡖࡲࡦࡸ࡬ࡩࡼ࠭ल"), bstack1lll1l1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨळ")]:
      continue
    options.set_capability(bstack1lll1111_opy_, bstack11111l11l_opy_[bstack1lll1111_opy_])
  if bstack1lll1l1_opy_ (u"ࠫࡦࡸࡧࡴࠩऴ") in bstack11111l11l_opy_:
    for arg in bstack11111l11l_opy_[bstack1lll1l1_opy_ (u"ࠬࡧࡲࡨࡵࠪव")]:
      options.add_argument(arg)
  if bstack1lll1l1_opy_ (u"࠭ࡴࡦࡥ࡫ࡲࡴࡲ࡯ࡨࡻࡓࡶࡪࡼࡩࡦࡹࠪश") in bstack11111l11l_opy_:
    options.bstack111ll1l1_opy_(bool(bstack11111l11l_opy_[bstack1lll1l1_opy_ (u"ࠧࡵࡧࡦ࡬ࡳࡵ࡬ࡰࡩࡼࡔࡷ࡫ࡶࡪࡧࡺࠫष")]))
def bstack1l1l11llll_opy_(options, bstack11llll11_opy_):
  for bstack1l1l1111ll_opy_ in bstack11llll11_opy_:
    if bstack1l1l1111ll_opy_ in [bstack1lll1l1_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬस"), bstack1lll1l1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧह")]:
      continue
    options._options[bstack1l1l1111ll_opy_] = bstack11llll11_opy_[bstack1l1l1111ll_opy_]
  if bstack1lll1l1_opy_ (u"ࠪࡥࡩࡪࡩࡵ࡫ࡲࡲࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧऺ") in bstack11llll11_opy_:
    for bstack1ll1l1l111_opy_ in bstack11llll11_opy_[bstack1lll1l1_opy_ (u"ࠫࡦࡪࡤࡪࡶ࡬ࡳࡳࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨऻ")]:
      options.bstack11ll1llll_opy_(
        bstack1ll1l1l111_opy_, bstack11llll11_opy_[bstack1lll1l1_opy_ (u"ࠬࡧࡤࡥ࡫ࡷ࡭ࡴࡴࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴ़ࠩ")][bstack1ll1l1l111_opy_])
  if bstack1lll1l1_opy_ (u"࠭ࡡࡳࡩࡶࠫऽ") in bstack11llll11_opy_:
    for arg in bstack11llll11_opy_[bstack1lll1l1_opy_ (u"ࠧࡢࡴࡪࡷࠬा")]:
      options.add_argument(arg)
def bstack1l11l11l1_opy_(options, caps):
  if not hasattr(options, bstack1lll1l1_opy_ (u"ࠨࡍࡈ࡝ࠬि")):
    return
  if options.KEY == bstack1lll1l1_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧी") and options.KEY in caps:
    bstack1l11llll1_opy_(options, caps[bstack1lll1l1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨु")])
  elif options.KEY == bstack1lll1l1_opy_ (u"ࠫࡲࡵࡺ࠻ࡨ࡬ࡶࡪ࡬࡯ࡹࡑࡳࡸ࡮ࡵ࡮ࡴࠩू") and options.KEY in caps:
    bstack111111l1_opy_(options, caps[bstack1lll1l1_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡩ࡭ࡷ࡫ࡦࡰࡺࡒࡴࡹ࡯࡯࡯ࡵࠪृ")])
  elif options.KEY == bstack1lll1l1_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠴࡯ࡱࡶ࡬ࡳࡳࡹࠧॄ") and options.KEY in caps:
    bstack1l111lll_opy_(options, caps[bstack1lll1l1_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯࠮ࡰࡲࡷ࡭ࡴࡴࡳࠨॅ")])
  elif options.KEY == bstack1lll1l1_opy_ (u"ࠨ࡯ࡶ࠾ࡪࡪࡧࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩॆ") and options.KEY in caps:
    bstack1lllll1l1l_opy_(options, caps[bstack1lll1l1_opy_ (u"ࠩࡰࡷ࠿࡫ࡤࡨࡧࡒࡴࡹ࡯࡯࡯ࡵࠪे")])
  elif options.KEY == bstack1lll1l1_opy_ (u"ࠪࡷࡪࡀࡩࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩै") and options.KEY in caps:
    bstack1l1l11llll_opy_(options, caps[bstack1lll1l1_opy_ (u"ࠫࡸ࡫࠺ࡪࡧࡒࡴࡹ࡯࡯࡯ࡵࠪॉ")])
def bstack1ll111l1_opy_(caps):
  global bstack1lll1111l_opy_
  if isinstance(os.environ.get(bstack1lll1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭ॊ")), str):
    bstack1lll1111l_opy_ = eval(os.getenv(bstack1lll1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧो")))
  if bstack1lll1111l_opy_:
    if bstack1ll111111l_opy_() < version.parse(bstack1lll1l1_opy_ (u"ࠧ࠳࠰࠶࠲࠵࠭ौ")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack1lll1l1_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨ्")
    if bstack1lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧॎ") in caps:
      browser = caps[bstack1lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨॏ")]
    elif bstack1lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬॐ") in caps:
      browser = caps[bstack1lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭॑")]
    browser = str(browser).lower()
    if browser == bstack1lll1l1_opy_ (u"࠭ࡩࡱࡪࡲࡲࡪ॒࠭") or browser == bstack1lll1l1_opy_ (u"ࠧࡪࡲࡤࡨࠬ॓"):
      browser = bstack1lll1l1_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࠨ॔")
    if browser == bstack1lll1l1_opy_ (u"ࠩࡶࡥࡲࡹࡵ࡯ࡩࠪॕ"):
      browser = bstack1lll1l1_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪॖ")
    if browser not in [bstack1lll1l1_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫॗ"), bstack1lll1l1_opy_ (u"ࠬ࡫ࡤࡨࡧࠪक़"), bstack1lll1l1_opy_ (u"࠭ࡩࡦࠩख़"), bstack1lll1l1_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࠧग़"), bstack1lll1l1_opy_ (u"ࠨࡨ࡬ࡶࡪ࡬࡯ࡹࠩज़")]:
      return None
    try:
      package = bstack1lll1l1_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰ࠲ࡼ࡫ࡢࡥࡴ࡬ࡺࡪࡸ࠮ࡼࡿ࠱ࡳࡵࡺࡩࡰࡰࡶࠫड़").format(browser)
      name = bstack1lll1l1_opy_ (u"ࠪࡓࡵࡺࡩࡰࡰࡶࠫढ़")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack111l1lll_opy_(options):
        return None
      for bstack11l11l1l1_opy_ in caps.keys():
        options.set_capability(bstack11l11l1l1_opy_, caps[bstack11l11l1l1_opy_])
      bstack1l11l11l1_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack111111l1l_opy_(options, bstack1llllll1l_opy_):
  if not bstack111l1lll_opy_(options):
    return
  for bstack11l11l1l1_opy_ in bstack1llllll1l_opy_.keys():
    if bstack11l11l1l1_opy_ in bstack1ll1l11l1l_opy_:
      continue
    if bstack11l11l1l1_opy_ in options._caps and type(options._caps[bstack11l11l1l1_opy_]) in [dict, list]:
      options._caps[bstack11l11l1l1_opy_] = update(options._caps[bstack11l11l1l1_opy_], bstack1llllll1l_opy_[bstack11l11l1l1_opy_])
    else:
      options.set_capability(bstack11l11l1l1_opy_, bstack1llllll1l_opy_[bstack11l11l1l1_opy_])
  bstack1l11l11l1_opy_(options, bstack1llllll1l_opy_)
  if bstack1lll1l1_opy_ (u"ࠫࡲࡵࡺ࠻ࡦࡨࡦࡺ࡭ࡧࡦࡴࡄࡨࡩࡸࡥࡴࡵࠪफ़") in options._caps:
    if options._caps[bstack1lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪय़")] and options._caps[bstack1lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫॠ")].lower() != bstack1lll1l1_opy_ (u"ࠧࡧ࡫ࡵࡩ࡫ࡵࡸࠨॡ"):
      del options._caps[bstack1lll1l1_opy_ (u"ࠨ࡯ࡲࡾ࠿ࡪࡥࡣࡷࡪ࡫ࡪࡸࡁࡥࡦࡵࡩࡸࡹࠧॢ")]
def bstack1lll1111l1_opy_(proxy_config):
  if bstack1lll1l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ॣ") in proxy_config:
    proxy_config[bstack1lll1l1_opy_ (u"ࠪࡷࡸࡲࡐࡳࡱࡻࡽࠬ।")] = proxy_config[bstack1lll1l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨ॥")]
    del (proxy_config[bstack1lll1l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩ०")])
  if bstack1lll1l1_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡙ࡿࡰࡦࠩ१") in proxy_config and proxy_config[bstack1lll1l1_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡚ࡹࡱࡧࠪ२")].lower() != bstack1lll1l1_opy_ (u"ࠨࡦ࡬ࡶࡪࡩࡴࠨ३"):
    proxy_config[bstack1lll1l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬ४")] = bstack1lll1l1_opy_ (u"ࠪࡱࡦࡴࡵࡢ࡮ࠪ५")
  if bstack1lll1l1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡄࡹࡹࡵࡣࡰࡰࡩ࡭࡬࡛ࡲ࡭ࠩ६") in proxy_config:
    proxy_config[bstack1lll1l1_opy_ (u"ࠬࡶࡲࡰࡺࡼࡘࡾࡶࡥࠨ७")] = bstack1lll1l1_opy_ (u"࠭ࡰࡢࡥࠪ८")
  return proxy_config
def bstack1l1l11l1ll_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack1lll1l1_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭९") in config:
    return proxy
  config[bstack1lll1l1_opy_ (u"ࠨࡲࡵࡳࡽࡿࠧ॰")] = bstack1lll1111l1_opy_(config[bstack1lll1l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࠨॱ")])
  if proxy == None:
    proxy = Proxy(config[bstack1lll1l1_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩॲ")])
  return proxy
def bstack11l111ll_opy_(self):
  global CONFIG
  global bstack1l1ll11l11_opy_
  try:
    proxy = bstack11lll1l11_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack1lll1l1_opy_ (u"ࠫ࠳ࡶࡡࡤࠩॳ")):
        proxies = bstack1l1111l11_opy_(proxy, bstack1lll11111_opy_())
        if len(proxies) > 0:
          protocol, bstack11l11111l_opy_ = proxies.popitem()
          if bstack1lll1l1_opy_ (u"ࠧࡀ࠯࠰ࠤॴ") in bstack11l11111l_opy_:
            return bstack11l11111l_opy_
          else:
            return bstack1lll1l1_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢॵ") + bstack11l11111l_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack1lll1l1_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡴࡷࡵࡸࡺࠢࡸࡶࡱࠦ࠺ࠡࡽࢀࠦॶ").format(str(e)))
  return bstack1l1ll11l11_opy_(self)
def bstack1ll11llll1_opy_():
  global CONFIG
  return bstack1lll1l11l1_opy_(CONFIG) and bstack1l1l11l111_opy_() and bstack11llll1ll_opy_() >= version.parse(bstack1llll1l1l1_opy_)
def bstack1l11l1l11_opy_():
  global CONFIG
  return (bstack1lll1l1_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫॷ") in CONFIG or bstack1lll1l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ॸ") in CONFIG) and bstack1l1l1l1l1l_opy_()
def bstack1ll1l1l1_opy_(config):
  bstack11lll11ll_opy_ = {}
  if bstack1lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧॹ") in config:
    bstack11lll11ll_opy_ = config[bstack1lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨॺ")]
  if bstack1lll1l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫॻ") in config:
    bstack11lll11ll_opy_ = config[bstack1lll1l1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬॼ")]
  proxy = bstack11lll1l11_opy_(config)
  if proxy:
    if proxy.endswith(bstack1lll1l1_opy_ (u"ࠧ࠯ࡲࡤࡧࠬॽ")) and os.path.isfile(proxy):
      bstack11lll11ll_opy_[bstack1lll1l1_opy_ (u"ࠨ࠯ࡳࡥࡨ࠳ࡦࡪ࡮ࡨࠫॾ")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack1lll1l1_opy_ (u"ࠩ࠱ࡴࡦࡩࠧॿ")):
        proxies = bstack1ll1lll1l1_opy_(config, bstack1lll11111_opy_())
        if len(proxies) > 0:
          protocol, bstack11l11111l_opy_ = proxies.popitem()
          if bstack1lll1l1_opy_ (u"ࠥ࠾࠴࠵ࠢঀ") in bstack11l11111l_opy_:
            parsed_url = urlparse(bstack11l11111l_opy_)
          else:
            parsed_url = urlparse(protocol + bstack1lll1l1_opy_ (u"ࠦ࠿࠵࠯ࠣঁ") + bstack11l11111l_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack11lll11ll_opy_[bstack1lll1l1_opy_ (u"ࠬࡶࡲࡰࡺࡼࡌࡴࡹࡴࠨং")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack11lll11ll_opy_[bstack1lll1l1_opy_ (u"࠭ࡰࡳࡱࡻࡽࡕࡵࡲࡵࠩঃ")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack11lll11ll_opy_[bstack1lll1l1_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡛ࡳࡦࡴࠪ঄")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack11lll11ll_opy_[bstack1lll1l1_opy_ (u"ࠨࡲࡵࡳࡽࡿࡐࡢࡵࡶࠫঅ")] = str(parsed_url.password)
  return bstack11lll11ll_opy_
def bstack1l1ll1l11l_opy_(config):
  if bstack1lll1l1_opy_ (u"ࠩࡷࡩࡸࡺࡃࡰࡰࡷࡩࡽࡺࡏࡱࡶ࡬ࡳࡳࡹࠧআ") in config:
    return config[bstack1lll1l1_opy_ (u"ࠪࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠨই")]
  return {}
def bstack111ll11l_opy_(caps):
  global bstack11l1lll11_opy_
  if bstack1lll1l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬঈ") in caps:
    caps[bstack1lll1l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭উ")][bstack1lll1l1_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬঊ")] = True
    if bstack11l1lll11_opy_:
      caps[bstack1lll1l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨঋ")][bstack1lll1l1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪঌ")] = bstack11l1lll11_opy_
  else:
    caps[bstack1lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࠧ঍")] = True
    if bstack11l1lll11_opy_:
      caps[bstack1lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ঎")] = bstack11l1lll11_opy_
def bstack111ll11l1_opy_():
  global CONFIG
  if bstack1lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨএ") in CONFIG and bstack1l11lllll_opy_(CONFIG[bstack1lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩঐ")]):
    bstack11lll11ll_opy_ = bstack1ll1l1l1_opy_(CONFIG)
    bstack1ll11ll111_opy_(CONFIG[bstack1lll1l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ঑")], bstack11lll11ll_opy_)
def bstack1ll11ll111_opy_(key, bstack11lll11ll_opy_):
  global bstack1ll1lll1_opy_
  logger.info(bstack1llll1l11_opy_)
  try:
    bstack1ll1lll1_opy_ = Local()
    bstack1l1111lll_opy_ = {bstack1lll1l1_opy_ (u"ࠧ࡬ࡧࡼࠫ঒"): key}
    bstack1l1111lll_opy_.update(bstack11lll11ll_opy_)
    logger.debug(bstack1l11ll11l_opy_.format(str(bstack1l1111lll_opy_)))
    bstack1ll1lll1_opy_.start(**bstack1l1111lll_opy_)
    if bstack1ll1lll1_opy_.isRunning():
      logger.info(bstack1ll1l1l11l_opy_)
  except Exception as e:
    bstack1ll1ll1ll1_opy_(bstack11ll1ll1l_opy_.format(str(e)))
def bstack1l1l11ll1l_opy_():
  global bstack1ll1lll1_opy_
  if bstack1ll1lll1_opy_.isRunning():
    logger.info(bstack1ll111ll1_opy_)
    bstack1ll1lll1_opy_.stop()
  bstack1ll1lll1_opy_ = None
def bstack11l1lll1_opy_(bstack1lllll1l11_opy_=[]):
  global CONFIG
  bstack1llll11l_opy_ = []
  bstack11l1l1ll_opy_ = [bstack1lll1l1_opy_ (u"ࠨࡱࡶࠫও"), bstack1lll1l1_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬঔ"), bstack1lll1l1_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧক"), bstack1lll1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭খ"), bstack1lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪগ"), bstack1lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧঘ")]
  try:
    for err in bstack1lllll1l11_opy_:
      bstack1l1ll1lll1_opy_ = {}
      for k in bstack11l1l1ll_opy_:
        val = CONFIG[bstack1lll1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪঙ")][int(err[bstack1lll1l1_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧচ")])].get(k)
        if val:
          bstack1l1ll1lll1_opy_[k] = val
      if(err[bstack1lll1l1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨছ")] != bstack1lll1l1_opy_ (u"ࠪࠫজ")):
        bstack1l1ll1lll1_opy_[bstack1lll1l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡵࠪঝ")] = {
          err[bstack1lll1l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪঞ")]: err[bstack1lll1l1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬট")]
        }
        bstack1llll11l_opy_.append(bstack1l1ll1lll1_opy_)
  except Exception as e:
    logger.debug(bstack1lll1l1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡩࡳࡷࡳࡡࡵࡶ࡬ࡲ࡬ࠦࡤࡢࡶࡤࠤ࡫ࡵࡲࠡࡧࡹࡩࡳࡺ࠺ࠡࠩঠ") + str(e))
  finally:
    return bstack1llll11l_opy_
def bstack1l11l1ll1_opy_(file_name):
  bstack11111111_opy_ = []
  try:
    bstack1111ll1l_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack1111ll1l_opy_):
      with open(bstack1111ll1l_opy_) as f:
        bstack1l1lll1111_opy_ = json.load(f)
        bstack11111111_opy_ = bstack1l1lll1111_opy_
      os.remove(bstack1111ll1l_opy_)
    return bstack11111111_opy_
  except Exception as e:
    logger.debug(bstack1lll1l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡪ࡮ࡴࡤࡪࡰࡪࠤࡪࡸࡲࡰࡴࠣࡰ࡮ࡹࡴ࠻ࠢࠪড") + str(e))
def bstack1ll11l1lll_opy_():
  global bstack1llll1llll_opy_
  global bstack1l1ll1ll1_opy_
  global bstack1l1l1111l_opy_
  global bstack1ll11l1ll1_opy_
  global bstack111l111l1_opy_
  global bstack1ll11l11ll_opy_
  percy.shutdown()
  bstack1llllll1l1_opy_ = os.environ.get(bstack1lll1l1_opy_ (u"ࠩࡉࡖࡆࡓࡅࡘࡑࡕࡏࡤ࡛ࡓࡆࡆࠪঢ"))
  if bstack1llllll1l1_opy_ in [bstack1lll1l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩণ"), bstack1lll1l1_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪত")]:
    bstack1lll1l111_opy_()
  if bstack1llll1llll_opy_:
    logger.warning(bstack1ll1lllll_opy_.format(str(bstack1llll1llll_opy_)))
  else:
    try:
      bstack1llll1ll1l_opy_ = bstack1l1l11l1l_opy_(bstack1lll1l1_opy_ (u"ࠬ࠴ࡢࡴࡶࡤࡧࡰ࠳ࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫথ"), logger)
      if bstack1llll1ll1l_opy_.get(bstack1lll1l1_opy_ (u"࠭࡮ࡶࡦࡪࡩࡤࡲ࡯ࡤࡣ࡯ࠫদ")) and bstack1llll1ll1l_opy_.get(bstack1lll1l1_opy_ (u"ࠧ࡯ࡷࡧ࡫ࡪࡥ࡬ࡰࡥࡤࡰࠬধ")).get(bstack1lll1l1_opy_ (u"ࠨࡪࡲࡷࡹࡴࡡ࡮ࡧࠪন")):
        logger.warning(bstack1ll1lllll_opy_.format(str(bstack1llll1ll1l_opy_[bstack1lll1l1_opy_ (u"ࠩࡱࡹࡩ࡭ࡥࡠ࡮ࡲࡧࡦࡲࠧ঩")][bstack1lll1l1_opy_ (u"ࠪ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠬপ")])))
    except Exception as e:
      logger.error(e)
  logger.info(bstack1ll111ll11_opy_)
  global bstack1ll1lll1_opy_
  if bstack1ll1lll1_opy_:
    bstack1l1l11ll1l_opy_()
  try:
    for driver in bstack1l1ll1ll1_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack11ll1l11l_opy_)
  if bstack1ll11l11ll_opy_ == bstack1lll1l1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪফ"):
    bstack111l111l1_opy_ = bstack1l11l1ll1_opy_(bstack1lll1l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭ব"))
  if bstack1ll11l11ll_opy_ == bstack1lll1l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ভ") and len(bstack1ll11l1ll1_opy_) == 0:
    bstack1ll11l1ll1_opy_ = bstack1l11l1ll1_opy_(bstack1lll1l1_opy_ (u"ࠧࡱࡹࡢࡴࡾࡺࡥࡴࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬম"))
    if len(bstack1ll11l1ll1_opy_) == 0:
      bstack1ll11l1ll1_opy_ = bstack1l11l1ll1_opy_(bstack1lll1l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡲࡳࡴࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧয"))
  bstack11lll111l_opy_ = bstack1lll1l1_opy_ (u"ࠩࠪর")
  if len(bstack1l1l1111l_opy_) > 0:
    bstack11lll111l_opy_ = bstack11l1lll1_opy_(bstack1l1l1111l_opy_)
  elif len(bstack1ll11l1ll1_opy_) > 0:
    bstack11lll111l_opy_ = bstack11l1lll1_opy_(bstack1ll11l1ll1_opy_)
  elif len(bstack111l111l1_opy_) > 0:
    bstack11lll111l_opy_ = bstack11l1lll1_opy_(bstack111l111l1_opy_)
  elif len(bstack1l1l1llll1_opy_) > 0:
    bstack11lll111l_opy_ = bstack11l1lll1_opy_(bstack1l1l1llll1_opy_)
  if bool(bstack11lll111l_opy_):
    bstack111111ll1_opy_(bstack11lll111l_opy_)
  else:
    bstack111111ll1_opy_()
  bstack1l1l11ll11_opy_(bstack1lll11ll1_opy_, logger)
def bstack1ll11l1ll_opy_(self, *args):
  logger.error(bstack1lll11l11l_opy_)
  bstack1ll11l1lll_opy_()
  sys.exit(1)
def bstack1ll1ll1ll1_opy_(err):
  logger.critical(bstack1llll1ll1_opy_.format(str(err)))
  bstack111111ll1_opy_(bstack1llll1ll1_opy_.format(str(err)), True)
  atexit.unregister(bstack1ll11l1lll_opy_)
  bstack1lll1l111_opy_()
  sys.exit(1)
def bstack1lll1lllll_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack111111ll1_opy_(message, True)
  atexit.unregister(bstack1ll11l1lll_opy_)
  bstack1lll1l111_opy_()
  sys.exit(1)
def bstack1l1lllllll_opy_():
  global CONFIG
  global bstack1ll111llll_opy_
  global bstack1lll1ll1l1_opy_
  global bstack1l11ll111_opy_
  CONFIG = bstack1ll1l1l1l1_opy_()
  bstack1ll1l1ll_opy_()
  bstack1lll1lll_opy_()
  CONFIG = bstack1l1111111_opy_(CONFIG)
  update(CONFIG, bstack1lll1ll1l1_opy_)
  update(CONFIG, bstack1ll111llll_opy_)
  CONFIG = bstack111l11lll_opy_(CONFIG)
  bstack1l11ll111_opy_ = bstack11ll11111_opy_(CONFIG)
  bstack11l1l11l_opy_.bstack1l1111l1_opy_(bstack1lll1l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫ঱"), bstack1l11ll111_opy_)
  if (bstack1lll1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧল") in CONFIG and bstack1lll1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ঳") in bstack1ll111llll_opy_) or (
          bstack1lll1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ঴") in CONFIG and bstack1lll1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ঵") not in bstack1lll1ll1l1_opy_):
    if os.getenv(bstack1lll1l1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬশ")):
      CONFIG[bstack1lll1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫষ")] = os.getenv(bstack1lll1l1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡢࡇࡔࡓࡂࡊࡐࡈࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧস"))
    else:
      bstack111l1l1l_opy_()
  elif (bstack1lll1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧহ") not in CONFIG and bstack1lll1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ঺") in CONFIG) or (
          bstack1lll1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ঻") in bstack1lll1ll1l1_opy_ and bstack1lll1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧ়ࠪ") not in bstack1ll111llll_opy_):
    del (CONFIG[bstack1lll1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪঽ")])
  if bstack1111l1l1_opy_(CONFIG):
    bstack1ll1ll1ll1_opy_(bstack11lll1ll_opy_)
  bstack11l1l11l1_opy_()
  bstack1ll11l1l1_opy_()
  if bstack1lll1111l_opy_:
    CONFIG[bstack1lll1l1_opy_ (u"ࠩࡤࡴࡵ࠭া")] = bstack11ll1l1ll_opy_(CONFIG)
    logger.info(bstack1111111l_opy_.format(CONFIG[bstack1lll1l1_opy_ (u"ࠪࡥࡵࡶࠧি")]))
def bstack1l11l1ll_opy_(config, bstack1l111l1l1_opy_):
  global CONFIG
  global bstack1lll1111l_opy_
  CONFIG = config
  bstack1lll1111l_opy_ = bstack1l111l1l1_opy_
def bstack1ll11l1l1_opy_():
  global CONFIG
  global bstack1lll1111l_opy_
  if bstack1lll1l1_opy_ (u"ࠫࡦࡶࡰࠨী") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1lll1lllll_opy_(e, bstack111l1l1ll_opy_)
    bstack1lll1111l_opy_ = True
    bstack11l1l11l_opy_.bstack1l1111l1_opy_(bstack1lll1l1_opy_ (u"ࠬࡧࡰࡱࡡࡤࡹࡹࡵ࡭ࡢࡶࡨࠫু"), True)
def bstack11ll1l1ll_opy_(config):
  bstack11l11l11l_opy_ = bstack1lll1l1_opy_ (u"࠭ࠧূ")
  app = config[bstack1lll1l1_opy_ (u"ࠧࡢࡲࡳࠫৃ")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack111l11l11_opy_:
      if os.path.exists(app):
        bstack11l11l11l_opy_ = bstack1lll11l1l1_opy_(config, app)
      elif bstack1ll11l11l1_opy_(app):
        bstack11l11l11l_opy_ = app
      else:
        bstack1ll1ll1ll1_opy_(bstack1ll1l11l_opy_.format(app))
    else:
      if bstack1ll11l11l1_opy_(app):
        bstack11l11l11l_opy_ = app
      elif os.path.exists(app):
        bstack11l11l11l_opy_ = bstack1lll11l1l1_opy_(app)
      else:
        bstack1ll1ll1ll1_opy_(bstack1l11l11l_opy_)
  else:
    if len(app) > 2:
      bstack1ll1ll1ll1_opy_(bstack1l1ll1ll1l_opy_)
    elif len(app) == 2:
      if bstack1lll1l1_opy_ (u"ࠨࡲࡤࡸ࡭࠭ৄ") in app and bstack1lll1l1_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡡ࡬ࡨࠬ৅") in app:
        if os.path.exists(app[bstack1lll1l1_opy_ (u"ࠪࡴࡦࡺࡨࠨ৆")]):
          bstack11l11l11l_opy_ = bstack1lll11l1l1_opy_(config, app[bstack1lll1l1_opy_ (u"ࠫࡵࡧࡴࡩࠩে")], app[bstack1lll1l1_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡤ࡯ࡤࠨৈ")])
        else:
          bstack1ll1ll1ll1_opy_(bstack1ll1l11l_opy_.format(app))
      else:
        bstack1ll1ll1ll1_opy_(bstack1l1ll1ll1l_opy_)
    else:
      for key in app:
        if key in bstack1l1l1l1l_opy_:
          if key == bstack1lll1l1_opy_ (u"࠭ࡰࡢࡶ࡫ࠫ৉"):
            if os.path.exists(app[key]):
              bstack11l11l11l_opy_ = bstack1lll11l1l1_opy_(config, app[key])
            else:
              bstack1ll1ll1ll1_opy_(bstack1ll1l11l_opy_.format(app))
          else:
            bstack11l11l11l_opy_ = app[key]
        else:
          bstack1ll1ll1ll1_opy_(bstack1l1l111lll_opy_)
  return bstack11l11l11l_opy_
def bstack1ll11l11l1_opy_(bstack11l11l11l_opy_):
  import re
  bstack1ll111ll1l_opy_ = re.compile(bstack1lll1l1_opy_ (u"ࡲࠣࡠ࡞ࡥ࠲ࢀࡁ࠮࡜࠳࠱࠾ࡢ࡟࠯࡞࠰ࡡ࠯ࠪࠢ৊"))
  bstack1ll1ll1ll_opy_ = re.compile(bstack1lll1l1_opy_ (u"ࡳࠤࡡ࡟ࡦ࠳ࡺࡂ࠯࡝࠴࠲࠿࡜ࡠ࠰࡟࠱ࡢ࠰࠯࡜ࡣ࠰ࡾࡆ࠳࡚࠱࠯࠼ࡠࡤ࠴࡜࠮࡟࠭ࠨࠧো"))
  if bstack1lll1l1_opy_ (u"ࠩࡥࡷ࠿࠵࠯ࠨৌ") in bstack11l11l11l_opy_ or re.fullmatch(bstack1ll111ll1l_opy_, bstack11l11l11l_opy_) or re.fullmatch(bstack1ll1ll1ll_opy_, bstack11l11l11l_opy_):
    return True
  else:
    return False
def bstack1lll11l1l1_opy_(config, path, bstack1llll11l1l_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack1lll1l1_opy_ (u"ࠪࡶࡧ্࠭")).read()).hexdigest()
  bstack1lll1l1111_opy_ = bstack1l1l111l1_opy_(md5_hash)
  bstack11l11l11l_opy_ = None
  if bstack1lll1l1111_opy_:
    logger.info(bstack1l1llll111_opy_.format(bstack1lll1l1111_opy_, md5_hash))
    return bstack1lll1l1111_opy_
  bstack1111ll11_opy_ = MultipartEncoder(
    fields={
      bstack1lll1l1_opy_ (u"ࠫ࡫࡯࡬ࡦࠩৎ"): (os.path.basename(path), open(os.path.abspath(path), bstack1lll1l1_opy_ (u"ࠬࡸࡢࠨ৏")), bstack1lll1l1_opy_ (u"࠭ࡴࡦࡺࡷ࠳ࡵࡲࡡࡪࡰࠪ৐")),
      bstack1lll1l1_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳ࡟ࡪࡦࠪ৑"): bstack1llll11l1l_opy_
    }
  )
  response = requests.post(bstack1lll1l1lll_opy_, data=bstack1111ll11_opy_,
                           headers={bstack1lll1l1_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧ৒"): bstack1111ll11_opy_.content_type},
                           auth=(config[bstack1lll1l1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ৓")], config[bstack1lll1l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭৔")]))
  try:
    res = json.loads(response.text)
    bstack11l11l11l_opy_ = res[bstack1lll1l1_opy_ (u"ࠫࡦࡶࡰࡠࡷࡵࡰࠬ৕")]
    logger.info(bstack1lll1llll1_opy_.format(bstack11l11l11l_opy_))
    bstack1111111l1_opy_(md5_hash, bstack11l11l11l_opy_)
  except ValueError as err:
    bstack1ll1ll1ll1_opy_(bstack1ll11lll1l_opy_.format(str(err)))
  return bstack11l11l11l_opy_
def bstack11l1l11l1_opy_():
  global CONFIG
  global bstack11ll11ll_opy_
  bstack111l1111_opy_ = 0
  bstack1lll11ll1l_opy_ = 1
  if bstack1lll1l1_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ৖") in CONFIG:
    bstack1lll11ll1l_opy_ = CONFIG[bstack1lll1l1_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭ৗ")]
  if bstack1lll1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ৘") in CONFIG:
    bstack111l1111_opy_ = len(CONFIG[bstack1lll1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ৙")])
  bstack11ll11ll_opy_ = int(bstack1lll11ll1l_opy_) * int(bstack111l1111_opy_)
def bstack1l1l111l1_opy_(md5_hash):
  bstack1lll11l1ll_opy_ = os.path.join(os.path.expanduser(bstack1lll1l1_opy_ (u"ࠩࢁࠫ৚")), bstack1lll1l1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪ৛"), bstack1lll1l1_opy_ (u"ࠫࡦࡶࡰࡖࡲ࡯ࡳࡦࡪࡍࡅ࠷ࡋࡥࡸ࡮࠮࡫ࡵࡲࡲࠬড়"))
  if os.path.exists(bstack1lll11l1ll_opy_):
    bstack1111llll_opy_ = json.load(open(bstack1lll11l1ll_opy_, bstack1lll1l1_opy_ (u"ࠬࡸࡢࠨঢ়")))
    if md5_hash in bstack1111llll_opy_:
      bstack1l11111ll_opy_ = bstack1111llll_opy_[md5_hash]
      bstack1l1l1lll_opy_ = datetime.datetime.now()
      bstack11lll1ll1_opy_ = datetime.datetime.strptime(bstack1l11111ll_opy_[bstack1lll1l1_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ৞")], bstack1lll1l1_opy_ (u"ࠧࠦࡦ࠲ࠩࡲ࠵࡚ࠥࠢࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫয়"))
      if (bstack1l1l1lll_opy_ - bstack11lll1ll1_opy_).days > 30:
        return None
      elif version.parse(str(__version__)) > version.parse(bstack1l11111ll_opy_[bstack1lll1l1_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ৠ")]):
        return None
      return bstack1l11111ll_opy_[bstack1lll1l1_opy_ (u"ࠩ࡬ࡨࠬৡ")]
  else:
    return None
def bstack1111111l1_opy_(md5_hash, bstack11l11l11l_opy_):
  bstack11l1llll1_opy_ = os.path.join(os.path.expanduser(bstack1lll1l1_opy_ (u"ࠪࢂࠬৢ")), bstack1lll1l1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫৣ"))
  if not os.path.exists(bstack11l1llll1_opy_):
    os.makedirs(bstack11l1llll1_opy_)
  bstack1lll11l1ll_opy_ = os.path.join(os.path.expanduser(bstack1lll1l1_opy_ (u"ࠬࢄࠧ৤")), bstack1lll1l1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭৥"), bstack1lll1l1_opy_ (u"ࠧࡢࡲࡳ࡙ࡵࡲ࡯ࡢࡦࡐࡈ࠺ࡎࡡࡴࡪ࠱࡮ࡸࡵ࡮ࠨ০"))
  bstack1lll111l1l_opy_ = {
    bstack1lll1l1_opy_ (u"ࠨ࡫ࡧࠫ১"): bstack11l11l11l_opy_,
    bstack1lll1l1_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ২"): datetime.datetime.strftime(datetime.datetime.now(), bstack1lll1l1_opy_ (u"ࠪࠩࡩ࠵ࠥ࡮࠱ࠨ࡝ࠥࠫࡈ࠻ࠧࡐ࠾࡙ࠪࠧ৩")),
    bstack1lll1l1_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ৪"): str(__version__)
  }
  if os.path.exists(bstack1lll11l1ll_opy_):
    bstack1111llll_opy_ = json.load(open(bstack1lll11l1ll_opy_, bstack1lll1l1_opy_ (u"ࠬࡸࡢࠨ৫")))
  else:
    bstack1111llll_opy_ = {}
  bstack1111llll_opy_[md5_hash] = bstack1lll111l1l_opy_
  with open(bstack1lll11l1ll_opy_, bstack1lll1l1_opy_ (u"ࠨࡷࠬࠤ৬")) as outfile:
    json.dump(bstack1111llll_opy_, outfile)
def bstack1ll1ll111l_opy_(self):
  return
def bstack111l1l11l_opy_(self):
  return
def bstack1llll11l1_opy_(self):
  global bstack1lll1l1l1_opy_
  bstack1lll1l1l1_opy_(self)
def bstack1111llll1_opy_():
  global bstack1lll1ll11_opy_
  bstack1lll1ll11_opy_ = True
def bstack11lll1111_opy_(self):
  global bstack1ll11l1l11_opy_
  global bstack111l1llll_opy_
  global bstack1l11l1111_opy_
  try:
    if bstack1lll1l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ৭") in bstack1ll11l1l11_opy_ and self.session_id != None and bstack1ll11111l_opy_(threading.current_thread(), bstack1lll1l1_opy_ (u"ࠨࡶࡨࡷࡹ࡙ࡴࡢࡶࡸࡷࠬ৮"), bstack1lll1l1_opy_ (u"ࠩࠪ৯")) != bstack1lll1l1_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫৰ"):
      bstack1lllll11_opy_ = bstack1lll1l1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫৱ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack1lll1l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ৲")
      if bstack1lllll11_opy_ == bstack1lll1l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭৳"):
        bstack1111l11l_opy_(logger)
      if self != None:
        bstack1l1l11ll_opy_(self, bstack1lllll11_opy_, bstack1lll1l1_opy_ (u"ࠧ࠭ࠢࠪ৴").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack1lll1l1_opy_ (u"ࠨࠩ৵")
    if bstack1lll1l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ৶") in bstack1ll11l1l11_opy_ and getattr(threading.current_thread(), bstack1lll1l1_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ৷"), None):
      bstack1l1l11l11l_opy_.bstack1l111ll1_opy_(self, bstack1ll1l1lll_opy_, logger, wait=True)
  except Exception as e:
    logger.debug(bstack1lll1l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡰࡥࡷࡱࡩ࡯ࡩࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࠧ৸") + str(e))
  bstack1l11l1111_opy_(self)
  self.session_id = None
def bstack1ll11lll11_opy_(self, command_executor=bstack1lll1l1_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴࠷࠲࠸࠰࠳࠲࠵࠴࠱࠻࠶࠷࠸࠹ࠨ৹"), *args, **kwargs):
  bstack1111111ll_opy_ = bstack11llll1l_opy_(self, command_executor, *args, **kwargs)
  try:
    logger.debug(bstack1lll1l1_opy_ (u"࠭ࡃࡰ࡯ࡰࡥࡳࡪࠠࡆࡺࡨࡧࡺࡺ࡯ࡳࠢࡺ࡬ࡪࡴࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣ࡭ࡸࠦࡦࡢ࡮ࡶࡩࠥ࠳ࠠࡼࡿࠪ৺").format(str(command_executor)))
    logger.debug(bstack1lll1l1_opy_ (u"ࠧࡉࡷࡥࠤ࡚ࡘࡌࠡ࡫ࡶࠤ࠲ࠦࡻࡾࠩ৻").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack1lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫৼ") in command_executor._url:
      bstack11l1l11l_opy_.bstack1l1111l1_opy_(bstack1lll1l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪ৽"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack1lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭৾") in command_executor):
    bstack11l1l11l_opy_.bstack1l1111l1_opy_(bstack1lll1l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬ৿"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack1l1ll11l_opy_.bstack1l1l1l111l_opy_(self)
  return bstack1111111ll_opy_
def bstack1ll11ll1_opy_(self, driver_command, *args, **kwargs):
  global bstack111lll111_opy_
  response = bstack111lll111_opy_(self, driver_command, *args, **kwargs)
  try:
    if driver_command == bstack1lll1l1_opy_ (u"ࠬࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠩ਀"):
      bstack1l1ll11l_opy_.bstack1l1llll11l_opy_({
          bstack1lll1l1_opy_ (u"࠭ࡩ࡮ࡣࡪࡩࠬਁ"): response[bstack1lll1l1_opy_ (u"ࠧࡷࡣ࡯ࡹࡪ࠭ਂ")],
          bstack1lll1l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨਃ"): bstack1l1ll11l_opy_.current_test_uuid() if bstack1l1ll11l_opy_.current_test_uuid() else bstack1l1ll11l_opy_.current_hook_uuid()
      })
  except:
    pass
  return response
def bstack1ll1ll1l1_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
  global CONFIG
  global bstack111l1llll_opy_
  global bstack1lll1llll_opy_
  global bstack1lll111ll1_opy_
  global bstack1l1l1lll1l_opy_
  global bstack111l11ll1_opy_
  global bstack1ll11l1l11_opy_
  global bstack11llll1l_opy_
  global bstack1l1ll1ll1_opy_
  global bstack11ll111l_opy_
  global bstack1ll1l1lll_opy_
  CONFIG[bstack1lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫ਄")] = str(bstack1ll11l1l11_opy_) + str(__version__)
  command_executor = bstack1lll11111_opy_()
  logger.debug(bstack11l1111ll_opy_.format(command_executor))
  proxy = bstack1l1l11l1ll_opy_(CONFIG, proxy)
  bstack1111l111_opy_ = 0 if bstack1lll1llll_opy_ < 0 else bstack1lll1llll_opy_
  try:
    if bstack1l1l1lll1l_opy_ is True:
      bstack1111l111_opy_ = int(multiprocessing.current_process().name)
    elif bstack111l11ll1_opy_ is True:
      bstack1111l111_opy_ = int(threading.current_thread().name)
  except:
    bstack1111l111_opy_ = 0
  bstack1llllll1l_opy_ = bstack1l1llllll1_opy_(CONFIG, bstack1111l111_opy_)
  logger.debug(bstack1111l1ll_opy_.format(str(bstack1llllll1l_opy_)))
  if bstack1lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧਅ") in CONFIG and bstack1l11lllll_opy_(CONFIG[bstack1lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨਆ")]):
    bstack111ll11l_opy_(bstack1llllll1l_opy_)
  if desired_capabilities:
    bstack1llll1lll1_opy_ = bstack1l1111111_opy_(desired_capabilities)
    bstack1llll1lll1_opy_[bstack1lll1l1_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬਇ")] = bstack1ll11lll1_opy_(CONFIG)
    bstack11ll11l1l_opy_ = bstack1l1llllll1_opy_(bstack1llll1lll1_opy_)
    if bstack11ll11l1l_opy_:
      bstack1llllll1l_opy_ = update(bstack11ll11l1l_opy_, bstack1llllll1l_opy_)
    desired_capabilities = None
  if options:
    bstack111111l1l_opy_(options, bstack1llllll1l_opy_)
  if not options:
    options = bstack1ll111l1_opy_(bstack1llllll1l_opy_)
  bstack1ll1l1lll_opy_ = CONFIG.get(bstack1lll1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩਈ"))[bstack1111l111_opy_]
  if bstack11111111l_opy_.bstack1l111ll11_opy_(CONFIG, bstack1111l111_opy_) and bstack11111111l_opy_.bstack1l1lll11_opy_(bstack1llllll1l_opy_, options):
    threading.current_thread().a11yPlatform = True
    bstack11111111l_opy_.set_capabilities(bstack1llllll1l_opy_, CONFIG)
  if proxy and bstack11llll1ll_opy_() >= version.parse(bstack1lll1l1_opy_ (u"ࠧ࠵࠰࠴࠴࠳࠶ࠧਉ")):
    options.proxy(proxy)
  if options and bstack11llll1ll_opy_() >= version.parse(bstack1lll1l1_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧਊ")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack11llll1ll_opy_() < version.parse(bstack1lll1l1_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨ਋")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack1llllll1l_opy_)
  logger.info(bstack1l1l1l11l_opy_)
  if bstack11llll1ll_opy_() >= version.parse(bstack1lll1l1_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪ਌")):
    bstack11llll1l_opy_(self, command_executor=command_executor,
              options=options, keep_alive=keep_alive, file_detector=file_detector)
  elif bstack11llll1ll_opy_() >= version.parse(bstack1lll1l1_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪ਍")):
    bstack11llll1l_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities, options=options,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  elif bstack11llll1ll_opy_() >= version.parse(bstack1lll1l1_opy_ (u"ࠬ࠸࠮࠶࠵࠱࠴ࠬ਎")):
    bstack11llll1l_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  else:
    bstack11llll1l_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive)
  try:
    bstack1l1l11l1l1_opy_ = bstack1lll1l1_opy_ (u"࠭ࠧਏ")
    if bstack11llll1ll_opy_() >= version.parse(bstack1lll1l1_opy_ (u"ࠧ࠵࠰࠳࠲࠵ࡨ࠱ࠨਐ")):
      bstack1l1l11l1l1_opy_ = self.caps.get(bstack1lll1l1_opy_ (u"ࠣࡱࡳࡸ࡮ࡳࡡ࡭ࡊࡸࡦ࡚ࡸ࡬ࠣ਑"))
    else:
      bstack1l1l11l1l1_opy_ = self.capabilities.get(bstack1lll1l1_opy_ (u"ࠤࡲࡴࡹ࡯࡭ࡢ࡮ࡋࡹࡧ࡛ࡲ࡭ࠤ਒"))
    if bstack1l1l11l1l1_opy_:
      bstack11l1lllll_opy_(bstack1l1l11l1l1_opy_)
      if bstack11llll1ll_opy_() <= version.parse(bstack1lll1l1_opy_ (u"ࠪ࠷࠳࠷࠳࠯࠲ࠪਓ")):
        self.command_executor._url = bstack1lll1l1_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧਔ") + bstack111111ll_opy_ + bstack1lll1l1_opy_ (u"ࠧࡀ࠸࠱࠱ࡺࡨ࠴࡮ࡵࡣࠤਕ")
      else:
        self.command_executor._url = bstack1lll1l1_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣਖ") + bstack1l1l11l1l1_opy_ + bstack1lll1l1_opy_ (u"ࠢ࠰ࡹࡧ࠳࡭ࡻࡢࠣਗ")
      logger.debug(bstack1ll1l111_opy_.format(bstack1l1l11l1l1_opy_))
    else:
      logger.debug(bstack1l1l1l1ll_opy_.format(bstack1lll1l1_opy_ (u"ࠣࡑࡳࡸ࡮ࡳࡡ࡭ࠢࡋࡹࡧࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥࠤਘ")))
  except Exception as e:
    logger.debug(bstack1l1l1l1ll_opy_.format(e))
  if bstack1lll1l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨਙ") in bstack1ll11l1l11_opy_:
    bstack1ll1l1l1l_opy_(bstack1lll1llll_opy_, bstack11ll111l_opy_)
  bstack111l1llll_opy_ = self.session_id
  if bstack1lll1l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪਚ") in bstack1ll11l1l11_opy_ or bstack1lll1l1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫਛ") in bstack1ll11l1l11_opy_ or bstack1lll1l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫਜ") in bstack1ll11l1l11_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
    bstack1l1ll11l_opy_.bstack1l1l1l111l_opy_(self)
  bstack1l1ll1ll1_opy_.append(self)
  if bstack1lll1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩਝ") in CONFIG and bstack1lll1l1_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬਞ") in CONFIG[bstack1lll1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫਟ")][bstack1111l111_opy_]:
    bstack1lll111ll1_opy_ = CONFIG[bstack1lll1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬਠ")][bstack1111l111_opy_][bstack1lll1l1_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨਡ")]
  logger.debug(bstack1ll1l11ll_opy_.format(bstack111l1llll_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    def bstack11111l1l1_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack1ll111l1ll_opy_
      if(bstack1lll1l1_opy_ (u"ࠦ࡮ࡴࡤࡦࡺ࠱࡮ࡸࠨਢ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack1lll1l1_opy_ (u"ࠬࢄࠧਣ")), bstack1lll1l1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ਤ"), bstack1lll1l1_opy_ (u"ࠧ࠯ࡵࡨࡷࡸ࡯࡯࡯࡫ࡧࡷ࠳ࡺࡸࡵࠩਥ")), bstack1lll1l1_opy_ (u"ࠨࡹࠪਦ")) as fp:
          fp.write(bstack1lll1l1_opy_ (u"ࠤࠥਧ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack1lll1l1_opy_ (u"ࠥ࡭ࡳࡪࡥࡹࡡࡥࡷࡹࡧࡣ࡬࠰࡭ࡷࠧਨ")))):
          with open(args[1], bstack1lll1l1_opy_ (u"ࠫࡷ࠭਩")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack1lll1l1_opy_ (u"ࠬࡧࡳࡺࡰࡦࠤ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦ࡟࡯ࡧࡺࡔࡦ࡭ࡥࠩࡥࡲࡲࡹ࡫ࡸࡵ࠮ࠣࡴࡦ࡭ࡥࠡ࠿ࠣࡺࡴ࡯ࡤࠡ࠲ࠬࠫਪ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack1llll111l_opy_)
            lines.insert(1, bstack1l1l1l1lll_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack1lll1l1_opy_ (u"ࠨࡩ࡯ࡦࡨࡼࡤࡨࡳࡵࡣࡦ࡯࠳ࡰࡳࠣਫ")), bstack1lll1l1_opy_ (u"ࠧࡸࠩਬ")) as bstack1ll111l111_opy_:
              bstack1ll111l111_opy_.writelines(lines)
        CONFIG[bstack1lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪਭ")] = str(bstack1ll11l1l11_opy_) + str(__version__)
        bstack1111l111_opy_ = 0 if bstack1lll1llll_opy_ < 0 else bstack1lll1llll_opy_
        try:
          if bstack1l1l1lll1l_opy_ is True:
            bstack1111l111_opy_ = int(multiprocessing.current_process().name)
          elif bstack111l11ll1_opy_ is True:
            bstack1111l111_opy_ = int(threading.current_thread().name)
        except:
          bstack1111l111_opy_ = 0
        CONFIG[bstack1lll1l1_opy_ (u"ࠤࡸࡷࡪ࡝࠳ࡄࠤਮ")] = False
        CONFIG[bstack1lll1l1_opy_ (u"ࠥ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤਯ")] = True
        bstack1llllll1l_opy_ = bstack1l1llllll1_opy_(CONFIG, bstack1111l111_opy_)
        logger.debug(bstack1111l1ll_opy_.format(str(bstack1llllll1l_opy_)))
        if CONFIG.get(bstack1lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨਰ")):
          bstack111ll11l_opy_(bstack1llllll1l_opy_)
        if bstack1lll1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ਱") in CONFIG and bstack1lll1l1_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫਲ") in CONFIG[bstack1lll1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪਲ਼")][bstack1111l111_opy_]:
          bstack1lll111ll1_opy_ = CONFIG[bstack1lll1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ਴")][bstack1111l111_opy_][bstack1lll1l1_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧਵ")]
        args.append(os.path.join(os.path.expanduser(bstack1lll1l1_opy_ (u"ࠪࢂࠬਸ਼")), bstack1lll1l1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫ਷"), bstack1lll1l1_opy_ (u"ࠬ࠴ࡳࡦࡵࡶ࡭ࡴࡴࡩࡥࡵ࠱ࡸࡽࡺࠧਸ")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack1llllll1l_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack1lll1l1_opy_ (u"ࠨࡩ࡯ࡦࡨࡼࡤࡨࡳࡵࡣࡦ࡯࠳ࡰࡳࠣਹ"))
      bstack1ll111l1ll_opy_ = True
      return bstack111l11l1_opy_(self, args, bufsize=bufsize, executable=executable,
                    stdin=stdin, stdout=stdout, stderr=stderr,
                    preexec_fn=preexec_fn, close_fds=close_fds,
                    shell=shell, cwd=cwd, env=env, universal_newlines=universal_newlines,
                    startupinfo=startupinfo, creationflags=creationflags,
                    restore_signals=restore_signals, start_new_session=start_new_session,
                    pass_fds=pass_fds, user=user, group=group, extra_groups=extra_groups,
                    encoding=encoding, errors=errors, text=text, umask=umask, pipesize=pipesize)
  except Exception as e:
    pass
  import playwright._impl._api_structures
  import playwright._impl._helper
  def bstack1l111l1l_opy_(self,
        executablePath = None,
        channel = None,
        args = None,
        ignoreDefaultArgs = None,
        handleSIGINT = None,
        handleSIGTERM = None,
        handleSIGHUP = None,
        timeout = None,
        env = None,
        headless = None,
        devtools = None,
        proxy = None,
        downloadsPath = None,
        slowMo = None,
        tracesDir = None,
        chromiumSandbox = None,
        firefoxUserPrefs = None
        ):
    global CONFIG
    global bstack1lll1llll_opy_
    global bstack1lll111ll1_opy_
    global bstack1l1l1lll1l_opy_
    global bstack111l11ll1_opy_
    global bstack1ll11l1l11_opy_
    CONFIG[bstack1lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩ਺")] = str(bstack1ll11l1l11_opy_) + str(__version__)
    bstack1111l111_opy_ = 0 if bstack1lll1llll_opy_ < 0 else bstack1lll1llll_opy_
    try:
      if bstack1l1l1lll1l_opy_ is True:
        bstack1111l111_opy_ = int(multiprocessing.current_process().name)
      elif bstack111l11ll1_opy_ is True:
        bstack1111l111_opy_ = int(threading.current_thread().name)
    except:
      bstack1111l111_opy_ = 0
    CONFIG[bstack1lll1l1_opy_ (u"ࠣ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢ਻")] = True
    bstack1llllll1l_opy_ = bstack1l1llllll1_opy_(CONFIG, bstack1111l111_opy_)
    logger.debug(bstack1111l1ll_opy_.format(str(bstack1llllll1l_opy_)))
    if CONFIG.get(bstack1lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ਼࠭")):
      bstack111ll11l_opy_(bstack1llllll1l_opy_)
    if bstack1lll1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭਽") in CONFIG and bstack1lll1l1_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩਾ") in CONFIG[bstack1lll1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨਿ")][bstack1111l111_opy_]:
      bstack1lll111ll1_opy_ = CONFIG[bstack1lll1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩੀ")][bstack1111l111_opy_][bstack1lll1l1_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬੁ")]
    import urllib
    import json
    bstack1l1l1l1l1_opy_ = bstack1lll1l1_opy_ (u"ࠨࡹࡶࡷ࠿࠵࠯ࡤࡦࡳ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࡃࡨࡧࡰࡴ࠿ࠪੂ") + urllib.parse.quote(json.dumps(bstack1llllll1l_opy_))
    browser = self.connect(bstack1l1l1l1l1_opy_)
    return browser
except Exception as e:
    pass
def bstack1l1111l1l_opy_():
    global bstack1ll111l1ll_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        BrowserType.launch = bstack1l111l1l_opy_
        bstack1ll111l1ll_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack11111l1l1_opy_
      bstack1ll111l1ll_opy_ = True
    except Exception as e:
      pass
def bstack1llllll11l_opy_(context, bstack111lll1ll_opy_):
  try:
    context.page.evaluate(bstack1lll1l1_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥ੃"), bstack1lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠧ੄")+ json.dumps(bstack111lll1ll_opy_) + bstack1lll1l1_opy_ (u"ࠦࢂࢃࠢ੅"))
  except Exception as e:
    logger.debug(bstack1lll1l1_opy_ (u"ࠧ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠠࡼࡿࠥ੆"), e)
def bstack11l11ll11_opy_(context, message, level):
  try:
    context.page.evaluate(bstack1lll1l1_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢੇ"), bstack1lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬੈ") + json.dumps(message) + bstack1lll1l1_opy_ (u"ࠨ࠮ࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠫ੉") + json.dumps(level) + bstack1lll1l1_opy_ (u"ࠩࢀࢁࠬ੊"))
  except Exception as e:
    logger.debug(bstack1lll1l1_opy_ (u"ࠥࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡡ࡯ࡰࡲࡸࡦࡺࡩࡰࡰࠣࡿࢂࠨੋ"), e)
def bstack1l1lll1l_opy_(self, url):
  global bstack1llllll1ll_opy_
  try:
    bstack1111l1l11_opy_(url)
  except Exception as err:
    logger.debug(bstack1lllll1lll_opy_.format(str(err)))
  try:
    bstack1llllll1ll_opy_(self, url)
  except Exception as e:
    try:
      bstack1l11ll11_opy_ = str(e)
      if any(err_msg in bstack1l11ll11_opy_ for err_msg in bstack1l1l1111_opy_):
        bstack1111l1l11_opy_(url, True)
    except Exception as err:
      logger.debug(bstack1lllll1lll_opy_.format(str(err)))
    raise e
def bstack1l1lll1l1l_opy_(self):
  global bstack1ll1l1lll1_opy_
  bstack1ll1l1lll1_opy_ = self
  return
def bstack1111lll1l_opy_(self):
  global bstack1ll1llll_opy_
  bstack1ll1llll_opy_ = self
  return
def bstack11ll1l11_opy_(test_name, bstack11111lll_opy_):
  global CONFIG
  if CONFIG.get(bstack1lll1l1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪੌ"), False):
    bstack11lll1l1_opy_ = os.path.relpath(bstack11111lll_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack11lll1l1_opy_)
    bstack111llll1_opy_ = suite_name + bstack1lll1l1_opy_ (u"ࠧ࠳੍ࠢ") + test_name
    threading.current_thread().percySessionName = bstack111llll1_opy_
def bstack1l1lll1l11_opy_(self, test, *args, **kwargs):
  global bstack1l111l11_opy_
  test_name = None
  bstack11111lll_opy_ = None
  if test:
    test_name = str(test.name)
    bstack11111lll_opy_ = str(test.source)
  bstack11ll1l11_opy_(test_name, bstack11111lll_opy_)
  bstack1l111l11_opy_(self, test, *args, **kwargs)
def bstack1lll1lll1_opy_(driver, bstack111llll1_opy_):
  if not bstack111lllll1_opy_ and bstack111llll1_opy_:
      bstack1l111ll1l_opy_ = {
          bstack1lll1l1_opy_ (u"࠭ࡡࡤࡶ࡬ࡳࡳ࠭੎"): bstack1lll1l1_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ੏"),
          bstack1lll1l1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ੐"): {
              bstack1lll1l1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧੑ"): bstack111llll1_opy_
          }
      }
      bstack1ll1l11lll_opy_ = bstack1lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨ੒").format(json.dumps(bstack1l111ll1l_opy_))
      driver.execute_script(bstack1ll1l11lll_opy_)
  if bstack1ll11111ll_opy_:
      bstack1lllll1ll_opy_ = {
          bstack1lll1l1_opy_ (u"ࠫࡦࡩࡴࡪࡱࡱࠫ੓"): bstack1lll1l1_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧ੔"),
          bstack1lll1l1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ੕"): {
              bstack1lll1l1_opy_ (u"ࠧࡥࡣࡷࡥࠬ੖"): bstack111llll1_opy_ + bstack1lll1l1_opy_ (u"ࠨࠢࡳࡥࡸࡹࡥࡥࠣࠪ੗"),
              bstack1lll1l1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ੘"): bstack1lll1l1_opy_ (u"ࠪ࡭ࡳ࡬࡯ࠨਖ਼")
          }
      }
      if bstack1ll11111ll_opy_.status == bstack1lll1l1_opy_ (u"ࠫࡕࡇࡓࡔࠩਗ਼"):
          bstack1lll1ll11l_opy_ = bstack1lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪਜ਼").format(json.dumps(bstack1lllll1ll_opy_))
          driver.execute_script(bstack1lll1ll11l_opy_)
          bstack1l1l11ll_opy_(driver, bstack1lll1l1_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ੜ"))
      elif bstack1ll11111ll_opy_.status == bstack1lll1l1_opy_ (u"ࠧࡇࡃࡌࡐࠬ੝"):
          reason = bstack1lll1l1_opy_ (u"ࠣࠤਫ਼")
          bstack1lll1ll111_opy_ = bstack111llll1_opy_ + bstack1lll1l1_opy_ (u"ࠩࠣࡪࡦ࡯࡬ࡦࡦࠪ੟")
          if bstack1ll11111ll_opy_.message:
              reason = str(bstack1ll11111ll_opy_.message)
              bstack1lll1ll111_opy_ = bstack1lll1ll111_opy_ + bstack1lll1l1_opy_ (u"ࠪࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲ࠻ࠢࠪ੠") + reason
          bstack1lllll1ll_opy_[bstack1lll1l1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ੡")] = {
              bstack1lll1l1_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ੢"): bstack1lll1l1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ੣"),
              bstack1lll1l1_opy_ (u"ࠧࡥࡣࡷࡥࠬ੤"): bstack1lll1ll111_opy_
          }
          bstack1lll1ll11l_opy_ = bstack1lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂ࠭੥").format(json.dumps(bstack1lllll1ll_opy_))
          driver.execute_script(bstack1lll1ll11l_opy_)
          bstack1l1l11ll_opy_(driver, bstack1lll1l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ੦"), reason)
          bstack1l11l111l_opy_(reason, str(bstack1ll11111ll_opy_), str(bstack1lll1llll_opy_), logger)
def bstack1ll11l11_opy_(driver, test):
  if CONFIG.get(bstack1lll1l1_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩ੧"), False) and CONFIG.get(bstack1lll1l1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡆࡥࡵࡺࡵࡳࡧࡐࡳࡩ࡫ࠧ੨"), bstack1lll1l1_opy_ (u"ࠧࡧࡵࡵࡱࠥ੩")) == bstack1lll1l1_opy_ (u"ࠨࡴࡦࡵࡷࡧࡦࡹࡥࠣ੪"):
      bstack1lll11ll11_opy_ = bstack1ll11111l_opy_(threading.current_thread(), bstack1lll1l1_opy_ (u"ࠧࡱࡧࡵࡧࡾ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ੫"), None)
      bstack11l111l1_opy_(driver, bstack1lll11ll11_opy_)
  if bstack1ll11111l_opy_(threading.current_thread(), bstack1lll1l1_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬ੬"), None) and bstack1ll11111l_opy_(
          threading.current_thread(), bstack1lll1l1_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ੭"), None):
      logger.info(bstack1lll1l1_opy_ (u"ࠥࡅࡺࡺ࡯࡮ࡣࡷࡩࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡧࡻࡩࡨࡻࡴࡪࡱࡱࠤ࡭ࡧࡳࠡࡧࡱࡨࡪࡪ࠮ࠡࡒࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣ࡭ࡸࠦࡵ࡯ࡦࡨࡶࡼࡧࡹ࠯ࠢࠥ੮"))
      bstack11111111l_opy_.bstack11l1ll1ll_opy_(driver, class_name=test.parent.name, name=test.name, module_name=None,
                              path=test.source, bstack1l1l111l1l_opy_=bstack1ll1l1lll_opy_)
def bstack1l111l11l_opy_(test, bstack111llll1_opy_):
    try:
      data = {}
      if test:
        data[bstack1lll1l1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ੯")] = bstack111llll1_opy_
      if bstack1ll11111ll_opy_:
        if bstack1ll11111ll_opy_.status == bstack1lll1l1_opy_ (u"ࠬࡖࡁࡔࡕࠪੰ"):
          data[bstack1lll1l1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ੱ")] = bstack1lll1l1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧੲ")
        elif bstack1ll11111ll_opy_.status == bstack1lll1l1_opy_ (u"ࠨࡈࡄࡍࡑ࠭ੳ"):
          data[bstack1lll1l1_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩੴ")] = bstack1lll1l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪੵ")
          if bstack1ll11111ll_opy_.message:
            data[bstack1lll1l1_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫ੶")] = str(bstack1ll11111ll_opy_.message)
      user = CONFIG[bstack1lll1l1_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ੷")]
      key = CONFIG[bstack1lll1l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ੸")]
      url = bstack1lll1l1_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡽࢀ࠾ࢀࢃࡀࡢࡲ࡬࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡢࡷࡷࡳࡲࡧࡴࡦ࠱ࡶࡩࡸࡹࡩࡰࡰࡶ࠳ࢀࢃ࠮࡫ࡵࡲࡲࠬ੹").format(user, key, bstack111l1llll_opy_)
      headers = {
        bstack1lll1l1_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧ੺"): bstack1lll1l1_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬ੻"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers)
    except Exception as e:
      logger.error(bstack1llll1ll11_opy_.format(str(e)))
def bstack111ll1ll1_opy_(test, bstack111llll1_opy_):
  global CONFIG
  global bstack1ll1llll_opy_
  global bstack1ll1l1lll1_opy_
  global bstack111l1llll_opy_
  global bstack1ll11111ll_opy_
  global bstack1lll111ll1_opy_
  global bstack1llll1l1_opy_
  global bstack1ll11l11l_opy_
  global bstack1l1l11111_opy_
  global bstack1ll1111l11_opy_
  global bstack1l1ll1ll1_opy_
  global bstack1ll1l1lll_opy_
  try:
    if not bstack111l1llll_opy_:
      with open(os.path.join(os.path.expanduser(bstack1lll1l1_opy_ (u"ࠪࢂࠬ੼")), bstack1lll1l1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫ੽"), bstack1lll1l1_opy_ (u"ࠬ࠴ࡳࡦࡵࡶ࡭ࡴࡴࡩࡥࡵ࠱ࡸࡽࡺࠧ੾"))) as f:
        bstack1111l1lll_opy_ = json.loads(bstack1lll1l1_opy_ (u"ࠨࡻࠣ੿") + f.read().strip() + bstack1lll1l1_opy_ (u"ࠧࠣࡺࠥ࠾ࠥࠨࡹࠣࠩ઀") + bstack1lll1l1_opy_ (u"ࠣࡿࠥઁ"))
        bstack111l1llll_opy_ = bstack1111l1lll_opy_[str(threading.get_ident())]
  except:
    pass
  if bstack1l1ll1ll1_opy_:
    for driver in bstack1l1ll1ll1_opy_:
      if bstack111l1llll_opy_ == driver.session_id:
        if test:
          bstack1ll11l11_opy_(driver, test)
        bstack1lll1lll1_opy_(driver, bstack111llll1_opy_)
  elif bstack111l1llll_opy_:
    bstack1l111l11l_opy_(test, bstack111llll1_opy_)
  if bstack1ll1llll_opy_:
    bstack1ll11l11l_opy_(bstack1ll1llll_opy_)
  if bstack1ll1l1lll1_opy_:
    bstack1l1l11111_opy_(bstack1ll1l1lll1_opy_)
  if bstack1lll1ll11_opy_:
    bstack1ll1111l11_opy_()
def bstack1l1lll1ll_opy_(self, test, *args, **kwargs):
  bstack111llll1_opy_ = None
  if test:
    bstack111llll1_opy_ = str(test.name)
  bstack111ll1ll1_opy_(test, bstack111llll1_opy_)
  bstack1llll1l1_opy_(self, test, *args, **kwargs)
def bstack1lll111111_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack1l11111l1_opy_
  global CONFIG
  global bstack1l1ll1ll1_opy_
  global bstack111l1llll_opy_
  bstack111lll1l_opy_ = None
  try:
    if bstack1ll11111l_opy_(threading.current_thread(), bstack1lll1l1_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨં"), None):
      try:
        if not bstack111l1llll_opy_:
          with open(os.path.join(os.path.expanduser(bstack1lll1l1_opy_ (u"ࠪࢂࠬઃ")), bstack1lll1l1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫ઄"), bstack1lll1l1_opy_ (u"ࠬ࠴ࡳࡦࡵࡶ࡭ࡴࡴࡩࡥࡵ࠱ࡸࡽࡺࠧઅ"))) as f:
            bstack1111l1lll_opy_ = json.loads(bstack1lll1l1_opy_ (u"ࠨࡻࠣઆ") + f.read().strip() + bstack1lll1l1_opy_ (u"ࠧࠣࡺࠥ࠾ࠥࠨࡹࠣࠩઇ") + bstack1lll1l1_opy_ (u"ࠣࡿࠥઈ"))
            bstack111l1llll_opy_ = bstack1111l1lll_opy_[str(threading.get_ident())]
      except:
        pass
      if bstack1l1ll1ll1_opy_:
        for driver in bstack1l1ll1ll1_opy_:
          if bstack111l1llll_opy_ == driver.session_id:
            bstack111lll1l_opy_ = driver
    bstack111l111ll_opy_ = bstack11111111l_opy_.bstack1llll1l1l_opy_(CONFIG, test.tags)
    if bstack111lll1l_opy_:
      threading.current_thread().isA11yTest = bstack11111111l_opy_.bstack1lll1l1l11_opy_(bstack111lll1l_opy_, bstack111l111ll_opy_)
    else:
      threading.current_thread().isA11yTest = bstack111l111ll_opy_
  except:
    pass
  bstack1l11111l1_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack1ll11111ll_opy_
  bstack1ll11111ll_opy_ = self._test
def bstack1ll111lll1_opy_():
  global bstack1ll111l11_opy_
  try:
    if os.path.exists(bstack1ll111l11_opy_):
      os.remove(bstack1ll111l11_opy_)
  except Exception as e:
    logger.debug(bstack1lll1l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡩ࡫࡬ࡦࡶ࡬ࡲ࡬ࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬઉ") + str(e))
def bstack111111111_opy_():
  global bstack1ll111l11_opy_
  bstack1llll1ll1l_opy_ = {}
  try:
    if not os.path.isfile(bstack1ll111l11_opy_):
      with open(bstack1ll111l11_opy_, bstack1lll1l1_opy_ (u"ࠪࡻࠬઊ")):
        pass
      with open(bstack1ll111l11_opy_, bstack1lll1l1_opy_ (u"ࠦࡼ࠱ࠢઋ")) as outfile:
        json.dump({}, outfile)
    if os.path.exists(bstack1ll111l11_opy_):
      bstack1llll1ll1l_opy_ = json.load(open(bstack1ll111l11_opy_, bstack1lll1l1_opy_ (u"ࠬࡸࡢࠨઌ")))
  except Exception as e:
    logger.debug(bstack1lll1l1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡴࡨࡥࡩ࡯࡮ࡨࠢࡵࡳࡧࡵࡴࠡࡴࡨࡴࡴࡸࡴࠡࡨ࡬ࡰࡪࡀࠠࠨઍ") + str(e))
  finally:
    return bstack1llll1ll1l_opy_
def bstack1ll1l1l1l_opy_(platform_index, item_index):
  global bstack1ll111l11_opy_
  try:
    bstack1llll1ll1l_opy_ = bstack111111111_opy_()
    bstack1llll1ll1l_opy_[item_index] = platform_index
    with open(bstack1ll111l11_opy_, bstack1lll1l1_opy_ (u"ࠢࡸ࠭ࠥ઎")) as outfile:
      json.dump(bstack1llll1ll1l_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1lll1l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡻࡷ࡯ࡴࡪࡰࡪࠤࡹࡵࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹࠦࡦࡪ࡮ࡨ࠾ࠥ࠭એ") + str(e))
def bstack1lllll11ll_opy_(bstack111l11ll_opy_):
  global CONFIG
  bstack1lllll1ll1_opy_ = bstack1lll1l1_opy_ (u"ࠩࠪઐ")
  if not bstack1lll1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ઑ") in CONFIG:
    logger.info(bstack1lll1l1_opy_ (u"ࠫࡓࡵࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠣࡴࡦࡹࡳࡦࡦࠣࡹࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡧࡦࡰࡨࡶࡦࡺࡥࠡࡴࡨࡴࡴࡸࡴࠡࡨࡲࡶࠥࡘ࡯ࡣࡱࡷࠤࡷࡻ࡮ࠨ઒"))
  try:
    platform = CONFIG[bstack1lll1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨઓ")][bstack111l11ll_opy_]
    if bstack1lll1l1_opy_ (u"࠭࡯ࡴࠩઔ") in platform:
      bstack1lllll1ll1_opy_ += str(platform[bstack1lll1l1_opy_ (u"ࠧࡰࡵࠪક")]) + bstack1lll1l1_opy_ (u"ࠨ࠮ࠣࠫખ")
    if bstack1lll1l1_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬગ") in platform:
      bstack1lllll1ll1_opy_ += str(platform[bstack1lll1l1_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ઘ")]) + bstack1lll1l1_opy_ (u"ࠫ࠱ࠦࠧઙ")
    if bstack1lll1l1_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩચ") in platform:
      bstack1lllll1ll1_opy_ += str(platform[bstack1lll1l1_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪછ")]) + bstack1lll1l1_opy_ (u"ࠧ࠭ࠢࠪજ")
    if bstack1lll1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪઝ") in platform:
      bstack1lllll1ll1_opy_ += str(platform[bstack1lll1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫઞ")]) + bstack1lll1l1_opy_ (u"ࠪ࠰ࠥ࠭ટ")
    if bstack1lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩઠ") in platform:
      bstack1lllll1ll1_opy_ += str(platform[bstack1lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪડ")]) + bstack1lll1l1_opy_ (u"࠭ࠬࠡࠩઢ")
    if bstack1lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨણ") in platform:
      bstack1lllll1ll1_opy_ += str(platform[bstack1lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩત")]) + bstack1lll1l1_opy_ (u"ࠩ࠯ࠤࠬથ")
  except Exception as e:
    logger.debug(bstack1lll1l1_opy_ (u"ࠪࡗࡴࡳࡥࠡࡧࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡴࡥࡳࡣࡷ࡭ࡳ࡭ࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠢࡶࡸࡷ࡯࡮ࡨࠢࡩࡳࡷࠦࡲࡦࡲࡲࡶࡹࠦࡧࡦࡰࡨࡶࡦࡺࡩࡰࡰࠪદ") + str(e))
  finally:
    if bstack1lllll1ll1_opy_[len(bstack1lllll1ll1_opy_) - 2:] == bstack1lll1l1_opy_ (u"ࠫ࠱ࠦࠧધ"):
      bstack1lllll1ll1_opy_ = bstack1lllll1ll1_opy_[:-2]
    return bstack1lllll1ll1_opy_
def bstack1l1lll11l1_opy_(path, bstack1lllll1ll1_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack1ll11ll1l1_opy_ = ET.parse(path)
    bstack1l1l1l1ll1_opy_ = bstack1ll11ll1l1_opy_.getroot()
    bstack1l1lll1l1_opy_ = None
    for suite in bstack1l1l1l1ll1_opy_.iter(bstack1lll1l1_opy_ (u"ࠬࡹࡵࡪࡶࡨࠫન")):
      if bstack1lll1l1_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭઩") in suite.attrib:
        suite.attrib[bstack1lll1l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬપ")] += bstack1lll1l1_opy_ (u"ࠨࠢࠪફ") + bstack1lllll1ll1_opy_
        bstack1l1lll1l1_opy_ = suite
    bstack1ll11lllll_opy_ = None
    for robot in bstack1l1l1l1ll1_opy_.iter(bstack1lll1l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨબ")):
      bstack1ll11lllll_opy_ = robot
    bstack111lll1l1_opy_ = len(bstack1ll11lllll_opy_.findall(bstack1lll1l1_opy_ (u"ࠪࡷࡺ࡯ࡴࡦࠩભ")))
    if bstack111lll1l1_opy_ == 1:
      bstack1ll11lllll_opy_.remove(bstack1ll11lllll_opy_.findall(bstack1lll1l1_opy_ (u"ࠫࡸࡻࡩࡵࡧࠪમ"))[0])
      bstack1l1l11lll_opy_ = ET.Element(bstack1lll1l1_opy_ (u"ࠬࡹࡵࡪࡶࡨࠫય"), attrib={bstack1lll1l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫર"): bstack1lll1l1_opy_ (u"ࠧࡔࡷ࡬ࡸࡪࡹࠧ઱"), bstack1lll1l1_opy_ (u"ࠨ࡫ࡧࠫલ"): bstack1lll1l1_opy_ (u"ࠩࡶ࠴ࠬળ")})
      bstack1ll11lllll_opy_.insert(1, bstack1l1l11lll_opy_)
      bstack1111ll1ll_opy_ = None
      for suite in bstack1ll11lllll_opy_.iter(bstack1lll1l1_opy_ (u"ࠪࡷࡺ࡯ࡴࡦࠩ઴")):
        bstack1111ll1ll_opy_ = suite
      bstack1111ll1ll_opy_.append(bstack1l1lll1l1_opy_)
      bstack11lllll11_opy_ = None
      for status in bstack1l1lll1l1_opy_.iter(bstack1lll1l1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫવ")):
        bstack11lllll11_opy_ = status
      bstack1111ll1ll_opy_.append(bstack11lllll11_opy_)
    bstack1ll11ll1l1_opy_.write(path)
  except Exception as e:
    logger.debug(bstack1lll1l1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡵࡷ࡮ࡴࡧࠡࡹ࡫࡭ࡱ࡫ࠠࡨࡧࡱࡩࡷࡧࡴࡪࡰࡪࠤࡷࡵࡢࡰࡶࠣࡶࡪࡶ࡯ࡳࡶࠪશ") + str(e))
def bstack1l1l1lll1_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack1ll111ll_opy_
  global CONFIG
  if bstack1lll1l1_opy_ (u"ࠨࡰࡺࡶ࡫ࡳࡳࡶࡡࡵࡪࠥષ") in options:
    del options[bstack1lll1l1_opy_ (u"ࠢࡱࡻࡷ࡬ࡴࡴࡰࡢࡶ࡫ࠦસ")]
  bstack11ll11ll1_opy_ = bstack111111111_opy_()
  for bstack11111l1l_opy_ in bstack11ll11ll1_opy_.keys():
    path = os.path.join(os.getcwd(), bstack1lll1l1_opy_ (u"ࠨࡲࡤࡦࡴࡺ࡟ࡳࡧࡶࡹࡱࡺࡳࠨહ"), str(bstack11111l1l_opy_), bstack1lll1l1_opy_ (u"ࠩࡲࡹࡹࡶࡵࡵ࠰ࡻࡱࡱ࠭઺"))
    bstack1l1lll11l1_opy_(path, bstack1lllll11ll_opy_(bstack11ll11ll1_opy_[bstack11111l1l_opy_]))
  bstack1ll111lll1_opy_()
  return bstack1ll111ll_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack1ll11ll11_opy_(self, ff_profile_dir):
  global bstack1111lll1_opy_
  if not ff_profile_dir:
    return None
  return bstack1111lll1_opy_(self, ff_profile_dir)
def bstack1l1llllll_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack11l1lll11_opy_
  bstack1lllllll11_opy_ = []
  if bstack1lll1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭઻") in CONFIG:
    bstack1lllllll11_opy_ = CONFIG[bstack1lll1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹ઼ࠧ")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack1lll1l1_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࠨઽ")],
      pabot_args[bstack1lll1l1_opy_ (u"ࠨࡶࡦࡴࡥࡳࡸ࡫ࠢા")],
      argfile,
      pabot_args.get(bstack1lll1l1_opy_ (u"ࠢࡩ࡫ࡹࡩࠧિ")),
      pabot_args[bstack1lll1l1_opy_ (u"ࠣࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠦી")],
      platform[0],
      bstack11l1lll11_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack1lll1l1_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡪ࡮ࡲࡥࡴࠤુ")] or [(bstack1lll1l1_opy_ (u"ࠥࠦૂ"), None)]
    for platform in enumerate(bstack1lllllll11_opy_)
  ]
def bstack1111lll11_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack1l111llll_opy_=bstack1lll1l1_opy_ (u"ࠫࠬૃ")):
  global bstack1ll1l1111_opy_
  self.platform_index = platform_index
  self.bstack1llll11l11_opy_ = bstack1l111llll_opy_
  bstack1ll1l1111_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack1lll111l1_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1l1ll1l1l1_opy_
  global bstack1llllllll1_opy_
  if not bstack1lll1l1_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧૄ") in item.options:
    item.options[bstack1lll1l1_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨૅ")] = []
  for v in item.options[bstack1lll1l1_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩ૆")]:
    if bstack1lll1l1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡑࡎࡄࡘࡋࡕࡒࡎࡋࡑࡈࡊ࡞ࠧે") in v:
      item.options[bstack1lll1l1_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫૈ")].remove(v)
    if bstack1lll1l1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡆࡐࡎࡇࡒࡈࡕࠪૉ") in v:
      item.options[bstack1lll1l1_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭૊")].remove(v)
  item.options[bstack1lll1l1_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧો")].insert(0, bstack1lll1l1_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡖࡌࡂࡖࡉࡓࡗࡓࡉࡏࡆࡈ࡜࠿ࢁࡽࠨૌ").format(item.platform_index))
  item.options[bstack1lll1l1_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦ્ࠩ")].insert(0, bstack1lll1l1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡅࡇࡉࡐࡔࡉࡁࡍࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖ࠿ࢁࡽࠨ૎").format(item.bstack1llll11l11_opy_))
  if bstack1llllllll1_opy_:
    item.options[bstack1lll1l1_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫ૏")].insert(0, bstack1lll1l1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡆࡐࡎࡇࡒࡈࡕ࠽ࡿࢂ࠭ૐ").format(bstack1llllllll1_opy_))
  return bstack1l1ll1l1l1_opy_(caller_id, datasources, is_last, item, outs_dir)
def bstack1ll1ll1111_opy_(command, item_index):
  if bstack11l1l11l_opy_.get_property(bstack1lll1l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬ૑")):
    os.environ[bstack1lll1l1_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭૒")] = json.dumps(CONFIG[bstack1lll1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ૓")][item_index % bstack111111lll_opy_])
  global bstack1llllllll1_opy_
  if bstack1llllllll1_opy_:
    command[0] = command[0].replace(bstack1lll1l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭૔"), bstack1lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠭ࡴࡦ࡮ࠤࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠥ࠳࠭ࡣࡵࡷࡥࡨࡱ࡟ࡪࡶࡨࡱࡤ࡯࡮ࡥࡧࡻࠤࠬ૕") + str(
      item_index) + bstack1lll1l1_opy_ (u"ࠩࠣࠫ૖") + bstack1llllllll1_opy_, 1)
  else:
    command[0] = command[0].replace(bstack1lll1l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ૗"),
                                    bstack1lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠰ࡷࡩࡱࠠࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠡ࠯࠰ࡦࡸࡺࡡࡤ࡭ࡢ࡭ࡹ࡫࡭ࡠ࡫ࡱࡨࡪࡾࠠࠨ૘") + str(item_index), 1)
def bstack1l1l1l11ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack111ll1l1l_opy_
  bstack1ll1ll1111_opy_(command, item_index)
  return bstack111ll1l1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
def bstack1ll1llll11_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack111ll1l1l_opy_
  bstack1ll1ll1111_opy_(command, item_index)
  return bstack111ll1l1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
def bstack1l1111ll1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack111ll1l1l_opy_
  bstack1ll1ll1111_opy_(command, item_index)
  return bstack111ll1l1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
def bstack1l1l11ll1_opy_(self, runner, quiet=False, capture=True):
  global bstack1lll11llll_opy_
  bstack1lll1l11_opy_ = bstack1lll11llll_opy_(self, runner, quiet=False, capture=True)
  if self.exception:
    if not hasattr(runner, bstack1lll1l1_opy_ (u"ࠬ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࡠࡣࡵࡶࠬ૙")):
      runner.exception_arr = []
    if not hasattr(runner, bstack1lll1l1_opy_ (u"࠭ࡥࡹࡥࡢࡸࡷࡧࡣࡦࡤࡤࡧࡰࡥࡡࡳࡴࠪ૚")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack1lll1l11_opy_
def bstack1l11llll_opy_(self, name, context, *args):
  os.environ[bstack1lll1l1_opy_ (u"ࠧࡄࡗࡕࡖࡊࡔࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡈࡆ࡚ࡁࠨ૛")] = json.dumps(CONFIG[bstack1lll1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૜")][int(threading.current_thread()._name) % bstack111111lll_opy_])
  global bstack111111l11_opy_
  if name == bstack1lll1l1_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡩࡩࡦࡺࡵࡳࡧࠪ૝"):
    bstack111111l11_opy_(self, name, context, *args)
    try:
      if not bstack111lllll1_opy_:
        bstack111lll1l_opy_ = threading.current_thread().bstackSessionDriver if bstack1lll11lll1_opy_(bstack1lll1l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩ૞")) else context.browser
        bstack111lll1ll_opy_ = str(self.feature.name)
        bstack1llllll11l_opy_(context, bstack111lll1ll_opy_)
        bstack111lll1l_opy_.execute_script(bstack1lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩ૟") + json.dumps(bstack111lll1ll_opy_) + bstack1lll1l1_opy_ (u"ࠬࢃࡽࠨૠ"))
      self.driver_before_scenario = False
    except Exception as e:
      logger.debug(bstack1lll1l1_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥ࡯࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡨࡨࡥࡹࡻࡲࡦ࠼ࠣࡿࢂ࠭ૡ").format(str(e)))
  elif name == bstack1lll1l1_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠩૢ"):
    bstack111111l11_opy_(self, name, context, *args)
    try:
      if not hasattr(self, bstack1lll1l1_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࡠࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪૣ")):
        self.driver_before_scenario = True
      if (not bstack111lllll1_opy_):
        scenario_name = args[0].name
        feature_name = bstack111lll1ll_opy_ = str(self.feature.name)
        bstack111lll1ll_opy_ = feature_name + bstack1lll1l1_opy_ (u"ࠩࠣ࠱ࠥ࠭૤") + scenario_name
        bstack111lll1l_opy_ = threading.current_thread().bstackSessionDriver if bstack1lll11lll1_opy_(bstack1lll1l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩ૥")) else context.browser
        if self.driver_before_scenario:
          bstack1llllll11l_opy_(context, bstack111lll1ll_opy_)
          bstack111lll1l_opy_.execute_script(bstack1lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩ૦") + json.dumps(bstack111lll1ll_opy_) + bstack1lll1l1_opy_ (u"ࠬࢃࡽࠨ૧"))
    except Exception as e:
      logger.debug(bstack1lll1l1_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥ࡯࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡵࡦࡩࡳࡧࡲࡪࡱ࠽ࠤࢀࢃࠧ૨").format(str(e)))
  elif name == bstack1lll1l1_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠨ૩"):
    try:
      bstack1ll1ll11l1_opy_ = args[0].status.name
      bstack111lll1l_opy_ = threading.current_thread().bstackSessionDriver if bstack1lll1l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧ૪") in threading.current_thread().__dict__.keys() else context.browser
      if str(bstack1ll1ll11l1_opy_).lower() == bstack1lll1l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ૫"):
        bstack1lll1lll1l_opy_ = bstack1lll1l1_opy_ (u"ࠪࠫ૬")
        bstack1lllll111l_opy_ = bstack1lll1l1_opy_ (u"ࠫࠬ૭")
        bstack1lll11l11_opy_ = bstack1lll1l1_opy_ (u"ࠬ࠭૮")
        try:
          import traceback
          bstack1lll1lll1l_opy_ = self.exception.__class__.__name__
          bstack1l1llll1_opy_ = traceback.format_tb(self.exc_traceback)
          bstack1lllll111l_opy_ = bstack1lll1l1_opy_ (u"࠭ࠠࠨ૯").join(bstack1l1llll1_opy_)
          bstack1lll11l11_opy_ = bstack1l1llll1_opy_[-1]
        except Exception as e:
          logger.debug(bstack1ll1111l1_opy_.format(str(e)))
        bstack1lll1lll1l_opy_ += bstack1lll11l11_opy_
        bstack11l11ll11_opy_(context, json.dumps(str(args[0].name) + bstack1lll1l1_opy_ (u"ࠢࠡ࠯ࠣࡊࡦ࡯࡬ࡦࡦࠤࡠࡳࠨ૰") + str(bstack1lllll111l_opy_)),
                            bstack1lll1l1_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢ૱"))
        if self.driver_before_scenario:
          bstack1ll1111111_opy_(getattr(context, bstack1lll1l1_opy_ (u"ࠩࡳࡥ࡬࡫ࠧ૲"), None), bstack1lll1l1_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥ૳"), bstack1lll1lll1l_opy_)
          bstack111lll1l_opy_.execute_script(bstack1lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩ૴") + json.dumps(str(args[0].name) + bstack1lll1l1_opy_ (u"ࠧࠦ࠭ࠡࡈࡤ࡭ࡱ࡫ࡤࠢ࡞ࡱࠦ૵") + str(bstack1lllll111l_opy_)) + bstack1lll1l1_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦࡪࡸࡲࡰࡴࠥࢁࢂ࠭૶"))
        if self.driver_before_scenario:
          bstack1l1l11ll_opy_(bstack111lll1l_opy_, bstack1lll1l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ૷"), bstack1lll1l1_opy_ (u"ࠣࡕࡦࡩࡳࡧࡲࡪࡱࠣࡪࡦ࡯࡬ࡦࡦࠣࡻ࡮ࡺࡨ࠻ࠢ࡟ࡲࠧ૸") + str(bstack1lll1lll1l_opy_))
      else:
        bstack11l11ll11_opy_(context, bstack1lll1l1_opy_ (u"ࠤࡓࡥࡸࡹࡥࡥࠣࠥૹ"), bstack1lll1l1_opy_ (u"ࠥ࡭ࡳ࡬࡯ࠣૺ"))
        if self.driver_before_scenario:
          bstack1ll1111111_opy_(getattr(context, bstack1lll1l1_opy_ (u"ࠫࡵࡧࡧࡦࠩૻ"), None), bstack1lll1l1_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧૼ"))
        bstack111lll1l_opy_.execute_script(bstack1lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫ૽") + json.dumps(str(args[0].name) + bstack1lll1l1_opy_ (u"ࠢࠡ࠯ࠣࡔࡦࡹࡳࡦࡦࠤࠦ૾")) + bstack1lll1l1_opy_ (u"ࠨ࠮ࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡩ࡯ࡨࡲࠦࢂࢃࠧ૿"))
        if self.driver_before_scenario:
          bstack1l1l11ll_opy_(bstack111lll1l_opy_, bstack1lll1l1_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤ଀"))
    except Exception as e:
      logger.debug(bstack1lll1l1_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦ࡭ࡢࡴ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥ࡯࡮ࠡࡣࡩࡸࡪࡸࠠࡧࡧࡤࡸࡺࡸࡥ࠻ࠢࡾࢁࠬଁ").format(str(e)))
  elif name == bstack1lll1l1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡪࡪࡧࡴࡶࡴࡨࠫଂ"):
    try:
      bstack111lll1l_opy_ = threading.current_thread().bstackSessionDriver if bstack1lll11lll1_opy_(bstack1lll1l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫଃ")) else context.browser
      if context.failed is True:
        bstack11l1l1lll_opy_ = []
        bstack1l1ll11l1l_opy_ = []
        bstack1l1ll11111_opy_ = []
        bstack1lll11ll_opy_ = bstack1lll1l1_opy_ (u"࠭ࠧ଄")
        try:
          import traceback
          for exc in self.exception_arr:
            bstack11l1l1lll_opy_.append(exc.__class__.__name__)
          for exc_tb in self.exc_traceback_arr:
            bstack1l1llll1_opy_ = traceback.format_tb(exc_tb)
            bstack11l111111_opy_ = bstack1lll1l1_opy_ (u"ࠧࠡࠩଅ").join(bstack1l1llll1_opy_)
            bstack1l1ll11l1l_opy_.append(bstack11l111111_opy_)
            bstack1l1ll11111_opy_.append(bstack1l1llll1_opy_[-1])
        except Exception as e:
          logger.debug(bstack1ll1111l1_opy_.format(str(e)))
        bstack1lll1lll1l_opy_ = bstack1lll1l1_opy_ (u"ࠨࠩଆ")
        for i in range(len(bstack11l1l1lll_opy_)):
          bstack1lll1lll1l_opy_ += bstack11l1l1lll_opy_[i] + bstack1l1ll11111_opy_[i] + bstack1lll1l1_opy_ (u"ࠩ࡟ࡲࠬଇ")
        bstack1lll11ll_opy_ = bstack1lll1l1_opy_ (u"ࠪࠤࠬଈ").join(bstack1l1ll11l1l_opy_)
        if not self.driver_before_scenario:
          bstack11l11ll11_opy_(context, bstack1lll11ll_opy_, bstack1lll1l1_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥଉ"))
          bstack1ll1111111_opy_(getattr(context, bstack1lll1l1_opy_ (u"ࠬࡶࡡࡨࡧࠪଊ"), None), bstack1lll1l1_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨଋ"), bstack1lll1lll1l_opy_)
          bstack111lll1l_opy_.execute_script(bstack1lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬଌ") + json.dumps(bstack1lll11ll_opy_) + bstack1lll1l1_opy_ (u"ࠨ࠮ࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡥࡳࡴࡲࡶࠧࢃࡽࠨ଍"))
          bstack1l1l11ll_opy_(bstack111lll1l_opy_, bstack1lll1l1_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤ଎"), bstack1lll1l1_opy_ (u"ࠥࡗࡴࡳࡥࠡࡵࡦࡩࡳࡧࡲࡪࡱࡶࠤ࡫ࡧࡩ࡭ࡧࡧ࠾ࠥࡢ࡮ࠣଏ") + str(bstack1lll1lll1l_opy_))
          bstack111lll11_opy_ = bstack1111lllll_opy_(bstack1lll11ll_opy_, self.feature.name, logger)
          if (bstack111lll11_opy_ != None):
            bstack1l1l1llll1_opy_.append(bstack111lll11_opy_)
      else:
        if not self.driver_before_scenario:
          bstack11l11ll11_opy_(context, bstack1lll1l1_opy_ (u"ࠦࡋ࡫ࡡࡵࡷࡵࡩ࠿ࠦࠢଐ") + str(self.feature.name) + bstack1lll1l1_opy_ (u"ࠧࠦࡰࡢࡵࡶࡩࡩࠧࠢ଑"), bstack1lll1l1_opy_ (u"ࠨࡩ࡯ࡨࡲࠦ଒"))
          bstack1ll1111111_opy_(getattr(context, bstack1lll1l1_opy_ (u"ࠧࡱࡣࡪࡩࠬଓ"), None), bstack1lll1l1_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣଔ"))
          bstack111lll1l_opy_.execute_script(bstack1lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧକ") + json.dumps(bstack1lll1l1_opy_ (u"ࠥࡊࡪࡧࡴࡶࡴࡨ࠾ࠥࠨଖ") + str(self.feature.name) + bstack1lll1l1_opy_ (u"ࠦࠥࡶࡡࡴࡵࡨࡨࠦࠨଗ")) + bstack1lll1l1_opy_ (u"ࠬ࠲ࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥ࡭ࡳ࡬࡯ࠣࡿࢀࠫଘ"))
          bstack1l1l11ll_opy_(bstack111lll1l_opy_, bstack1lll1l1_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ଙ"))
          bstack111lll11_opy_ = bstack1111lllll_opy_(bstack1lll11ll_opy_, self.feature.name, logger)
          if (bstack111lll11_opy_ != None):
            bstack1l1l1llll1_opy_.append(bstack111lll11_opy_)
    except Exception as e:
      logger.debug(bstack1lll1l1_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡱࡦࡸ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢ࡬ࡲࠥࡧࡦࡵࡧࡵࠤ࡫࡫ࡡࡵࡷࡵࡩ࠿ࠦࡻࡾࠩଚ").format(str(e)))
  else:
    bstack111111l11_opy_(self, name, context, *args)
  if name in [bstack1lll1l1_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡧࡧࡤࡸࡺࡸࡥࠨଛ"), bstack1lll1l1_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪଜ")]:
    bstack111111l11_opy_(self, name, context, *args)
    if (name == bstack1lll1l1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫଝ") and self.driver_before_scenario) or (
            name == bstack1lll1l1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡪࡪࡧࡴࡶࡴࡨࠫଞ") and not self.driver_before_scenario):
      try:
        bstack111lll1l_opy_ = threading.current_thread().bstackSessionDriver if bstack1lll11lll1_opy_(bstack1lll1l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫଟ")) else context.browser
        bstack111lll1l_opy_.quit()
      except Exception:
        pass
def bstack11l11l1ll_opy_(config, startdir):
  return bstack1lll1l1_opy_ (u"ࠨࡤࡳ࡫ࡹࡩࡷࡀࠠࡼ࠲ࢀࠦଠ").format(bstack1lll1l1_opy_ (u"ࠢࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠨଡ"))
notset = Notset()
def bstack1ll1lll11_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack1lll111l11_opy_
  if str(name).lower() == bstack1lll1l1_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࠨଢ"):
    return bstack1lll1l1_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠣଣ")
  else:
    return bstack1lll111l11_opy_(self, name, default, skip)
def bstack1l1lllll1l_opy_(item, when):
  global bstack11ll1l111_opy_
  try:
    bstack11ll1l111_opy_(item, when)
  except Exception as e:
    pass
def bstack1l1lll11ll_opy_():
  return
def bstack1lll1ll1l_opy_(type, name, status, reason, bstack1ll1l11l1_opy_, bstack11ll1ll1_opy_):
  bstack1l111ll1l_opy_ = {
    bstack1lll1l1_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪତ"): type,
    bstack1lll1l1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧଥ"): {}
  }
  if type == bstack1lll1l1_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧଦ"):
    bstack1l111ll1l_opy_[bstack1lll1l1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩଧ")][bstack1lll1l1_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ନ")] = bstack1ll1l11l1_opy_
    bstack1l111ll1l_opy_[bstack1lll1l1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ଩")][bstack1lll1l1_opy_ (u"ࠩࡧࡥࡹࡧࠧପ")] = json.dumps(str(bstack11ll1ll1_opy_))
  if type == bstack1lll1l1_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫଫ"):
    bstack1l111ll1l_opy_[bstack1lll1l1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧବ")][bstack1lll1l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪଭ")] = name
  if type == bstack1lll1l1_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩମ"):
    bstack1l111ll1l_opy_[bstack1lll1l1_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪଯ")][bstack1lll1l1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨର")] = status
    if status == bstack1lll1l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ଱"):
      bstack1l111ll1l_opy_[bstack1lll1l1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ଲ")][bstack1lll1l1_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫଳ")] = json.dumps(str(reason))
  bstack1ll1l11lll_opy_ = bstack1lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪ଴").format(json.dumps(bstack1l111ll1l_opy_))
  return bstack1ll1l11lll_opy_
def bstack11ll1111_opy_(driver_command, response):
    if driver_command == bstack1lll1l1_opy_ (u"࠭ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠪଵ"):
        bstack1l1ll11l_opy_.bstack1l1llll11l_opy_({
            bstack1lll1l1_opy_ (u"ࠧࡪ࡯ࡤ࡫ࡪ࠭ଶ"): response[bstack1lll1l1_opy_ (u"ࠨࡸࡤࡰࡺ࡫ࠧଷ")],
            bstack1lll1l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩସ"): bstack1l1ll11l_opy_.current_test_uuid()
        })
def bstack1lll1lll11_opy_(item, call, rep):
  global bstack1l1l1111l1_opy_
  global bstack1l1ll1ll1_opy_
  global bstack111lllll1_opy_
  name = bstack1lll1l1_opy_ (u"ࠪࠫହ")
  try:
    if rep.when == bstack1lll1l1_opy_ (u"ࠫࡨࡧ࡬࡭ࠩ଺"):
      bstack111l1llll_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack111lllll1_opy_:
          name = str(rep.nodeid)
          bstack1ll111111_opy_ = bstack1lll1ll1l_opy_(bstack1lll1l1_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭଻"), name, bstack1lll1l1_opy_ (u"଼࠭ࠧ"), bstack1lll1l1_opy_ (u"ࠧࠨଽ"), bstack1lll1l1_opy_ (u"ࠨࠩା"), bstack1lll1l1_opy_ (u"ࠩࠪି"))
          threading.current_thread().bstack11l1l1ll1_opy_ = name
          for driver in bstack1l1ll1ll1_opy_:
            if bstack111l1llll_opy_ == driver.session_id:
              driver.execute_script(bstack1ll111111_opy_)
      except Exception as e:
        logger.debug(bstack1lll1l1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠤ࡫ࡵࡲࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡹࡥࡴࡵ࡬ࡳࡳࡀࠠࡼࡿࠪୀ").format(str(e)))
      try:
        bstack1l1l111l11_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack1lll1l1_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬୁ"):
          status = bstack1lll1l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬୂ") if rep.outcome.lower() == bstack1lll1l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ୃ") else bstack1lll1l1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧୄ")
          reason = bstack1lll1l1_opy_ (u"ࠨࠩ୅")
          if status == bstack1lll1l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ୆"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack1lll1l1_opy_ (u"ࠪ࡭ࡳ࡬࡯ࠨେ") if status == bstack1lll1l1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫୈ") else bstack1lll1l1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ୉")
          data = name + bstack1lll1l1_opy_ (u"࠭ࠠࡱࡣࡶࡷࡪࡪࠡࠨ୊") if status == bstack1lll1l1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧୋ") else name + bstack1lll1l1_opy_ (u"ࠨࠢࡩࡥ࡮ࡲࡥࡥࠣࠣࠫୌ") + reason
          bstack11l11ll1l_opy_ = bstack1lll1ll1l_opy_(bstack1lll1l1_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨ୍ࠫ"), bstack1lll1l1_opy_ (u"ࠪࠫ୎"), bstack1lll1l1_opy_ (u"ࠫࠬ୏"), bstack1lll1l1_opy_ (u"ࠬ࠭୐"), level, data)
          for driver in bstack1l1ll1ll1_opy_:
            if bstack111l1llll_opy_ == driver.session_id:
              driver.execute_script(bstack11l11ll1l_opy_)
      except Exception as e:
        logger.debug(bstack1lll1l1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡧࡴࡴࡴࡦࡺࡷࠤ࡫ࡵࡲࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡹࡥࡴࡵ࡬ࡳࡳࡀࠠࡼࡿࠪ୑").format(str(e)))
  except Exception as e:
    logger.debug(bstack1lll1l1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡷࡹࡧࡴࡦࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࠠࡴࡶࡤࡸࡺࡹ࠺ࠡࡽࢀࠫ୒").format(str(e)))
  bstack1l1l1111l1_opy_(item, call, rep)
def bstack11l111l1_opy_(driver, bstack1l1ll111l_opy_):
  PercySDK.screenshot(driver, bstack1l1ll111l_opy_)
def bstack1ll1l1ll1_opy_(driver):
  if bstack1llll111ll_opy_.bstack111lll11l_opy_() is True or bstack1llll111ll_opy_.capturing() is True:
    return
  bstack1llll111ll_opy_.bstack1l1l111l_opy_()
  while not bstack1llll111ll_opy_.bstack111lll11l_opy_():
    bstack11l1l1l1_opy_ = bstack1llll111ll_opy_.bstack1l1l1ll1_opy_()
    bstack11l111l1_opy_(driver, bstack11l1l1l1_opy_)
  bstack1llll111ll_opy_.bstack1ll11ll1l_opy_()
def bstack1llll1l1ll_opy_(sequence, driver_command, response = None):
    try:
      if sequence != bstack1lll1l1_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࠨ୓"):
        return
      if not CONFIG.get(bstack1lll1l1_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨ୔"), False):
        return
      bstack11l1l1l1_opy_ = bstack1ll11111l_opy_(threading.current_thread(), bstack1lll1l1_opy_ (u"ࠪࡴࡪࡸࡣࡺࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭୕"), None)
      for command in bstack1lll1l1ll1_opy_:
        if command == driver_command:
          for driver in bstack1l1ll1ll1_opy_:
            bstack1ll1l1ll1_opy_(driver)
      bstack1lll11l111_opy_ = CONFIG.get(bstack1lll1l1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡆࡥࡵࡺࡵࡳࡧࡐࡳࡩ࡫ࠧୖ"), bstack1lll1l1_opy_ (u"ࠧࡧࡵࡵࡱࠥୗ"))
      if driver_command in bstack1l1ll1ll11_opy_[bstack1lll11l111_opy_]:
        bstack1llll111ll_opy_.bstack111l1l111_opy_(bstack11l1l1l1_opy_, driver_command)
    except Exception as e:
      pass
def bstack1lll11lll_opy_(framework_name):
  global bstack1ll11l1l11_opy_
  global bstack1ll111l1ll_opy_
  global bstack1llll1ll_opy_
  bstack1ll11l1l11_opy_ = framework_name
  logger.info(bstack1l1ll11l1_opy_.format(bstack1ll11l1l11_opy_.split(bstack1lll1l1_opy_ (u"࠭࠭ࠨ୘"))[0]))
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack1l11ll111_opy_:
      Service.start = bstack1ll1ll111l_opy_
      Service.stop = bstack111l1l11l_opy_
      webdriver.Remote.get = bstack1l1lll1l_opy_
      WebDriver.close = bstack1llll11l1_opy_
      WebDriver.quit = bstack11lll1111_opy_
      webdriver.Remote.__init__ = bstack1ll1ll1l1_opy_
      WebDriver.getAccessibilityResults = getAccessibilityResults
      WebDriver.bstack11l111l1l_opy_ = getAccessibilityResults
      WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
      WebDriver.bstack1ll1ll11ll_opy_ = getAccessibilityResultsSummary
    if not bstack1l11ll111_opy_ and bstack1l1ll11l_opy_.on():
      webdriver.Remote.__init__ = bstack1ll11lll11_opy_
    if bstack1lll1l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭୙") in str(framework_name).lower() and bstack1l1ll11l_opy_.on():
      WebDriver.execute = bstack1ll11ll1_opy_
    bstack1ll111l1ll_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack1l11ll111_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack1111llll1_opy_
  except Exception as e:
    pass
  bstack1l1111l1l_opy_()
  if not bstack1ll111l1ll_opy_:
    bstack1lll1lllll_opy_(bstack1lll1l1_opy_ (u"ࠣࡒࡤࡧࡰࡧࡧࡦࡵࠣࡲࡴࡺࠠࡪࡰࡶࡸࡦࡲ࡬ࡦࡦࠥ୚"), bstack1ll1lll11l_opy_)
  if bstack1ll11llll1_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      RemoteConnection._get_proxy_url = bstack11l111ll_opy_
    except Exception as e:
      logger.error(bstack11lll111_opy_.format(str(e)))
  if bstack1l11l1l11_opy_():
    bstack111ll111_opy_(CONFIG, logger)
  if (bstack1lll1l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ୛") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if CONFIG.get(bstack1lll1l1_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩଡ଼"), False):
          bstack11l111lll_opy_(bstack1llll1l1ll_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack1ll11ll11_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1111lll1l_opy_
      except Exception as e:
        logger.warn(bstack11111ll1l_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack1l1lll1l1l_opy_
      except Exception as e:
        logger.debug(bstack1lll1111ll_opy_ + str(e))
    except Exception as e:
      bstack1lll1lllll_opy_(e, bstack11111ll1l_opy_)
    Output.start_test = bstack1l1lll1l11_opy_
    Output.end_test = bstack1l1lll1ll_opy_
    TestStatus.__init__ = bstack1lll111111_opy_
    QueueItem.__init__ = bstack1111lll11_opy_
    pabot._create_items = bstack1l1llllll_opy_
    try:
      from pabot import __version__ as bstack11111l1ll_opy_
      if version.parse(bstack11111l1ll_opy_) >= version.parse(bstack1lll1l1_opy_ (u"ࠫ࠷࠴࠱࠶࠰࠳ࠫଢ଼")):
        pabot._run = bstack1l1111ll1_opy_
      elif version.parse(bstack11111l1ll_opy_) >= version.parse(bstack1lll1l1_opy_ (u"ࠬ࠸࠮࠲࠵࠱࠴ࠬ୞")):
        pabot._run = bstack1ll1llll11_opy_
      else:
        pabot._run = bstack1l1l1l11ll_opy_
    except Exception as e:
      pabot._run = bstack1l1l1l11ll_opy_
    pabot._create_command_for_execution = bstack1lll111l1_opy_
    pabot._report_results = bstack1l1l1lll1_opy_
  if bstack1lll1l1_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ୟ") in str(framework_name).lower():
    if not bstack1l11ll111_opy_:
      return
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1lll1lllll_opy_(e, bstack111ll111l_opy_)
    Runner.run_hook = bstack1l11llll_opy_
    Step.run = bstack1l1l11ll1_opy_
  if bstack1lll1l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧୠ") in str(framework_name).lower():
    if not bstack1l11ll111_opy_:
      return
    try:
      if CONFIG.get(bstack1lll1l1_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧୡ"), False):
          bstack11l111lll_opy_(bstack1llll1l1ll_opy_)
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack11l11l1ll_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack1l1lll11ll_opy_
      Config.getoption = bstack1ll1lll11_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack1lll1lll11_opy_
    except Exception as e:
      pass
def bstack1ll1111lll_opy_():
  global CONFIG
  if bstack1lll1l1_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩୢ") in CONFIG and int(CONFIG[bstack1lll1l1_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪୣ")]) > 1:
    logger.warn(bstack1lll1ll1ll_opy_)
def bstack111llll1l_opy_(arg, bstack111l1l11_opy_, bstack11111111_opy_=None):
  global CONFIG
  global bstack111111ll_opy_
  global bstack1lll1111l_opy_
  global bstack1l11ll111_opy_
  global bstack11l1l11l_opy_
  bstack1llllll1l1_opy_ = bstack1lll1l1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ୤")
  if bstack111l1l11_opy_ and isinstance(bstack111l1l11_opy_, str):
    bstack111l1l11_opy_ = eval(bstack111l1l11_opy_)
  CONFIG = bstack111l1l11_opy_[bstack1lll1l1_opy_ (u"ࠬࡉࡏࡏࡈࡌࡋࠬ୥")]
  bstack111111ll_opy_ = bstack111l1l11_opy_[bstack1lll1l1_opy_ (u"࠭ࡈࡖࡄࡢ࡙ࡗࡒࠧ୦")]
  bstack1lll1111l_opy_ = bstack111l1l11_opy_[bstack1lll1l1_opy_ (u"ࠧࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩ୧")]
  bstack1l11ll111_opy_ = bstack111l1l11_opy_[bstack1lll1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫ୨")]
  bstack11l1l11l_opy_.bstack1l1111l1_opy_(bstack1lll1l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪ୩"), bstack1l11ll111_opy_)
  os.environ[bstack1lll1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬ୪")] = bstack1llllll1l1_opy_
  os.environ[bstack1lll1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࠪ୫")] = json.dumps(CONFIG)
  os.environ[bstack1lll1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡍ࡛ࡂࡠࡗࡕࡐࠬ୬")] = bstack111111ll_opy_
  os.environ[bstack1lll1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧ୭")] = str(bstack1lll1111l_opy_)
  os.environ[bstack1lll1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐ࡚ࡖࡈࡗ࡙ࡥࡐࡍࡗࡊࡍࡓ࠭୮")] = str(True)
  if bstack1l1l1l1111_opy_(arg, [bstack1lll1l1_opy_ (u"ࠨ࠯ࡱࠫ୯"), bstack1lll1l1_opy_ (u"ࠩ࠰࠱ࡳࡻ࡭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪ୰")]) != -1:
    os.environ[bstack1lll1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓ࡝࡙ࡋࡓࡕࡡࡓࡅࡗࡇࡌࡍࡇࡏࠫୱ")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack1l111lll1_opy_)
    return
  bstack1ll1l11l11_opy_()
  global bstack11ll11ll_opy_
  global bstack1lll1llll_opy_
  global bstack11l1lll11_opy_
  global bstack1llllllll1_opy_
  global bstack1ll11l1ll1_opy_
  global bstack1llll1ll_opy_
  global bstack1l1l1lll1l_opy_
  arg.append(bstack1lll1l1_opy_ (u"ࠦ࠲࡝ࠢ୲"))
  arg.append(bstack1lll1l1_opy_ (u"ࠧ࡯ࡧ࡯ࡱࡵࡩ࠿ࡓ࡯ࡥࡷ࡯ࡩࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡩ࡮ࡲࡲࡶࡹ࡫ࡤ࠻ࡲࡼࡸࡪࡹࡴ࠯ࡒࡼࡸࡪࡹࡴࡘࡣࡵࡲ࡮ࡴࡧࠣ୳"))
  arg.append(bstack1lll1l1_opy_ (u"ࠨ࠭ࡘࠤ୴"))
  arg.append(bstack1lll1l1_opy_ (u"ࠢࡪࡩࡱࡳࡷ࡫࠺ࡕࡪࡨࠤ࡭ࡵ࡯࡬࡫ࡰࡴࡱࠨ୵"))
  global bstack11llll1l_opy_
  global bstack1l11l1111_opy_
  global bstack1l11111l1_opy_
  global bstack1111lll1_opy_
  global bstack1ll1l1111_opy_
  global bstack1l1ll1l1l1_opy_
  global bstack1lll1l1l1_opy_
  global bstack1llllll1ll_opy_
  global bstack1l1ll11l11_opy_
  global bstack1lll111l11_opy_
  global bstack11ll1l111_opy_
  global bstack1l1l1111l1_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack11llll1l_opy_ = webdriver.Remote.__init__
    bstack1l11l1111_opy_ = WebDriver.quit
    bstack1lll1l1l1_opy_ = WebDriver.close
    bstack1llllll1ll_opy_ = WebDriver.get
  except Exception as e:
    pass
  if bstack1lll1l11l1_opy_(CONFIG) and bstack1l1l11l111_opy_():
    if bstack11llll1ll_opy_() < version.parse(bstack1llll1l1l1_opy_):
      logger.error(bstack11111l11_opy_.format(bstack11llll1ll_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack1l1ll11l11_opy_ = RemoteConnection._get_proxy_url
      except Exception as e:
        logger.error(bstack11lll111_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack1lll111l11_opy_ = Config.getoption
    from _pytest import runner
    bstack11ll1l111_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack1l1llll1ll_opy_)
  try:
    from pytest_bdd import reporting
    bstack1l1l1111l1_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack1lll1l1_opy_ (u"ࠨࡒ࡯ࡩࡦࡹࡥࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡰࠢࡵࡹࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࡴࠩ୶"))
  bstack11l1lll11_opy_ = CONFIG.get(bstack1lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭୷"), {}).get(bstack1lll1l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ୸"))
  bstack1l1l1lll1l_opy_ = True
  bstack1lll11lll_opy_(bstack1111ll11l_opy_)
  os.environ[bstack1lll1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢ࡙ࡘࡋࡒࡏࡃࡐࡉࠬ୹")] = CONFIG[bstack1lll1l1_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ୺")]
  os.environ[bstack1lll1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡃࡄࡇࡖࡗࡤࡑࡅ࡚ࠩ୻")] = CONFIG[bstack1lll1l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ୼")]
  os.environ[bstack1lll1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫ୽")] = bstack1l11ll111_opy_.__str__()
  from _pytest.config import main as bstack1ll111lll_opy_
  bstack1ll111lll_opy_(arg)
  if bstack1lll1l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠭୾") in multiprocessing.current_process().__dict__.keys():
    for bstack11l111l11_opy_ in multiprocessing.current_process().bstack_error_list:
      bstack11111111_opy_.append(bstack11l111l11_opy_)
def bstack11llllll_opy_(arg):
  bstack1lll11lll_opy_(bstack11111l111_opy_)
  os.environ[bstack1lll1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ୿")] = str(bstack1lll1111l_opy_)
  from behave.__main__ import main as bstack1111l1ll1_opy_
  bstack1111l1ll1_opy_(arg)
def bstack11ll1l1l1_opy_():
  logger.info(bstack1lll1l1l1l_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack1lll1l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪ஀"), help=bstack1lll1l1_opy_ (u"ࠬࡍࡥ࡯ࡧࡵࡥࡹ࡫ࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡣࡰࡰࡩ࡭࡬࠭஁"))
  parser.add_argument(bstack1lll1l1_opy_ (u"࠭࠭ࡶࠩஂ"), bstack1lll1l1_opy_ (u"ࠧ࠮࠯ࡸࡷࡪࡸ࡮ࡢ࡯ࡨࠫஃ"), help=bstack1lll1l1_opy_ (u"ࠨ࡛ࡲࡹࡷࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡻࡳࡦࡴࡱࡥࡲ࡫ࠧ஄"))
  parser.add_argument(bstack1lll1l1_opy_ (u"ࠩ࠰࡯ࠬஅ"), bstack1lll1l1_opy_ (u"ࠪ࠱࠲ࡱࡥࡺࠩஆ"), help=bstack1lll1l1_opy_ (u"ࠫ࡞ࡵࡵࡳࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡣࡦࡧࡪࡹࡳࠡ࡭ࡨࡽࠬஇ"))
  parser.add_argument(bstack1lll1l1_opy_ (u"ࠬ࠳ࡦࠨஈ"), bstack1lll1l1_opy_ (u"࠭࠭࠮ࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫஉ"), help=bstack1lll1l1_opy_ (u"࡚ࠧࡱࡸࡶࠥࡺࡥࡴࡶࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ஊ"))
  bstack11ll11l1_opy_ = parser.parse_args()
  try:
    bstack1l1l111ll_opy_ = bstack1lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡨࡧࡱࡩࡷ࡯ࡣ࠯ࡻࡰࡰ࠳ࡹࡡ࡮ࡲ࡯ࡩࠬ஋")
    if bstack11ll11l1_opy_.framework and bstack11ll11l1_opy_.framework not in (bstack1lll1l1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ஌"), bstack1lll1l1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠶ࠫ஍")):
      bstack1l1l111ll_opy_ = bstack1lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠴ࡹ࡮࡮࠱ࡷࡦࡳࡰ࡭ࡧࠪஎ")
    bstack11ll111ll_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1l1l111ll_opy_)
    bstack1l11l11ll_opy_ = open(bstack11ll111ll_opy_, bstack1lll1l1_opy_ (u"ࠬࡸࠧஏ"))
    bstack1lll1l111l_opy_ = bstack1l11l11ll_opy_.read()
    bstack1l11l11ll_opy_.close()
    if bstack11ll11l1_opy_.username:
      bstack1lll1l111l_opy_ = bstack1lll1l111l_opy_.replace(bstack1lll1l1_opy_ (u"࡙࠭ࡐࡗࡕࡣ࡚࡙ࡅࡓࡐࡄࡑࡊ࠭ஐ"), bstack11ll11l1_opy_.username)
    if bstack11ll11l1_opy_.key:
      bstack1lll1l111l_opy_ = bstack1lll1l111l_opy_.replace(bstack1lll1l1_opy_ (u"࡚ࠧࡑࡘࡖࡤࡇࡃࡄࡇࡖࡗࡤࡑࡅ࡚ࠩ஑"), bstack11ll11l1_opy_.key)
    if bstack11ll11l1_opy_.framework:
      bstack1lll1l111l_opy_ = bstack1lll1l111l_opy_.replace(bstack1lll1l1_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩஒ"), bstack11ll11l1_opy_.framework)
    file_name = bstack1lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰࠬஓ")
    file_path = os.path.abspath(file_name)
    bstack1l11111l_opy_ = open(file_path, bstack1lll1l1_opy_ (u"ࠪࡻࠬஔ"))
    bstack1l11111l_opy_.write(bstack1lll1l111l_opy_)
    bstack1l11111l_opy_.close()
    logger.info(bstack1ll1l1llll_opy_)
    try:
      os.environ[bstack1lll1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭க")] = bstack11ll11l1_opy_.framework if bstack11ll11l1_opy_.framework != None else bstack1lll1l1_opy_ (u"ࠧࠨ஖")
      config = yaml.safe_load(bstack1lll1l111l_opy_)
      config[bstack1lll1l1_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭஗")] = bstack1lll1l1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴ࠭ࡴࡧࡷࡹࡵ࠭஘")
      bstack1111l11ll_opy_(bstack11llll111_opy_, config)
    except Exception as e:
      logger.debug(bstack11ll1lll_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack1l11ll1l_opy_.format(str(e)))
def bstack1111l11ll_opy_(bstack1111l11l1_opy_, config, bstack1ll11111_opy_={}):
  global bstack1l11ll111_opy_
  global bstack1ll11l11ll_opy_
  if not config:
    return
  bstack1l1ll1l11_opy_ = bstack1l11ll1ll_opy_ if not bstack1l11ll111_opy_ else (
    bstack1l1lll111l_opy_ if bstack1lll1l1_opy_ (u"ࠨࡣࡳࡴࠬங") in config else bstack11l11111_opy_)
  data = {
    bstack1lll1l1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫச"): config[bstack1lll1l1_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬ஛")],
    bstack1lll1l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧஜ"): config[bstack1lll1l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨ஝")],
    bstack1lll1l1_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪஞ"): bstack1111l11l1_opy_,
    bstack1lll1l1_opy_ (u"ࠧࡥࡧࡷࡩࡨࡺࡥࡥࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫட"): os.environ.get(bstack1lll1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪ஠"), bstack1ll11l11ll_opy_),
    bstack1lll1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ஡"): bstack1lllllll1_opy_,
    bstack1lll1l1_opy_ (u"ࠪࡳࡵࡺࡩ࡮ࡣ࡯ࡣ࡭ࡻࡢࡠࡷࡵࡰࠬ஢"): bstack1ll1l11111_opy_(),
    bstack1lll1l1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧண"): {
      bstack1lll1l1_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪத"): str(config[bstack1lll1l1_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭஥")]) if bstack1lll1l1_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧ஦") in config else bstack1lll1l1_opy_ (u"ࠣࡷࡱ࡯ࡳࡵࡷ࡯ࠤ஧"),
      bstack1lll1l1_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨ࡚ࡪࡸࡳࡪࡱࡱࠫந"): sys.version,
      bstack1lll1l1_opy_ (u"ࠪࡶࡪ࡬ࡥࡳࡴࡨࡶࠬன"): bstack111l1ll1l_opy_(os.getenv(bstack1lll1l1_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࠨப"), bstack1lll1l1_opy_ (u"ࠧࠨ஫"))),
      bstack1lll1l1_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࠨ஬"): bstack1lll1l1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ஭"),
      bstack1lll1l1_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࠩம"): bstack1l1ll1l11_opy_,
      bstack1lll1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬய"): config[bstack1lll1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ர")] if config[bstack1lll1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧற")] else bstack1lll1l1_opy_ (u"ࠧࡻ࡮࡬ࡰࡲࡻࡳࠨல"),
      bstack1lll1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨள"): str(config[bstack1lll1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩழ")]) if bstack1lll1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪவ") in config else bstack1lll1l1_opy_ (u"ࠤࡸࡲࡰࡴ࡯ࡸࡰࠥஶ"),
      bstack1lll1l1_opy_ (u"ࠪࡳࡸ࠭ஷ"): sys.platform,
      bstack1lll1l1_opy_ (u"ࠫ࡭ࡵࡳࡵࡰࡤࡱࡪ࠭ஸ"): socket.gethostname()
    }
  }
  update(data[bstack1lll1l1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨஹ")], bstack1ll11111_opy_)
  try:
    response = bstack1ll1ll1lll_opy_(bstack1lll1l1_opy_ (u"࠭ࡐࡐࡕࡗࠫ஺"), bstack1llll11ll_opy_(bstack11lll1lll_opy_), data, {
      bstack1lll1l1_opy_ (u"ࠧࡢࡷࡷ࡬ࠬ஻"): (config[bstack1lll1l1_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ஼")], config[bstack1lll1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ஽")])
    })
    if response:
      logger.debug(bstack1l11l1l1_opy_.format(bstack1111l11l1_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack1l1ll1l1ll_opy_.format(str(e)))
def bstack111l1ll1l_opy_(framework):
  return bstack1lll1l1_opy_ (u"ࠥࡿࢂ࠳ࡰࡺࡶ࡫ࡳࡳࡧࡧࡦࡰࡷ࠳ࢀࢃࠢா").format(str(framework), __version__) if framework else bstack1lll1l1_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࡥ࡬࡫࡮ࡵ࠱ࡾࢁࠧி").format(
    __version__)
def bstack1ll1l11l11_opy_():
  global CONFIG
  if bool(CONFIG):
    return
  try:
    bstack1l1lllllll_opy_()
    logger.debug(bstack111l1ll1_opy_.format(str(CONFIG)))
    bstack1l1l11l1_opy_()
    bstack1ll1ll1l11_opy_()
  except Exception as e:
    logger.error(bstack1lll1l1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࡺࡶࠬࠡࡧࡵࡶࡴࡸ࠺ࠡࠤீ") + str(e))
    sys.exit(1)
  sys.excepthook = bstack11l1llll_opy_
  atexit.register(bstack1ll11l1lll_opy_)
  signal.signal(signal.SIGINT, bstack1ll11l1ll_opy_)
  signal.signal(signal.SIGTERM, bstack1ll11l1ll_opy_)
def bstack11l1llll_opy_(exctype, value, traceback):
  global bstack1l1ll1ll1_opy_
  try:
    for driver in bstack1l1ll1ll1_opy_:
      bstack1l1l11ll_opy_(driver, bstack1lll1l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ு"), bstack1lll1l1_opy_ (u"ࠢࡔࡧࡶࡷ࡮ࡵ࡮ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡹ࡬ࡸ࡭ࡀࠠ࡝ࡰࠥூ") + str(value))
  except Exception:
    pass
  bstack111111ll1_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack111111ll1_opy_(message=bstack1lll1l1_opy_ (u"ࠨࠩ௃"), bstack1l1l1l111_opy_ = False):
  global CONFIG
  bstack1l11ll1l1_opy_ = bstack1lll1l1_opy_ (u"ࠩࡪࡰࡴࡨࡡ࡭ࡇࡻࡧࡪࡶࡴࡪࡱࡱࠫ௄") if bstack1l1l1l111_opy_ else bstack1lll1l1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ௅")
  try:
    if message:
      bstack1ll11111_opy_ = {
        bstack1l11ll1l1_opy_ : str(message)
      }
      bstack1111l11ll_opy_(bstack1l1ll111ll_opy_, CONFIG, bstack1ll11111_opy_)
    else:
      bstack1111l11ll_opy_(bstack1l1ll111ll_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack1llll1111_opy_.format(str(e)))
def bstack11l1l1111_opy_(bstack111ll11ll_opy_, size):
  bstack1ll111l11l_opy_ = []
  while len(bstack111ll11ll_opy_) > size:
    bstack1lllllll1l_opy_ = bstack111ll11ll_opy_[:size]
    bstack1ll111l11l_opy_.append(bstack1lllllll1l_opy_)
    bstack111ll11ll_opy_ = bstack111ll11ll_opy_[size:]
  bstack1ll111l11l_opy_.append(bstack111ll11ll_opy_)
  return bstack1ll111l11l_opy_
def bstack1llllllll_opy_(args):
  if bstack1lll1l1_opy_ (u"ࠫ࠲ࡳࠧெ") in args and bstack1lll1l1_opy_ (u"ࠬࡶࡤࡣࠩே") in args:
    return True
  return False
def run_on_browserstack(bstack1111l1111_opy_=None, bstack11111111_opy_=None, bstack1l1ll1llll_opy_=False):
  global CONFIG
  global bstack111111ll_opy_
  global bstack1lll1111l_opy_
  global bstack1ll11l11ll_opy_
  bstack1llllll1l1_opy_ = bstack1lll1l1_opy_ (u"࠭ࠧை")
  bstack1l1l11ll11_opy_(bstack1lll11ll1_opy_, logger)
  if bstack1111l1111_opy_ and isinstance(bstack1111l1111_opy_, str):
    bstack1111l1111_opy_ = eval(bstack1111l1111_opy_)
  if bstack1111l1111_opy_:
    CONFIG = bstack1111l1111_opy_[bstack1lll1l1_opy_ (u"ࠧࡄࡑࡑࡊࡎࡍࠧ௉")]
    bstack111111ll_opy_ = bstack1111l1111_opy_[bstack1lll1l1_opy_ (u"ࠨࡊࡘࡆࡤ࡛ࡒࡍࠩொ")]
    bstack1lll1111l_opy_ = bstack1111l1111_opy_[bstack1lll1l1_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫோ")]
    bstack11l1l11l_opy_.bstack1l1111l1_opy_(bstack1lll1l1_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬௌ"), bstack1lll1111l_opy_)
    bstack1llllll1l1_opy_ = bstack1lll1l1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ்ࠫ")
  if not bstack1l1ll1llll_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack1l111lll1_opy_)
      return
    if sys.argv[1] == bstack1lll1l1_opy_ (u"ࠬ࠳࠭ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ௎") or sys.argv[1] == bstack1lll1l1_opy_ (u"࠭࠭ࡷࠩ௏"):
      logger.info(bstack1lll1l1_opy_ (u"ࠧࡃࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡐࡺࡶ࡫ࡳࡳࠦࡓࡅࡍࠣࡺࢀࢃࠧௐ").format(__version__))
      return
    if sys.argv[1] == bstack1lll1l1_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧ௑"):
      bstack11ll1l1l1_opy_()
      return
  args = sys.argv
  bstack1ll1l11l11_opy_()
  global bstack11ll11ll_opy_
  global bstack111111lll_opy_
  global bstack1l1l1lll1l_opy_
  global bstack111l11ll1_opy_
  global bstack1lll1llll_opy_
  global bstack11l1lll11_opy_
  global bstack1llllllll1_opy_
  global bstack1l1l1111l_opy_
  global bstack1ll11l1ll1_opy_
  global bstack1llll1ll_opy_
  global bstack1l1l1l11l1_opy_
  bstack111111lll_opy_ = len(CONFIG[bstack1lll1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ௒")])
  if not bstack1llllll1l1_opy_:
    if args[1] == bstack1lll1l1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ௓") or args[1] == bstack1lll1l1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ࠷ࠬ௔"):
      bstack1llllll1l1_opy_ = bstack1lll1l1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ௕")
      args = args[2:]
    elif args[1] == bstack1lll1l1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ௖"):
      bstack1llllll1l1_opy_ = bstack1lll1l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ௗ")
      args = args[2:]
    elif args[1] == bstack1lll1l1_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧ௘"):
      bstack1llllll1l1_opy_ = bstack1lll1l1_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨ௙")
      args = args[2:]
    elif args[1] == bstack1lll1l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫ௚"):
      bstack1llllll1l1_opy_ = bstack1lll1l1_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬ௛")
      args = args[2:]
    elif args[1] == bstack1lll1l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ௜"):
      bstack1llllll1l1_opy_ = bstack1lll1l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭௝")
      args = args[2:]
    elif args[1] == bstack1lll1l1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ௞"):
      bstack1llllll1l1_opy_ = bstack1lll1l1_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ௟")
      args = args[2:]
    else:
      if not bstack1lll1l1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ௠") in CONFIG or str(CONFIG[bstack1lll1l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭௡")]).lower() in [bstack1lll1l1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ௢"), bstack1lll1l1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ࠸࠭௣")]:
        bstack1llllll1l1_opy_ = bstack1lll1l1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭௤")
        args = args[1:]
      elif str(CONFIG[bstack1lll1l1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ௥")]).lower() == bstack1lll1l1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ௦"):
        bstack1llllll1l1_opy_ = bstack1lll1l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ௧")
        args = args[1:]
      elif str(CONFIG[bstack1lll1l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭௨")]).lower() == bstack1lll1l1_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪ௩"):
        bstack1llllll1l1_opy_ = bstack1lll1l1_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫ௪")
        args = args[1:]
      elif str(CONFIG[bstack1lll1l1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ௫")]).lower() == bstack1lll1l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ௬"):
        bstack1llllll1l1_opy_ = bstack1lll1l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ௭")
        args = args[1:]
      elif str(CONFIG[bstack1lll1l1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ௮")]).lower() == bstack1lll1l1_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ௯"):
        bstack1llllll1l1_opy_ = bstack1lll1l1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ௰")
        args = args[1:]
      else:
        os.environ[bstack1lll1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧ௱")] = bstack1llllll1l1_opy_
        bstack1ll1ll1ll1_opy_(bstack11lll11l_opy_)
  os.environ[bstack1lll1l1_opy_ (u"࠭ࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࡡࡘࡗࡊࡊࠧ௲")] = bstack1llllll1l1_opy_
  bstack1ll11l11ll_opy_ = bstack1llllll1l1_opy_
  global bstack111l11l1_opy_
  if bstack1111l1111_opy_:
    try:
      os.environ[bstack1lll1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩ௳")] = bstack1llllll1l1_opy_
      bstack1111l11ll_opy_(bstack11111lll1_opy_, CONFIG)
    except Exception as e:
      logger.debug(bstack1llll1111_opy_.format(str(e)))
  global bstack11llll1l_opy_
  global bstack1l11l1111_opy_
  global bstack1l111l11_opy_
  global bstack1llll1l1_opy_
  global bstack1l1l11111_opy_
  global bstack1ll11l11l_opy_
  global bstack1l11111l1_opy_
  global bstack1111lll1_opy_
  global bstack111ll1l1l_opy_
  global bstack1ll1l1111_opy_
  global bstack1l1ll1l1l1_opy_
  global bstack1lll1l1l1_opy_
  global bstack111111l11_opy_
  global bstack1lll11llll_opy_
  global bstack1llllll1ll_opy_
  global bstack1l1ll11l11_opy_
  global bstack1lll111l11_opy_
  global bstack11ll1l111_opy_
  global bstack1ll111ll_opy_
  global bstack1l1l1111l1_opy_
  global bstack111lll111_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack11llll1l_opy_ = webdriver.Remote.__init__
    bstack1l11l1111_opy_ = WebDriver.quit
    bstack1lll1l1l1_opy_ = WebDriver.close
    bstack1llllll1ll_opy_ = WebDriver.get
    bstack111lll111_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack111l11l1_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    global bstack1ll1111l11_opy_
    from QWeb.keywords import browser
    bstack1ll1111l11_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack1lll1l11l1_opy_(CONFIG) and bstack1l1l11l111_opy_():
    if bstack11llll1ll_opy_() < version.parse(bstack1llll1l1l1_opy_):
      logger.error(bstack11111l11_opy_.format(bstack11llll1ll_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack1l1ll11l11_opy_ = RemoteConnection._get_proxy_url
      except Exception as e:
        logger.error(bstack11lll111_opy_.format(str(e)))
  if bstack1llllll1l1_opy_ != bstack1lll1l1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ௴") or (bstack1llllll1l1_opy_ == bstack1lll1l1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ௵") and not bstack1111l1111_opy_):
    bstack1ll1llll1l_opy_()
  if (bstack1llllll1l1_opy_ in [bstack1lll1l1_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ௶"), bstack1lll1l1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ௷"), bstack1lll1l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭௸")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack1ll11ll11_opy_
        bstack1ll11l11l_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack11111ll1l_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack1l1l11111_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack1lll1111ll_opy_ + str(e))
    except Exception as e:
      bstack1lll1lllll_opy_(e, bstack11111ll1l_opy_)
    if bstack1llllll1l1_opy_ != bstack1lll1l1_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧ௹"):
      bstack1ll111lll1_opy_()
    bstack1l111l11_opy_ = Output.start_test
    bstack1llll1l1_opy_ = Output.end_test
    bstack1l11111l1_opy_ = TestStatus.__init__
    bstack111ll1l1l_opy_ = pabot._run
    bstack1ll1l1111_opy_ = QueueItem.__init__
    bstack1l1ll1l1l1_opy_ = pabot._create_command_for_execution
    bstack1ll111ll_opy_ = pabot._report_results
  if bstack1llllll1l1_opy_ == bstack1lll1l1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ௺"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1lll1lllll_opy_(e, bstack111ll111l_opy_)
    bstack111111l11_opy_ = Runner.run_hook
    bstack1lll11llll_opy_ = Step.run
  if bstack1llllll1l1_opy_ == bstack1lll1l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ௻"):
    try:
      from _pytest.config import Config
      bstack1lll111l11_opy_ = Config.getoption
      from _pytest import runner
      bstack11ll1l111_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack1l1llll1ll_opy_)
    try:
      from pytest_bdd import reporting
      bstack1l1l1111l1_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack1lll1l1_opy_ (u"ࠩࡓࡰࡪࡧࡳࡦࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡱࠣࡶࡺࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࡵࠪ௼"))
  if bstack1llllll1l1_opy_ in bstack11l11lll1_opy_:
    try:
      framework_name = bstack1lll1l1_opy_ (u"ࠪࡖࡴࡨ࡯ࡵࠩ௽") if bstack1llllll1l1_opy_ in [bstack1lll1l1_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪ௾"), bstack1lll1l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ௿"), bstack1lll1l1_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧఀ")] else bstack1ll1lll1ll_opy_(bstack1llllll1l1_opy_)
      bstack1l1ll11l_opy_.launch(CONFIG, {
        bstack1lll1l1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࠨఁ"): bstack1lll1l1_opy_ (u"ࠨࡽ࠳ࢁ࠲ࡩࡵࡤࡷࡰࡦࡪࡸࠧం").format(framework_name) if bstack1llllll1l1_opy_ == bstack1lll1l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩః") and bstack1lll1ll1_opy_() else framework_name,
        bstack1lll1l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧఄ"): bstack11l1l111l_opy_(framework_name),
        bstack1lll1l1_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩఅ"): __version__
      })
    except Exception as e:
      logger.debug(bstack1l1l1ll1ll_opy_.format(bstack1lll1l1_opy_ (u"ࠬࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬఆ"), str(e)))
  if bstack1llllll1l1_opy_ in bstack11ll11l11_opy_:
    try:
      framework_name = bstack1lll1l1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬఇ") if bstack1llllll1l1_opy_ in [bstack1lll1l1_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ఈ"), bstack1lll1l1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧఉ")] else bstack1llllll1l1_opy_
      if bstack1l11ll111_opy_ and bstack1lll1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩఊ") in CONFIG and CONFIG[bstack1lll1l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪఋ")] == True:
        if bstack1lll1l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫఌ") in CONFIG:
          os.environ[bstack1lll1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭఍")] = os.getenv(bstack1lll1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧఎ"), json.dumps(CONFIG[bstack1lll1l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧఏ")]))
          CONFIG[bstack1lll1l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨఐ")].pop(bstack1lll1l1_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ఑"), None)
          CONFIG[bstack1lll1l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪఒ")].pop(bstack1lll1l1_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩఓ"), None)
        bstack11ll111l1_opy_, bstack1ll1llllll_opy_ = bstack11111111l_opy_.bstack1l1l11lll1_opy_(CONFIG, bstack1llllll1l1_opy_, bstack11l1l111l_opy_(framework_name))
        if not bstack11ll111l1_opy_ is None:
          os.environ[bstack1lll1l1_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪఔ")] = bstack11ll111l1_opy_
          os.environ[bstack1lll1l1_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡕࡇࡖࡘࡤࡘࡕࡏࡡࡌࡈࠬక")] = str(bstack1ll1llllll_opy_)
    except Exception as e:
      logger.debug(bstack1l1l1ll1ll_opy_.format(bstack1lll1l1_opy_ (u"ࠧࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧఖ"), str(e)))
  if bstack1llllll1l1_opy_ == bstack1lll1l1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨగ"):
    bstack1l1l1lll1l_opy_ = True
    if bstack1111l1111_opy_ and bstack1l1ll1llll_opy_:
      bstack11l1lll11_opy_ = CONFIG.get(bstack1lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ఘ"), {}).get(bstack1lll1l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬఙ"))
      bstack1lll11lll_opy_(bstack1llll111_opy_)
    elif bstack1111l1111_opy_:
      bstack11l1lll11_opy_ = CONFIG.get(bstack1lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨచ"), {}).get(bstack1lll1l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧఛ"))
      global bstack1l1ll1ll1_opy_
      try:
        if bstack1llllllll_opy_(bstack1111l1111_opy_[bstack1lll1l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩజ")]) and multiprocessing.current_process().name == bstack1lll1l1_opy_ (u"ࠧ࠱ࠩఝ"):
          bstack1111l1111_opy_[bstack1lll1l1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫఞ")].remove(bstack1lll1l1_opy_ (u"ࠩ࠰ࡱࠬట"))
          bstack1111l1111_opy_[bstack1lll1l1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ఠ")].remove(bstack1lll1l1_opy_ (u"ࠫࡵࡪࡢࠨడ"))
          bstack1111l1111_opy_[bstack1lll1l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨఢ")] = bstack1111l1111_opy_[bstack1lll1l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩణ")][0]
          with open(bstack1111l1111_opy_[bstack1lll1l1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪత")], bstack1lll1l1_opy_ (u"ࠨࡴࠪథ")) as f:
            bstack111lllll_opy_ = f.read()
          bstack11l1lll1l_opy_ = bstack1lll1l1_opy_ (u"ࠤࠥࠦ࡫ࡸ࡯࡮ࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡵࡧ࡯ࠥ࡯࡭ࡱࡱࡵࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣ࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࢀࡥ࠼ࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡩ࠭ࢁࡽࠪ࠽ࠣࡪࡷࡵ࡭ࠡࡲࡧࡦࠥ࡯࡭ࡱࡱࡵࡸࠥࡖࡤࡣ࠽ࠣࡳ࡬ࡥࡤࡣࠢࡀࠤࡕࡪࡢ࠯ࡦࡲࡣࡧࡸࡥࡢ࡭࠾ࠎࡩ࡫ࡦࠡ࡯ࡲࡨࡤࡨࡲࡦࡣ࡮ࠬࡸ࡫࡬ࡧ࠮ࠣࡥࡷ࡭ࠬࠡࡶࡨࡱࡵࡵࡲࡢࡴࡼࠤࡂࠦ࠰ࠪ࠼ࠍࠤࠥࡺࡲࡺ࠼ࠍࠤࠥࠦࠠࡢࡴࡪࠤࡂࠦࡳࡵࡴࠫ࡭ࡳࡺࠨࡢࡴࡪ࠭࠰࠷࠰ࠪࠌࠣࠤࡪࡾࡣࡦࡲࡷࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡢࡵࠣࡩ࠿ࠐࠠࠡࠢࠣࡴࡦࡹࡳࠋࠢࠣࡳ࡬ࡥࡤࡣࠪࡶࡩࡱ࡬ࠬࡢࡴࡪ࠰ࡹ࡫࡭ࡱࡱࡵࡥࡷࡿࠩࠋࡒࡧࡦ࠳ࡪ࡯ࡠࡤࠣࡁࠥࡳ࡯ࡥࡡࡥࡶࡪࡧ࡫ࠋࡒࡧࡦ࠳ࡪ࡯ࡠࡤࡵࡩࡦࡱࠠ࠾ࠢࡰࡳࡩࡥࡢࡳࡧࡤ࡯ࠏࡖࡤࡣࠪࠬ࠲ࡸ࡫ࡴࡠࡶࡵࡥࡨ࡫ࠨࠪ࡞ࡱࠦࠧࠨద").format(str(bstack1111l1111_opy_))
          bstack1llll11lll_opy_ = bstack11l1lll1l_opy_ + bstack111lllll_opy_
          bstack1l1l1lllll_opy_ = bstack1111l1111_opy_[bstack1lll1l1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ధ")] + bstack1lll1l1_opy_ (u"ࠫࡤࡨࡳࡵࡣࡦ࡯ࡤࡺࡥ࡮ࡲ࠱ࡴࡾ࠭న")
          with open(bstack1l1l1lllll_opy_, bstack1lll1l1_opy_ (u"ࠬࡽࠧ఩")):
            pass
          with open(bstack1l1l1lllll_opy_, bstack1lll1l1_opy_ (u"ࠨࡷࠬࠤప")) as f:
            f.write(bstack1llll11lll_opy_)
          import subprocess
          bstack111l11111_opy_ = subprocess.run([bstack1lll1l1_opy_ (u"ࠢࡱࡻࡷ࡬ࡴࡴࠢఫ"), bstack1l1l1lllll_opy_])
          if os.path.exists(bstack1l1l1lllll_opy_):
            os.unlink(bstack1l1l1lllll_opy_)
          os._exit(bstack111l11111_opy_.returncode)
        else:
          if bstack1llllllll_opy_(bstack1111l1111_opy_[bstack1lll1l1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫబ")]):
            bstack1111l1111_opy_[bstack1lll1l1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬభ")].remove(bstack1lll1l1_opy_ (u"ࠪ࠱ࡲ࠭మ"))
            bstack1111l1111_opy_[bstack1lll1l1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧయ")].remove(bstack1lll1l1_opy_ (u"ࠬࡶࡤࡣࠩర"))
            bstack1111l1111_opy_[bstack1lll1l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩఱ")] = bstack1111l1111_opy_[bstack1lll1l1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪల")][0]
          bstack1lll11lll_opy_(bstack1llll111_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack1111l1111_opy_[bstack1lll1l1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫళ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack1lll1l1_opy_ (u"ࠩࡢࡣࡳࡧ࡭ࡦࡡࡢࠫఴ")] = bstack1lll1l1_opy_ (u"ࠪࡣࡤࡳࡡࡪࡰࡢࡣࠬవ")
          mod_globals[bstack1lll1l1_opy_ (u"ࠫࡤࡥࡦࡪ࡮ࡨࡣࡤ࠭శ")] = os.path.abspath(bstack1111l1111_opy_[bstack1lll1l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨష")])
          exec(open(bstack1111l1111_opy_[bstack1lll1l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩస")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack1lll1l1_opy_ (u"ࠧࡄࡣࡸ࡫࡭ࡺࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࢀࢃࠧహ").format(str(e)))
          for driver in bstack1l1ll1ll1_opy_:
            bstack11111111_opy_.append({
              bstack1lll1l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭఺"): bstack1111l1111_opy_[bstack1lll1l1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ఻")],
              bstack1lll1l1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳ఼ࠩ"): str(e),
              bstack1lll1l1_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪఽ"): multiprocessing.current_process().name
            })
            bstack1l1l11ll_opy_(driver, bstack1lll1l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬా"), bstack1lll1l1_opy_ (u"ࠨࡓࡦࡵࡶ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪࠠࡸ࡫ࡷ࡬࠿ࠦ࡜࡯ࠤి") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1l1ll1ll1_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack1lll1111l_opy_, CONFIG, logger)
      bstack111ll11l1_opy_()
      bstack1ll1111lll_opy_()
      bstack111l1l11_opy_ = {
        bstack1lll1l1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪీ"): args[0],
        bstack1lll1l1_opy_ (u"ࠨࡅࡒࡒࡋࡏࡇࠨు"): CONFIG,
        bstack1lll1l1_opy_ (u"ࠩࡋ࡙ࡇࡥࡕࡓࡎࠪూ"): bstack111111ll_opy_,
        bstack1lll1l1_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬృ"): bstack1lll1111l_opy_
      }
      percy.bstack1lllllllll_opy_()
      if bstack1lll1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧౄ") in CONFIG:
        bstack1l1l1llll_opy_ = []
        manager = multiprocessing.Manager()
        bstack11l11lll_opy_ = manager.list()
        if bstack1llllllll_opy_(args):
          for index, platform in enumerate(CONFIG[bstack1lll1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ౅")]):
            if index == 0:
              bstack111l1l11_opy_[bstack1lll1l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩె")] = args
            bstack1l1l1llll_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack111l1l11_opy_, bstack11l11lll_opy_)))
        else:
          for index, platform in enumerate(CONFIG[bstack1lll1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪే")]):
            bstack1l1l1llll_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack111l1l11_opy_, bstack11l11lll_opy_)))
        for t in bstack1l1l1llll_opy_:
          t.start()
        for t in bstack1l1l1llll_opy_:
          t.join()
        bstack1l1l1111l_opy_ = list(bstack11l11lll_opy_)
      else:
        if bstack1llllllll_opy_(args):
          bstack111l1l11_opy_[bstack1lll1l1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫై")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack111l1l11_opy_,))
          test.start()
          test.join()
        else:
          bstack1lll11lll_opy_(bstack1llll111_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack1lll1l1_opy_ (u"ࠩࡢࡣࡳࡧ࡭ࡦࡡࡢࠫ౉")] = bstack1lll1l1_opy_ (u"ࠪࡣࡤࡳࡡࡪࡰࡢࡣࠬొ")
          mod_globals[bstack1lll1l1_opy_ (u"ࠫࡤࡥࡦࡪ࡮ࡨࡣࡤ࠭ో")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack1llllll1l1_opy_ == bstack1lll1l1_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫౌ") or bstack1llllll1l1_opy_ == bstack1lll1l1_opy_ (u"࠭ࡲࡰࡤࡲࡸ్ࠬ"):
    percy.init(bstack1lll1111l_opy_, CONFIG, logger)
    percy.bstack1lllllllll_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack1lll1lllll_opy_(e, bstack11111ll1l_opy_)
    bstack111ll11l1_opy_()
    bstack1lll11lll_opy_(bstack1l1l1lll11_opy_)
    if bstack1lll1l1_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬ౎") in args:
      i = args.index(bstack1lll1l1_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭౏"))
      args.pop(i)
      args.pop(i)
    args.insert(0, str(bstack11ll11ll_opy_))
    args.insert(0, str(bstack1lll1l1_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧ౐")))
    if bstack1l1ll11l_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack1111ll1l1_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack111l111l_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack1lll1l1_opy_ (u"ࠥࡖࡔࡈࡏࡕࡡࡒࡔ࡙ࡏࡏࡏࡕࠥ౑"),
        ).parse_args(bstack1111ll1l1_opy_)
        args.insert(args.index(bstack111l111l_opy_[0]), str(bstack1lll1l1_opy_ (u"ࠫ࠲࠳࡬ࡪࡵࡷࡩࡳ࡫ࡲࠨ౒")))
        args.insert(args.index(bstack111l111l_opy_[0]), str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1lll1l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡸ࡯ࡣࡱࡷࡣࡱ࡯ࡳࡵࡧࡱࡩࡷ࠴ࡰࡺࠩ౓"))))
        if bstack1l11lllll_opy_(os.environ.get(bstack1lll1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࠫ౔"))) and str(os.environ.get(bstack1lll1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࡤ࡚ࡅࡔࡖࡖౕࠫ"), bstack1lll1l1_opy_ (u"ࠨࡰࡸࡰࡱౖ࠭"))) != bstack1lll1l1_opy_ (u"ࠩࡱࡹࡱࡲࠧ౗"):
          for bstack11l1111l_opy_ in bstack111l111l_opy_:
            args.remove(bstack11l1111l_opy_)
          bstack1l1l1l11_opy_ = os.environ.get(bstack1lll1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࡠࡖࡈࡗ࡙࡙ࠧౘ")).split(bstack1lll1l1_opy_ (u"ࠫ࠱࠭ౙ"))
          for bstack1lll111l_opy_ in bstack1l1l1l11_opy_:
            args.append(bstack1lll111l_opy_)
      except Exception as e:
        logger.error(bstack1lll1l1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡥࡹࡺࡡࡤࡪ࡬ࡲ࡬ࠦ࡬ࡪࡵࡷࡩࡳ࡫ࡲࠡࡨࡲࡶࠥࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽ࠳ࠦࡅࡳࡴࡲࡶࠥ࠳ࠠࠣౚ").format(e))
    pabot.main(args)
  elif bstack1llllll1l1_opy_ == bstack1lll1l1_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧ౛"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1lll1lllll_opy_(e, bstack11111ll1l_opy_)
    for a in args:
      if bstack1lll1l1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡐࡍࡃࡗࡊࡔࡘࡍࡊࡐࡇࡉ࡝࠭౜") in a:
        bstack1lll1llll_opy_ = int(a.split(bstack1lll1l1_opy_ (u"ࠨ࠼ࠪౝ"))[1])
      if bstack1lll1l1_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡆࡈࡊࡑࡕࡃࡂࡎࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭౞") in a:
        bstack11l1lll11_opy_ = str(a.split(bstack1lll1l1_opy_ (u"ࠪ࠾ࠬ౟"))[1])
      if bstack1lll1l1_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡇࡑࡏࡁࡓࡉࡖࠫౠ") in a:
        bstack1llllllll1_opy_ = str(a.split(bstack1lll1l1_opy_ (u"ࠬࡀࠧౡ"))[1])
    bstack11l1ll11_opy_ = None
    if bstack1lll1l1_opy_ (u"࠭࠭࠮ࡤࡶࡸࡦࡩ࡫ࡠ࡫ࡷࡩࡲࡥࡩ࡯ࡦࡨࡼࠬౢ") in args:
      i = args.index(bstack1lll1l1_opy_ (u"ࠧ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽ࠭ౣ"))
      args.pop(i)
      bstack11l1ll11_opy_ = args.pop(i)
    if bstack11l1ll11_opy_ is not None:
      global bstack11ll111l_opy_
      bstack11ll111l_opy_ = bstack11l1ll11_opy_
    bstack1lll11lll_opy_(bstack1l1l1lll11_opy_)
    run_cli(args)
    if bstack1lll1l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸࠬ౤") in multiprocessing.current_process().__dict__.keys():
      for bstack11l111l11_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack11111111_opy_.append(bstack11l111l11_opy_)
  elif bstack1llllll1l1_opy_ == bstack1lll1l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ౥"):
    percy.init(bstack1lll1111l_opy_, CONFIG, logger)
    percy.bstack1lllllllll_opy_()
    bstack1ll1111ll1_opy_ = bstack1l1l11l11l_opy_(args, logger, CONFIG, bstack1l11ll111_opy_)
    bstack1ll1111ll1_opy_.bstack1ll1lll111_opy_()
    bstack111ll11l1_opy_()
    bstack111l11ll1_opy_ = True
    bstack1llll1ll_opy_ = bstack1ll1111ll1_opy_.bstack1ll11l111_opy_()
    bstack1ll1111ll1_opy_.bstack111l1l11_opy_(bstack111lllll1_opy_)
    bstack1ll11l1ll1_opy_ = bstack1ll1111ll1_opy_.bstack1ll1l1111l_opy_(bstack111llll1l_opy_, {
      bstack1lll1l1_opy_ (u"ࠪࡌ࡚ࡈ࡟ࡖࡔࡏࠫ౦"): bstack111111ll_opy_,
      bstack1lll1l1_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭౧"): bstack1lll1111l_opy_,
      bstack1lll1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨ౨"): bstack1l11ll111_opy_
    })
    bstack1l1l1l11l1_opy_ = 1 if len(bstack1ll11l1ll1_opy_) > 0 else 0
  elif bstack1llllll1l1_opy_ == bstack1lll1l1_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭౩"):
    try:
      from behave.__main__ import main as bstack1111l1ll1_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1lll1lllll_opy_(e, bstack111ll111l_opy_)
    bstack111ll11l1_opy_()
    bstack111l11ll1_opy_ = True
    bstack11l1ll11l_opy_ = 1
    if bstack1lll1l1_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ౪") in CONFIG:
      bstack11l1ll11l_opy_ = CONFIG[bstack1lll1l1_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ౫")]
    bstack11lll11l1_opy_ = int(bstack11l1ll11l_opy_) * int(len(CONFIG[bstack1lll1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ౬")]))
    config = Configuration(args)
    bstack1l1ll111l1_opy_ = config.paths
    if len(bstack1l1ll111l1_opy_) == 0:
      import glob
      pattern = bstack1lll1l1_opy_ (u"ࠪ࠮࠯࠵ࠪ࠯ࡨࡨࡥࡹࡻࡲࡦࠩ౭")
      bstack1lll1l1ll_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack1lll1l1ll_opy_)
      config = Configuration(args)
      bstack1l1ll111l1_opy_ = config.paths
    bstack11111ll1_opy_ = [os.path.normpath(item) for item in bstack1l1ll111l1_opy_]
    bstack1l111l1ll_opy_ = [os.path.normpath(item) for item in args]
    bstack1l1lll11l_opy_ = [item for item in bstack1l111l1ll_opy_ if item not in bstack11111ll1_opy_]
    import platform as pf
    if pf.system().lower() == bstack1lll1l1_opy_ (u"ࠫࡼ࡯࡮ࡥࡱࡺࡷࠬ౮"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack11111ll1_opy_ = [str(PurePosixPath(PureWindowsPath(bstack1l1ll1l1l_opy_)))
                    for bstack1l1ll1l1l_opy_ in bstack11111ll1_opy_]
    bstack1l1ll11lll_opy_ = []
    for spec in bstack11111ll1_opy_:
      bstack1l1l1ll111_opy_ = []
      bstack1l1l1ll111_opy_ += bstack1l1lll11l_opy_
      bstack1l1l1ll111_opy_.append(spec)
      bstack1l1ll11lll_opy_.append(bstack1l1l1ll111_opy_)
    execution_items = []
    for bstack1l1l1ll111_opy_ in bstack1l1ll11lll_opy_:
      for index, _ in enumerate(CONFIG[bstack1lll1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ౯")]):
        item = {}
        item[bstack1lll1l1_opy_ (u"࠭ࡡࡳࡩࠪ౰")] = bstack1lll1l1_opy_ (u"ࠧࠡࠩ౱").join(bstack1l1l1ll111_opy_)
        item[bstack1lll1l1_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧ౲")] = index
        execution_items.append(item)
    bstack11l111ll1_opy_ = bstack11l1l1111_opy_(execution_items, bstack11lll11l1_opy_)
    for execution_item in bstack11l111ll1_opy_:
      bstack1l1l1llll_opy_ = []
      for item in execution_item:
        bstack1l1l1llll_opy_.append(bstack11lll1l1l_opy_(name=str(item[bstack1lll1l1_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ౳")]),
                                             target=bstack11llllll_opy_,
                                             args=(item[bstack1lll1l1_opy_ (u"ࠪࡥࡷ࡭ࠧ౴")],)))
      for t in bstack1l1l1llll_opy_:
        t.start()
      for t in bstack1l1l1llll_opy_:
        t.join()
  else:
    bstack1ll1ll1ll1_opy_(bstack11lll11l_opy_)
  if not bstack1111l1111_opy_:
    bstack1lll1l111_opy_()
def browserstack_initialize(bstack11ll11lll_opy_=None):
  run_on_browserstack(bstack11ll11lll_opy_, None, True)
def bstack1lll1l111_opy_():
  global CONFIG
  global bstack1ll11l11ll_opy_
  global bstack1l1l1l11l1_opy_
  bstack1l1ll11l_opy_.stop()
  bstack1l1ll11l_opy_.bstack1l1ll1111_opy_()
  if bstack11111111l_opy_.bstack1llll1l111_opy_(CONFIG):
    bstack11111111l_opy_.bstack1l1ll1lll_opy_()
  [bstack1ll1lll1l_opy_, bstack1ll1l1ll11_opy_] = bstack1l1l11111l_opy_()
  if bstack1ll1lll1l_opy_ is not None and bstack11l11l111_opy_() != -1:
    sessions = bstack1l111111l_opy_(bstack1ll1lll1l_opy_)
    bstack1l1lll111_opy_(sessions, bstack1ll1l1ll11_opy_)
  if bstack1ll11l11ll_opy_ == bstack1lll1l1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ౵") and bstack1l1l1l11l1_opy_ != 0:
    sys.exit(bstack1l1l1l11l1_opy_)
def bstack1ll1lll1ll_opy_(bstack1l1ll1111l_opy_):
  if bstack1l1ll1111l_opy_:
    return bstack1l1ll1111l_opy_.capitalize()
  else:
    return bstack1lll1l1_opy_ (u"ࠬ࠭౶")
def bstack1l1l1ll1l_opy_(bstack1lll11l1_opy_):
  if bstack1lll1l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ౷") in bstack1lll11l1_opy_ and bstack1lll11l1_opy_[bstack1lll1l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ౸")] != bstack1lll1l1_opy_ (u"ࠨࠩ౹"):
    return bstack1lll11l1_opy_[bstack1lll1l1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ౺")]
  else:
    bstack111llll1_opy_ = bstack1lll1l1_opy_ (u"ࠥࠦ౻")
    if bstack1lll1l1_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫ౼") in bstack1lll11l1_opy_ and bstack1lll11l1_opy_[bstack1lll1l1_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬ౽")] != None:
      bstack111llll1_opy_ += bstack1lll11l1_opy_[bstack1lll1l1_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭౾")] + bstack1lll1l1_opy_ (u"ࠢ࠭ࠢࠥ౿")
      if bstack1lll11l1_opy_[bstack1lll1l1_opy_ (u"ࠨࡱࡶࠫಀ")] == bstack1lll1l1_opy_ (u"ࠤ࡬ࡳࡸࠨಁ"):
        bstack111llll1_opy_ += bstack1lll1l1_opy_ (u"ࠥ࡭ࡔ࡙ࠠࠣಂ")
      bstack111llll1_opy_ += (bstack1lll11l1_opy_[bstack1lll1l1_opy_ (u"ࠫࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨಃ")] or bstack1lll1l1_opy_ (u"ࠬ࠭಄"))
      return bstack111llll1_opy_
    else:
      bstack111llll1_opy_ += bstack1ll1lll1ll_opy_(bstack1lll11l1_opy_[bstack1lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧಅ")]) + bstack1lll1l1_opy_ (u"ࠢࠡࠤಆ") + (
              bstack1lll11l1_opy_[bstack1lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪಇ")] or bstack1lll1l1_opy_ (u"ࠩࠪಈ")) + bstack1lll1l1_opy_ (u"ࠥ࠰ࠥࠨಉ")
      if bstack1lll11l1_opy_[bstack1lll1l1_opy_ (u"ࠫࡴࡹࠧಊ")] == bstack1lll1l1_opy_ (u"ࠧ࡝ࡩ࡯ࡦࡲࡻࡸࠨಋ"):
        bstack111llll1_opy_ += bstack1lll1l1_opy_ (u"ࠨࡗࡪࡰࠣࠦಌ")
      bstack111llll1_opy_ += bstack1lll11l1_opy_[bstack1lll1l1_opy_ (u"ࠧࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠫ಍")] or bstack1lll1l1_opy_ (u"ࠨࠩಎ")
      return bstack111llll1_opy_
def bstack11l11llll_opy_(bstack1l1ll1l111_opy_):
  if bstack1l1ll1l111_opy_ == bstack1lll1l1_opy_ (u"ࠤࡧࡳࡳ࡫ࠢಏ"):
    return bstack1lll1l1_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿࡭ࡲࡦࡧࡱ࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧ࡭ࡲࡦࡧࡱࠦࡃࡉ࡯࡮ࡲ࡯ࡩࡹ࡫ࡤ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭ಐ")
  elif bstack1l1ll1l111_opy_ == bstack1lll1l1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦ಑"):
    return bstack1lll1l1_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡳࡧࡧ࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧࡸࡥࡥࠤࡁࡊࡦ࡯࡬ࡦࡦ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨಒ")
  elif bstack1l1ll1l111_opy_ == bstack1lll1l1_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨಓ"):
    return bstack1lll1l1_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡪࡶࡪ࡫࡮࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡪࡶࡪ࡫࡮ࠣࡀࡓࡥࡸࡹࡥࡥ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧಔ")
  elif bstack1l1ll1l111_opy_ == bstack1lll1l1_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢಕ"):
    return bstack1lll1l1_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾ࡷ࡫ࡤ࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡵࡩࡩࠨ࠾ࡆࡴࡵࡳࡷࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫಖ")
  elif bstack1l1ll1l111_opy_ == bstack1lll1l1_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷࠦಗ"):
    return bstack1lll1l1_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࠣࡦࡧࡤ࠷࠷࠼࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࠥࡨࡩࡦ࠹࠲࠷ࠤࡁࡘ࡮ࡳࡥࡰࡷࡷࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩಘ")
  elif bstack1l1ll1l111_opy_ == bstack1lll1l1_opy_ (u"ࠧࡸࡵ࡯ࡰ࡬ࡲ࡬ࠨಙ"):
    return bstack1lll1l1_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡤ࡯ࡥࡨࡱ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡤ࡯ࡥࡨࡱࠢ࠿ࡔࡸࡲࡳ࡯࡮ࡨ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧಚ")
  else:
    return bstack1lll1l1_opy_ (u"ࠧ࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽ࡦࡱࡧࡣ࡬࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࡦࡱࡧࡣ࡬ࠤࡁࠫಛ") + bstack1ll1lll1ll_opy_(
      bstack1l1ll1l111_opy_) + bstack1lll1l1_opy_ (u"ࠨ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧಜ")
def bstack1ll1ll1l_opy_(session):
  return bstack1lll1l1_opy_ (u"ࠩ࠿ࡸࡷࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡲࡰࡹࠥࡂࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠦࡳࡦࡵࡶ࡭ࡴࡴ࠭࡯ࡣࡰࡩࠧࡄ࠼ࡢࠢ࡫ࡶࡪ࡬࠽ࠣࡽࢀࠦࠥࡺࡡࡳࡩࡨࡸࡂࠨ࡟ࡣ࡮ࡤࡲࡰࠨ࠾ࡼࡿ࠿࠳ࡦࡄ࠼࠰ࡶࡧࡂࢀࢃࡻࡾ࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࡃࢁࡽ࠽࠱ࡷࡨࡃࡂࡴࡥࠢࡤࡰ࡮࡭࡮࠾ࠤࡦࡩࡳࡺࡥࡳࠤࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࡀࡾࢁࡁ࠵ࡴࡥࡀ࠿ࡸࡩࠦࡡ࡭࡫ࡪࡲࡂࠨࡣࡦࡰࡷࡩࡷࠨࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࡄࡻࡾ࠾࠲ࡸࡩࡄ࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࡁࡿࢂࡂ࠯ࡵࡦࡁࡀ࠴ࡺࡲ࠿ࠩಝ").format(
    session[bstack1lll1l1_opy_ (u"ࠪࡴࡺࡨ࡬ࡪࡥࡢࡹࡷࡲࠧಞ")], bstack1l1l1ll1l_opy_(session), bstack11l11llll_opy_(session[bstack1lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡷࡹࡧࡴࡶࡵࠪಟ")]),
    bstack11l11llll_opy_(session[bstack1lll1l1_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬಠ")]),
    bstack1ll1lll1ll_opy_(session[bstack1lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧಡ")] or session[bstack1lll1l1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧಢ")] or bstack1lll1l1_opy_ (u"ࠨࠩಣ")) + bstack1lll1l1_opy_ (u"ࠤࠣࠦತ") + (session[bstack1lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬಥ")] or bstack1lll1l1_opy_ (u"ࠫࠬದ")),
    session[bstack1lll1l1_opy_ (u"ࠬࡵࡳࠨಧ")] + bstack1lll1l1_opy_ (u"ࠨࠠࠣನ") + session[bstack1lll1l1_opy_ (u"ࠧࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠫ಩")], session[bstack1lll1l1_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࠪಪ")] or bstack1lll1l1_opy_ (u"ࠩࠪಫ"),
    session[bstack1lll1l1_opy_ (u"ࠪࡧࡷ࡫ࡡࡵࡧࡧࡣࡦࡺࠧಬ")] if session[bstack1lll1l1_opy_ (u"ࠫࡨࡸࡥࡢࡶࡨࡨࡤࡧࡴࠨಭ")] else bstack1lll1l1_opy_ (u"ࠬ࠭ಮ"))
def bstack1l1lll111_opy_(sessions, bstack1ll1l1ll11_opy_):
  try:
    bstack1l1l1ll11_opy_ = bstack1lll1l1_opy_ (u"ࠨࠢಯ")
    if not os.path.exists(bstack1l11lll11_opy_):
      os.mkdir(bstack1l11lll11_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1lll1l1_opy_ (u"ࠧࡢࡵࡶࡩࡹࡹ࠯ࡳࡧࡳࡳࡷࡺ࠮ࡩࡶࡰࡰࠬರ")), bstack1lll1l1_opy_ (u"ࠨࡴࠪಱ")) as f:
      bstack1l1l1ll11_opy_ = f.read()
    bstack1l1l1ll11_opy_ = bstack1l1l1ll11_opy_.replace(bstack1lll1l1_opy_ (u"ࠩࡾࠩࡗࡋࡓࡖࡎࡗࡗࡤࡉࡏࡖࡐࡗࠩࢂ࠭ಲ"), str(len(sessions)))
    bstack1l1l1ll11_opy_ = bstack1l1l1ll11_opy_.replace(bstack1lll1l1_opy_ (u"ࠪࡿࠪࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠦࡿࠪಳ"), bstack1ll1l1ll11_opy_)
    bstack1l1l1ll11_opy_ = bstack1l1l1ll11_opy_.replace(bstack1lll1l1_opy_ (u"ࠫࢀࠫࡂࡖࡋࡏࡈࡤࡔࡁࡎࡇࠨࢁࠬ಴"),
                                              sessions[0].get(bstack1lll1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣࡳࡧ࡭ࡦࠩವ")) if sessions[0] else bstack1lll1l1_opy_ (u"࠭ࠧಶ"))
    with open(os.path.join(bstack1l11lll11_opy_, bstack1lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠳ࡲࡦࡲࡲࡶࡹ࠴ࡨࡵ࡯࡯ࠫಷ")), bstack1lll1l1_opy_ (u"ࠨࡹࠪಸ")) as stream:
      stream.write(bstack1l1l1ll11_opy_.split(bstack1lll1l1_opy_ (u"ࠩࡾࠩࡘࡋࡓࡔࡋࡒࡒࡘࡥࡄࡂࡖࡄࠩࢂ࠭ಹ"))[0])
      for session in sessions:
        stream.write(bstack1ll1ll1l_opy_(session))
      stream.write(bstack1l1l1ll11_opy_.split(bstack1lll1l1_opy_ (u"ࠪࡿ࡙ࠪࡅࡔࡕࡌࡓࡓ࡙࡟ࡅࡃࡗࡅࠪࢃࠧ಺"))[1])
    logger.info(bstack1lll1l1_opy_ (u"ࠫࡌ࡫࡮ࡦࡴࡤࡸࡪࡪࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡢࡶ࡫࡯ࡨࠥࡧࡲࡵ࡫ࡩࡥࡨࡺࡳࠡࡣࡷࠤࢀࢃࠧ಻").format(bstack1l11lll11_opy_));
  except Exception as e:
    logger.debug(bstack111l1ll11_opy_.format(str(e)))
def bstack1l111111l_opy_(bstack1ll1lll1l_opy_):
  global CONFIG
  try:
    host = bstack1lll1l1_opy_ (u"ࠬࡧࡰࡪ࠯ࡦࡰࡴࡻࡤࠨ಼") if bstack1lll1l1_opy_ (u"࠭ࡡࡱࡲࠪಽ") in CONFIG else bstack1lll1l1_opy_ (u"ࠧࡢࡲ࡬ࠫಾ")
    user = CONFIG[bstack1lll1l1_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪಿ")]
    key = CONFIG[bstack1lll1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬೀ")]
    bstack1l11lll1l_opy_ = bstack1lll1l1_opy_ (u"ࠪࡥࡵࡶ࠭ࡢࡷࡷࡳࡲࡧࡴࡦࠩು") if bstack1lll1l1_opy_ (u"ࠫࡦࡶࡰࠨೂ") in CONFIG else bstack1lll1l1_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧೃ")
    url = bstack1lll1l1_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡼࡿ࠽ࡿࢂࡆࡻࡾ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࢁࡽ࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀ࠳ࡸ࡫ࡳࡴ࡫ࡲࡲࡸ࠴ࡪࡴࡱࡱࠫೄ").format(user, key, host, bstack1l11lll1l_opy_,
                                                                                bstack1ll1lll1l_opy_)
    headers = {
      bstack1lll1l1_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡶࡼࡴࡪ࠭೅"): bstack1lll1l1_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫೆ"),
    }
    proxies = bstack1ll1lll1l1_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies)
    if response.json():
      return list(map(lambda session: session[bstack1lll1l1_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࠧೇ")], response.json()))
  except Exception as e:
    logger.debug(bstack1ll11lll_opy_.format(str(e)))
def bstack1l1l11111l_opy_():
  global CONFIG
  global bstack1lllllll1_opy_
  try:
    if bstack1lll1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ೈ") in CONFIG:
      host = bstack1lll1l1_opy_ (u"ࠫࡦࡶࡩ࠮ࡥ࡯ࡳࡺࡪࠧ೉") if bstack1lll1l1_opy_ (u"ࠬࡧࡰࡱࠩೊ") in CONFIG else bstack1lll1l1_opy_ (u"࠭ࡡࡱ࡫ࠪೋ")
      user = CONFIG[bstack1lll1l1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩೌ")]
      key = CONFIG[bstack1lll1l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼ್ࠫ")]
      bstack1l11lll1l_opy_ = bstack1lll1l1_opy_ (u"ࠩࡤࡴࡵ࠳ࡡࡶࡶࡲࡱࡦࡺࡥࠨ೎") if bstack1lll1l1_opy_ (u"ࠪࡥࡵࡶࠧ೏") in CONFIG else bstack1lll1l1_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭೐")
      url = bstack1lll1l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡻࡾ࠼ࡾࢁࡅࢁࡽ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࢀࢃ࠯ࡣࡷ࡬ࡰࡩࡹ࠮࡫ࡵࡲࡲࠬ೑").format(user, key, host, bstack1l11lll1l_opy_)
      headers = {
        bstack1lll1l1_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡵࡻࡳࡩࠬ೒"): bstack1lll1l1_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪ೓"),
      }
      if bstack1lll1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ೔") in CONFIG:
        params = {bstack1lll1l1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧೕ"): CONFIG[bstack1lll1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ೖ")], bstack1lll1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ೗"): CONFIG[bstack1lll1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ೘")]}
      else:
        params = {bstack1lll1l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ೙"): CONFIG[bstack1lll1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ೚")]}
      proxies = bstack1ll1lll1l1_opy_(CONFIG, url)
      response = requests.get(url, params=params, headers=headers, proxies=proxies)
      if response.json():
        bstack1lllll1l1_opy_ = response.json()[0][bstack1lll1l1_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡨࡵࡪ࡮ࡧࠫ೛")]
        if bstack1lllll1l1_opy_:
          bstack1ll1l1ll11_opy_ = bstack1lllll1l1_opy_[bstack1lll1l1_opy_ (u"ࠩࡳࡹࡧࡲࡩࡤࡡࡸࡶࡱ࠭೜")].split(bstack1lll1l1_opy_ (u"ࠪࡴࡺࡨ࡬ࡪࡥ࠰ࡦࡺ࡯࡬ࡥࠩೝ"))[0] + bstack1lll1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡶ࠳ࠬೞ") + bstack1lllll1l1_opy_[
            bstack1lll1l1_opy_ (u"ࠬ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ೟")]
          logger.info(bstack11l11l1l_opy_.format(bstack1ll1l1ll11_opy_))
          bstack1lllllll1_opy_ = bstack1lllll1l1_opy_[bstack1lll1l1_opy_ (u"࠭ࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩೠ")]
          bstack11ll1111l_opy_ = CONFIG[bstack1lll1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪೡ")]
          if bstack1lll1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪೢ") in CONFIG:
            bstack11ll1111l_opy_ += bstack1lll1l1_opy_ (u"ࠩࠣࠫೣ") + CONFIG[bstack1lll1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ೤")]
          if bstack11ll1111l_opy_ != bstack1lllll1l1_opy_[bstack1lll1l1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ೥")]:
            logger.debug(bstack1l1ll11ll_opy_.format(bstack1lllll1l1_opy_[bstack1lll1l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ೦")], bstack11ll1111l_opy_))
          return [bstack1lllll1l1_opy_[bstack1lll1l1_opy_ (u"࠭ࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩ೧")], bstack1ll1l1ll11_opy_]
    else:
      logger.warn(bstack1ll11l1111_opy_)
  except Exception as e:
    logger.debug(bstack1l1ll1l1_opy_.format(str(e)))
  return [None, None]
def bstack1111l1l11_opy_(url, bstack1llll11ll1_opy_=False):
  global CONFIG
  global bstack1llll1llll_opy_
  if not bstack1llll1llll_opy_:
    hostname = bstack11l11ll1_opy_(url)
    is_private = bstack1ll1l111l_opy_(hostname)
    if (bstack1lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ೨") in CONFIG and not bstack1l11lllll_opy_(CONFIG[bstack1lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ೩")])) and (is_private or bstack1llll11ll1_opy_):
      bstack1llll1llll_opy_ = hostname
def bstack11l11ll1_opy_(url):
  return urlparse(url).hostname
def bstack1ll1l111l_opy_(hostname):
  for bstack1ll1lllll1_opy_ in bstack111ll1111_opy_:
    regex = re.compile(bstack1ll1lllll1_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack1lll11lll1_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def getAccessibilityResults(driver):
  global CONFIG
  global bstack1lll1llll_opy_
  if not bstack11111111l_opy_.bstack1l111ll11_opy_(CONFIG, bstack1lll1llll_opy_):
    logger.warning(bstack1lll1l1_opy_ (u"ࠤࡑࡳࡹࠦࡡ࡯ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡥࡤࡲࡳࡵࡴࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡶࡪࡹࡵ࡭ࡶࡶ࠲ࠧ೪"))
    return {}
  try:
    results = driver.execute_script(bstack1lll1l1_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡳࡧࡷࡹࡷࡴࠠ࡯ࡧࡺࠤࡕࡸ࡯࡮࡫ࡶࡩ࠭࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࠩࡴࡨࡷࡴࡲࡶࡦ࠮ࠣࡶࡪࡰࡥࡤࡶࠬࠤࢀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡹࡸࡹࠡࡽࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡩ࡯࡯ࡵࡷࠤࡪࡼࡥ࡯ࡶࠣࡁࠥࡴࡥࡸࠢࡆࡹࡸࡺ࡯࡮ࡇࡹࡩࡳࡺࠨࠨࡃ࠴࠵࡞ࡥࡔࡂࡒࡢࡋࡊ࡚࡟ࡓࡇࡖ࡙ࡑ࡚ࡓࠨࠫ࠾ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡣࡰࡰࡶࡸࠥ࡬࡮ࠡ࠿ࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥ࠮ࡥࡷࡧࡱࡸ࠮ࠦࡻࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡸ࡫ࡱࡨࡴࡽ࠮ࡳࡧࡰࡳࡻ࡫ࡅࡷࡧࡱࡸࡑ࡯ࡳࡵࡧࡱࡩࡷ࠮ࠧࡂ࠳࠴࡝ࡤࡘࡅࡔࡗࡏࡘࡘࡥࡒࡆࡕࡓࡓࡓ࡙ࡅࠨ࠮ࠣࡪࡳ࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡳࡧࡶࡳࡱࡼࡥࠩࡧࡹࡩࡳࡺ࠮ࡥࡧࡷࡥ࡮ࡲ࠮ࡥࡣࡷࡥ࠮ࡁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࢀ࠿ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡸ࡫ࡱࡨࡴࡽ࠮ࡢࡦࡧࡉࡻ࡫࡮ࡵࡎ࡬ࡷࡹ࡫࡮ࡦࡴࠫࠫࡆ࠷࠱࡚ࡡࡕࡉࡘ࡛ࡌࡕࡕࡢࡖࡊ࡙ࡐࡐࡐࡖࡉࠬ࠲ࠠࡧࡰࠬ࠿ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡸ࡫ࡱࡨࡴࡽ࠮ࡥ࡫ࡶࡴࡦࡺࡣࡩࡇࡹࡩࡳࡺࠨࡦࡸࡨࡲࡹ࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽࠡࡥࡤࡸࡨ࡮ࠠࡼࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡷ࡫ࡪࡦࡥࡷࠬ࠮ࡁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃࠊࠡࠢࠣࠤࠥࠦࠠࠡࡿࠬ࠿ࠏࠦࠠࠡࠢࠥࠦࠧ೫"))
    return results
  except Exception:
    logger.error(bstack1lll1l1_opy_ (u"ࠦࡓࡵࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳࠡࡹࡨࡶࡪࠦࡦࡰࡷࡱࡨ࠳ࠨ೬"))
    return {}
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack1lll1llll_opy_
  if not bstack11111111l_opy_.bstack1l111ll11_opy_(CONFIG, bstack1lll1llll_opy_):
    logger.warning(bstack1lll1l1_opy_ (u"ࠧࡔ࡯ࡵࠢࡤࡲࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡩࡸࡹࡩࡰࡰ࠯ࠤࡨࡧ࡮࡯ࡱࡷࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹࠠࡴࡷࡰࡱࡦࡸࡹ࠯ࠤ೭"))
    return {}
  try:
    bstack1ll1111l1l_opy_ = driver.execute_script(bstack1lll1l1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡶࡪࡺࡵࡳࡰࠣࡲࡪࡽࠠࡑࡴࡲࡱ࡮ࡹࡥࠩࡨࡸࡲࡨࡺࡩࡰࡰࠣࠬࡷ࡫ࡳࡰ࡮ࡹࡩ࠱ࠦࡲࡦ࡬ࡨࡧࡹ࠯ࠠࡼࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡵࡴࡼࠤࢀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡥࡲࡲࡸࡺࠠࡦࡸࡨࡲࡹࠦ࠽ࠡࡰࡨࡻࠥࡉࡵࡴࡶࡲࡱࡊࡼࡥ࡯ࡶࠫࠫࡆ࠷࠱࡚ࡡࡗࡅࡕࡥࡇࡆࡖࡢࡖࡊ࡙ࡕࡍࡖࡖࡣࡘ࡛ࡍࡎࡃࡕ࡝ࠬ࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡧࡴࡴࡳࡵࠢࡩࡲࠥࡃࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࠫࡩࡻ࡫࡮ࡵࠫࠣࡿࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡼ࡯࡮ࡥࡱࡺ࠲ࡷ࡫࡭ࡰࡸࡨࡉࡻ࡫࡮ࡵࡎ࡬ࡷࡹ࡫࡮ࡦࡴࠫࠫࡆ࠷࠱࡚ࡡࡕࡉࡘ࡛ࡌࡕࡕࡢࡗ࡚ࡓࡍࡂࡔ࡜ࡣࡗࡋࡓࡑࡑࡑࡗࡊ࠭ࠬࠡࡨࡱ࠭ࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡸࡥࡴࡱ࡯ࡺࡪ࠮ࡥࡷࡧࡱࡸ࠳ࡪࡥࡵࡣ࡬ࡰ࠳ࡹࡵ࡮࡯ࡤࡶࡾ࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡹ࡬ࡲࡩࡵࡷ࠯ࡣࡧࡨࡊࡼࡥ࡯ࡶࡏ࡭ࡸࡺࡥ࡯ࡧࡵࠬࠬࡇ࠱࠲࡛ࡢࡖࡊ࡙ࡕࡍࡖࡖࡣࡘ࡛ࡍࡎࡃࡕ࡝ࡤࡘࡅࡔࡒࡒࡒࡘࡋࠧ࠭ࠢࡩࡲ࠮ࡁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡺ࡭ࡳࡪ࡯ࡸ࠰ࡧ࡭ࡸࡶࡡࡵࡥ࡫ࡉࡻ࡫࡮ࡵࠪࡨࡺࡪࡴࡴࠪ࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿࠣࡧࡦࡺࡣࡩࠢࡾࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡲࡦ࡬ࡨࡧࡹ࠮ࠩ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾࠌࠣࠤࠥࠦࠠࠡࠢࠣࢁ࠮ࡁࠊࠡࠢࠣࠤࠧࠨࠢ೮"))
    return bstack1ll1111l1l_opy_
  except Exception:
    logger.error(bstack1lll1l1_opy_ (u"ࠢࡏࡱࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡷࡺࡳ࡭ࡢࡴࡼࠤࡼࡧࡳࠡࡨࡲࡹࡳࡪ࠮ࠣ೯"))
    return {}