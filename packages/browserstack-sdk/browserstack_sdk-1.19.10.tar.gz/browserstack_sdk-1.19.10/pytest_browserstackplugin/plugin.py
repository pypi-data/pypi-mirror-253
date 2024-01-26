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
import atexit
import datetime
import inspect
import logging
import os
import signal
import sys
import threading
from uuid import uuid4
from bstack_utils.percy_sdk import PercySDK
import tempfile
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack1l1llllll1_opy_, bstack1l1111111_opy_, update, bstack1ll111l1_opy_,
                                       bstack11l11l1ll_opy_, bstack1l1lll11ll_opy_, bstack1ll1ll111l_opy_, bstack111l1l11l_opy_,
                                       bstack1llll11l1_opy_, bstack111111l1l_opy_, bstack1lll1lllll_opy_, bstack1l11l1ll_opy_,
                                       bstack1l1l11l1ll_opy_, getAccessibilityResults, getAccessibilityResultsSummary)
from browserstack_sdk.bstack1ll1ll11_opy_ import bstack1l1l11l11l_opy_
from browserstack_sdk._version import __version__
from bstack_utils.capture import bstack1l11lll1ll_opy_
from bstack_utils.config import Config
from bstack_utils.constants import bstack111ll1lll_opy_, bstack1ll1l111ll_opy_, bstack1llll1l1l1_opy_, bstack1l1l1111_opy_, \
    bstack1111ll11l_opy_
from bstack_utils.helper import bstack1ll11111l_opy_, bstack1l1l11l111_opy_, bstack11l11l1ll1_opy_, bstack11llll1l1_opy_, \
    bstack11l11llll1_opy_, \
    bstack11l1llll11_opy_, bstack11llll1ll_opy_, bstack1lll11111_opy_, bstack11l1l1ll11_opy_, bstack1lll1ll1_opy_, Notset, \
    bstack1ll11lll1_opy_, bstack11l1ll1ll1_opy_, bstack11l11lll1l_opy_, Result, bstack11l11l111l_opy_, bstack11l1l11lll_opy_, bstack1l11l11lll_opy_, \
    bstack11l1lllll_opy_, bstack1111l11l_opy_, bstack1l11lllll_opy_, bstack11l1l111ll_opy_
from bstack_utils.bstack11l1111lll_opy_ import bstack11l111lll1_opy_
from bstack_utils.messages import bstack1l1l1l1ll_opy_, bstack1ll1l111_opy_, bstack1l1l1l11l_opy_, bstack11l1111ll_opy_, bstack1l1llll1ll_opy_, \
    bstack11lll111_opy_, bstack11111l11_opy_, bstack1111l1ll_opy_, bstack1lllll1lll_opy_, bstack1ll1l11ll_opy_, \
    bstack1ll1lll11l_opy_, bstack1l1ll11l1_opy_
from bstack_utils.proxy import bstack11lll1l11_opy_, bstack1l1111l11_opy_
from bstack_utils.bstack1llllll11_opy_ import bstack1111l1ll11_opy_, bstack1111l1l1l1_opy_, bstack1111l11l11_opy_, bstack1111l11l1l_opy_, \
    bstack1111l11lll_opy_, bstack1111l1l111_opy_, bstack1111ll1111_opy_, bstack1l1l111l11_opy_, bstack1111l1lll1_opy_
from bstack_utils.bstack11lllll1_opy_ import bstack11l111lll_opy_
from bstack_utils.bstack1ll111l1l_opy_ import bstack1lll1ll1l_opy_, bstack1111l1l11_opy_, bstack111ll11l_opy_, \
    bstack1l1l11ll_opy_, bstack1ll1111111_opy_
from bstack_utils.bstack1l11ll1l11_opy_ import bstack1l111l1l11_opy_
from bstack_utils.bstack1ll1l1l1ll_opy_ import bstack1l1ll11l_opy_
import bstack_utils.bstack1ll1ll111_opy_ as bstack11111111l_opy_
bstack11llll1l_opy_ = None
bstack1l11l1111_opy_ = None
bstack1l11111l1_opy_ = None
bstack1111lll1_opy_ = None
bstack1ll1l1111_opy_ = None
bstack1l1ll1l1l1_opy_ = None
bstack1l1ll11l11_opy_ = None
bstack1lll1l1l1_opy_ = None
bstack1llllll1ll_opy_ = None
bstack111l11l1_opy_ = None
bstack1lll111l11_opy_ = None
bstack11ll1l111_opy_ = None
bstack1l1l1111l1_opy_ = None
bstack1ll11l1l11_opy_ = bstack1lll1l1_opy_ (u"࠭ࠧᔷ")
CONFIG = {}
bstack1lll1111l_opy_ = False
bstack111111ll_opy_ = bstack1lll1l1_opy_ (u"ࠧࠨᔸ")
bstack11l1lll11_opy_ = bstack1lll1l1_opy_ (u"ࠨࠩᔹ")
bstack1l1l1lll1l_opy_ = False
bstack1l1ll1ll1_opy_ = []
bstack1l1l1ll11l_opy_ = bstack1ll1l111ll_opy_
bstack1llll11llll_opy_ = bstack1lll1l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩᔺ")
bstack1llll11l1ll_opy_ = False
bstack1ll1l1lll_opy_ = {}
logger = logging.getLogger(__name__)
logging.basicConfig(level=bstack1l1l1ll11l_opy_,
                    format=bstack1lll1l1_opy_ (u"ࠪࡠࡳࠫࠨࡢࡵࡦࡸ࡮ࡳࡥࠪࡵࠣ࡟ࠪ࠮࡮ࡢ࡯ࡨ࠭ࡸࡣ࡛ࠦࠪ࡯ࡩࡻ࡫࡬࡯ࡣࡰࡩ࠮ࡹ࡝ࠡ࠯ࠣࠩ࠭ࡳࡥࡴࡵࡤ࡫ࡪ࠯ࡳࠨᔻ"),
                    datefmt=bstack1lll1l1_opy_ (u"ࠫࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭ᔼ"),
                    stream=sys.stdout)
