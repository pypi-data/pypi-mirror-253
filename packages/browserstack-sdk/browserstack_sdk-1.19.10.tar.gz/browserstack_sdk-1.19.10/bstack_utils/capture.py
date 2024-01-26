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
import sys
class bstack1l11lll1ll_opy_:
    def __init__(self, handler):
        self._11ll1l11l1_opy_ = sys.stdout.write
        self._11ll1l1111_opy_ = sys.stderr.write
        self.handler = handler
        self._started = False
    def start(self):
        if self._started:
            return
        self._started = True
        sys.stdout.write = self.bstack11ll1l111l_opy_
        sys.stdout.error = self.bstack11ll11llll_opy_
    def bstack11ll1l111l_opy_(self, _str):
        self._11ll1l11l1_opy_(_str)
        if self.handler:
            self.handler({bstack1lll1l1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨຜ"): bstack1lll1l1_opy_ (u"ࠪࡍࡓࡌࡏࠨຝ"), bstack1lll1l1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬພ"): _str})
    def bstack11ll11llll_opy_(self, _str):
        self._11ll1l1111_opy_(_str)
        if self.handler:
            self.handler({bstack1lll1l1_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫຟ"): bstack1lll1l1_opy_ (u"࠭ࡅࡓࡔࡒࡖࠬຠ"), bstack1lll1l1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨມ"): _str})
    def reset(self):
        if not self._started:
            return
        self._started = False
        sys.stdout.write = self._11ll1l11l1_opy_
        sys.stderr.write = self._11ll1l1111_opy_