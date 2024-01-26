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
import threading
bstack1111l11111_opy_ = 1000
bstack11111ll1ll_opy_ = 5
bstack1111l1111l_opy_ = 30
bstack11111ll1l1_opy_ = 2
class bstack11111lllll_opy_:
    def __init__(self, handler, bstack11111ll111_opy_=bstack1111l11111_opy_, bstack11111lll11_opy_=bstack11111ll1ll_opy_):
        self.queue = []
        self.handler = handler
        self.bstack11111ll111_opy_ = bstack11111ll111_opy_
        self.bstack11111lll11_opy_ = bstack11111lll11_opy_
        self.lock = threading.Lock()
        self.timer = None
    def start(self):
        if not self.timer:
            self.bstack11111l1lll_opy_()
    def bstack11111l1lll_opy_(self):
        self.timer = threading.Timer(self.bstack11111lll11_opy_, self.bstack11111llll1_opy_)
        self.timer.start()
    def bstack1111l111l1_opy_(self):
        self.timer.cancel()
    def bstack11111ll11l_opy_(self):
        self.bstack1111l111l1_opy_()
        self.bstack11111l1lll_opy_()
    def add(self, event):
        with self.lock:
            self.queue.append(event)
            if len(self.queue) >= self.bstack11111ll111_opy_:
                t = threading.Thread(target=self.bstack11111llll1_opy_)
                t.start()
                self.bstack11111ll11l_opy_()
    def bstack11111llll1_opy_(self):
        if len(self.queue) <= 0:
            return
        data = self.queue[:self.bstack11111ll111_opy_]
        del self.queue[:self.bstack11111ll111_opy_]
        self.handler(data)
    def shutdown(self):
        self.bstack1111l111l1_opy_()
        while len(self.queue) > 0:
            self.bstack11111llll1_opy_()