store = {
    bstack1lll1l1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᔽ"): []
}
bstack1llll11ll11_opy_ = False
def bstack1l1l11l1_opy_():
    global CONFIG
    global bstack1l1l1ll11l_opy_
    if bstack1lll1l1_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨᔾ") in CONFIG:
        bstack1l1l1ll11l_opy_ = bstack111ll1lll_opy_[CONFIG[bstack1lll1l1_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩᔿ")]]
        logging.getLogger().setLevel(bstack1l1l1ll11l_opy_)
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_1l11ll11ll_opy_ = {}
current_test_uuid = None
def bstack1llllll11l_opy_(page, bstack111lll1ll_opy_):
    try:
        page.evaluate(bstack1lll1l1_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤᕀ"),
                      bstack1lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿࠭ᕁ") + json.dumps(
                          bstack111lll1ll_opy_) + bstack1lll1l1_opy_ (u"ࠥࢁࢂࠨᕂ"))
    except Exception as e:
        print(bstack1lll1l1_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡻࡾࠤᕃ"), e)
def bstack11l11ll11_opy_(page, message, level):
    try:
        page.evaluate(bstack1lll1l1_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨᕄ"), bstack1lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫᕅ") + json.dumps(
            message) + bstack1lll1l1_opy_ (u"ࠧ࠭ࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠪᕆ") + json.dumps(level) + bstack1lll1l1_opy_ (u"ࠨࡿࢀࠫᕇ"))
    except Exception as e:
        print(bstack1lll1l1_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡧ࡮࡯ࡱࡷࡥࡹ࡯࡯࡯ࠢࡾࢁࠧᕈ"), e)
def pytest_configure(config):
    bstack11l1l11l_opy_ = Config.bstack1lllll11l1_opy_()
    config.args = bstack1l1ll11l_opy_.bstack1lllllll111_opy_(config.args)
    bstack11l1l11l_opy_.bstack1lll11111l_opy_(bstack1l11lllll_opy_(config.getoption(bstack1lll1l1_opy_ (u"ࠪࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧᕉ"))))
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    bstack1llll1l11l1_opy_ = item.config.getoption(bstack1lll1l1_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ᕊ"))
    plugins = item.config.getoption(bstack1lll1l1_opy_ (u"ࠧࡶ࡬ࡶࡩ࡬ࡲࡸࠨᕋ"))
    report = outcome.get_result()
    bstack1lllll11111_opy_(item, call, report)
    if bstack1lll1l1_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡵࡲࡵࡨ࡫ࡱࠦᕌ") not in plugins or bstack1lll1ll1_opy_():
        return
    summary = []
    driver = getattr(item, bstack1lll1l1_opy_ (u"ࠢࡠࡦࡵ࡭ࡻ࡫ࡲࠣᕍ"), None)
    page = getattr(item, bstack1lll1l1_opy_ (u"ࠣࡡࡳࡥ࡬࡫ࠢᕎ"), None)
    try:
        if (driver == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None):
        bstack1llll1l1111_opy_(item, report, summary, bstack1llll1l11l1_opy_)
    if (page is not None):
        bstack1lllll111ll_opy_(item, report, summary, bstack1llll1l11l1_opy_)
def bstack1llll1l1111_opy_(item, report, summary, bstack1llll1l11l1_opy_):
    if report.when == bstack1lll1l1_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨᕏ") and report.skipped:
        bstack1111l1lll1_opy_(report)
    if report.when in [bstack1lll1l1_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤᕐ"), bstack1lll1l1_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨᕑ")]:
        return
    if not bstack11l11l1ll1_opy_():
        return
    try:
        if (str(bstack1llll1l11l1_opy_).lower() != bstack1lll1l1_opy_ (u"ࠬࡺࡲࡶࡧࠪᕒ")):
            item._driver.execute_script(
                bstack1lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠣࠫᕓ") + json.dumps(
                    report.nodeid) + bstack1lll1l1_opy_ (u"ࠧࡾࡿࠪᕔ"))
        os.environ[bstack1lll1l1_opy_ (u"ࠨࡒ࡜ࡘࡊ࡙ࡔࡠࡖࡈࡗ࡙ࡥࡎࡂࡏࡈࠫᕕ")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack1lll1l1_opy_ (u"ࠤ࡚ࡅࡗࡔࡉࡏࡉ࠽ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠ࡮ࡣࡵ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨ࠾ࠥࢁ࠰ࡾࠤᕖ").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack1lll1l1_opy_ (u"ࠥࡻࡦࡹࡸࡧࡣ࡬ࡰࠧᕗ")))
    bstack1lll1lll1l_opy_ = bstack1lll1l1_opy_ (u"ࠦࠧᕘ")
    bstack1111l1lll1_opy_(report)
    if not passed:
        try:
            bstack1lll1lll1l_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack1lll1l1_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡨࡪࡺࡥࡳ࡯࡬ࡲࡪࠦࡦࡢ࡫࡯ࡹࡷ࡫ࠠࡳࡧࡤࡷࡴࡴ࠺ࠡࡽ࠳ࢁࠧᕙ").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack1lll1lll1l_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack1lll1l1_opy_ (u"ࠨࡷࡢࡵࡻࡪࡦ࡯࡬ࠣᕚ")))
        bstack1lll1lll1l_opy_ = bstack1lll1l1_opy_ (u"ࠢࠣᕛ")
        if not passed:
            try:
                bstack1lll1lll1l_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack1lll1l1_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡤࡦࡶࡨࡶࡲ࡯࡮ࡦࠢࡩࡥ࡮ࡲࡵࡳࡧࠣࡶࡪࡧࡳࡰࡰ࠽ࠤࢀ࠶ࡽࠣᕜ").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack1lll1lll1l_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack1lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡯࡮ࡧࡱࠥ࠰ࠥࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡪࡡࡵࡣࠥ࠾ࠥ࠭ᕝ")
                    + json.dumps(bstack1lll1l1_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠤࠦᕞ"))
                    + bstack1lll1l1_opy_ (u"ࠦࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃࠢᕟ")
                )
            else:
                item._driver.execute_script(
                    bstack1lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣࡧࡵࡶࡴࡸࠢ࠭ࠢ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡧࡥࡹࡧࠢ࠻ࠢࠪᕠ")
                    + json.dumps(str(bstack1lll1lll1l_opy_))
                    + bstack1lll1l1_opy_ (u"ࠨ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾࠤᕡ")
                )
        except Exception as e:
            summary.append(bstack1lll1l1_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡧ࡮࡯ࡱࡷࡥࡹ࡫࠺ࠡࡽ࠳ࢁࠧᕢ").format(e))
def bstack1llll11l1l1_opy_(test_name, error_message):
    try:
        bstack1llll1llll1_opy_ = []
        bstack1111l111_opy_ = os.environ.get(bstack1lll1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨᕣ"), bstack1lll1l1_opy_ (u"ࠩ࠳ࠫᕤ"))
        bstack111lll11_opy_ = {bstack1lll1l1_opy_ (u"ࠪࡲࡦࡳࡥࠨᕥ"): test_name, bstack1lll1l1_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᕦ"): error_message, bstack1lll1l1_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫᕧ"): bstack1111l111_opy_}
        bstack1lllll1111l_opy_ = os.path.join(tempfile.gettempdir(), bstack1lll1l1_opy_ (u"࠭ࡰࡸࡡࡳࡽࡹ࡫ࡳࡵࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫᕨ"))
        if os.path.exists(bstack1lllll1111l_opy_):
            with open(bstack1lllll1111l_opy_) as f:
                bstack1llll1llll1_opy_ = json.load(f)
        bstack1llll1llll1_opy_.append(bstack111lll11_opy_)
        with open(bstack1lllll1111l_opy_, bstack1lll1l1_opy_ (u"ࠧࡸࠩᕩ")) as f:
            json.dump(bstack1llll1llll1_opy_, f)
    except Exception as e:
        logger.debug(bstack1lll1l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡪࡸࡳࡪࡵࡷ࡭ࡳ࡭ࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡵࡿࡴࡦࡵࡷࠤࡪࡸࡲࡰࡴࡶ࠾ࠥ࠭ᕪ") + str(e))
def bstack1lllll111ll_opy_(item, report, summary, bstack1llll1l11l1_opy_):
    if report.when in [bstack1lll1l1_opy_ (u"ࠤࡶࡩࡹࡻࡰࠣᕫ"), bstack1lll1l1_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࠧᕬ")]:
        return
    if (str(bstack1llll1l11l1_opy_).lower() != bstack1lll1l1_opy_ (u"ࠫࡹࡸࡵࡦࠩᕭ")):
        bstack1llllll11l_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack1lll1l1_opy_ (u"ࠧࡽࡡࡴࡺࡩࡥ࡮ࡲࠢᕮ")))
    bstack1lll1lll1l_opy_ = bstack1lll1l1_opy_ (u"ࠨࠢᕯ")
    bstack1111l1lll1_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack1lll1lll1l_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack1lll1l1_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡪࡥࡵࡧࡵࡱ࡮ࡴࡥࠡࡨࡤ࡭ࡱࡻࡲࡦࠢࡵࡩࡦࡹ࡯࡯࠼ࠣࡿ࠵ࢃࠢᕰ").format(e)
                )
        try:
            if passed:
                bstack1ll1111111_opy_(getattr(item, bstack1lll1l1_opy_ (u"ࠨࡡࡳࡥ࡬࡫ࠧᕱ"), None), bstack1lll1l1_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤᕲ"))
            else:
                error_message = bstack1lll1l1_opy_ (u"ࠪࠫᕳ")
                if bstack1lll1lll1l_opy_:
                    bstack11l11ll11_opy_(item._page, str(bstack1lll1lll1l_opy_), bstack1lll1l1_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥᕴ"))
                    bstack1ll1111111_opy_(getattr(item, bstack1lll1l1_opy_ (u"ࠬࡥࡰࡢࡩࡨࠫᕵ"), None), bstack1lll1l1_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨᕶ"), str(bstack1lll1lll1l_opy_))
                    error_message = str(bstack1lll1lll1l_opy_)
                else:
                    bstack1ll1111111_opy_(getattr(item, bstack1lll1l1_opy_ (u"ࠧࡠࡲࡤ࡫ࡪ࠭ᕷ"), None), bstack1lll1l1_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣᕸ"))
                bstack1llll11l1l1_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack1lll1l1_opy_ (u"ࠤ࡚ࡅࡗࡔࡉࡏࡉ࠽ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡶࡲࡧࡥࡹ࡫ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳ࠻ࠢࡾ࠴ࢂࠨᕹ").format(e))
try:
    from typing import Generator
    import pytest_playwright.pytest_playwright as p
    @pytest.fixture
    def page(context: BrowserContext, request: pytest.FixtureRequest) -> Generator[Page, None, None]:
        page = context.new_page()
        request.node._page = page
        yield page
except:
    pass
def pytest_addoption(parser):
    parser.addoption(bstack1lll1l1_opy_ (u"ࠥ࠱࠲ࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢᕺ"), default=bstack1lll1l1_opy_ (u"ࠦࡋࡧ࡬ࡴࡧࠥᕻ"), help=bstack1lll1l1_opy_ (u"ࠧࡇࡵࡵࡱࡰࡥࡹ࡯ࡣࠡࡵࡨࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠦᕼ"))
    parser.addoption(bstack1lll1l1_opy_ (u"ࠨ࠭࠮ࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠧᕽ"), default=bstack1lll1l1_opy_ (u"ࠢࡇࡣ࡯ࡷࡪࠨᕾ"), help=bstack1lll1l1_opy_ (u"ࠣࡃࡸࡸࡴࡳࡡࡵ࡫ࡦࠤࡸ࡫ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠢᕿ"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack1lll1l1_opy_ (u"ࠤ࠰࠱ࡩࡸࡩࡷࡧࡵࠦᖀ"), action=bstack1lll1l1_opy_ (u"ࠥࡷࡹࡵࡲࡦࠤᖁ"), default=bstack1lll1l1_opy_ (u"ࠦࡨ࡮ࡲࡰ࡯ࡨࠦᖂ"),
                         help=bstack1lll1l1_opy_ (u"ࠧࡊࡲࡪࡸࡨࡶࠥࡺ࡯ࠡࡴࡸࡲࠥࡺࡥࡴࡶࡶࠦᖃ"))
def bstack1l1111l111_opy_(log):
    if not (log[bstack1lll1l1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᖄ")] and log[bstack1lll1l1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᖅ")].strip()):
        return
    active = bstack1l111lllll_opy_()
    log = {
        bstack1lll1l1_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᖆ"): log[bstack1lll1l1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᖇ")],
        bstack1lll1l1_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ᖈ"): datetime.datetime.utcnow().isoformat() + bstack1lll1l1_opy_ (u"ࠫ࡟࠭ᖉ"),
        bstack1lll1l1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᖊ"): log[bstack1lll1l1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᖋ")],
    }
    if active:
        if active[bstack1lll1l1_opy_ (u"ࠧࡵࡻࡳࡩࠬᖌ")] == bstack1lll1l1_opy_ (u"ࠨࡪࡲࡳࡰ࠭ᖍ"):
            log[bstack1lll1l1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᖎ")] = active[bstack1lll1l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᖏ")]
        elif active[bstack1lll1l1_opy_ (u"ࠫࡹࡿࡰࡦࠩᖐ")] == bstack1lll1l1_opy_ (u"ࠬࡺࡥࡴࡶࠪᖑ"):
            log[bstack1lll1l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᖒ")] = active[bstack1lll1l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᖓ")]
    bstack1l1ll11l_opy_.bstack1l11l11l11_opy_([log])
def bstack1l111lllll_opy_():
    if len(store[bstack1lll1l1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬᖔ")]) > 0 and store[bstack1lll1l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ᖕ")][-1]:
        return {
            bstack1lll1l1_opy_ (u"ࠪࡸࡾࡶࡥࠨᖖ"): bstack1lll1l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩᖗ"),
            bstack1lll1l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᖘ"): store[bstack1lll1l1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᖙ")][-1]
        }
    if store.get(bstack1lll1l1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫᖚ"), None):
        return {
            bstack1lll1l1_opy_ (u"ࠨࡶࡼࡴࡪ࠭ᖛ"): bstack1lll1l1_opy_ (u"ࠩࡷࡩࡸࡺࠧᖜ"),
            bstack1lll1l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᖝ"): store[bstack1lll1l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨᖞ")]
        }
    return None
