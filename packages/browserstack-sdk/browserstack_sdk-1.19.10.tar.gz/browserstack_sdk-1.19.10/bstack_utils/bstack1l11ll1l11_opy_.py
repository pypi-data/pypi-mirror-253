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
from uuid import uuid4
from bstack_utils.helper import bstack11llll1l1_opy_, bstack11l1ll1ll1_opy_
from bstack_utils.bstack1llllll11_opy_ import bstack1111l111ll_opy_
class bstack1l111l1ll1_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, bstack1l1111ll1l_opy_=None, framework=None, tags=[], scope=[], bstack111111ll1l_opy_=None, bstack111111ll11_opy_=True, bstack111111lll1_opy_=None, bstack1111l11l1_opy_=None, result=None, duration=None, bstack1l111l1l1l_opy_=None, meta={}):
        self.bstack1l111l1l1l_opy_ = bstack1l111l1l1l_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack111111ll11_opy_:
            self.uuid = uuid4().__str__()
        self.bstack1l1111ll1l_opy_ = bstack1l1111ll1l_opy_
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack111111ll1l_opy_ = bstack111111ll1l_opy_
        self.bstack111111lll1_opy_ = bstack111111lll1_opy_
        self.bstack1111l11l1_opy_ = bstack1111l11l1_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
    def bstack1l111111ll_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack111111l1ll_opy_(self):
        bstack111111l111_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack1lll1l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨᐥ"): bstack111111l111_opy_,
            bstack1lll1l1_opy_ (u"࠭࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠨᐦ"): bstack111111l111_opy_,
            bstack1lll1l1_opy_ (u"ࠧࡷࡥࡢࡪ࡮ࡲࡥࡱࡣࡷ࡬ࠬᐧ"): bstack111111l111_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack1lll1l1_opy_ (u"ࠣࡗࡱࡩࡽࡶࡥࡤࡶࡨࡨࠥࡧࡲࡨࡷࡰࡩࡳࡺ࠺ࠡࠤᐨ") + key)
            setattr(self, key, val)
    def bstack1llllllll11_opy_(self):
        return {
            bstack1lll1l1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᐩ"): self.name,
            bstack1lll1l1_opy_ (u"ࠪࡦࡴࡪࡹࠨᐪ"): {
                bstack1lll1l1_opy_ (u"ࠫࡱࡧ࡮ࡨࠩᐫ"): bstack1lll1l1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬᐬ"),
                bstack1lll1l1_opy_ (u"࠭ࡣࡰࡦࡨࠫᐭ"): self.code
            },
            bstack1lll1l1_opy_ (u"ࠧࡴࡥࡲࡴࡪࡹࠧᐮ"): self.scope,
            bstack1lll1l1_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭ᐯ"): self.tags,
            bstack1lll1l1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬᐰ"): self.framework,
            bstack1lll1l1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᐱ"): self.bstack1l1111ll1l_opy_
        }
    def bstack1111111l11_opy_(self):
        return {
         bstack1lll1l1_opy_ (u"ࠫࡲ࡫ࡴࡢࠩᐲ"): self.meta
        }
    def bstack1lllllllll1_opy_(self):
        return {
            bstack1lll1l1_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡗ࡫ࡲࡶࡰࡓࡥࡷࡧ࡭ࠨᐳ"): {
                bstack1lll1l1_opy_ (u"࠭ࡲࡦࡴࡸࡲࡤࡴࡡ࡮ࡧࠪᐴ"): self.bstack111111ll1l_opy_
            }
        }
    def bstack11111111ll_opy_(self, bstack11111111l1_opy_, details):
        step = next(filter(lambda st: st[bstack1lll1l1_opy_ (u"ࠧࡪࡦࠪᐵ")] == bstack11111111l1_opy_, self.meta[bstack1lll1l1_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧᐶ")]), None)
        step.update(details)
    def bstack1111111lll_opy_(self, bstack11111111l1_opy_):
        step = next(filter(lambda st: st[bstack1lll1l1_opy_ (u"ࠩ࡬ࡨࠬᐷ")] == bstack11111111l1_opy_, self.meta[bstack1lll1l1_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩᐸ")]), None)
        step.update({
            bstack1lll1l1_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᐹ"): bstack11llll1l1_opy_()
        })
    def bstack1l111ll11l_opy_(self, bstack11111111l1_opy_, result, duration=None):
        bstack111111lll1_opy_ = bstack11llll1l1_opy_()
        if bstack11111111l1_opy_ is not None and self.meta.get(bstack1lll1l1_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫᐺ")):
            step = next(filter(lambda st: st[bstack1lll1l1_opy_ (u"࠭ࡩࡥࠩᐻ")] == bstack11111111l1_opy_, self.meta[bstack1lll1l1_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ᐼ")]), None)
            step.update({
                bstack1lll1l1_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᐽ"): bstack111111lll1_opy_,
                bstack1lll1l1_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࠫᐾ"): duration if duration else bstack11l1ll1ll1_opy_(step[bstack1lll1l1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᐿ")], bstack111111lll1_opy_),
                bstack1lll1l1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᑀ"): result.result,
                bstack1lll1l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ᑁ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack1111111ll1_opy_):
        if self.meta.get(bstack1lll1l1_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬᑂ")):
            self.meta[bstack1lll1l1_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ᑃ")].append(bstack1111111ll1_opy_)
        else:
            self.meta[bstack1lll1l1_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧᑄ")] = [ bstack1111111ll1_opy_ ]
    def bstack111111l1l1_opy_(self):
        return {
            bstack1lll1l1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᑅ"): self.bstack1l111111ll_opy_(),
            **self.bstack1llllllll11_opy_(),
            **self.bstack111111l1ll_opy_(),
            **self.bstack1111111l11_opy_()
        }
    def bstack1111111111_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack1lll1l1_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᑆ"): self.bstack111111lll1_opy_,
            bstack1lll1l1_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡡࡰࡷࠬᑇ"): self.duration,
            bstack1lll1l1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᑈ"): self.result.result
        }
        if data[bstack1lll1l1_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᑉ")] == bstack1lll1l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᑊ"):
            data[bstack1lll1l1_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧᑋ")] = self.result.bstack11lll1ll1l_opy_()
            data[bstack1lll1l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪᑌ")] = [{bstack1lll1l1_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭ᑍ"): self.result.bstack11l1l11ll1_opy_()}]
        return data
    def bstack1111111l1l_opy_(self):
        return {
            bstack1lll1l1_opy_ (u"ࠫࡺࡻࡩࡥࠩᑎ"): self.bstack1l111111ll_opy_(),
            **self.bstack1llllllll11_opy_(),
            **self.bstack111111l1ll_opy_(),
            **self.bstack1111111111_opy_(),
            **self.bstack1111111l11_opy_()
        }
    def bstack1l11l1ll1l_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack1lll1l1_opy_ (u"࡙ࠬࡴࡢࡴࡷࡩࡩ࠭ᑏ") in event:
            return self.bstack111111l1l1_opy_()
        elif bstack1lll1l1_opy_ (u"࠭ࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨᑐ") in event:
            return self.bstack1111111l1l_opy_()
    def bstack1l11l1l111_opy_(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack111111lll1_opy_ = time if time else bstack11llll1l1_opy_()
        self.duration = duration if duration else bstack11l1ll1ll1_opy_(self.bstack1l1111ll1l_opy_, self.bstack111111lll1_opy_)
        if result:
            self.result = result
class bstack1l111l1l11_opy_(bstack1l111l1ll1_opy_):
    def __init__(self, hooks=[], bstack11lllllll1_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack11lllllll1_opy_ = bstack11lllllll1_opy_
        super().__init__(*args, **kwargs, bstack1111l11l1_opy_=bstack1lll1l1_opy_ (u"ࠧࡵࡧࡶࡸࠬᑑ"))
    @classmethod
    def bstack111111111l_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1lll1l1_opy_ (u"ࠨ࡫ࡧࠫᑒ"): id(step),
                bstack1lll1l1_opy_ (u"ࠩࡷࡩࡽࡺࠧᑓ"): step.name,
                bstack1lll1l1_opy_ (u"ࠪ࡯ࡪࡿࡷࡰࡴࡧࠫᑔ"): step.keyword,
            })
        return bstack1l111l1l11_opy_(
            **kwargs,
            meta={
                bstack1lll1l1_opy_ (u"ࠫ࡫࡫ࡡࡵࡷࡵࡩࠬᑕ"): {
                    bstack1lll1l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᑖ"): feature.name,
                    bstack1lll1l1_opy_ (u"࠭ࡰࡢࡶ࡫ࠫᑗ"): feature.filename,
                    bstack1lll1l1_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬᑘ"): feature.description
                },
                bstack1lll1l1_opy_ (u"ࠨࡵࡦࡩࡳࡧࡲࡪࡱࠪᑙ"): {
                    bstack1lll1l1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᑚ"): scenario.name
                },
                bstack1lll1l1_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩᑛ"): steps,
                bstack1lll1l1_opy_ (u"ࠫࡪࡾࡡ࡮ࡲ࡯ࡩࡸ࠭ᑜ"): bstack1111l111ll_opy_(test)
            }
        )
    def bstack111111l11l_opy_(self):
        return {
            bstack1lll1l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫᑝ"): self.hooks
        }
    def bstack1llllllllll_opy_(self):
        if self.bstack11lllllll1_opy_:
            return {
                bstack1lll1l1_opy_ (u"࠭ࡩ࡯ࡶࡨ࡫ࡷࡧࡴࡪࡱࡱࡷࠬᑞ"): self.bstack11lllllll1_opy_
            }
        return {}
    def bstack1111111l1l_opy_(self):
        return {
            **super().bstack1111111l1l_opy_(),
            **self.bstack111111l11l_opy_()
        }
    def bstack111111l1l1_opy_(self):
        return {
            **super().bstack111111l1l1_opy_(),
            **self.bstack1llllllllll_opy_()
        }
    def bstack1l11l1l111_opy_(self):
        return bstack1lll1l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࠩᑟ")
class bstack1l111l1lll_opy_(bstack1l111l1ll1_opy_):
    def __init__(self, hook_type, *args, **kwargs):
        self.hook_type = hook_type
        super().__init__(*args, **kwargs, bstack1111l11l1_opy_=bstack1lll1l1_opy_ (u"ࠨࡪࡲࡳࡰ࠭ᑠ"))
    def bstack1l11ll111l_opy_(self):
        return self.hook_type
    def bstack1llllllll1l_opy_(self):
        return {
            bstack1lll1l1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡵࡻࡳࡩࠬᑡ"): self.hook_type
        }
    def bstack1111111l1l_opy_(self):
        return {
            **super().bstack1111111l1l_opy_(),
            **self.bstack1llllllll1l_opy_()
        }
    def bstack111111l1l1_opy_(self):
        return {
            **super().bstack111111l1l1_opy_(),
            **self.bstack1llllllll1l_opy_()
        }
    def bstack1l11l1l111_opy_(self):
        return bstack1lll1l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࠬᑢ")