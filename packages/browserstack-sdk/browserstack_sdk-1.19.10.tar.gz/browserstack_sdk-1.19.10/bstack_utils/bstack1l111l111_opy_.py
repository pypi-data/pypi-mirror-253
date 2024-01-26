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
from collections import deque
from bstack_utils.constants import *
class bstack1l111111_opy_:
    def __init__(self):
        self._1111lllll1_opy_ = deque()
        self._1111lll1ll_opy_ = {}
        self._1111lll111_opy_ = False
    def bstack111l111ll1_opy_(self, test_name, bstack1111lll1l1_opy_):
        bstack111l111111_opy_ = self._1111lll1ll_opy_.get(test_name, {})
        return bstack111l111111_opy_.get(bstack1111lll1l1_opy_, 0)
    def bstack111l111l11_opy_(self, test_name, bstack1111lll1l1_opy_):
        bstack1111lll11l_opy_ = self.bstack111l111ll1_opy_(test_name, bstack1111lll1l1_opy_)
        self.bstack111l1111l1_opy_(test_name, bstack1111lll1l1_opy_)
        return bstack1111lll11l_opy_
    def bstack111l1111l1_opy_(self, test_name, bstack1111lll1l1_opy_):
        if test_name not in self._1111lll1ll_opy_:
            self._1111lll1ll_opy_[test_name] = {}
        bstack111l111111_opy_ = self._1111lll1ll_opy_[test_name]
        bstack1111lll11l_opy_ = bstack111l111111_opy_.get(bstack1111lll1l1_opy_, 0)
        bstack111l111111_opy_[bstack1111lll1l1_opy_] = bstack1111lll11l_opy_ + 1
    def bstack111l1l111_opy_(self, bstack1111llll1l_opy_, bstack111l1111ll_opy_):
        bstack1111llll11_opy_ = self.bstack111l111l11_opy_(bstack1111llll1l_opy_, bstack111l1111ll_opy_)
        bstack111l111l1l_opy_ = bstack11ll11l1ll_opy_[bstack111l1111ll_opy_]
        bstack111l11111l_opy_ = bstack1lll1l1_opy_ (u"ࠤࡾࢁ࠲ࢁࡽ࠮ࡽࢀࠦ᎖").format(bstack1111llll1l_opy_, bstack111l111l1l_opy_, bstack1111llll11_opy_)
        self._1111lllll1_opy_.append(bstack111l11111l_opy_)
    def bstack111lll11l_opy_(self):
        return len(self._1111lllll1_opy_) == 0
    def bstack1l1l1ll1_opy_(self):
        bstack1111llllll_opy_ = self._1111lllll1_opy_.popleft()
        return bstack1111llllll_opy_
    def capturing(self):
        return self._1111lll111_opy_
    def bstack1l1l111l_opy_(self):
        self._1111lll111_opy_ = True
    def bstack1ll11ll1l_opy_(self):
        self._1111lll111_opy_ = False