bstack1l11111l11_opy_ = bstack1l11lll1ll_opy_(bstack1l1111l111_opy_)
def pytest_runtest_call(item):
    try:
        global CONFIG
        global bstack1llll11l1ll_opy_
        item._1llll1lll1l_opy_ = True
        bstack111l111ll_opy_ = bstack11111111l_opy_.bstack1llll1l1l_opy_(CONFIG, bstack11l1llll11_opy_(item.own_markers))
        item._a11y_test_case = bstack111l111ll_opy_
        if bstack1llll11l1ll_opy_:
            driver = getattr(item, bstack1lll1l1_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭ᖟ"), None)
            item._a11y_started = bstack11111111l_opy_.bstack1lll1l1l11_opy_(driver, bstack111l111ll_opy_)
        if not bstack1l1ll11l_opy_.on() or bstack1llll11llll_opy_ != bstack1lll1l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ᖠ"):
            return
        global current_test_uuid, bstack1l11111l11_opy_
        bstack1l11111l11_opy_.start()
        bstack1l11111l1l_opy_ = {
            bstack1lll1l1_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᖡ"): uuid4().__str__(),
            bstack1lll1l1_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᖢ"): datetime.datetime.utcnow().isoformat() + bstack1lll1l1_opy_ (u"ࠩ࡝ࠫᖣ")
        }
        current_test_uuid = bstack1l11111l1l_opy_[bstack1lll1l1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᖤ")]
        store[bstack1lll1l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨᖥ")] = bstack1l11111l1l_opy_[bstack1lll1l1_opy_ (u"ࠬࡻࡵࡪࡦࠪᖦ")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _1l11ll11ll_opy_[item.nodeid] = {**_1l11ll11ll_opy_[item.nodeid], **bstack1l11111l1l_opy_}
        bstack1llll1lllll_opy_(item, _1l11ll11ll_opy_[item.nodeid], bstack1lll1l1_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧᖧ"))
    except Exception as err:
        print(bstack1lll1l1_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡲࡶࡰࡷࡩࡸࡺ࡟ࡤࡣ࡯ࡰ࠿ࠦࡻࡾࠩᖨ"), str(err))
def pytest_runtest_setup(item):
    global bstack1llll11ll11_opy_
    threading.current_thread().percySessionName = item.nodeid
    if bstack11l1l1ll11_opy_():
        atexit.register(bstack1ll11l1lll_opy_)
        if not bstack1llll11ll11_opy_:
            try:
                bstack1lllll11lll_opy_ = [signal.SIGINT, signal.SIGTERM]
                if not bstack11l1l111ll_opy_():
                    bstack1lllll11lll_opy_.extend([signal.SIGHUP, signal.SIGQUIT])
                for s in bstack1lllll11lll_opy_:
                    signal.signal(s, bstack1llll11lll1_opy_)
                bstack1llll11ll11_opy_ = True
            except Exception as e:
                logger.debug(
                    bstack1lll1l1_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡪࡰࠣࡶࡪ࡭ࡩࡴࡶࡨࡶࠥࡹࡩࡨࡰࡤࡰࠥ࡮ࡡ࡯ࡦ࡯ࡩࡷࡹ࠺ࠡࠤᖩ") + str(e))
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack1111l1ll11_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack1lll1l1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᖪ")
    try:
        if not bstack1l1ll11l_opy_.on():
            return
        bstack1l11111l11_opy_.start()
        uuid = uuid4().__str__()
        bstack1l11111l1l_opy_ = {
            bstack1lll1l1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᖫ"): uuid,
            bstack1lll1l1_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᖬ"): datetime.datetime.utcnow().isoformat() + bstack1lll1l1_opy_ (u"ࠬࡠࠧᖭ"),
            bstack1lll1l1_opy_ (u"࠭ࡴࡺࡲࡨࠫᖮ"): bstack1lll1l1_opy_ (u"ࠧࡩࡱࡲ࡯ࠬᖯ"),
            bstack1lll1l1_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫᖰ"): bstack1lll1l1_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧᖱ"),
            bstack1lll1l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡰࡤࡱࡪ࠭ᖲ"): bstack1lll1l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪᖳ")
        }
        threading.current_thread().current_hook_uuid = uuid
        threading.current_thread().current_test_item = item
        store[bstack1lll1l1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩᖴ")] = item
        store[bstack1lll1l1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᖵ")] = [uuid]
        if not _1l11ll11ll_opy_.get(item.nodeid, None):
            _1l11ll11ll_opy_[item.nodeid] = {bstack1lll1l1_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ᖶ"): [], bstack1lll1l1_opy_ (u"ࠨࡨ࡬ࡼࡹࡻࡲࡦࡵࠪᖷ"): []}
        _1l11ll11ll_opy_[item.nodeid][bstack1lll1l1_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨᖸ")].append(bstack1l11111l1l_opy_[bstack1lll1l1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᖹ")])
        _1l11ll11ll_opy_[item.nodeid + bstack1lll1l1_opy_ (u"ࠫ࠲ࡹࡥࡵࡷࡳࠫᖺ")] = bstack1l11111l1l_opy_
        bstack1llll1ll111_opy_(item, bstack1l11111l1l_opy_, bstack1lll1l1_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ᖻ"))
    except Exception as err:
        print(bstack1lll1l1_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡸࡵ࡯ࡶࡨࡷࡹࡥࡳࡦࡶࡸࡴ࠿ࠦࡻࡾࠩᖼ"), str(err))
def pytest_runtest_teardown(item):
    try:
        global bstack1ll1l1lll_opy_
        if CONFIG.get(bstack1lll1l1_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭ᖽ"), False):
            if CONFIG.get(bstack1lll1l1_opy_ (u"ࠨࡲࡨࡶࡨࡿࡃࡢࡲࡷࡹࡷ࡫ࡍࡰࡦࡨࠫᖾ"), bstack1lll1l1_opy_ (u"ࠤࡤࡹࡹࡵࠢᖿ")) == bstack1lll1l1_opy_ (u"ࠥࡸࡪࡹࡴࡤࡣࡶࡩࠧᗀ"):
                bstack1llll1l1l11_opy_ = bstack1ll11111l_opy_(threading.current_thread(), bstack1lll1l1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧᗁ"), None)
                bstack1lll11ll11_opy_ = bstack1llll1l1l11_opy_ + bstack1lll1l1_opy_ (u"ࠧ࠳ࡴࡦࡵࡷࡧࡦࡹࡥࠣᗂ")
                driver = getattr(item, bstack1lll1l1_opy_ (u"࠭࡟ࡥࡴ࡬ࡺࡪࡸࠧᗃ"), None)
                PercySDK.screenshot(driver, bstack1lll11ll11_opy_)
        if getattr(item, bstack1lll1l1_opy_ (u"ࠧࡠࡣ࠴࠵ࡾࡥࡳࡵࡣࡵࡸࡪࡪࠧᗄ"), False):
            bstack1l1l11l11l_opy_.bstack1l111ll1_opy_(getattr(item, bstack1lll1l1_opy_ (u"ࠨࡡࡧࡶ࡮ࡼࡥࡳࠩᗅ"), None), bstack1ll1l1lll_opy_, logger, item)
        if not bstack1l1ll11l_opy_.on():
            return
        bstack1l11111l1l_opy_ = {
            bstack1lll1l1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᗆ"): uuid4().__str__(),
            bstack1lll1l1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᗇ"): datetime.datetime.utcnow().isoformat() + bstack1lll1l1_opy_ (u"ࠫ࡟࠭ᗈ"),
            bstack1lll1l1_opy_ (u"ࠬࡺࡹࡱࡧࠪᗉ"): bstack1lll1l1_opy_ (u"࠭ࡨࡰࡱ࡮ࠫᗊ"),
            bstack1lll1l1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪᗋ"): bstack1lll1l1_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬᗌ"),
            bstack1lll1l1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟࡯ࡣࡰࡩࠬᗍ"): bstack1lll1l1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬᗎ")
        }
        _1l11ll11ll_opy_[item.nodeid + bstack1lll1l1_opy_ (u"ࠫ࠲ࡺࡥࡢࡴࡧࡳࡼࡴࠧᗏ")] = bstack1l11111l1l_opy_
        bstack1llll1ll111_opy_(item, bstack1l11111l1l_opy_, bstack1lll1l1_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ᗐ"))
    except Exception as err:
        print(bstack1lll1l1_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡸࡵ࡯ࡶࡨࡷࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮࠻ࠢࡾࢁࠬᗑ"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if not bstack1l1ll11l_opy_.on():
        yield
        return
    start_time = datetime.datetime.now()
    if bstack1111l11l1l_opy_(fixturedef.argname):
        store[bstack1lll1l1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠ࡯ࡲࡨࡺࡲࡥࡠ࡫ࡷࡩࡲ࠭ᗒ")] = request.node
    elif bstack1111l11lll_opy_(fixturedef.argname):
        store[bstack1lll1l1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡦࡰࡦࡹࡳࡠ࡫ࡷࡩࡲ࠭ᗓ")] = request.node
    outcome = yield
    try:
        fixture = {
            bstack1lll1l1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᗔ"): fixturedef.argname,
            bstack1lll1l1_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪᗕ"): bstack11l11llll1_opy_(outcome),
            bstack1lll1l1_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭ᗖ"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        current_test_item = store[bstack1lll1l1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩᗗ")]
        if not _1l11ll11ll_opy_.get(current_test_item.nodeid, None):
            _1l11ll11ll_opy_[current_test_item.nodeid] = {bstack1lll1l1_opy_ (u"࠭ࡦࡪࡺࡷࡹࡷ࡫ࡳࠨᗘ"): []}
        _1l11ll11ll_opy_[current_test_item.nodeid][bstack1lll1l1_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩᗙ")].append(fixture)
    except Exception as err:
        logger.debug(bstack1lll1l1_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠࡵࡨࡸࡺࡶ࠺ࠡࡽࢀࠫᗚ"), str(err))
if bstack1lll1ll1_opy_() and bstack1l1ll11l_opy_.on():
    def pytest_bdd_before_step(request, step):
        try:
            _1l11ll11ll_opy_[request.node.nodeid][bstack1lll1l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬᗛ")].bstack1111111lll_opy_(id(step))
        except Exception as err:
            print(bstack1lll1l1_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳ࠾ࠥࢁࡽࠨᗜ"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        try:
            _1l11ll11ll_opy_[request.node.nodeid][bstack1lll1l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧᗝ")].bstack1l111ll11l_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack1lll1l1_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡧࡪࡤࡠࡵࡷࡩࡵࡥࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠩᗞ"), str(err))
    def pytest_bdd_after_step(request, step):
        try:
            bstack1l11ll1l11_opy_: bstack1l111l1l11_opy_ = _1l11ll11ll_opy_[request.node.nodeid][bstack1lll1l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩᗟ")]
            bstack1l11ll1l11_opy_.bstack1l111ll11l_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack1lll1l1_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡢࡥࡦࡢࡷࡹ࡫ࡰࡠࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠫᗠ"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack1llll11llll_opy_
        try:
            if not bstack1l1ll11l_opy_.on() or bstack1llll11llll_opy_ != bstack1lll1l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠬᗡ"):
                return
            global bstack1l11111l11_opy_
            bstack1l11111l11_opy_.start()
            if not _1l11ll11ll_opy_.get(request.node.nodeid, None):
                _1l11ll11ll_opy_[request.node.nodeid] = {}
            bstack1l11ll1l11_opy_ = bstack1l111l1l11_opy_.bstack111111111l_opy_(
                scenario, feature, request.node,
                name=bstack1111l1l111_opy_(request.node, scenario),
                bstack1l1111ll1l_opy_=bstack11llll1l1_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack1lll1l1_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵ࠯ࡦࡹࡨࡻ࡭ࡣࡧࡵࠫᗢ"),
                tags=bstack1111ll1111_opy_(feature, scenario)
            )
            _1l11ll11ll_opy_[request.node.nodeid][bstack1lll1l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ᗣ")] = bstack1l11ll1l11_opy_
            bstack1llll11l111_opy_(bstack1l11ll1l11_opy_.uuid)
            bstack1l1ll11l_opy_.bstack1l111lll11_opy_(bstack1lll1l1_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬᗤ"), bstack1l11ll1l11_opy_)
        except Exception as err:
            print(bstack1lll1l1_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡧࡪࡤࡠࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱ࠽ࠤࢀࢃࠧᗥ"), str(err))
def bstack1llll1lll11_opy_(bstack1llll1ll11l_opy_):
    if bstack1llll1ll11l_opy_ in store[bstack1lll1l1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᗦ")]:
        store[bstack1lll1l1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᗧ")].remove(bstack1llll1ll11l_opy_)
def bstack1llll11l111_opy_(bstack1llll11l11l_opy_):
    store[bstack1lll1l1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬᗨ")] = bstack1llll11l11l_opy_
    threading.current_thread().current_test_uuid = bstack1llll11l11l_opy_
@bstack1l1ll11l_opy_.bstack1llllll1ll1_opy_
def bstack1lllll11111_opy_(item, call, report):
    global bstack1llll11llll_opy_
    bstack1l1l1lll_opy_ = bstack11llll1l1_opy_()
    if hasattr(report, bstack1lll1l1_opy_ (u"ࠩࡶࡸࡴࡶࠧᗩ")):
        bstack1l1l1lll_opy_ = bstack11l11l111l_opy_(report.stop)
    if hasattr(report, bstack1lll1l1_opy_ (u"ࠪࡷࡹࡧࡲࡵࠩᗪ")):
        bstack1l1l1lll_opy_ = bstack11l11l111l_opy_(report.start)
    try:
        if getattr(report, bstack1lll1l1_opy_ (u"ࠫࡼ࡮ࡥ࡯ࠩᗫ"), bstack1lll1l1_opy_ (u"ࠬ࠭ᗬ")) == bstack1lll1l1_opy_ (u"࠭ࡣࡢ࡮࡯ࠫᗭ"):
            bstack1l11111l11_opy_.reset()
        if getattr(report, bstack1lll1l1_opy_ (u"ࠧࡸࡪࡨࡲࠬᗮ"), bstack1lll1l1_opy_ (u"ࠨࠩᗯ")) == bstack1lll1l1_opy_ (u"ࠩࡦࡥࡱࡲࠧᗰ"):
            if bstack1llll11llll_opy_ == bstack1lll1l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪᗱ"):
                _1l11ll11ll_opy_[item.nodeid][bstack1lll1l1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᗲ")] = bstack1l1l1lll_opy_
                bstack1llll1lllll_opy_(item, _1l11ll11ll_opy_[item.nodeid], bstack1lll1l1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧᗳ"), report, call)
                store[bstack1lll1l1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪᗴ")] = None
            elif bstack1llll11llll_opy_ == bstack1lll1l1_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠦᗵ"):
                bstack1l11ll1l11_opy_ = _1l11ll11ll_opy_[item.nodeid][bstack1lll1l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫᗶ")]
                bstack1l11ll1l11_opy_.set(hooks=_1l11ll11ll_opy_[item.nodeid].get(bstack1lll1l1_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨᗷ"), []))
                exception, bstack1l11l11111_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack1l11l11111_opy_ = [call.excinfo.exconly(), getattr(report, bstack1lll1l1_opy_ (u"ࠪࡰࡴࡴࡧࡳࡧࡳࡶࡹ࡫ࡸࡵࠩᗸ"), bstack1lll1l1_opy_ (u"ࠫࠬᗹ"))]
                bstack1l11ll1l11_opy_.stop(time=bstack1l1l1lll_opy_, result=Result(result=getattr(report, bstack1lll1l1_opy_ (u"ࠬࡵࡵࡵࡥࡲࡱࡪ࠭ᗺ"), bstack1lll1l1_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ᗻ")), exception=exception, bstack1l11l11111_opy_=bstack1l11l11111_opy_))
                bstack1l1ll11l_opy_.bstack1l111lll11_opy_(bstack1lll1l1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩᗼ"), _1l11ll11ll_opy_[item.nodeid][bstack1lll1l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫᗽ")])
        elif getattr(report, bstack1lll1l1_opy_ (u"ࠩࡺ࡬ࡪࡴࠧᗾ"), bstack1lll1l1_opy_ (u"ࠪࠫᗿ")) in [bstack1lll1l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪᘀ"), bstack1lll1l1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧᘁ")]:
            bstack1l11111ll1_opy_ = item.nodeid + bstack1lll1l1_opy_ (u"࠭࠭ࠨᘂ") + getattr(report, bstack1lll1l1_opy_ (u"ࠧࡸࡪࡨࡲࠬᘃ"), bstack1lll1l1_opy_ (u"ࠨࠩᘄ"))
            if getattr(report, bstack1lll1l1_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪᘅ"), False):
                hook_type = bstack1lll1l1_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠨᘆ") if getattr(report, bstack1lll1l1_opy_ (u"ࠫࡼ࡮ࡥ࡯ࠩᘇ"), bstack1lll1l1_opy_ (u"ࠬ࠭ᘈ")) == bstack1lll1l1_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬᘉ") else bstack1lll1l1_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠫᘊ")
                _1l11ll11ll_opy_[bstack1l11111ll1_opy_] = {
                    bstack1lll1l1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᘋ"): uuid4().__str__(),
                    bstack1lll1l1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ᘌ"): bstack1l1l1lll_opy_,
                    bstack1lll1l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭ᘍ"): hook_type
                }
            _1l11ll11ll_opy_[bstack1l11111ll1_opy_][bstack1lll1l1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᘎ")] = bstack1l1l1lll_opy_
            bstack1llll1lll11_opy_(_1l11ll11ll_opy_[bstack1l11111ll1_opy_][bstack1lll1l1_opy_ (u"ࠬࡻࡵࡪࡦࠪᘏ")])
            bstack1llll1ll111_opy_(item, _1l11ll11ll_opy_[bstack1l11111ll1_opy_], bstack1lll1l1_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨᘐ"), report, call)
            if getattr(report, bstack1lll1l1_opy_ (u"ࠧࡸࡪࡨࡲࠬᘑ"), bstack1lll1l1_opy_ (u"ࠨࠩᘒ")) == bstack1lll1l1_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨᘓ"):
                if getattr(report, bstack1lll1l1_opy_ (u"ࠪࡳࡺࡺࡣࡰ࡯ࡨࠫᘔ"), bstack1lll1l1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᘕ")) == bstack1lll1l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᘖ"):
                    bstack1l11111l1l_opy_ = {
                        bstack1lll1l1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᘗ"): uuid4().__str__(),
                        bstack1lll1l1_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫᘘ"): bstack11llll1l1_opy_(),
                        bstack1lll1l1_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᘙ"): bstack11llll1l1_opy_()
                    }
                    _1l11ll11ll_opy_[item.nodeid] = {**_1l11ll11ll_opy_[item.nodeid], **bstack1l11111l1l_opy_}
                    bstack1llll1lllll_opy_(item, _1l11ll11ll_opy_[item.nodeid], bstack1lll1l1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪᘚ"))
                    bstack1llll1lllll_opy_(item, _1l11ll11ll_opy_[item.nodeid], bstack1lll1l1_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬᘛ"), report, call)
    except Exception as err:
        print(bstack1lll1l1_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣ࡬ࡦࡴࡤ࡭ࡧࡢࡳ࠶࠷ࡹࡠࡶࡨࡷࡹࡥࡥࡷࡧࡱࡸ࠿ࠦࡻࡾࠩᘜ"), str(err))
def bstack1llll111l1l_opy_(test, bstack1l11111l1l_opy_, result=None, call=None, bstack1111l11l1_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack1l11ll1l11_opy_ = {
        bstack1lll1l1_opy_ (u"ࠬࡻࡵࡪࡦࠪᘝ"): bstack1l11111l1l_opy_[bstack1lll1l1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᘞ")],
        bstack1lll1l1_opy_ (u"ࠧࡵࡻࡳࡩࠬᘟ"): bstack1lll1l1_opy_ (u"ࠨࡶࡨࡷࡹ࠭ᘠ"),
        bstack1lll1l1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᘡ"): test.name,
        bstack1lll1l1_opy_ (u"ࠪࡦࡴࡪࡹࠨᘢ"): {
            bstack1lll1l1_opy_ (u"ࠫࡱࡧ࡮ࡨࠩᘣ"): bstack1lll1l1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬᘤ"),
            bstack1lll1l1_opy_ (u"࠭ࡣࡰࡦࡨࠫᘥ"): inspect.getsource(test.obj)
        },
        bstack1lll1l1_opy_ (u"ࠧࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᘦ"): test.name,
        bstack1lll1l1_opy_ (u"ࠨࡵࡦࡳࡵ࡫ࠧᘧ"): test.name,
        bstack1lll1l1_opy_ (u"ࠩࡶࡧࡴࡶࡥࡴࠩᘨ"): bstack1l1ll11l_opy_.bstack1l11ll1lll_opy_(test),
        bstack1lll1l1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ᘩ"): file_path,
        bstack1lll1l1_opy_ (u"ࠫࡱࡵࡣࡢࡶ࡬ࡳࡳ࠭ᘪ"): file_path,
        bstack1lll1l1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᘫ"): bstack1lll1l1_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧᘬ"),
        bstack1lll1l1_opy_ (u"ࠧࡷࡥࡢࡪ࡮ࡲࡥࡱࡣࡷ࡬ࠬᘭ"): file_path,
        bstack1lll1l1_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᘮ"): bstack1l11111l1l_opy_[bstack1lll1l1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ᘯ")],
        bstack1lll1l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ᘰ"): bstack1lll1l1_opy_ (u"ࠫࡕࡿࡴࡦࡵࡷࠫᘱ"),
        bstack1lll1l1_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡗ࡫ࡲࡶࡰࡓࡥࡷࡧ࡭ࠨᘲ"): {
            bstack1lll1l1_opy_ (u"࠭ࡲࡦࡴࡸࡲࡤࡴࡡ࡮ࡧࠪᘳ"): test.nodeid
        },
        bstack1lll1l1_opy_ (u"ࠧࡵࡣࡪࡷࠬᘴ"): bstack11l1llll11_opy_(test.own_markers)
    }
    if bstack1111l11l1_opy_ in [bstack1lll1l1_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩᘵ"), bstack1lll1l1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫᘶ")]:
        bstack1l11ll1l11_opy_[bstack1lll1l1_opy_ (u"ࠪࡱࡪࡺࡡࠨᘷ")] = {
            bstack1lll1l1_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭ᘸ"): bstack1l11111l1l_opy_.get(bstack1lll1l1_opy_ (u"ࠬ࡬ࡩࡹࡶࡸࡶࡪࡹࠧᘹ"), [])
        }
    if bstack1111l11l1_opy_ == bstack1lll1l1_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓ࡬࡫ࡳࡴࡪࡪࠧᘺ"):
        bstack1l11ll1l11_opy_[bstack1lll1l1_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᘻ")] = bstack1lll1l1_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩᘼ")
        bstack1l11ll1l11_opy_[bstack1lll1l1_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨᘽ")] = bstack1l11111l1l_opy_[bstack1lll1l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩᘾ")]
        bstack1l11ll1l11_opy_[bstack1lll1l1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᘿ")] = bstack1l11111l1l_opy_[bstack1lll1l1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᙀ")]
    if result:
        bstack1l11ll1l11_opy_[bstack1lll1l1_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᙁ")] = result.outcome
        bstack1l11ll1l11_opy_[bstack1lll1l1_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨᙂ")] = result.duration * 1000
        bstack1l11ll1l11_opy_[bstack1lll1l1_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᙃ")] = bstack1l11111l1l_opy_[bstack1lll1l1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᙄ")]
        if result.failed:
            bstack1l11ll1l11_opy_[bstack1lll1l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩᙅ")] = bstack1l1ll11l_opy_.bstack11lll1ll1l_opy_(call.excinfo.typename)
            bstack1l11ll1l11_opy_[bstack1lll1l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬᙆ")] = bstack1l1ll11l_opy_.bstack1lllll1l111_opy_(call.excinfo, result)
        bstack1l11ll1l11_opy_[bstack1lll1l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫᙇ")] = bstack1l11111l1l_opy_[bstack1lll1l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᙈ")]
    if outcome:
        bstack1l11ll1l11_opy_[bstack1lll1l1_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᙉ")] = bstack11l11llll1_opy_(outcome)
        bstack1l11ll1l11_opy_[bstack1lll1l1_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩᙊ")] = 0
        bstack1l11ll1l11_opy_[bstack1lll1l1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᙋ")] = bstack1l11111l1l_opy_[bstack1lll1l1_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᙌ")]
        if bstack1l11ll1l11_opy_[bstack1lll1l1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᙍ")] == bstack1lll1l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᙎ"):
            bstack1l11ll1l11_opy_[bstack1lll1l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠬᙏ")] = bstack1lll1l1_opy_ (u"ࠧࡖࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࠨᙐ")  # bstack1llll1ll1l1_opy_
            bstack1l11ll1l11_opy_[bstack1lll1l1_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩᙑ")] = [{bstack1lll1l1_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬᙒ"): [bstack1lll1l1_opy_ (u"ࠪࡷࡴࡳࡥࠡࡧࡵࡶࡴࡸࠧᙓ")]}]
        bstack1l11ll1l11_opy_[bstack1lll1l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪᙔ")] = bstack1l11111l1l_opy_[bstack1lll1l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫᙕ")]
    return bstack1l11ll1l11_opy_
def bstack1llll111ll1_opy_(test, bstack1l111l1111_opy_, bstack1111l11l1_opy_, result, call, outcome, bstack1llll1l1l1l_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack1l111l1111_opy_[bstack1lll1l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡹࡿࡰࡦࠩᙖ")]
    hook_name = bstack1l111l1111_opy_[bstack1lll1l1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡴࡡ࡮ࡧࠪᙗ")]
    hook_data = {
        bstack1lll1l1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᙘ"): bstack1l111l1111_opy_[bstack1lll1l1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᙙ")],
        bstack1lll1l1_opy_ (u"ࠪࡸࡾࡶࡥࠨᙚ"): bstack1lll1l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩᙛ"),
        bstack1lll1l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᙜ"): bstack1lll1l1_opy_ (u"࠭ࡻࡾࠩᙝ").format(bstack1111l1l1l1_opy_(hook_name)),
        bstack1lll1l1_opy_ (u"ࠧࡣࡱࡧࡽࠬᙞ"): {
            bstack1lll1l1_opy_ (u"ࠨ࡮ࡤࡲ࡬࠭ᙟ"): bstack1lll1l1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩᙠ"),
            bstack1lll1l1_opy_ (u"ࠪࡧࡴࡪࡥࠨᙡ"): None
        },
        bstack1lll1l1_opy_ (u"ࠫࡸࡩ࡯ࡱࡧࠪᙢ"): test.name,
        bstack1lll1l1_opy_ (u"ࠬࡹࡣࡰࡲࡨࡷࠬᙣ"): bstack1l1ll11l_opy_.bstack1l11ll1lll_opy_(test, hook_name),
        bstack1lll1l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩᙤ"): file_path,
        bstack1lll1l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡹ࡯࡯࡯ࠩᙥ"): file_path,
        bstack1lll1l1_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᙦ"): bstack1lll1l1_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪᙧ"),
        bstack1lll1l1_opy_ (u"ࠪࡺࡨࡥࡦࡪ࡮ࡨࡴࡦࡺࡨࠨᙨ"): file_path,
        bstack1lll1l1_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᙩ"): bstack1l111l1111_opy_[bstack1lll1l1_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᙪ")],
        bstack1lll1l1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩᙫ"): bstack1lll1l1_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺ࠭ࡤࡷࡦࡹࡲࡨࡥࡳࠩᙬ") if bstack1llll11llll_opy_ == bstack1lll1l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠬ᙭") else bstack1lll1l1_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵࠩ᙮"),
        bstack1lll1l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭ᙯ"): hook_type
    }
    bstack1llll1l1lll_opy_ = bstack1l11l1llll_opy_(_1l11ll11ll_opy_.get(test.nodeid, None))
    if bstack1llll1l1lll_opy_:
        hook_data[bstack1lll1l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡩࡥࠩᙰ")] = bstack1llll1l1lll_opy_
    if result:
        hook_data[bstack1lll1l1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᙱ")] = result.outcome
        hook_data[bstack1lll1l1_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧᙲ")] = result.duration * 1000
        hook_data[bstack1lll1l1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᙳ")] = bstack1l111l1111_opy_[bstack1lll1l1_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᙴ")]
        if result.failed:
            hook_data[bstack1lll1l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨᙵ")] = bstack1l1ll11l_opy_.bstack11lll1ll1l_opy_(call.excinfo.typename)
            hook_data[bstack1lll1l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫᙶ")] = bstack1l1ll11l_opy_.bstack1lllll1l111_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack1lll1l1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᙷ")] = bstack11l11llll1_opy_(outcome)
        hook_data[bstack1lll1l1_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡢࡱࡸ࠭ᙸ")] = 100
        hook_data[bstack1lll1l1_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᙹ")] = bstack1l111l1111_opy_[bstack1lll1l1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᙺ")]
        if hook_data[bstack1lll1l1_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᙻ")] == bstack1lll1l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᙼ"):
            hook_data[bstack1lll1l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩᙽ")] = bstack1lll1l1_opy_ (u"࡚ࠫࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠬᙾ")  # bstack1llll1ll1l1_opy_
            hook_data[bstack1lll1l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ᙿ")] = [{bstack1lll1l1_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩ "): [bstack1lll1l1_opy_ (u"ࠧࡴࡱࡰࡩࠥ࡫ࡲࡳࡱࡵࠫᚁ")]}]
    if bstack1llll1l1l1l_opy_:
        hook_data[bstack1lll1l1_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᚂ")] = bstack1llll1l1l1l_opy_.result
        hook_data[bstack1lll1l1_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪᚃ")] = bstack11l1ll1ll1_opy_(bstack1l111l1111_opy_[bstack1lll1l1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᚄ")], bstack1l111l1111_opy_[bstack1lll1l1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᚅ")])
        hook_data[bstack1lll1l1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᚆ")] = bstack1l111l1111_opy_[bstack1lll1l1_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᚇ")]
        if hook_data[bstack1lll1l1_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᚈ")] == bstack1lll1l1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᚉ"):
            hook_data[bstack1lll1l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨᚊ")] = bstack1l1ll11l_opy_.bstack11lll1ll1l_opy_(bstack1llll1l1l1l_opy_.exception_type)
            hook_data[bstack1lll1l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫᚋ")] = [{bstack1lll1l1_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧᚌ"): bstack11l11lll1l_opy_(bstack1llll1l1l1l_opy_.exception)}]
    return hook_data
def bstack1llll1lllll_opy_(test, bstack1l11111l1l_opy_, bstack1111l11l1_opy_, result=None, call=None, outcome=None):
    bstack1l11ll1l11_opy_ = bstack1llll111l1l_opy_(test, bstack1l11111l1l_opy_, result, call, bstack1111l11l1_opy_, outcome)
    driver = getattr(test, bstack1lll1l1_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭ᚍ"), None)
    if bstack1111l11l1_opy_ == bstack1lll1l1_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧᚎ") and driver:
        bstack1l11ll1l11_opy_[bstack1lll1l1_opy_ (u"ࠧࡪࡰࡷࡩ࡬ࡸࡡࡵ࡫ࡲࡲࡸ࠭ᚏ")] = bstack1l1ll11l_opy_.bstack1l111l11l1_opy_(driver)
    if bstack1111l11l1_opy_ == bstack1lll1l1_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩᚐ"):
        bstack1111l11l1_opy_ = bstack1lll1l1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫᚑ")
    bstack1l11l1l1ll_opy_ = {
        bstack1lll1l1_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧᚒ"): bstack1111l11l1_opy_,
        bstack1lll1l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭ᚓ"): bstack1l11ll1l11_opy_
    }
    bstack1l1ll11l_opy_.bstack1l11l1111l_opy_(bstack1l11l1l1ll_opy_)
def bstack1llll1ll111_opy_(test, bstack1l11111l1l_opy_, bstack1111l11l1_opy_, result=None, call=None, outcome=None, bstack1llll1l1l1l_opy_=None):
    hook_data = bstack1llll111ll1_opy_(test, bstack1l11111l1l_opy_, bstack1111l11l1_opy_, result, call, outcome, bstack1llll1l1l1l_opy_)
    bstack1l11l1l1ll_opy_ = {
        bstack1lll1l1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩᚔ"): bstack1111l11l1_opy_,
        bstack1lll1l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࠨᚕ"): hook_data
    }
    bstack1l1ll11l_opy_.bstack1l11l1111l_opy_(bstack1l11l1l1ll_opy_)
def bstack1l11l1llll_opy_(bstack1l11111l1l_opy_):
    if not bstack1l11111l1l_opy_:
        return None
    if bstack1l11111l1l_opy_.get(bstack1lll1l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪᚖ"), None):
        return getattr(bstack1l11111l1l_opy_[bstack1lll1l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫᚗ")], bstack1lll1l1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᚘ"), None)
    return bstack1l11111l1l_opy_.get(bstack1lll1l1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᚙ"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    yield
    try:
        if not bstack1l1ll11l_opy_.on():
            return
        places = [bstack1lll1l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪᚚ"), bstack1lll1l1_opy_ (u"ࠬࡩࡡ࡭࡮ࠪ᚛"), bstack1lll1l1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨ᚜")]
        bstack1l11lll111_opy_ = []
        for bstack1lllll11ll1_opy_ in places:
            records = caplog.get_records(bstack1lllll11ll1_opy_)
            bstack1llll1ll1ll_opy_ = bstack1lll1l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ᚝") if bstack1lllll11ll1_opy_ == bstack1lll1l1_opy_ (u"ࠨࡥࡤࡰࡱ࠭᚞") else bstack1lll1l1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ᚟")
            bstack1llll11ll1l_opy_ = request.node.nodeid + (bstack1lll1l1_opy_ (u"ࠪࠫᚠ") if bstack1lllll11ll1_opy_ == bstack1lll1l1_opy_ (u"ࠫࡨࡧ࡬࡭ࠩᚡ") else bstack1lll1l1_opy_ (u"ࠬ࠳ࠧᚢ") + bstack1lllll11ll1_opy_)
            bstack1llll11l11l_opy_ = bstack1l11l1llll_opy_(_1l11ll11ll_opy_.get(bstack1llll11ll1l_opy_, None))
            if not bstack1llll11l11l_opy_:
                continue
            for record in records:
                if bstack11l1l11lll_opy_(record.message):
                    continue
                bstack1l11lll111_opy_.append({
                    bstack1lll1l1_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩᚣ"): datetime.datetime.utcfromtimestamp(record.created).isoformat() + bstack1lll1l1_opy_ (u"࡛ࠧࠩᚤ"),
                    bstack1lll1l1_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᚥ"): record.levelname,
                    bstack1lll1l1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᚦ"): record.message,
                    bstack1llll1ll1ll_opy_: bstack1llll11l11l_opy_
                })
        if len(bstack1l11lll111_opy_) > 0:
            bstack1l1ll11l_opy_.bstack1l11l11l11_opy_(bstack1l11lll111_opy_)
    except Exception as err:
        print(bstack1lll1l1_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡩࡨࡵ࡮ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧ࠽ࠤࢀࢃࠧᚧ"), str(err))
def bstack11ll1111_opy_(sequence, driver_command, response=None):
    if sequence == bstack1lll1l1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࠪᚨ"):
        if driver_command == bstack1lll1l1_opy_ (u"ࠬࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠩᚩ"):
            bstack1l1ll11l_opy_.bstack1l1llll11l_opy_({
                bstack1lll1l1_opy_ (u"࠭ࡩ࡮ࡣࡪࡩࠬᚪ"): response[bstack1lll1l1_opy_ (u"ࠧࡷࡣ࡯ࡹࡪ࠭ᚫ")],
                bstack1lll1l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᚬ"): store[bstack1lll1l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭ᚭ")]
            })
def bstack1ll11l1lll_opy_():
    global bstack1l1ll1ll1_opy_
    bstack1l1ll11l_opy_.bstack1l11ll1111_opy_()
    for driver in bstack1l1ll1ll1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1llll11lll1_opy_(*args):
    global bstack1l1ll1ll1_opy_
    bstack1l1ll11l_opy_.bstack1l11ll1111_opy_()
    for driver in bstack1l1ll1ll1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1ll11lll11_opy_(self, *args, **kwargs):
    bstack1111111ll_opy_ = bstack11llll1l_opy_(self, *args, **kwargs)
    bstack1l1ll11l_opy_.bstack1l1l1l111l_opy_(self)
    return bstack1111111ll_opy_
def bstack1lll11lll_opy_(framework_name):
    global bstack1ll11l1l11_opy_
    global bstack1ll111l1ll_opy_
    bstack1ll11l1l11_opy_ = framework_name
    logger.info(bstack1l1ll11l1_opy_.format(bstack1ll11l1l11_opy_.split(bstack1lll1l1_opy_ (u"ࠪ࠱ࠬᚮ"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack11l11l1ll1_opy_():
            Service.start = bstack1ll1ll111l_opy_
            Service.stop = bstack111l1l11l_opy_
            webdriver.Remote.__init__ = bstack1ll1ll1l1_opy_
            webdriver.Remote.get = bstack1l1lll1l_opy_
            if not isinstance(os.getenv(bstack1lll1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔ࡞࡚ࡅࡔࡖࡢࡔࡆࡘࡁࡍࡎࡈࡐࠬᚯ")), str):
                return
            WebDriver.close = bstack1llll11l1_opy_
            WebDriver.quit = bstack11lll1111_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.bstack11l111l1l_opy_ = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
            WebDriver.bstack1ll1ll11ll_opy_ = getAccessibilityResultsSummary
        if not bstack11l11l1ll1_opy_() and bstack1l1ll11l_opy_.on():
            webdriver.Remote.__init__ = bstack1ll11lll11_opy_
        bstack1ll111l1ll_opy_ = True
    except Exception as e:
        pass
    bstack1l1111l1l_opy_()
    if os.environ.get(bstack1lll1l1_opy_ (u"࡙ࠬࡅࡍࡇࡑࡍ࡚ࡓ࡟ࡐࡔࡢࡔࡑࡇ࡙ࡘࡔࡌࡋࡍ࡚࡟ࡊࡐࡖࡘࡆࡒࡌࡆࡆࠪᚰ")):
        bstack1ll111l1ll_opy_ = eval(os.environ.get(bstack1lll1l1_opy_ (u"࠭ࡓࡆࡎࡈࡒࡎ࡛ࡍࡠࡑࡕࡣࡕࡒࡁ࡚࡙ࡕࡍࡌࡎࡔࡠࡋࡑࡗ࡙ࡇࡌࡍࡇࡇࠫᚱ")))
    if not bstack1ll111l1ll_opy_:
        bstack1lll1lllll_opy_(bstack1lll1l1_opy_ (u"ࠢࡑࡣࡦ࡯ࡦ࡭ࡥࡴࠢࡱࡳࡹࠦࡩ࡯ࡵࡷࡥࡱࡲࡥࡥࠤᚲ"), bstack1ll1lll11l_opy_)
    if bstack1ll11llll1_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            RemoteConnection._get_proxy_url = bstack11l111ll_opy_
        except Exception as e:
            logger.error(bstack11lll111_opy_.format(str(e)))
    if bstack1lll1l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨᚳ") in str(framework_name).lower():
        if not bstack11l11l1ll1_opy_():
            return
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            pytest_selenium.pytest_report_header = bstack11l11l1ll_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1l1lll11ll_opy_
            Config.getoption = bstack1ll1lll11_opy_
        except Exception as e:
            pass
        try:
            from pytest_bdd import reporting
            reporting.runtest_makereport = bstack1lll1lll11_opy_
        except Exception as e:
            pass
def bstack11lll1111_opy_(self):
    global bstack1ll11l1l11_opy_
    global bstack111l1llll_opy_
    global bstack1l11l1111_opy_
    try:
        if bstack1lll1l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩᚴ") in bstack1ll11l1l11_opy_ and self.session_id != None and bstack1ll11111l_opy_(threading.current_thread(), bstack1lll1l1_opy_ (u"ࠪࡸࡪࡹࡴࡔࡶࡤࡸࡺࡹࠧᚵ"), bstack1lll1l1_opy_ (u"ࠫࠬᚶ")) != bstack1lll1l1_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ᚷ"):
            bstack1lllll11_opy_ = bstack1lll1l1_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ᚸ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack1lll1l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᚹ")
            bstack1111l11l_opy_(logger, True)
            if self != None:
                bstack1l1l11ll_opy_(self, bstack1lllll11_opy_, bstack1lll1l1_opy_ (u"ࠨ࠮ࠣࠫᚺ").join(threading.current_thread().bstackTestErrorMessages))
        item = store.get(bstack1lll1l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡷࡩࡲ࠭ᚻ"), None)
        if item is not None and bstack1llll11l1ll_opy_:
            bstack1l1l11l11l_opy_.bstack1l111ll1_opy_(self, bstack1ll1l1lll_opy_, logger, item)
        threading.current_thread().testStatus = bstack1lll1l1_opy_ (u"ࠪࠫᚼ")
    except Exception as e:
        logger.debug(bstack1lll1l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡰࡥࡷࡱࡩ࡯ࡩࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࠧᚽ") + str(e))
    bstack1l11l1111_opy_(self)
    self.session_id = None
def bstack1ll1ll1l1_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack111l1llll_opy_
    global bstack1lll111ll1_opy_
    global bstack1l1l1lll1l_opy_
    global bstack1ll11l1l11_opy_
    global bstack11llll1l_opy_
    global bstack1l1ll1ll1_opy_
    global bstack111111ll_opy_
    global bstack11l1lll11_opy_
    global bstack1llll11l1ll_opy_
    global bstack1ll1l1lll_opy_
    CONFIG[bstack1lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧᚾ")] = str(bstack1ll11l1l11_opy_) + str(__version__)
    command_executor = bstack1lll11111_opy_(bstack111111ll_opy_)
    logger.debug(bstack11l1111ll_opy_.format(command_executor))
    proxy = bstack1l1l11l1ll_opy_(CONFIG, proxy)
    bstack1111l111_opy_ = 0
    try:
        if bstack1l1l1lll1l_opy_ is True:
            bstack1111l111_opy_ = int(os.environ.get(bstack1lll1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᚿ")))
    except:
        bstack1111l111_opy_ = 0
    bstack1llllll1l_opy_ = bstack1l1llllll1_opy_(CONFIG, bstack1111l111_opy_)
    logger.debug(bstack1111l1ll_opy_.format(str(bstack1llllll1l_opy_)))
    bstack1ll1l1lll_opy_ = CONFIG.get(bstack1lll1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪᛀ"))[bstack1111l111_opy_]
    if bstack1lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬᛁ") in CONFIG and CONFIG[bstack1lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ᛂ")]:
        bstack111ll11l_opy_(bstack1llllll1l_opy_, bstack11l1lll11_opy_)
    if desired_capabilities:
        bstack1llll1lll1_opy_ = bstack1l1111111_opy_(desired_capabilities)
        bstack1llll1lll1_opy_[bstack1lll1l1_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪᛃ")] = bstack1ll11lll1_opy_(CONFIG)
        bstack11ll11l1l_opy_ = bstack1l1llllll1_opy_(bstack1llll1lll1_opy_)
        if bstack11ll11l1l_opy_:
            bstack1llllll1l_opy_ = update(bstack11ll11l1l_opy_, bstack1llllll1l_opy_)
        desired_capabilities = None
    if options:
        bstack111111l1l_opy_(options, bstack1llllll1l_opy_)
    if not options:
        options = bstack1ll111l1_opy_(bstack1llllll1l_opy_)
    if bstack11111111l_opy_.bstack1l111ll11_opy_(CONFIG, bstack1111l111_opy_) and bstack11111111l_opy_.bstack1l1lll11_opy_(bstack1llllll1l_opy_, options):
        bstack1llll11l1ll_opy_ = True
        bstack11111111l_opy_.set_capabilities(bstack1llllll1l_opy_, CONFIG)
    if proxy and bstack11llll1ll_opy_() >= version.parse(bstack1lll1l1_opy_ (u"ࠫ࠹࠴࠱࠱࠰࠳ࠫᛄ")):
        options.proxy(proxy)
    if options and bstack11llll1ll_opy_() >= version.parse(bstack1lll1l1_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫᛅ")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack11llll1ll_opy_() < version.parse(bstack1lll1l1_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬᛆ")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack1llllll1l_opy_)
    logger.info(bstack1l1l1l11l_opy_)
    if bstack11llll1ll_opy_() >= version.parse(bstack1lll1l1_opy_ (u"ࠧ࠵࠰࠴࠴࠳࠶ࠧᛇ")):
        bstack11llll1l_opy_(self, command_executor=command_executor,
                  options=options, keep_alive=keep_alive, file_detector=file_detector)
    elif bstack11llll1ll_opy_() >= version.parse(bstack1lll1l1_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧᛈ")):
        bstack11llll1l_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities, options=options,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    elif bstack11llll1ll_opy_() >= version.parse(bstack1lll1l1_opy_ (u"ࠩ࠵࠲࠺࠹࠮࠱ࠩᛉ")):
        bstack11llll1l_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    else:
        bstack11llll1l_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive)
    try:
        bstack1l1l11l1l1_opy_ = bstack1lll1l1_opy_ (u"ࠪࠫᛊ")
        if bstack11llll1ll_opy_() >= version.parse(bstack1lll1l1_opy_ (u"ࠫ࠹࠴࠰࠯࠲ࡥ࠵ࠬᛋ")):
            bstack1l1l11l1l1_opy_ = self.caps.get(bstack1lll1l1_opy_ (u"ࠧࡵࡰࡵ࡫ࡰࡥࡱࡎࡵࡣࡗࡵࡰࠧᛌ"))
        else:
            bstack1l1l11l1l1_opy_ = self.capabilities.get(bstack1lll1l1_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡱࡦࡲࡈࡶࡤࡘࡶࡱࠨᛍ"))
        if bstack1l1l11l1l1_opy_:
            bstack11l1lllll_opy_(bstack1l1l11l1l1_opy_)
            if bstack11llll1ll_opy_() <= version.parse(bstack1lll1l1_opy_ (u"ࠧ࠴࠰࠴࠷࠳࠶ࠧᛎ")):
                self.command_executor._url = bstack1lll1l1_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤᛏ") + bstack111111ll_opy_ + bstack1lll1l1_opy_ (u"ࠤ࠽࠼࠵࠵ࡷࡥ࠱࡫ࡹࡧࠨᛐ")
            else:
                self.command_executor._url = bstack1lll1l1_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠧᛑ") + bstack1l1l11l1l1_opy_ + bstack1lll1l1_opy_ (u"ࠦ࠴ࡽࡤ࠰ࡪࡸࡦࠧᛒ")
            logger.debug(bstack1ll1l111_opy_.format(bstack1l1l11l1l1_opy_))
        else:
            logger.debug(bstack1l1l1l1ll_opy_.format(bstack1lll1l1_opy_ (u"ࠧࡕࡰࡵ࡫ࡰࡥࡱࠦࡈࡶࡤࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩࠨᛓ")))
    except Exception as e:
        logger.debug(bstack1l1l1l1ll_opy_.format(e))
    bstack111l1llll_opy_ = self.session_id
    if bstack1lll1l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ᛔ") in bstack1ll11l1l11_opy_:
        threading.current_thread().bstackSessionId = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        item = store.get(bstack1lll1l1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫᛕ"), None)
        if item:
            bstack1lllll11l1l_opy_ = getattr(item, bstack1lll1l1_opy_ (u"ࠨࡡࡷࡩࡸࡺ࡟ࡤࡣࡶࡩࡤࡹࡴࡢࡴࡷࡩࡩ࠭ᛖ"), False)
            if not getattr(item, bstack1lll1l1_opy_ (u"ࠩࡢࡨࡷ࡯ࡶࡦࡴࠪᛗ"), None) and bstack1lllll11l1l_opy_:
                setattr(store[bstack1lll1l1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧᛘ")], bstack1lll1l1_opy_ (u"ࠫࡤࡪࡲࡪࡸࡨࡶࠬᛙ"), self)
        bstack1l1ll11l_opy_.bstack1l1l1l111l_opy_(self)
    bstack1l1ll1ll1_opy_.append(self)
    if bstack1lll1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨᛚ") in CONFIG and bstack1lll1l1_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫᛛ") in CONFIG[bstack1lll1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪᛜ")][bstack1111l111_opy_]:
        bstack1lll111ll1_opy_ = CONFIG[bstack1lll1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫᛝ")][bstack1111l111_opy_][bstack1lll1l1_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧᛞ")]
    logger.debug(bstack1ll1l11ll_opy_.format(bstack111l1llll_opy_))
def bstack1l1lll1l_opy_(self, url):
    global bstack1llllll1ll_opy_
    global CONFIG
    try:
        bstack1111l1l11_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack1lllll1lll_opy_.format(str(err)))
    try:
        bstack1llllll1ll_opy_(self, url)
    except Exception as e:
        try:
            bstack1l11ll11_opy_ = str(e)
            if any(err_msg in bstack1l11ll11_opy_ for err_msg in bstack1l1l1111_opy_):
                bstack1111l1l11_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack1lllll1lll_opy_.format(str(err)))
        raise e
def bstack1l1lllll1l_opy_(item, when):
    global bstack11ll1l111_opy_
    try:
        bstack11ll1l111_opy_(item, when)
    except Exception as e:
        pass
def bstack1lll1lll11_opy_(item, call, rep):
    global bstack1l1l1111l1_opy_
    global bstack1l1ll1ll1_opy_
    name = bstack1lll1l1_opy_ (u"ࠪࠫᛟ")
    try:
        if rep.when == bstack1lll1l1_opy_ (u"ࠫࡨࡧ࡬࡭ࠩᛠ"):
            bstack111l1llll_opy_ = threading.current_thread().bstackSessionId
            bstack1llll1l11l1_opy_ = item.config.getoption(bstack1lll1l1_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧᛡ"))
            try:
                if (str(bstack1llll1l11l1_opy_).lower() != bstack1lll1l1_opy_ (u"࠭ࡴࡳࡷࡨࠫᛢ")):
                    name = str(rep.nodeid)
                    bstack1ll111111_opy_ = bstack1lll1ll1l_opy_(bstack1lll1l1_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨᛣ"), name, bstack1lll1l1_opy_ (u"ࠨࠩᛤ"), bstack1lll1l1_opy_ (u"ࠩࠪᛥ"), bstack1lll1l1_opy_ (u"ࠪࠫᛦ"), bstack1lll1l1_opy_ (u"ࠫࠬᛧ"))
                    os.environ[bstack1lll1l1_opy_ (u"ࠬࡖ࡙ࡕࡇࡖࡘࡤ࡚ࡅࡔࡖࡢࡒࡆࡓࡅࠨᛨ")] = name
                    for driver in bstack1l1ll1ll1_opy_:
                        if bstack111l1llll_opy_ == driver.session_id:
                            driver.execute_script(bstack1ll111111_opy_)
            except Exception as e:
                logger.debug(bstack1lll1l1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠠࡧࡱࡵࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡵࡨࡷࡸ࡯࡯࡯࠼ࠣࡿࢂ࠭ᛩ").format(str(e)))
            try:
                bstack1l1l111l11_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack1lll1l1_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨᛪ"):
                    status = bstack1lll1l1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ᛫") if rep.outcome.lower() == bstack1lll1l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ᛬") else bstack1lll1l1_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ᛭")
                    reason = bstack1lll1l1_opy_ (u"ࠫࠬᛮ")
                    if status == bstack1lll1l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᛯ"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack1lll1l1_opy_ (u"࠭ࡩ࡯ࡨࡲࠫᛰ") if status == bstack1lll1l1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᛱ") else bstack1lll1l1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᛲ")
                    data = name + bstack1lll1l1_opy_ (u"ࠩࠣࡴࡦࡹࡳࡦࡦࠤࠫᛳ") if status == bstack1lll1l1_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᛴ") else name + bstack1lll1l1_opy_ (u"ࠫࠥ࡬ࡡࡪ࡮ࡨࡨࠦࠦࠧᛵ") + reason
                    bstack11l11ll1l_opy_ = bstack1lll1ll1l_opy_(bstack1lll1l1_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧᛶ"), bstack1lll1l1_opy_ (u"࠭ࠧᛷ"), bstack1lll1l1_opy_ (u"ࠧࠨᛸ"), bstack1lll1l1_opy_ (u"ࠨࠩ᛹"), level, data)
                    for driver in bstack1l1ll1ll1_opy_:
                        if bstack111l1llll_opy_ == driver.session_id:
                            driver.execute_script(bstack11l11ll1l_opy_)
            except Exception as e:
                logger.debug(bstack1lll1l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡣࡰࡰࡷࡩࡽࡺࠠࡧࡱࡵࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡵࡨࡷࡸ࡯࡯࡯࠼ࠣࡿࢂ࠭᛺").format(str(e)))
    except Exception as e:
        logger.debug(bstack1lll1l1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡵࡣࡷࡩࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺࡥࡴࡶࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࢀࢃࠧ᛻").format(str(e)))
    bstack1l1l1111l1_opy_(item, call, rep)
notset = Notset()
def bstack1ll1lll11_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack1lll111l11_opy_
    if str(name).lower() == bstack1lll1l1_opy_ (u"ࠫࡩࡸࡩࡷࡧࡵࠫ᛼"):
        return bstack1lll1l1_opy_ (u"ࠧࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠦ᛽")
    else:
        return bstack1lll111l11_opy_(self, name, default, skip)
def bstack11l111ll_opy_(self):
    global CONFIG
    global bstack1l1ll11l11_opy_
    try:
        proxy = bstack11lll1l11_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack1lll1l1_opy_ (u"࠭࠮ࡱࡣࡦࠫ᛾")):
                proxies = bstack1l1111l11_opy_(proxy, bstack1lll11111_opy_())
                if len(proxies) > 0:
                    protocol, bstack11l11111l_opy_ = proxies.popitem()
                    if bstack1lll1l1_opy_ (u"ࠢ࠻࠱࠲ࠦ᛿") in bstack11l11111l_opy_:
                        return bstack11l11111l_opy_
                    else:
                        return bstack1lll1l1_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤᜀ") + bstack11l11111l_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack1lll1l1_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡶࡲࡰࡺࡼࠤࡺࡸ࡬ࠡ࠼ࠣࡿࢂࠨᜁ").format(str(e)))
    return bstack1l1ll11l11_opy_(self)
def bstack1ll11llll1_opy_():
    return (bstack1lll1l1_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ᜂ") in CONFIG or bstack1lll1l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨᜃ") in CONFIG) and bstack1l1l11l111_opy_() and bstack11llll1ll_opy_() >= version.parse(
        bstack1llll1l1l1_opy_)
def bstack1l111l1l_opy_(self,
               executablePath=None,
               channel=None,
               args=None,
               ignoreDefaultArgs=None,
               handleSIGINT=None,
               handleSIGTERM=None,
               handleSIGHUP=None,
               timeout=None,
               env=None,
               headless=None,
               devtools=None,
               proxy=None,
               downloadsPath=None,
               slowMo=None,
               tracesDir=None,
               chromiumSandbox=None,
               firefoxUserPrefs=None
               ):
    global CONFIG
    global bstack1lll111ll1_opy_
    global bstack1l1l1lll1l_opy_
    global bstack1ll11l1l11_opy_
    CONFIG[bstack1lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧᜄ")] = str(bstack1ll11l1l11_opy_) + str(__version__)
    bstack1111l111_opy_ = 0
    try:
        if bstack1l1l1lll1l_opy_ is True:
            bstack1111l111_opy_ = int(os.environ.get(bstack1lll1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᜅ")))
    except:
        bstack1111l111_opy_ = 0
    CONFIG[bstack1lll1l1_opy_ (u"ࠢࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨᜆ")] = True
    bstack1llllll1l_opy_ = bstack1l1llllll1_opy_(CONFIG, bstack1111l111_opy_)
    logger.debug(bstack1111l1ll_opy_.format(str(bstack1llllll1l_opy_)))
    if CONFIG.get(bstack1lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬᜇ")):
        bstack111ll11l_opy_(bstack1llllll1l_opy_, bstack11l1lll11_opy_)
    if bstack1lll1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬᜈ") in CONFIG and bstack1lll1l1_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨᜉ") in CONFIG[bstack1lll1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧᜊ")][bstack1111l111_opy_]:
        bstack1lll111ll1_opy_ = CONFIG[bstack1lll1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨᜋ")][bstack1111l111_opy_][bstack1lll1l1_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫᜌ")]
    import urllib
    import json
    bstack1l1l1l1l1_opy_ = bstack1lll1l1_opy_ (u"ࠧࡸࡵࡶ࠾࠴࠵ࡣࡥࡲ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࡂࡧࡦࡶࡳ࠾ࠩᜍ") + urllib.parse.quote(json.dumps(bstack1llllll1l_opy_))
    browser = self.connect(bstack1l1l1l1l1_opy_)
    return browser
def bstack1l1111l1l_opy_():
    global bstack1ll111l1ll_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        BrowserType.launch = bstack1l111l1l_opy_
        bstack1ll111l1ll_opy_ = True
    except Exception as e:
        pass
def bstack1llll1l111l_opy_():
    global CONFIG
    global bstack1lll1111l_opy_
    global bstack111111ll_opy_
    global bstack11l1lll11_opy_
    global bstack1l1l1lll1l_opy_
    CONFIG = json.loads(os.environ.get(bstack1lll1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍࠧᜎ")))
    bstack1lll1111l_opy_ = eval(os.environ.get(bstack1lll1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪᜏ")))
    bstack111111ll_opy_ = os.environ.get(bstack1lll1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡋ࡙ࡇࡥࡕࡓࡎࠪᜐ"))
    bstack1l11l1ll_opy_(CONFIG, bstack1lll1111l_opy_)
    bstack1l1l11l1_opy_()
    global bstack11llll1l_opy_
    global bstack1l11l1111_opy_
    global bstack1l11111l1_opy_
    global bstack1111lll1_opy_
    global bstack1ll1l1111_opy_
    global bstack1l1ll1l1l1_opy_
    global bstack1lll1l1l1_opy_
    global bstack1llllll1ll_opy_
    global bstack1l1ll11l11_opy_
    global bstack1lll111l11_opy_
    global bstack11ll1l111_opy_
    global bstack1l1l1111l1_opy_
    try:
        from selenium import webdriver
        from selenium.webdriver.remote.webdriver import WebDriver
        bstack11llll1l_opy_ = webdriver.Remote.__init__
        bstack1l11l1111_opy_ = WebDriver.quit
        bstack1lll1l1l1_opy_ = WebDriver.close
        bstack1llllll1ll_opy_ = WebDriver.get
    except Exception as e:
        pass
    if (bstack1lll1l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧᜑ") in CONFIG or bstack1lll1l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩᜒ") in CONFIG) and bstack1l1l11l111_opy_():
        if bstack11llll1ll_opy_() < version.parse(bstack1llll1l1l1_opy_):
            logger.error(bstack11111l11_opy_.format(bstack11llll1ll_opy_()))
        else:
            try:
                from selenium.webdriver.remote.remote_connection import RemoteConnection
                bstack1l1ll11l11_opy_ = RemoteConnection._get_proxy_url
            except Exception as e:
                logger.error(bstack11lll111_opy_.format(str(e)))
    try:
        from _pytest.config import Config
        bstack1lll111l11_opy_ = Config.getoption
        from _pytest import runner
        bstack11ll1l111_opy_ = runner._update_current_test_var
    except Exception as e:
        logger.warn(e, bstack1l1llll1ll_opy_)
    try:
        from pytest_bdd import reporting
        bstack1l1l1111l1_opy_ = reporting.runtest_makereport
    except Exception as e:
        logger.debug(bstack1lll1l1_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹࡵࠠࡳࡷࡱࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡨࡷࡹࡹࠧᜓ"))
    bstack11l1lll11_opy_ = CONFIG.get(bstack1lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶ᜔ࠫ"), {}).get(bstack1lll1l1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴ᜕ࠪ"))
    bstack1l1l1lll1l_opy_ = True
    bstack1lll11lll_opy_(bstack1111ll11l_opy_)
if (bstack11l1l1ll11_opy_()):
    bstack1llll1l111l_opy_()
@bstack1l11l11lll_opy_(class_method=False)
def bstack1lllll11l11_opy_(hook_name, event, bstack1llll1l11ll_opy_=None):
    if hook_name not in [bstack1lll1l1_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡨࡸࡲࡨࡺࡩࡰࡰࠪ᜖"), bstack1lll1l1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧ᜗"), bstack1lll1l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠪ᜘"), bstack1lll1l1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠧ᜙"), bstack1lll1l1_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡩ࡬ࡢࡵࡶࠫ᜚"), bstack1lll1l1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡦࡰࡦࡹࡳࠨ᜛"), bstack1lll1l1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧ᜜"), bstack1lll1l1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠫ᜝")]:
        return
    node = store[bstack1lll1l1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧ᜞")]
    if hook_name in [bstack1lll1l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠪᜟ"), bstack1lll1l1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠧᜠ")]:
        node = store[bstack1lll1l1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟࡮ࡱࡧࡹࡱ࡫࡟ࡪࡶࡨࡱࠬᜡ")]
    elif hook_name in [bstack1lll1l1_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡣ࡭ࡣࡶࡷࠬᜢ"), bstack1lll1l1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡧࡱࡧࡳࡴࠩᜣ")]:
        node = store[bstack1lll1l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡧࡱࡧࡳࡴࡡ࡬ࡸࡪࡳࠧᜤ")]
    if event == bstack1lll1l1_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪᜥ"):
        hook_type = bstack1111l11l11_opy_(hook_name)
        uuid = uuid4().__str__()
        bstack1l111l1111_opy_ = {
            bstack1lll1l1_opy_ (u"ࠫࡺࡻࡩࡥࠩᜦ"): uuid,
            bstack1lll1l1_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᜧ"): bstack11llll1l1_opy_(),
            bstack1lll1l1_opy_ (u"࠭ࡴࡺࡲࡨࠫᜨ"): bstack1lll1l1_opy_ (u"ࠧࡩࡱࡲ࡯ࠬᜩ"),
            bstack1lll1l1_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫᜪ"): hook_type,
            bstack1lll1l1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟࡯ࡣࡰࡩࠬᜫ"): hook_name
        }
        store[bstack1lll1l1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧᜬ")].append(uuid)
        bstack1lllll111l1_opy_ = node.nodeid
        if hook_type == bstack1lll1l1_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠩᜭ"):
            if not _1l11ll11ll_opy_.get(bstack1lllll111l1_opy_, None):
                _1l11ll11ll_opy_[bstack1lllll111l1_opy_] = {bstack1lll1l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫᜮ"): []}
            _1l11ll11ll_opy_[bstack1lllll111l1_opy_][bstack1lll1l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᜯ")].append(bstack1l111l1111_opy_[bstack1lll1l1_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᜰ")])
        _1l11ll11ll_opy_[bstack1lllll111l1_opy_ + bstack1lll1l1_opy_ (u"ࠨ࠯ࠪᜱ") + hook_name] = bstack1l111l1111_opy_
        bstack1llll1ll111_opy_(node, bstack1l111l1111_opy_, bstack1lll1l1_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪᜲ"))
    elif event == bstack1lll1l1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࠩᜳ"):
        bstack1l11111ll1_opy_ = node.nodeid + bstack1lll1l1_opy_ (u"ࠫ࠲᜴࠭") + hook_name
        _1l11ll11ll_opy_[bstack1l11111ll1_opy_][bstack1lll1l1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ᜵")] = bstack11llll1l1_opy_()
        bstack1llll1lll11_opy_(_1l11ll11ll_opy_[bstack1l11111ll1_opy_][bstack1lll1l1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ᜶")])
        bstack1llll1ll111_opy_(node, _1l11ll11ll_opy_[bstack1l11111ll1_opy_], bstack1lll1l1_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ᜷"), bstack1llll1l1l1l_opy_=bstack1llll1l11ll_opy_)
def bstack1llll1l1ll1_opy_():
    global bstack1llll11llll_opy_
    if bstack1lll1ll1_opy_():
        bstack1llll11llll_opy_ = bstack1lll1l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠬ᜸")
    else:
        bstack1llll11llll_opy_ = bstack1lll1l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ᜹")
@bstack1l1ll11l_opy_.bstack1llllll1ll1_opy_
def bstack1llll111lll_opy_():
    bstack1llll1l1ll1_opy_()
    if bstack1l1l11l111_opy_():
        bstack11l111lll_opy_(bstack11ll1111_opy_)
    bstack11l1111lll_opy_ = bstack11l111lll1_opy_(bstack1lllll11l11_opy_)
bstack1llll111lll_opy_()