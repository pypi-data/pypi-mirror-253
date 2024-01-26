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
class RobotHandler():
    def __init__(self, args, logger, bstack11llll11l1_opy_, bstack11lllll11l_opy_):
        self.args = args
        self.logger = logger
        self.bstack11llll11l1_opy_ = bstack11llll11l1_opy_
        self.bstack11lllll11l_opy_ = bstack11lllll11l_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1l11ll1lll_opy_(bstack11lll1lll1_opy_):
        bstack11lll1ll11_opy_ = []
        if bstack11lll1lll1_opy_:
            tokens = str(os.path.basename(bstack11lll1lll1_opy_)).split(bstack1lll1l1_opy_ (u"ࠢࡠࠤ฀"))
            camelcase_name = bstack1lll1l1_opy_ (u"ࠣࠢࠥก").join(t.title() for t in tokens)
            suite_name, bstack11lll1l1ll_opy_ = os.path.splitext(camelcase_name)
            bstack11lll1ll11_opy_.append(suite_name)
        return bstack11lll1ll11_opy_
    @staticmethod
    def bstack11lll1ll1l_opy_(typename):
        if bstack1lll1l1_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧข") in typename:
            return bstack1lll1l1_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵࠦฃ")
        return bstack1lll1l1_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧค")