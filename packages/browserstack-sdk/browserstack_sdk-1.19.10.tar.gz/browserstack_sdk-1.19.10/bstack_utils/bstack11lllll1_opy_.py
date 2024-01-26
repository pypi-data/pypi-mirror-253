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
class bstack11l111lll_opy_:
    def __init__(self, handler):
        self._11111l1l11_opy_ = None
        self.handler = handler
        self._11111l11ll_opy_ = self.bstack11111l1ll1_opy_()
        self.patch()
    def patch(self):
        self._11111l1l11_opy_ = self._11111l11ll_opy_.execute
        self._11111l11ll_opy_.execute = self.bstack11111l1l1l_opy_()
    def bstack11111l1l1l_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack1lll1l1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫ࠢᏯ"), driver_command)
            response = self._11111l1l11_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack1lll1l1_opy_ (u"ࠣࡣࡩࡸࡪࡸࠢᏰ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11111l11ll_opy_.execute = self._11111l1l11_opy_
    @staticmethod
    def bstack11111l1ll1_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver