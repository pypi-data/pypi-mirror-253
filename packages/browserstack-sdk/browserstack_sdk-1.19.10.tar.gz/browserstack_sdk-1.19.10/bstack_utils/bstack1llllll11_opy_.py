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
import re
from bstack_utils.bstack1ll111l1l_opy_ import bstack1111l1ll1l_opy_
def bstack1111l1llll_opy_(fixture_name):
    if fixture_name.startswith(bstack1lll1l1_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡹࡥࡵࡷࡳࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᎼ")):
        return bstack1lll1l1_opy_ (u"࠭ࡳࡦࡶࡸࡴ࠲࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧᎽ")
    elif fixture_name.startswith(bstack1lll1l1_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᎾ")):
        return bstack1lll1l1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭࡮ࡱࡧࡹࡱ࡫ࠧᎿ")
    elif fixture_name.startswith(bstack1lll1l1_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᏀ")):
        return bstack1lll1l1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲ࠲࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧᏁ")
    elif fixture_name.startswith(bstack1lll1l1_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᏂ")):
        return bstack1lll1l1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࠭࡮ࡱࡧࡹࡱ࡫ࠧᏃ")
def bstack1111l1l1ll_opy_(fixture_name):
    return bool(re.match(bstack1lll1l1_opy_ (u"࠭࡞ࡠࡺࡸࡲ࡮ࡺ࡟ࠩࡵࡨࡸࡺࡶࡼࡵࡧࡤࡶࡩࡵࡷ࡯ࠫࡢࠬ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࢂ࡭ࡰࡦࡸࡰࡪ࠯࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠ࠰࠭ࠫᏄ"), fixture_name))
def bstack1111l11l1l_opy_(fixture_name):
    return bool(re.match(bstack1lll1l1_opy_ (u"ࠧ࡟ࡡࡻࡹࡳ࡯ࡴࡠࠪࡶࡩࡹࡻࡰࡽࡶࡨࡥࡷࡪ࡯ࡸࡰࠬࡣࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࠴ࠪࠨᏅ"), fixture_name))
def bstack1111l11lll_opy_(fixture_name):
    return bool(re.match(bstack1lll1l1_opy_ (u"ࠨࡠࡢࡼࡺࡴࡩࡵࡡࠫࡷࡪࡺࡵࡱࡾࡷࡩࡦࡸࡤࡰࡹࡱ࠭ࡤࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࠴ࠪࠨᏆ"), fixture_name))
def bstack1111l11ll1_opy_(fixture_name):
    if fixture_name.startswith(bstack1lll1l1_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᏇ")):
        return bstack1lll1l1_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡩࡹࡳࡩࡴࡪࡱࡱࠫᏈ"), bstack1lll1l1_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠩᏉ")
    elif fixture_name.startswith(bstack1lll1l1_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᏊ")):
        return bstack1lll1l1_opy_ (u"࠭ࡳࡦࡶࡸࡴ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᏋ"), bstack1lll1l1_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡂࡎࡏࠫᏌ")
    elif fixture_name.startswith(bstack1lll1l1_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭Ꮝ")):
        return bstack1lll1l1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱ࠱࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭Ꮞ"), bstack1lll1l1_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡈࡅࡈࡎࠧᏏ")
    elif fixture_name.startswith(bstack1lll1l1_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᏐ")):
        return bstack1lll1l1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࠭࡮ࡱࡧࡹࡱ࡫ࠧᏑ"), bstack1lll1l1_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡇࡌࡍࠩᏒ")
    return None, None
def bstack1111l1l1l1_opy_(hook_name):
    if hook_name in [bstack1lll1l1_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭Ꮣ"), bstack1lll1l1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࠪᏔ")]:
        return hook_name.capitalize()
    return hook_name
def bstack1111l11l11_opy_(hook_name):
    if hook_name in [bstack1lll1l1_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡨࡸࡲࡨࡺࡩࡰࡰࠪᏕ"), bstack1lll1l1_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡩࡹ࡮࡯ࡥࠩᏖ")]:
        return bstack1lll1l1_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠩᏗ")
    elif hook_name in [bstack1lll1l1_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࠫᏘ"), bstack1lll1l1_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡩ࡬ࡢࡵࡶࠫᏙ")]:
        return bstack1lll1l1_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡂࡎࡏࠫᏚ")
    elif hook_name in [bstack1lll1l1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᏛ"), bstack1lll1l1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠫᏜ")]:
        return bstack1lll1l1_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡈࡅࡈࡎࠧᏝ")
    elif hook_name in [bstack1lll1l1_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡰࡦࡸࡰࡪ࠭Ꮮ"), bstack1lll1l1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡤ࡮ࡤࡷࡸ࠭Ꮯ")]:
        return bstack1lll1l1_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡇࡌࡍࠩᏠ")
    return hook_name
def bstack1111l1l111_opy_(node, scenario):
    if hasattr(node, bstack1lll1l1_opy_ (u"ࠧࡤࡣ࡯ࡰࡸࡶࡥࡤࠩᏡ")):
        parts = node.nodeid.rsplit(bstack1lll1l1_opy_ (u"ࠣ࡝ࠥᏢ"))
        params = parts[-1]
        return bstack1lll1l1_opy_ (u"ࠤࡾࢁࠥࡡࡻࡾࠤᏣ").format(scenario.name, params)
    return scenario.name
def bstack1111l111ll_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack1lll1l1_opy_ (u"ࠪࡧࡦࡲ࡬ࡴࡲࡨࡧࠬᏤ")):
            examples = list(node.callspec.params[bstack1lll1l1_opy_ (u"ࠫࡤࡶࡹࡵࡧࡶࡸࡤࡨࡤࡥࡡࡨࡼࡦࡳࡰ࡭ࡧࠪᏥ")].values())
        return examples
    except:
        return []
def bstack1111ll1111_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack1111l1lll1_opy_(report):
    try:
        status = bstack1lll1l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᏦ")
        if report.passed or (report.failed and hasattr(report, bstack1lll1l1_opy_ (u"ࠨࡷࡢࡵࡻࡪࡦ࡯࡬ࠣᏧ"))):
            status = bstack1lll1l1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᏨ")
        elif report.skipped:
            status = bstack1lll1l1_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩᏩ")
        bstack1111l1ll1l_opy_(status)
    except:
        pass
def bstack1l1l111l11_opy_(status):
    try:
        bstack1111l1l11l_opy_ = bstack1lll1l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᏪ")
        if status == bstack1lll1l1_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᏫ"):
            bstack1111l1l11l_opy_ = bstack1lll1l1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᏬ")
        elif status == bstack1lll1l1_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭Ꮽ"):
            bstack1111l1l11l_opy_ = bstack1lll1l1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧᏮ")
        bstack1111l1ll1l_opy_(bstack1111l1l11l_opy_)
    except:
        pass
def bstack1111l1ll11_opy_(item=None, report=None, summary=None, extra=None):
    return