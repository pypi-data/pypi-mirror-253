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
from browserstack_sdk.bstack1ll1ll11_opy_ import bstack1l1l11l11l_opy_
from browserstack_sdk.bstack1l11l111ll_opy_ import RobotHandler
def bstack11l1l111l_opy_(framework):
    if framework.lower() == bstack1lll1l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨᄭ"):
        return bstack1l1l11l11l_opy_.version()
    elif framework.lower() == bstack1lll1l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨᄮ"):
        return RobotHandler.version()
    elif framework.lower() == bstack1lll1l1_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪᄯ"):
        import behave
        return behave.__version__
    else:
        return bstack1lll1l1_opy_ (u"ࠫࡺࡴ࡫࡯ࡱࡺࡲࠬᄰ")