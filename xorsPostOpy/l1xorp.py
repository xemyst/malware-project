# coding: UTF-8
import sys
l1ll_opy_ = sys.version_info [0] == 2
l1l1_opy_ = 2048
l1ll1l_opy_ = 7
def l11l1_opy_ (ll_opy_):
    global l1l_opy_
    l1llll_opy_ = ord (ll_opy_ [-1])
    l111l_opy_ = ll_opy_ [:-1]
    l1l1l_opy_ = l1llll_opy_ % len (l111l_opy_)
    l1l11_opy_ = l111l_opy_ [:l1l1l_opy_] + l111l_opy_ [l1l1l_opy_:]
    if l1ll_opy_:
        l1ll1_opy_ = unicode () .join ([unichr (ord (char) - l1l1_opy_ - (l11ll_opy_ + l1llll_opy_) % l1ll1l_opy_) for l11ll_opy_, char in enumerate (l1l11_opy_)])
    else:
        l1ll1_opy_ = str () .join ([chr (ord (char) - l1l1_opy_ - (l11ll_opy_ + l1llll_opy_) % l1ll1l_opy_) for l11ll_opy_, char in enumerate (l1l11_opy_)])
    return eval (l1ll1_opy_)
l1lll1_opy_ = open(l11l1_opy_ (u"ࠫࡲࡧ࡬ࡸࡣࡵࡩࠬࠀ"),l11l1_opy_ (u"ࠬࡸࡢࠨࠁ"))
l11_opy_ = open(l11l1_opy_ (u"࠭ࡤࡦࡥࡲࡨࡪ࠭ࠂ"), l11l1_opy_ (u"ࠧࡸ࠭ࡥࠫࠃ"))
l1111_opy_ = l1lll1_opy_.read(1)
l1lll_opy_ = 0
l1_opy_ = 7
l111_opy_ = 7
while l1111_opy_ != l11l1_opy_ (u"ࠣࠤࠄ"):
    l1111_opy_ = ord(l1111_opy_)
    l1_opy_ = l1lll_opy_
    if 1 ==1:
      if l1lll_opy_ % 5 ==1:
          l111_opy_ = l1lll_opy_ % 17
          l111_opy_ += 2
          l111_opy_ = l111_opy_ * 4
          l1111_opy_ = l1111_opy_ ^ l111_opy_
      if l1lll_opy_ % 3 ==1:
          l111_opy_ = l1lll_opy_ % 19
          l111_opy_ += 2
          l111_opy_ = l111_opy_ * 5
          l1111_opy_ = l1111_opy_ ^ l111_opy_
      if l1lll_opy_ % 2 ==1:
          l111_opy_ = l1lll_opy_ % 47
          l111_opy_ += 2
          l111_opy_ = l111_opy_ * 2
          l1111_opy_ = l1111_opy_ ^ l111_opy_
      else:
          l111_opy_ = l1lll_opy_ % 31
          l111_opy_ += 2
          l111_opy_ = l111_opy_ + 6
          l1111_opy_ = l1111_opy_ ^ l111_opy_
    l11_opy_.write(l11l1_opy_ (u"ࠩࠨࡧࠬࠅ") % l1111_opy_)
    l1111_opy_ = l1lll1_opy_.read(1)
    l1lll_opy_ += 1
l11_opy_.close()