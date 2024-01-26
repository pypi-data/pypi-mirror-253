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
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.helper import bstack11l11l1l1l_opy_, bstack11l11ll1_opy_, bstack1ll11111l_opy_, bstack1ll1l111l_opy_, \
    bstack11l1lll11l_opy_
def bstack1ll11l1lll_opy_(bstack11111l11l1_opy_):
    for driver in bstack11111l11l1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1l1l11ll_opy_(driver, status, reason=bstack1lll1l1_opy_ (u"ࠩࠪᏱ")):
    bstack11l1l11l_opy_ = Config.bstack1lllll11l1_opy_()
    if bstack11l1l11l_opy_.bstack11llll111l_opy_():
        return
    bstack1ll111111_opy_ = bstack1lll1ll1l_opy_(bstack1lll1l1_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭Ᏺ"), bstack1lll1l1_opy_ (u"ࠫࠬᏳ"), status, reason, bstack1lll1l1_opy_ (u"ࠬ࠭Ᏼ"), bstack1lll1l1_opy_ (u"࠭ࠧᏵ"))
    driver.execute_script(bstack1ll111111_opy_)
def bstack1ll1111111_opy_(page, status, reason=bstack1lll1l1_opy_ (u"ࠧࠨ᏶")):
    try:
        if page is None:
            return
        bstack11l1l11l_opy_ = Config.bstack1lllll11l1_opy_()
        if bstack11l1l11l_opy_.bstack11llll111l_opy_():
            return
        bstack1ll111111_opy_ = bstack1lll1ll1l_opy_(bstack1lll1l1_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫ᏷"), bstack1lll1l1_opy_ (u"ࠩࠪᏸ"), status, reason, bstack1lll1l1_opy_ (u"ࠪࠫᏹ"), bstack1lll1l1_opy_ (u"ࠫࠬᏺ"))
        page.evaluate(bstack1lll1l1_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨᏻ"), bstack1ll111111_opy_)
    except Exception as e:
        print(bstack1lll1l1_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡴࡶࡤࡸࡺࡹࠠࡧࡱࡵࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡽࢀࠦᏼ"), e)
def bstack1lll1ll1l_opy_(type, name, status, reason, bstack1ll1l11l1_opy_, bstack11ll1ll1_opy_):
    bstack1l111ll1l_opy_ = {
        bstack1lll1l1_opy_ (u"ࠧࡢࡥࡷ࡭ࡴࡴࠧᏽ"): type,
        bstack1lll1l1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ᏾"): {}
    }
    if type == bstack1lll1l1_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨࠫ᏿"):
        bstack1l111ll1l_opy_[bstack1lll1l1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭᐀")][bstack1lll1l1_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪᐁ")] = bstack1ll1l11l1_opy_
        bstack1l111ll1l_opy_[bstack1lll1l1_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᐂ")][bstack1lll1l1_opy_ (u"࠭ࡤࡢࡶࡤࠫᐃ")] = json.dumps(str(bstack11ll1ll1_opy_))
    if type == bstack1lll1l1_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨᐄ"):
        bstack1l111ll1l_opy_[bstack1lll1l1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᐅ")][bstack1lll1l1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᐆ")] = name
    if type == bstack1lll1l1_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭ᐇ"):
        bstack1l111ll1l_opy_[bstack1lll1l1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᐈ")][bstack1lll1l1_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬᐉ")] = status
        if status == bstack1lll1l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᐊ") and str(reason) != bstack1lll1l1_opy_ (u"ࠢࠣᐋ"):
            bstack1l111ll1l_opy_[bstack1lll1l1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᐌ")][bstack1lll1l1_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩᐍ")] = json.dumps(str(reason))
    bstack1ll1l11lll_opy_ = bstack1lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨᐎ").format(json.dumps(bstack1l111ll1l_opy_))
    return bstack1ll1l11lll_opy_
def bstack1111l1l11_opy_(url, config, logger, bstack1llll11ll1_opy_=False):
    hostname = bstack11l11ll1_opy_(url)
    is_private = bstack1ll1l111l_opy_(hostname)
    try:
        if is_private or bstack1llll11ll1_opy_:
            file_path = bstack11l11l1l1l_opy_(bstack1lll1l1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᐏ"), bstack1lll1l1_opy_ (u"ࠬ࠴ࡢࡴࡶࡤࡧࡰ࠳ࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫᐐ"), logger)
            if os.environ.get(bstack1lll1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡓࡕࡔࡠࡕࡈࡘࡤࡋࡒࡓࡑࡕࠫᐑ")) and eval(
                    os.environ.get(bstack1lll1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡔࡏࡕࡡࡖࡉ࡙ࡥࡅࡓࡔࡒࡖࠬᐒ"))):
                return
            if (bstack1lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬᐓ") in config and not config[bstack1lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ᐔ")]):
                os.environ[bstack1lll1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡐࡒࡘࡤ࡙ࡅࡕࡡࡈࡖࡗࡕࡒࠨᐕ")] = str(True)
                bstack111111llll_opy_ = {bstack1lll1l1_opy_ (u"ࠫ࡭ࡵࡳࡵࡰࡤࡱࡪ࠭ᐖ"): hostname}
                bstack11l1lll11l_opy_(bstack1lll1l1_opy_ (u"ࠬ࠴ࡢࡴࡶࡤࡧࡰ࠳ࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫᐗ"), bstack1lll1l1_opy_ (u"࠭࡮ࡶࡦࡪࡩࡤࡲ࡯ࡤࡣ࡯ࠫᐘ"), bstack111111llll_opy_, logger)
    except Exception as e:
        pass
def bstack111ll11l_opy_(caps, bstack11111l111l_opy_):
    if bstack1lll1l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᐙ") in caps:
        caps[bstack1lll1l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᐚ")][bstack1lll1l1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࠨᐛ")] = True
        if bstack11111l111l_opy_:
            caps[bstack1lll1l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᐜ")][bstack1lll1l1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ᐝ")] = bstack11111l111l_opy_
    else:
        caps[bstack1lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡱࡵࡣࡢ࡮ࠪᐞ")] = True
        if bstack11111l111l_opy_:
            caps[bstack1lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧᐟ")] = bstack11111l111l_opy_
def bstack1111l1ll1l_opy_(bstack1l11l11ll1_opy_):
    bstack11111l1111_opy_ = bstack1ll11111l_opy_(threading.current_thread(), bstack1lll1l1_opy_ (u"ࠧࡵࡧࡶࡸࡘࡺࡡࡵࡷࡶࠫᐠ"), bstack1lll1l1_opy_ (u"ࠨࠩᐡ"))
    if bstack11111l1111_opy_ == bstack1lll1l1_opy_ (u"ࠩࠪᐢ") or bstack11111l1111_opy_ == bstack1lll1l1_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫᐣ"):
        threading.current_thread().testStatus = bstack1l11l11ll1_opy_
    else:
        if bstack1l11l11ll1_opy_ == bstack1lll1l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᐤ"):
            threading.current_thread().testStatus = bstack1l11l11ll1_opy_