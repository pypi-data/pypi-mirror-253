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
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result
def _11l111l1l1_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack11l111lll1_opy_:
    def __init__(self, handler):
        self._11l1111l11_opy_ = {}
        self._11l111l111_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        self._11l1111l11_opy_[bstack1lll1l1_opy_ (u"ࠨࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫዊ")] = Module._inject_setup_function_fixture
        self._11l1111l11_opy_[bstack1lll1l1_opy_ (u"ࠩࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪዋ")] = Module._inject_setup_module_fixture
        self._11l1111l11_opy_[bstack1lll1l1_opy_ (u"ࠪࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠪዌ")] = Class._inject_setup_class_fixture
        self._11l1111l11_opy_[bstack1lll1l1_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࠬው")] = Class._inject_setup_method_fixture
        Module._inject_setup_function_fixture = self.bstack11l11l1111_opy_(bstack1lll1l1_opy_ (u"ࠬ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨዎ"))
        Module._inject_setup_module_fixture = self.bstack11l11l1111_opy_(bstack1lll1l1_opy_ (u"࠭࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧዏ"))
        Class._inject_setup_class_fixture = self.bstack11l11l1111_opy_(bstack1lll1l1_opy_ (u"ࠧࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫ࠧዐ"))
        Class._inject_setup_method_fixture = self.bstack11l11l1111_opy_(bstack1lll1l1_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࠩዑ"))
    def bstack11l111l1ll_opy_(self, bstack11l1111ll1_opy_, hook_type):
        meth = getattr(bstack11l1111ll1_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._11l111l111_opy_[hook_type] = meth
            setattr(bstack11l1111ll1_opy_, hook_type, self.bstack11l1111l1l_opy_(hook_type))
    def bstack11l11111l1_opy_(self, instance, bstack11l111llll_opy_):
        if bstack11l111llll_opy_ == bstack1lll1l1_opy_ (u"ࠤࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠧዒ"):
            self.bstack11l111l1ll_opy_(instance.obj, bstack1lll1l1_opy_ (u"ࠥࡷࡪࡺࡵࡱࡡࡩࡹࡳࡩࡴࡪࡱࡱࠦዓ"))
            self.bstack11l111l1ll_opy_(instance.obj, bstack1lll1l1_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠣዔ"))
        if bstack11l111llll_opy_ == bstack1lll1l1_opy_ (u"ࠧࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪࠨዕ"):
            self.bstack11l111l1ll_opy_(instance.obj, bstack1lll1l1_opy_ (u"ࠨࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࠧዖ"))
            self.bstack11l111l1ll_opy_(instance.obj, bstack1lll1l1_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡳࡩࡻ࡬ࡦࠤ዗"))
        if bstack11l111llll_opy_ == bstack1lll1l1_opy_ (u"ࠣࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣዘ"):
            self.bstack11l111l1ll_opy_(instance.obj, bstack1lll1l1_opy_ (u"ࠤࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠢዙ"))
            self.bstack11l111l1ll_opy_(instance.obj, bstack1lll1l1_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠦዚ"))
        if bstack11l111llll_opy_ == bstack1lll1l1_opy_ (u"ࠦࡲ࡫ࡴࡩࡱࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࠧዛ"):
            self.bstack11l111l1ll_opy_(instance.obj, bstack1lll1l1_opy_ (u"ࠧࡹࡥࡵࡷࡳࡣࡲ࡫ࡴࡩࡱࡧࠦዜ"))
            self.bstack11l111l1ll_opy_(instance.obj, bstack1lll1l1_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡨࡸ࡭ࡵࡤࠣዝ"))
    @staticmethod
    def bstack11l111l11l_opy_(hook_type, func, args):
        if hook_type in [bstack1lll1l1_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ዞ"), bstack1lll1l1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠪዟ")]:
            _11l111l1l1_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack11l1111l1l_opy_(self, hook_type):
        def bstack11l11111ll_opy_(arg=None):
            self.handler(hook_type, bstack1lll1l1_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࠩዠ"))
            result = None
            exception = None
            try:
                self.bstack11l111l11l_opy_(hook_type, self._11l111l111_opy_[hook_type], (arg,))
                result = Result(result=bstack1lll1l1_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪዡ"))
            except Exception as e:
                result = Result(result=bstack1lll1l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫዢ"), exception=e)
                self.handler(hook_type, bstack1lll1l1_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫዣ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1lll1l1_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬዤ"), result)
        def bstack11l111ll11_opy_(this, arg=None):
            self.handler(hook_type, bstack1lll1l1_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫ࠧዥ"))
            result = None
            exception = None
            try:
                self.bstack11l111l11l_opy_(hook_type, self._11l111l111_opy_[hook_type], (this, arg))
                result = Result(result=bstack1lll1l1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨዦ"))
            except Exception as e:
                result = Result(result=bstack1lll1l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩዧ"), exception=e)
                self.handler(hook_type, bstack1lll1l1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࠩየ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1lll1l1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࠪዩ"), result)
        if hook_type in [bstack1lll1l1_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲ࡫ࡴࡩࡱࡧࠫዪ"), bstack1lll1l1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡨࡸ࡭ࡵࡤࠨያ")]:
            return bstack11l111ll11_opy_
        return bstack11l11111ll_opy_
    def bstack11l11l1111_opy_(self, bstack11l111llll_opy_):
        def bstack11l111ll1l_opy_(this, *args, **kwargs):
            self.bstack11l11111l1_opy_(this, bstack11l111llll_opy_)
            self._11l1111l11_opy_[bstack11l111llll_opy_](this, *args, **kwargs)
        return bstack11l111ll1l_opy_