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
import json
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack111l1111_opy_ = {}
        bstack1l1l111111_opy_ = os.environ.get(bstack1lll1l1_opy_ (u"ࠨࡅࡘࡖࡗࡋࡎࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡉࡇࡔࡂࠩ೰"), bstack1lll1l1_opy_ (u"ࠩࠪೱ"))
        if not bstack1l1l111111_opy_:
            return bstack111l1111_opy_
        try:
            bstack1l11llllll_opy_ = json.loads(bstack1l1l111111_opy_)
            if bstack1lll1l1_opy_ (u"ࠥࡳࡸࠨೲ") in bstack1l11llllll_opy_:
                bstack111l1111_opy_[bstack1lll1l1_opy_ (u"ࠦࡴࡹࠢೳ")] = bstack1l11llllll_opy_[bstack1lll1l1_opy_ (u"ࠧࡵࡳࠣ೴")]
            if bstack1lll1l1_opy_ (u"ࠨ࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠥ೵") in bstack1l11llllll_opy_ or bstack1lll1l1_opy_ (u"ࠢࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠥ೶") in bstack1l11llllll_opy_:
                bstack111l1111_opy_[bstack1lll1l1_opy_ (u"ࠣࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠦ೷")] = bstack1l11llllll_opy_.get(bstack1lll1l1_opy_ (u"ࠤࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳࠨ೸"), bstack1l11llllll_opy_.get(bstack1lll1l1_opy_ (u"ࠥࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳࠨ೹")))
            if bstack1lll1l1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࠧ೺") in bstack1l11llllll_opy_ or bstack1lll1l1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠥ೻") in bstack1l11llllll_opy_:
                bstack111l1111_opy_[bstack1lll1l1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠦ೼")] = bstack1l11llllll_opy_.get(bstack1lll1l1_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࠣ೽"), bstack1l11llllll_opy_.get(bstack1lll1l1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪࠨ೾")))
            if bstack1lll1l1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠦ೿") in bstack1l11llllll_opy_ or bstack1lll1l1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠦഀ") in bstack1l11llllll_opy_:
                bstack111l1111_opy_[bstack1lll1l1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠧഁ")] = bstack1l11llllll_opy_.get(bstack1lll1l1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠢം"), bstack1l11llllll_opy_.get(bstack1lll1l1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠢഃ")))
            if bstack1lll1l1_opy_ (u"ࠢࡥࡧࡹ࡭ࡨ࡫ࠢഄ") in bstack1l11llllll_opy_ or bstack1lll1l1_opy_ (u"ࠣࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠧഅ") in bstack1l11llllll_opy_:
                bstack111l1111_opy_[bstack1lll1l1_opy_ (u"ࠤࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪࠨആ")] = bstack1l11llllll_opy_.get(bstack1lll1l1_opy_ (u"ࠥࡨࡪࡼࡩࡤࡧࠥഇ"), bstack1l11llllll_opy_.get(bstack1lll1l1_opy_ (u"ࠦࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠣഈ")))
            if bstack1lll1l1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࠢഉ") in bstack1l11llllll_opy_ or bstack1lll1l1_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧഊ") in bstack1l11llllll_opy_:
                bstack111l1111_opy_[bstack1lll1l1_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨഋ")] = bstack1l11llllll_opy_.get(bstack1lll1l1_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠥഌ"), bstack1l11llllll_opy_.get(bstack1lll1l1_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠣ഍")))
            if bstack1lll1l1_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡤࡼࡥࡳࡵ࡬ࡳࡳࠨഎ") in bstack1l11llllll_opy_ or bstack1lll1l1_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳࠨഏ") in bstack1l11llllll_opy_:
                bstack111l1111_opy_[bstack1lll1l1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢഐ")] = bstack1l11llllll_opy_.get(bstack1lll1l1_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠤ഑"), bstack1l11llllll_opy_.get(bstack1lll1l1_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤഒ")))
            if bstack1lll1l1_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭ࡗࡣࡵ࡭ࡦࡨ࡬ࡦࡵࠥഓ") in bstack1l11llllll_opy_:
                bstack111l1111_opy_[bstack1lll1l1_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡘࡤࡶ࡮ࡧࡢ࡭ࡧࡶࠦഔ")] = bstack1l11llllll_opy_[bstack1lll1l1_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯࡙ࡥࡷ࡯ࡡࡣ࡮ࡨࡷࠧക")]
        except Exception as error:
            logger.error(bstack1lll1l1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡤࡷࡵࡶࡪࡴࡴࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠣࡨࡦࡺࡡ࠻ࠢࠥഖ") +  str(error))
        return bstack111l1111_opy_