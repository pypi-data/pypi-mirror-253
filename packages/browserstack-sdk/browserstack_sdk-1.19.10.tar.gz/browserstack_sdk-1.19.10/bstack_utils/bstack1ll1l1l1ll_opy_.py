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
import datetime
import json
import logging
import os
import threading
from bstack_utils.helper import bstack11lll111l1_opy_, bstack1l1llll1l_opy_, get_host_info, bstack11ll1ll1l1_opy_, bstack11lll1l11l_opy_, bstack11l11ll1ll_opy_, \
    bstack11l1ll111l_opy_, bstack11l1ll11l1_opy_, bstack1ll1ll1lll_opy_, bstack11l1lll1ll_opy_, bstack1l11lllll_opy_, bstack1l11l11lll_opy_
from bstack_utils.bstack11111lll1l_opy_ import bstack11111lllll_opy_
from bstack_utils.bstack1l11ll1l11_opy_ import bstack1l111l1ll1_opy_
bstack1lllllll11l_opy_ = [
    bstack1lll1l1_opy_ (u"ࠫࡑࡵࡧࡄࡴࡨࡥࡹ࡫ࡤࠨᑣ"), bstack1lll1l1_opy_ (u"ࠬࡉࡂࡕࡕࡨࡷࡸ࡯࡯࡯ࡅࡵࡩࡦࡺࡥࡥࠩᑤ"), bstack1lll1l1_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨᑥ"), bstack1lll1l1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔ࡭࡬ࡴࡵ࡫ࡤࠨᑦ"),
    bstack1lll1l1_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪᑧ"), bstack1lll1l1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪᑨ"), bstack1lll1l1_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᑩ")
]
bstack1lllll1l1ll_opy_ = bstack1lll1l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡩ࡯࡭࡮ࡨࡧࡹࡵࡲ࠮ࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫᑪ")
logger = logging.getLogger(__name__)
class bstack1l1ll11l_opy_:
    bstack11111lll1l_opy_ = None
    bs_config = None
    @classmethod
    @bstack1l11l11lll_opy_(class_method=True)
    def launch(cls, bs_config, bstack1lllll1llll_opy_):
        cls.bs_config = bs_config
        if not cls.bstack1llllll1l11_opy_():
            return
        cls.bstack1lllllll1ll_opy_()
        bstack11ll1lll11_opy_ = bstack11ll1ll1l1_opy_(bs_config)
        bstack11ll1ll111_opy_ = bstack11lll1l11l_opy_(bs_config)
        data = {
            bstack1lll1l1_opy_ (u"ࠬ࡬࡯ࡳ࡯ࡤࡸࠬᑫ"): bstack1lll1l1_opy_ (u"࠭ࡪࡴࡱࡱࠫᑬ"),
            bstack1lll1l1_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡠࡰࡤࡱࡪ࠭ᑭ"): bs_config.get(bstack1lll1l1_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ᑮ"), bstack1lll1l1_opy_ (u"ࠩࠪᑯ")),
            bstack1lll1l1_opy_ (u"ࠪࡲࡦࡳࡥࠨᑰ"): bs_config.get(bstack1lll1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧᑱ"), os.path.basename(os.path.abspath(os.getcwd()))),
            bstack1lll1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᑲ"): bs_config.get(bstack1lll1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᑳ")),
            bstack1lll1l1_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬᑴ"): bs_config.get(bstack1lll1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫᑵ"), bstack1lll1l1_opy_ (u"ࠩࠪᑶ")),
            bstack1lll1l1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡡࡷ࡭ࡲ࡫ࠧᑷ"): datetime.datetime.now().isoformat(),
            bstack1lll1l1_opy_ (u"ࠫࡹࡧࡧࡴࠩᑸ"): bstack11l11ll1ll_opy_(bs_config),
            bstack1lll1l1_opy_ (u"ࠬ࡮࡯ࡴࡶࡢ࡭ࡳ࡬࡯ࠨᑹ"): get_host_info(),
            bstack1lll1l1_opy_ (u"࠭ࡣࡪࡡ࡬ࡲ࡫ࡵࠧᑺ"): bstack1l1llll1l_opy_(),
            bstack1lll1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡲࡶࡰࡢ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧᑻ"): os.environ.get(bstack1lll1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡒࡖࡐࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧᑼ")),
            bstack1lll1l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࡡࡷࡩࡸࡺࡳࡠࡴࡨࡶࡺࡴࠧᑽ"): os.environ.get(bstack1lll1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࠨᑾ"), False),
            bstack1lll1l1_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࡤࡩ࡯࡯ࡶࡵࡳࡱ࠭ᑿ"): bstack11lll111l1_opy_(),
            bstack1lll1l1_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᒀ"): {
                bstack1lll1l1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡐࡤࡱࡪ࠭ᒁ"): bstack1lllll1llll_opy_.get(bstack1lll1l1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࠨᒂ"), bstack1lll1l1_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴࠨᒃ")),
                bstack1lll1l1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬᒄ"): bstack1lllll1llll_opy_.get(bstack1lll1l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧᒅ")),
                bstack1lll1l1_opy_ (u"ࠫࡸࡪ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨᒆ"): bstack1lllll1llll_opy_.get(bstack1lll1l1_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪᒇ"))
            }
        }
        config = {
            bstack1lll1l1_opy_ (u"࠭ࡡࡶࡶ࡫ࠫᒈ"): (bstack11ll1lll11_opy_, bstack11ll1ll111_opy_),
            bstack1lll1l1_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨᒉ"): cls.default_headers()
        }
        response = bstack1ll1ll1lll_opy_(bstack1lll1l1_opy_ (u"ࠨࡒࡒࡗ࡙࠭ᒊ"), cls.request_url(bstack1lll1l1_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡹ࡮ࡲࡤࡴࠩᒋ")), data, config)
        if response.status_code != 200:
            os.environ[bstack1lll1l1_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡃࡐࡏࡓࡐࡊ࡚ࡅࡅࠩᒌ")] = bstack1lll1l1_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪᒍ")
            os.environ[bstack1lll1l1_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡍ࡛࡙࠭ᒎ")] = bstack1lll1l1_opy_ (u"࠭࡮ࡶ࡮࡯ࠫᒏ")
            os.environ[bstack1lll1l1_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡌࡆ࡙ࡈࡆࡆࡢࡍࡉ࠭ᒐ")] = bstack1lll1l1_opy_ (u"ࠣࡰࡸࡰࡱࠨᒑ")
            os.environ[bstack1lll1l1_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡁࡍࡎࡒ࡛ࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࡕࠪᒒ")] = bstack1lll1l1_opy_ (u"ࠥࡲࡺࡲ࡬ࠣᒓ")
            bstack1llllll111l_opy_ = response.json()
            if bstack1llllll111l_opy_ and bstack1llllll111l_opy_[bstack1lll1l1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᒔ")]:
                error_message = bstack1llllll111l_opy_[bstack1lll1l1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᒕ")]
                if bstack1llllll111l_opy_[bstack1lll1l1_opy_ (u"࠭ࡥࡳࡴࡲࡶ࡙ࡿࡰࡦࠩᒖ")] == bstack1lll1l1_opy_ (u"ࠧࡆࡔࡕࡓࡗࡥࡉࡏࡘࡄࡐࡎࡊ࡟ࡄࡔࡈࡈࡊࡔࡔࡊࡃࡏࡗࠬᒗ"):
                    logger.error(error_message)
                elif bstack1llllll111l_opy_[bstack1lll1l1_opy_ (u"ࠨࡧࡵࡶࡴࡸࡔࡺࡲࡨࠫᒘ")] == bstack1lll1l1_opy_ (u"ࠩࡈࡖࡗࡕࡒࡠࡃࡆࡇࡊ࡙ࡓࡠࡆࡈࡒࡎࡋࡄࠨᒙ"):
                    logger.info(error_message)
                elif bstack1llllll111l_opy_[bstack1lll1l1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࡖࡼࡴࡪ࠭ᒚ")] == bstack1lll1l1_opy_ (u"ࠫࡊࡘࡒࡐࡔࡢࡗࡉࡑ࡟ࡅࡇࡓࡖࡊࡉࡁࡕࡇࡇࠫᒛ"):
                    logger.error(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack1lll1l1_opy_ (u"ࠧࡊࡡࡵࡣࠣࡹࡵࡲ࡯ࡢࡦࠣࡸࡴࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯࡚ࠥࡥࡴࡶࠣࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠣࡪࡦ࡯࡬ࡦࡦࠣࡨࡺ࡫ࠠࡵࡱࠣࡷࡴࡳࡥࠡࡧࡵࡶࡴࡸࠢᒜ"))
            return [None, None, None]
        logger.debug(bstack1lll1l1_opy_ (u"࠭ࡔࡦࡵࡷࠤࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠤࡇࡻࡩ࡭ࡦࠣࡧࡷ࡫ࡡࡵ࡫ࡲࡲ࡙ࠥࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭ࠣࠪᒝ"))
        os.environ[bstack1lll1l1_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡇࡔࡓࡐࡍࡇࡗࡉࡉ࠭ᒞ")] = bstack1lll1l1_opy_ (u"ࠨࡶࡵࡹࡪ࠭ᒟ")
        bstack1llllll111l_opy_ = response.json()
        if bstack1llllll111l_opy_.get(bstack1lll1l1_opy_ (u"ࠩ࡭ࡻࡹ࠭ᒠ")):
            os.environ[bstack1lll1l1_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡋ࡙ࡗࠫᒡ")] = bstack1llllll111l_opy_[bstack1lll1l1_opy_ (u"ࠫ࡯ࡽࡴࠨᒢ")]
            os.environ[bstack1lll1l1_opy_ (u"ࠬࡉࡒࡆࡆࡈࡒ࡙ࡏࡁࡍࡕࡢࡊࡔࡘ࡟ࡄࡔࡄࡗࡍࡥࡒࡆࡒࡒࡖ࡙ࡏࡎࡈࠩᒣ")] = json.dumps({
                bstack1lll1l1_opy_ (u"࠭ࡵࡴࡧࡵࡲࡦࡳࡥࠨᒤ"): bstack11ll1lll11_opy_,
                bstack1lll1l1_opy_ (u"ࠧࡱࡣࡶࡷࡼࡵࡲࡥࠩᒥ"): bstack11ll1ll111_opy_
            })
        if bstack1llllll111l_opy_.get(bstack1lll1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪᒦ")):
            os.environ[bstack1lll1l1_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡎࡁࡔࡊࡈࡈࡤࡏࡄࠨᒧ")] = bstack1llllll111l_opy_[bstack1lll1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬᒨ")]
        if bstack1llllll111l_opy_.get(bstack1lll1l1_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡢࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨᒩ")):
            os.environ[bstack1lll1l1_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡄࡐࡑࡕࡗࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࡘ࠭ᒪ")] = str(bstack1llllll111l_opy_[bstack1lll1l1_opy_ (u"࠭ࡡ࡭࡮ࡲࡻࡤࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪᒫ")])
        return [bstack1llllll111l_opy_[bstack1lll1l1_opy_ (u"ࠧ࡫ࡹࡷࠫᒬ")], bstack1llllll111l_opy_[bstack1lll1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪᒭ")], bstack1llllll111l_opy_[bstack1lll1l1_opy_ (u"ࠩࡤࡰࡱࡵࡷࡠࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡸ࠭ᒮ")]]
    @classmethod
    @bstack1l11l11lll_opy_(class_method=True)
    def stop(cls):
        if not cls.on():
            return
        if os.environ[bstack1lll1l1_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡋ࡙ࡗࠫᒯ")] == bstack1lll1l1_opy_ (u"ࠦࡳࡻ࡬࡭ࠤᒰ") or os.environ[bstack1lll1l1_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡊࡄࡗࡍࡋࡄࡠࡋࡇࠫᒱ")] == bstack1lll1l1_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦᒲ"):
            print(bstack1lll1l1_opy_ (u"ࠧࡆ࡚ࡆࡉࡕ࡚ࡉࡐࡐࠣࡍࡓࠦࡳࡵࡱࡳࡆࡺ࡯࡬ࡥࡗࡳࡷࡹࡸࡥࡢ࡯ࠣࡖࡊࡗࡕࡆࡕࡗࠤ࡙ࡕࠠࡕࡇࡖࡘࠥࡕࡂࡔࡇࡕ࡚ࡆࡈࡉࡍࡋࡗ࡝ࠥࡀࠠࡎ࡫ࡶࡷ࡮ࡴࡧࠡࡣࡸࡸ࡭࡫࡮ࡵ࡫ࡦࡥࡹ࡯࡯࡯ࠢࡷࡳࡰ࡫࡮ࠨᒳ"))
            return {
                bstack1lll1l1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨᒴ"): bstack1lll1l1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᒵ"),
                bstack1lll1l1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᒶ"): bstack1lll1l1_opy_ (u"࡙ࠫࡵ࡫ࡦࡰ࠲ࡦࡺ࡯࡬ࡥࡋࡇࠤ࡮ࡹࠠࡶࡰࡧࡩ࡫࡯࡮ࡦࡦ࠯ࠤࡧࡻࡩ࡭ࡦࠣࡧࡷ࡫ࡡࡵ࡫ࡲࡲࠥࡳࡩࡨࡪࡷࠤ࡭ࡧࡶࡦࠢࡩࡥ࡮ࡲࡥࡥࠩᒷ")
            }
        else:
            cls.bstack11111lll1l_opy_.shutdown()
            data = {
                bstack1lll1l1_opy_ (u"ࠬࡹࡴࡰࡲࡢࡸ࡮ࡳࡥࠨᒸ"): datetime.datetime.now().isoformat()
            }
            config = {
                bstack1lll1l1_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧᒹ"): cls.default_headers()
            }
            bstack11l11lllll_opy_ = bstack1lll1l1_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿ࠲ࡷࡹࡵࡰࠨᒺ").format(os.environ[bstack1lll1l1_opy_ (u"ࠣࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠢᒻ")])
            bstack1llllll1lll_opy_ = cls.request_url(bstack11l11lllll_opy_)
            response = bstack1ll1ll1lll_opy_(bstack1lll1l1_opy_ (u"ࠩࡓ࡙࡙࠭ᒼ"), bstack1llllll1lll_opy_, data, config)
            if not response.ok:
                raise Exception(bstack1lll1l1_opy_ (u"ࠥࡗࡹࡵࡰࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡱࡳࡹࠦ࡯࡬ࠤᒽ"))
    @classmethod
    def bstack1l11ll1111_opy_(cls):
        if cls.bstack11111lll1l_opy_ is None:
            return
        cls.bstack11111lll1l_opy_.shutdown()
    @classmethod
    def bstack1l1ll1111_opy_(cls):
        if cls.on():
            print(
                bstack1lll1l1_opy_ (u"࡛ࠫ࡯ࡳࡪࡶࠣ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿࠣࡸࡴࠦࡶࡪࡧࡺࠤࡧࡻࡩ࡭ࡦࠣࡶࡪࡶ࡯ࡳࡶ࠯ࠤ࡮ࡴࡳࡪࡩ࡫ࡸࡸ࠲ࠠࡢࡰࡧࠤࡲࡧ࡮ࡺࠢࡰࡳࡷ࡫ࠠࡥࡧࡥࡹ࡬࡭ࡩ࡯ࡩࠣ࡭ࡳ࡬࡯ࡳ࡯ࡤࡸ࡮ࡵ࡮ࠡࡣ࡯ࡰࠥࡧࡴࠡࡱࡱࡩࠥࡶ࡬ࡢࡥࡨࠥࡡࡴࠧᒾ").format(os.environ[bstack1lll1l1_opy_ (u"ࠧࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡊࡄࡗࡍࡋࡄࡠࡋࡇࠦᒿ")]))
    @classmethod
    def bstack1lllllll1ll_opy_(cls):
        if cls.bstack11111lll1l_opy_ is not None:
            return
        cls.bstack11111lll1l_opy_ = bstack11111lllll_opy_(cls.bstack1llllll11ll_opy_)
        cls.bstack11111lll1l_opy_.start()
    @classmethod
    def bstack1l11l1111l_opy_(cls, bstack1l11llll11_opy_, bstack1lllll1ll11_opy_=bstack1lll1l1_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡢࡢࡶࡦ࡬ࠬᓀ")):
        if not cls.on():
            return
        bstack1111l11l1_opy_ = bstack1l11llll11_opy_[bstack1lll1l1_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫᓁ")]
        bstack1llllll11l1_opy_ = {
            bstack1lll1l1_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩᓂ"): bstack1lll1l1_opy_ (u"ࠩࡗࡩࡸࡺ࡟ࡔࡶࡤࡶࡹࡥࡕࡱ࡮ࡲࡥࡩ࠭ᓃ"),
            bstack1lll1l1_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬᓄ"): bstack1lll1l1_opy_ (u"࡙ࠫ࡫ࡳࡵࡡࡈࡲࡩࡥࡕࡱ࡮ࡲࡥࡩ࠭ᓅ"),
            bstack1lll1l1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙࡫ࡪࡲࡳࡩࡩ࠭ᓆ"): bstack1lll1l1_opy_ (u"࠭ࡔࡦࡵࡷࡣࡘࡱࡩࡱࡲࡨࡨࡤ࡛ࡰ࡭ࡱࡤࡨࠬᓇ"),
            bstack1lll1l1_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫᓈ"): bstack1lll1l1_opy_ (u"ࠨࡎࡲ࡫ࡤ࡛ࡰ࡭ࡱࡤࡨࠬᓉ"),
            bstack1lll1l1_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪᓊ"): bstack1lll1l1_opy_ (u"ࠪࡌࡴࡵ࡫ࡠࡕࡷࡥࡷࡺ࡟ࡖࡲ࡯ࡳࡦࡪࠧᓋ"),
            bstack1lll1l1_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᓌ"): bstack1lll1l1_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡢࡉࡳࡪ࡟ࡖࡲ࡯ࡳࡦࡪࠧᓍ"),
            bstack1lll1l1_opy_ (u"࠭ࡃࡃࡖࡖࡩࡸࡹࡩࡰࡰࡆࡶࡪࡧࡴࡦࡦࠪᓎ"): bstack1lll1l1_opy_ (u"ࠧࡄࡄࡗࡣ࡚ࡶ࡬ࡰࡣࡧࠫᓏ")
        }.get(bstack1111l11l1_opy_)
        if bstack1lllll1ll11_opy_ == bstack1lll1l1_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡤࡸࡨ࡮ࠧᓐ"):
            cls.bstack1lllllll1ll_opy_()
            cls.bstack11111lll1l_opy_.add(bstack1l11llll11_opy_)
        elif bstack1lllll1ll11_opy_ == bstack1lll1l1_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧᓑ"):
            cls.bstack1llllll11ll_opy_([bstack1l11llll11_opy_], bstack1lllll1ll11_opy_)
    @classmethod
    @bstack1l11l11lll_opy_(class_method=True)
    def bstack1llllll11ll_opy_(cls, bstack1l11llll11_opy_, bstack1lllll1ll11_opy_=bstack1lll1l1_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡦࡺࡣࡩࠩᓒ")):
        config = {
            bstack1lll1l1_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬᓓ"): cls.default_headers()
        }
        response = bstack1ll1ll1lll_opy_(bstack1lll1l1_opy_ (u"ࠬࡖࡏࡔࡖࠪᓔ"), cls.request_url(bstack1lllll1ll11_opy_), bstack1l11llll11_opy_, config)
        bstack11ll1l1lll_opy_ = response.json()
    @classmethod
    @bstack1l11l11lll_opy_(class_method=True)
    def bstack1l11l11l11_opy_(cls, bstack1l11lll111_opy_):
        bstack1lllll1l11l_opy_ = []
        for log in bstack1l11lll111_opy_:
            bstack1llllll1l1l_opy_ = {
                bstack1lll1l1_opy_ (u"࠭࡫ࡪࡰࡧࠫᓕ"): bstack1lll1l1_opy_ (u"ࠧࡕࡇࡖࡘࡤࡒࡏࡈࠩᓖ"),
                bstack1lll1l1_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᓗ"): log[bstack1lll1l1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᓘ")],
                bstack1lll1l1_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ᓙ"): log[bstack1lll1l1_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧᓚ")],
                bstack1lll1l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡢࡶࡪࡹࡰࡰࡰࡶࡩࠬᓛ"): {},
                bstack1lll1l1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᓜ"): log[bstack1lll1l1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᓝ")],
            }
            if bstack1lll1l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᓞ") in log:
                bstack1llllll1l1l_opy_[bstack1lll1l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᓟ")] = log[bstack1lll1l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᓠ")]
            elif bstack1lll1l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᓡ") in log:
                bstack1llllll1l1l_opy_[bstack1lll1l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᓢ")] = log[bstack1lll1l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᓣ")]
            bstack1lllll1l11l_opy_.append(bstack1llllll1l1l_opy_)
        cls.bstack1l11l1111l_opy_({
            bstack1lll1l1_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫᓤ"): bstack1lll1l1_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬᓥ"),
            bstack1lll1l1_opy_ (u"ࠩ࡯ࡳ࡬ࡹࠧᓦ"): bstack1lllll1l11l_opy_
        })
    @classmethod
    @bstack1l11l11lll_opy_(class_method=True)
    def bstack1lllll1ll1l_opy_(cls, steps):
        bstack1llllll1111_opy_ = []
        for step in steps:
            bstack1lllll1lll1_opy_ = {
                bstack1lll1l1_opy_ (u"ࠪ࡯࡮ࡴࡤࠨᓧ"): bstack1lll1l1_opy_ (u"࡙ࠫࡋࡓࡕࡡࡖࡘࡊࡖࠧᓨ"),
                bstack1lll1l1_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫᓩ"): step[bstack1lll1l1_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᓪ")],
                bstack1lll1l1_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪᓫ"): step[bstack1lll1l1_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫᓬ")],
                bstack1lll1l1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᓭ"): step[bstack1lll1l1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᓮ")],
                bstack1lll1l1_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭ᓯ"): step[bstack1lll1l1_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧᓰ")]
            }
            if bstack1lll1l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᓱ") in step:
                bstack1lllll1lll1_opy_[bstack1lll1l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᓲ")] = step[bstack1lll1l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᓳ")]
            elif bstack1lll1l1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᓴ") in step:
                bstack1lllll1lll1_opy_[bstack1lll1l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᓵ")] = step[bstack1lll1l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᓶ")]
            bstack1llllll1111_opy_.append(bstack1lllll1lll1_opy_)
        cls.bstack1l11l1111l_opy_({
            bstack1lll1l1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩᓷ"): bstack1lll1l1_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪᓸ"),
            bstack1lll1l1_opy_ (u"ࠧ࡭ࡱࡪࡷࠬᓹ"): bstack1llllll1111_opy_
        })
    @classmethod
    @bstack1l11l11lll_opy_(class_method=True)
    def bstack1l1llll11l_opy_(cls, screenshot):
        cls.bstack1l11l1111l_opy_({
            bstack1lll1l1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬᓺ"): bstack1lll1l1_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭ᓻ"),
            bstack1lll1l1_opy_ (u"ࠪࡰࡴ࡭ࡳࠨᓼ"): [{
                bstack1lll1l1_opy_ (u"ࠫࡰ࡯࡮ࡥࠩᓽ"): bstack1lll1l1_opy_ (u"࡚ࠬࡅࡔࡖࡢࡗࡈࡘࡅࡆࡐࡖࡌࡔ࡚ࠧᓾ"),
                bstack1lll1l1_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩᓿ"): datetime.datetime.utcnow().isoformat() + bstack1lll1l1_opy_ (u"࡛ࠧࠩᔀ"),
                bstack1lll1l1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᔁ"): screenshot[bstack1lll1l1_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨᔂ")],
                bstack1lll1l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᔃ"): screenshot[bstack1lll1l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᔄ")]
            }]
        }, bstack1lllll1ll11_opy_=bstack1lll1l1_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪᔅ"))
    @classmethod
    @bstack1l11l11lll_opy_(class_method=True)
    def bstack1l1l1l111l_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1l11l1111l_opy_({
            bstack1lll1l1_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪᔆ"): bstack1lll1l1_opy_ (u"ࠧࡄࡄࡗࡗࡪࡹࡳࡪࡱࡱࡇࡷ࡫ࡡࡵࡧࡧࠫᔇ"),
            bstack1lll1l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪᔈ"): {
                bstack1lll1l1_opy_ (u"ࠤࡸࡹ࡮ࡪࠢᔉ"): cls.current_test_uuid(),
                bstack1lll1l1_opy_ (u"ࠥ࡭ࡳࡺࡥࡨࡴࡤࡸ࡮ࡵ࡮ࡴࠤᔊ"): cls.bstack1l111l11l1_opy_(driver)
            }
        })
    @classmethod
    def on(cls):
        if os.environ.get(bstack1lll1l1_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡌ࡚ࡘࠬᔋ"), None) is None or os.environ[bstack1lll1l1_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡍ࡛࡙࠭ᔌ")] == bstack1lll1l1_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦᔍ"):
            return False
        return True
    @classmethod
    def bstack1llllll1l11_opy_(cls):
        return bstack1l11lllll_opy_(cls.bs_config.get(bstack1lll1l1_opy_ (u"ࠧࡵࡧࡶࡸࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫᔎ"), False))
    @staticmethod
    def request_url(url):
        return bstack1lll1l1_opy_ (u"ࠨࡽࢀ࠳ࢀࢃࠧᔏ").format(bstack1lllll1l1ll_opy_, url)
    @staticmethod
    def default_headers():
        headers = {
            bstack1lll1l1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨᔐ"): bstack1lll1l1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ᔑ"),
            bstack1lll1l1_opy_ (u"ࠫ࡝࠳ࡂࡔࡖࡄࡇࡐ࠳ࡔࡆࡕࡗࡓࡕ࡙ࠧᔒ"): bstack1lll1l1_opy_ (u"ࠬࡺࡲࡶࡧࠪᔓ")
        }
        if os.environ.get(bstack1lll1l1_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡎ࡜࡚ࠧᔔ"), None):
            headers[bstack1lll1l1_opy_ (u"ࠧࡂࡷࡷ࡬ࡴࡸࡩࡻࡣࡷ࡭ࡴࡴࠧᔕ")] = bstack1lll1l1_opy_ (u"ࠨࡄࡨࡥࡷ࡫ࡲࠡࡽࢀࠫᔖ").format(os.environ[bstack1lll1l1_opy_ (u"ࠤࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡊࡘࡖࠥᔗ")])
        return headers
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack1lll1l1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧᔘ"), None)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack1lll1l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᔙ"), None)
    @staticmethod
    def bstack1l111lllll_opy_():
        if getattr(threading.current_thread(), bstack1lll1l1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩᔚ"), None):
            return {
                bstack1lll1l1_opy_ (u"࠭ࡴࡺࡲࡨࠫᔛ"): bstack1lll1l1_opy_ (u"ࠧࡵࡧࡶࡸࠬᔜ"),
                bstack1lll1l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᔝ"): getattr(threading.current_thread(), bstack1lll1l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭ᔞ"), None)
            }
        if getattr(threading.current_thread(), bstack1lll1l1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧᔟ"), None):
            return {
                bstack1lll1l1_opy_ (u"ࠫࡹࡿࡰࡦࠩᔠ"): bstack1lll1l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪᔡ"),
                bstack1lll1l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᔢ"): getattr(threading.current_thread(), bstack1lll1l1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᔣ"), None)
            }
        return None
    @staticmethod
    def bstack1l111l11l1_opy_(driver):
        return {
            bstack11l1ll11l1_opy_(): bstack11l1ll111l_opy_(driver)
        }
    @staticmethod
    def bstack1lllll1l111_opy_(exception_info, report):
        return [{bstack1lll1l1_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫᔤ"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack11lll1ll1l_opy_(typename):
        if bstack1lll1l1_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧᔥ") in typename:
            return bstack1lll1l1_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵࠦᔦ")
        return bstack1lll1l1_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧᔧ")
    @staticmethod
    def bstack1llllll1ll1_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l1ll11l_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1l11ll1lll_opy_(test, hook_name=None):
        bstack1lllllll1l1_opy_ = test.parent
        if hook_name in [bstack1lll1l1_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡨࡲࡡࡴࡵࠪᔨ"), bstack1lll1l1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡥ࡯ࡥࡸࡹࠧᔩ"), bstack1lll1l1_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭ᔪ"), bstack1lll1l1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠪᔫ")]:
            bstack1lllllll1l1_opy_ = test
        scope = []
        while bstack1lllllll1l1_opy_ is not None:
            scope.append(bstack1lllllll1l1_opy_.name)
            bstack1lllllll1l1_opy_ = bstack1lllllll1l1_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack1lllll1l1l1_opy_(hook_type):
        if hook_type == bstack1lll1l1_opy_ (u"ࠤࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠢᔬ"):
            return bstack1lll1l1_opy_ (u"ࠥࡗࡪࡺࡵࡱࠢ࡫ࡳࡴࡱࠢᔭ")
        elif hook_type == bstack1lll1l1_opy_ (u"ࠦࡆࡌࡔࡆࡔࡢࡉࡆࡉࡈࠣᔮ"):
            return bstack1lll1l1_opy_ (u"࡚ࠧࡥࡢࡴࡧࡳࡼࡴࠠࡩࡱࡲ࡯ࠧᔯ")
    @staticmethod
    def bstack1lllllll111_opy_(bstack11111ll1_opy_):
        try:
            if not bstack1l1ll11l_opy_.on():
                return bstack11111ll1_opy_
            if os.environ.get(bstack1lll1l1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࠦᔰ"), None) == bstack1lll1l1_opy_ (u"ࠢࡵࡴࡸࡩࠧᔱ"):
                tests = os.environ.get(bstack1lll1l1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓࡥࡔࡆࡕࡗࡗࠧᔲ"), None)
                if tests is None or tests == bstack1lll1l1_opy_ (u"ࠤࡱࡹࡱࡲࠢᔳ"):
                    return bstack11111ll1_opy_
                bstack11111ll1_opy_ = tests.split(bstack1lll1l1_opy_ (u"ࠪ࠰ࠬᔴ"))
                return bstack11111ll1_opy_
        except Exception as exc:
            print(bstack1lll1l1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡶࡪࡸࡵ࡯ࠢ࡫ࡥࡳࡪ࡬ࡦࡴ࠽ࠤࠧᔵ"), str(exc))
        return bstack11111ll1_opy_
    @classmethod
    def bstack1l111lll11_opy_(cls, event: str, bstack1l11llll11_opy_: bstack1l111l1ll1_opy_):
        bstack1l11l1l1ll_opy_ = {
            bstack1lll1l1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩᔶ"): event,
            bstack1l11llll11_opy_.bstack1l11l1l111_opy_(): bstack1l11llll11_opy_.bstack1l11l1ll1l_opy_(event)
        }
        bstack1l1ll11l_opy_.bstack1l11l1111l_opy_(bstack1l11l1l1ll_opy_)