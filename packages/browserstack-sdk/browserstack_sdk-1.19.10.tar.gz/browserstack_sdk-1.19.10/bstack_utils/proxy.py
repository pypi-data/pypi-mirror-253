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
from urllib.parse import urlparse
from bstack_utils.messages import bstack111lllll1l_opy_
def bstack1111ll111l_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack1111ll11l1_opy_(bstack1111ll11ll_opy_, bstack1111ll1lll_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack1111ll11ll_opy_):
        with open(bstack1111ll11ll_opy_) as f:
            pac = PACFile(f.read())
    elif bstack1111ll111l_opy_(bstack1111ll11ll_opy_):
        pac = get_pac(url=bstack1111ll11ll_opy_)
    else:
        raise Exception(bstack1lll1l1_opy_ (u"ࠪࡔࡦࡩࠠࡧ࡫࡯ࡩࠥࡪ࡯ࡦࡵࠣࡲࡴࡺࠠࡦࡺ࡬ࡷࡹࡀࠠࡼࡿࠪ᎗").format(bstack1111ll11ll_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack1lll1l1_opy_ (u"ࠦ࠽࠴࠸࠯࠺࠱࠼ࠧ᎘"), 80))
        bstack1111ll1l1l_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack1111ll1l1l_opy_ = bstack1lll1l1_opy_ (u"ࠬ࠶࠮࠱࠰࠳࠲࠵࠭᎙")
    proxy_url = session.get_pac().find_proxy_for_url(bstack1111ll1lll_opy_, bstack1111ll1l1l_opy_)
    return proxy_url
def bstack1lll1l11l1_opy_(config):
    return bstack1lll1l1_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩ᎚") in config or bstack1lll1l1_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫ᎛") in config
def bstack11lll1l11_opy_(config):
    if not bstack1lll1l11l1_opy_(config):
        return
    if config.get(bstack1lll1l1_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫ᎜")):
        return config.get(bstack1lll1l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬ᎝"))
    if config.get(bstack1lll1l1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧ᎞")):
        return config.get(bstack1lll1l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨ᎟"))
def bstack1ll1lll1l1_opy_(config, bstack1111ll1lll_opy_):
    proxy = bstack11lll1l11_opy_(config)
    proxies = {}
    if config.get(bstack1lll1l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨᎠ")) or config.get(bstack1lll1l1_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪᎡ")):
        if proxy.endswith(bstack1lll1l1_opy_ (u"ࠧ࠯ࡲࡤࡧࠬᎢ")):
            proxies = bstack1l1111l11_opy_(proxy, bstack1111ll1lll_opy_)
        else:
            proxies = {
                bstack1lll1l1_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧᎣ"): proxy
            }
    return proxies
def bstack1l1111l11_opy_(bstack1111ll11ll_opy_, bstack1111ll1lll_opy_):
    proxies = {}
    global bstack1111ll1ll1_opy_
    if bstack1lll1l1_opy_ (u"ࠩࡓࡅࡈࡥࡐࡓࡑ࡛࡝ࠬᎤ") in globals():
        return bstack1111ll1ll1_opy_
    try:
        proxy = bstack1111ll11l1_opy_(bstack1111ll11ll_opy_, bstack1111ll1lll_opy_)
        if bstack1lll1l1_opy_ (u"ࠥࡈࡎࡘࡅࡄࡖࠥᎥ") in proxy:
            proxies = {}
        elif bstack1lll1l1_opy_ (u"ࠦࡍ࡚ࡔࡑࠤᎦ") in proxy or bstack1lll1l1_opy_ (u"ࠧࡎࡔࡕࡒࡖࠦᎧ") in proxy or bstack1lll1l1_opy_ (u"ࠨࡓࡐࡅࡎࡗࠧᎨ") in proxy:
            bstack1111ll1l11_opy_ = proxy.split(bstack1lll1l1_opy_ (u"ࠢࠡࠤᎩ"))
            if bstack1lll1l1_opy_ (u"ࠣ࠼࠲࠳ࠧᎪ") in bstack1lll1l1_opy_ (u"ࠤࠥᎫ").join(bstack1111ll1l11_opy_[1:]):
                proxies = {
                    bstack1lll1l1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩᎬ"): bstack1lll1l1_opy_ (u"ࠦࠧᎭ").join(bstack1111ll1l11_opy_[1:])
                }
            else:
                proxies = {
                    bstack1lll1l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫᎮ"): str(bstack1111ll1l11_opy_[0]).lower() + bstack1lll1l1_opy_ (u"ࠨ࠺࠰࠱ࠥᎯ") + bstack1lll1l1_opy_ (u"ࠢࠣᎰ").join(bstack1111ll1l11_opy_[1:])
                }
        elif bstack1lll1l1_opy_ (u"ࠣࡒࡕࡓ࡝࡟ࠢᎱ") in proxy:
            bstack1111ll1l11_opy_ = proxy.split(bstack1lll1l1_opy_ (u"ࠤࠣࠦᎲ"))
            if bstack1lll1l1_opy_ (u"ࠥ࠾࠴࠵ࠢᎳ") in bstack1lll1l1_opy_ (u"ࠦࠧᎴ").join(bstack1111ll1l11_opy_[1:]):
                proxies = {
                    bstack1lll1l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫᎵ"): bstack1lll1l1_opy_ (u"ࠨࠢᎶ").join(bstack1111ll1l11_opy_[1:])
                }
            else:
                proxies = {
                    bstack1lll1l1_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭Ꮇ"): bstack1lll1l1_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤᎸ") + bstack1lll1l1_opy_ (u"ࠤࠥᎹ").join(bstack1111ll1l11_opy_[1:])
                }
        else:
            proxies = {
                bstack1lll1l1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩᎺ"): proxy
            }
    except Exception as e:
        print(bstack1lll1l1_opy_ (u"ࠦࡸࡵ࡭ࡦࠢࡨࡶࡷࡵࡲࠣᎻ"), bstack111lllll1l_opy_.format(bstack1111ll11ll_opy_, str(e)))
    bstack1111ll1ll1_opy_ = proxies
    return proxies