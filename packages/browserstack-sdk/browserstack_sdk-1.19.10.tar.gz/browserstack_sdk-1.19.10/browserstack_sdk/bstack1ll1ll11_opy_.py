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
import multiprocessing
import os
import json
from time import sleep
import bstack_utils.bstack1ll1ll111_opy_ as bstack11111111l_opy_
from browserstack_sdk.bstack1l1llll11_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack1l1llll1ll_opy_
class bstack1l1l11l11l_opy_:
    def __init__(self, args, logger, bstack11llll11l1_opy_, bstack11lllll11l_opy_):
        self.args = args
        self.logger = logger
        self.bstack11llll11l1_opy_ = bstack11llll11l1_opy_
        self.bstack11lllll11l_opy_ = bstack11lllll11l_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack11111ll1_opy_ = []
        self.bstack11llll1ll1_opy_ = None
        self.bstack1l1ll11lll_opy_ = []
        self.bstack11llllll11_opy_ = self.bstack1ll11l111_opy_()
        self.bstack11l1ll11l_opy_ = -1
    def bstack111l1l11_opy_(self, bstack11llll1111_opy_):
        self.parse_args()
        self.bstack11llll1lll_opy_()
        self.bstack11lll1llll_opy_(bstack11llll1111_opy_)
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    def bstack11lllll111_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack11l1ll11l_opy_ = -1
        if bstack1lll1l1_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭෣") in self.bstack11llll11l1_opy_:
            self.bstack11l1ll11l_opy_ = int(self.bstack11llll11l1_opy_[bstack1lll1l1_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ෤")])
        try:
            bstack11lllll1ll_opy_ = [bstack1lll1l1_opy_ (u"ࠨ࠯࠰ࡨࡷ࡯ࡶࡦࡴࠪ෥"), bstack1lll1l1_opy_ (u"ࠩ࠰࠱ࡵࡲࡵࡨ࡫ࡱࡷࠬ෦"), bstack1lll1l1_opy_ (u"ࠪ࠱ࡵ࠭෧")]
            if self.bstack11l1ll11l_opy_ >= 0:
                bstack11lllll1ll_opy_.extend([bstack1lll1l1_opy_ (u"ࠫ࠲࠳࡮ࡶ࡯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬ෨"), bstack1lll1l1_opy_ (u"ࠬ࠳࡮ࠨ෩")])
            for arg in bstack11lllll1ll_opy_:
                self.bstack11lllll111_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack11llll1lll_opy_(self):
        bstack11llll1ll1_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack11llll1ll1_opy_ = bstack11llll1ll1_opy_
        return bstack11llll1ll1_opy_
    def bstack1ll1lll111_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            import importlib
            bstack11llll1l1l_opy_ = importlib.find_loader(bstack1lll1l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠨ෪"))
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack1l1llll1ll_opy_)
    def bstack11lll1llll_opy_(self, bstack11llll1111_opy_):
        bstack11l1l11l_opy_ = Config.bstack1lllll11l1_opy_()
        if bstack11llll1111_opy_:
            self.bstack11llll1ll1_opy_.append(bstack1lll1l1_opy_ (u"ࠧ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ෫"))
            self.bstack11llll1ll1_opy_.append(bstack1lll1l1_opy_ (u"ࠨࡖࡵࡹࡪ࠭෬"))
        if bstack11l1l11l_opy_.bstack11llll111l_opy_():
            self.bstack11llll1ll1_opy_.append(bstack1lll1l1_opy_ (u"ࠩ࠰࠱ࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨ෭"))
            self.bstack11llll1ll1_opy_.append(bstack1lll1l1_opy_ (u"ࠪࡘࡷࡻࡥࠨ෮"))
        self.bstack11llll1ll1_opy_.append(bstack1lll1l1_opy_ (u"ࠫ࠲ࡶࠧ෯"))
        self.bstack11llll1ll1_opy_.append(bstack1lll1l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡴࡱࡻࡧࡪࡰࠪ෰"))
        self.bstack11llll1ll1_opy_.append(bstack1lll1l1_opy_ (u"࠭࠭࠮ࡦࡵ࡭ࡻ࡫ࡲࠨ෱"))
        self.bstack11llll1ll1_opy_.append(bstack1lll1l1_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧෲ"))
        if self.bstack11l1ll11l_opy_ > 1:
            self.bstack11llll1ll1_opy_.append(bstack1lll1l1_opy_ (u"ࠨ࠯ࡱࠫෳ"))
            self.bstack11llll1ll1_opy_.append(str(self.bstack11l1ll11l_opy_))
    def bstack11llll11ll_opy_(self):
        bstack1l1ll11lll_opy_ = []
        for spec in self.bstack11111ll1_opy_:
            bstack1l1l1ll111_opy_ = [spec]
            bstack1l1l1ll111_opy_ += self.bstack11llll1ll1_opy_
            bstack1l1ll11lll_opy_.append(bstack1l1l1ll111_opy_)
        self.bstack1l1ll11lll_opy_ = bstack1l1ll11lll_opy_
        return bstack1l1ll11lll_opy_
    def bstack1ll11l111_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack11llllll11_opy_ = True
            return True
        except Exception as e:
            self.bstack11llllll11_opy_ = False
        return self.bstack11llllll11_opy_
    def bstack1ll1l1111l_opy_(self, bstack11llll1l11_opy_, bstack111l1l11_opy_):
        bstack111l1l11_opy_[bstack1lll1l1_opy_ (u"ࠩࡆࡓࡓࡌࡉࡈࠩ෴")] = self.bstack11llll11l1_opy_
        multiprocessing.set_start_method(bstack1lll1l1_opy_ (u"ࠪࡷࡵࡧࡷ࡯ࠩ෵"))
        if bstack1lll1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ෶") in self.bstack11llll11l1_opy_:
            bstack1l1l1llll_opy_ = []
            manager = multiprocessing.Manager()
            bstack11l11lll_opy_ = manager.list()
            for index, platform in enumerate(self.bstack11llll11l1_opy_[bstack1lll1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ෷")]):
                bstack1l1l1llll_opy_.append(multiprocessing.Process(name=str(index),
                                                           target=bstack11llll1l11_opy_,
                                                           args=(self.bstack11llll1ll1_opy_, bstack111l1l11_opy_, bstack11l11lll_opy_)))
            i = 0
            bstack11lllll1l1_opy_ = len(self.bstack11llll11l1_opy_[bstack1lll1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ෸")])
            for t in bstack1l1l1llll_opy_:
                os.environ[bstack1lll1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧ෹")] = str(i)
                os.environ[bstack1lll1l1_opy_ (u"ࠨࡅࡘࡖࡗࡋࡎࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡉࡇࡔࡂࠩ෺")] = json.dumps(self.bstack11llll11l1_opy_[bstack1lll1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ෻")][i % bstack11lllll1l1_opy_])
                i += 1
                t.start()
            for t in bstack1l1l1llll_opy_:
                t.join()
            return list(bstack11l11lll_opy_)
    @staticmethod
    def bstack1l111ll1_opy_(driver, bstack1l1l111l1l_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack1lll1l1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧ෼"), None)
        if item and getattr(item, bstack1lll1l1_opy_ (u"ࠫࡤࡧ࠱࠲ࡻࡢࡸࡪࡹࡴࡠࡥࡤࡷࡪ࠭෽"), None) and not getattr(item, bstack1lll1l1_opy_ (u"ࠬࡥࡡ࠲࠳ࡼࡣࡸࡺ࡯ࡱࡡࡧࡳࡳ࡫ࠧ෾"), False):
            logger.info(
                bstack1lll1l1_opy_ (u"ࠨࡁࡶࡶࡲࡱࡦࡺࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤࡪࡾࡥࡤࡷࡷ࡭ࡴࡴࠠࡩࡣࡶࠤࡪࡴࡤࡦࡦ࠱ࠤࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡨࡲࡶࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡺࡥࡴࡶ࡬ࡲ࡬ࠦࡩࡴࠢࡸࡲࡩ࡫ࡲࡸࡣࡼ࠲ࠧ෿"))
            bstack11llllll1l_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack11111111l_opy_.bstack11l1ll1ll_opy_(driver, bstack11llllll1l_opy_, item.name, item.module.__name__, item.path, bstack1l1l111l1l_opy_)
            item._a11y_stop_done = True
            if wait:
                sleep(2)