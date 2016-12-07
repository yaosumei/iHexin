# -*- coding: utf-8 -*-
from time import sleep
from page_object.appium_page_objects import page_element
from pages.fenshikxian.fenshiKxian_page import FenshiKxianPage
from pages.public.denglu_page import DengluPage
from pages.public.public_method import PublicMethod
from pages.public.public_page import PublicPage
from pages.public.searchStock_page import SearchStockPage
from pages.shouye.home_page import HomePage
from pages.zixuangu.bianjizixuan_page import BianjizixuanPage
from pages.zixuangu.kanZhulizijin_page import KanZhulizijinPage
from pages.zixuangu.optional_page import OptionalPage
from pages.zixuangu.tianjiazixuan_page import TianjiazixuanPage
from pages.zixuangu.wodezichan_page import WodezichanPage
from pages.zixuangu.zixuanDapan_page import ZixuanDapanPage
from pages.zixuangu.zixuangufenzu_page import ZixuangufenzuPage
from pages.zixuangu.zixuangugonggao_page import ZixuangugonggaoPage
from pages.zixuangu.zixuanguxinwen_page import ZixuanguxinwenPage
from pages.zixuangu.zixun_page import ZixunPage
from pages.index_page import IndexPage
from pages.public.denglu_page import DengluPage
from pages.gerenzhongxin.gerenzhongxin_page import GerenzhongxinPage
from appium.webdriver.common.touch_action import TouchAction

# 登录
def test_step1(driver):
    home_page = HomePage(driver)
    denglu_page = DengluPage(driver)

    if not home_page.button_337705299:
        denglu_page.sign_in('337705299', '123456')
    assert home_page.button_337705299
    assert home_page.feivip_button
    assert home_page.qiehuanyejianmoshi_button
    assert home_page.sousuo_button
"""
# 首页－>自选页面
def test_step2(driver):
    optional_page = OptionalPage(driver)
    public_page = PublicPage(driver)
    public_method = PublicMethod(driver)
    bianjizixuan_page = BianjizixuanPage(driver)

    public_page.zixuan_button.click()
    assert optional_page.zixuan_staticText
    assert optional_page.tongbuzixuangu_btn
    assert optional_page.duoshoujiPCtongbu_staText

    public_method.public_tap_element(optional_page.bianji_button)
    assert bianjizixuan_page.cell001_stock_staText.text == u'上证指数'
    assert bianjizixuan_page.cell002_stock_staText.text == u'创业板指'
    assert bianjizixuan_page.cell003_stock_staText.text == u'同花顺'
    bianjizixuan_page.fanhui_button.click()

# 自选－>看主力资金
def test_step3(driver):
    optional_page = OptionalPage(driver)
    kanzhulizijin_page = KanZhulizijinPage(driver)
    public_page = PublicPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    public_method = PublicMethod(driver)

    public_page.zixuan_button.click()
    optional_page.zijin_btn.click()
    sleep(1)
    assert kanzhulizijin_page.kanzhulizijin_staticText
    assert kanzhulizijin_page.gengduo_button
    assert kanzhulizijin_page.zixuan_btn

    # step4 点击更多按钮
    #kanzhulizijin_page.gengduo_button.click()
    # step5
    # 点击更多旁边的删除按钮和引导图差不多,只会出现一次,以后在做

    # step6  点击沪深按钮
    kanzhulizijin_page.hushen_btn.click()
    assert not kanzhulizijin_page.zixuangushunxu_btn
    # 判断列表不为空
    kanzhulizijin_page.hx_ergodic_hushen_zhibiao()
    # step7 上滑动
    kanzhulizijin_page.hx_upglide()
    # step8 下滑动
    kanzhulizijin_page.hx_glide()
    kanzhulizijin_page.hx_glide()
    # 左右滑
    for n in range(4):
        kanzhulizijin_page.hx_left()
    for n in range(3):
        kanzhulizijin_page.hx_right()
    # step11-18
    kanzhulizijin_page.cell001.click()
    fenshikxian_page.change_gupiao(5)
    fenshikxian_page.fanhui_button.click()
    # 点击行业按钮
    kanzhulizijin_page.hangye_btn.click()
    kanzhulizijin_page.hx_ergodic_zhibiao()
    # step7 上滑动
    kanzhulizijin_page.hx_upglide()
    # step8 下滑动
    kanzhulizijin_page.hx_glide()
    kanzhulizijin_page.hx_glide()
    # 左右滑
    for n in range(4):
        kanzhulizijin_page.hx_left()
    for n in range(3):
        kanzhulizijin_page.hx_right()
    sleep(1)
    kanzhulizijin_page.cell001.click()
    sleep(1)
    fenshikxian_page.change_gupiao(5)
    fenshikxian_page.fanhui_button.click()
    # 点击概念按钮
    kanzhulizijin_page.gainian_btn.click()
    kanzhulizijin_page.hx_ergodic_zhibiao()
    # step7 上滑动
    kanzhulizijin_page.hx_upglide()
    # step8 下滑动
    kanzhulizijin_page.hx_glide()
    kanzhulizijin_page.hx_glide()
    # 左右滑
    for n in range(4):
        kanzhulizijin_page.hx_left()
    for n in range(3):
        kanzhulizijin_page.hx_right()
    sleep(1)
    kanzhulizijin_page.cell001.click()
    sleep(1)
    fenshikxian_page.change_gupiao(5)
    fenshikxian_page.fanhui_button.click()

    kanzhulizijin_page.fanhui_btn.click()

# 自选－> 资产页面
def test_step19(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    wodezichan_page = WodezichanPage(driver)
    public_page.zixuan_button.click()
    optional_page.zichan_btn.click()
    # step20 返回
    assert wodezichan_page.wodezichan_staText
    wodezichan_page.fanhui_btn.click()

# 自选－> 沪,深,创大盘页面
def test_step21(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    zixuanDapan_page = ZixuanDapanPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)

    public_page.zixuan_button.click()
    # step22-40

    optional_page.zixuanIndexItemName_staText.click()
    zixuanDapan_page.shen_btn.click()
    zixuanDapan_page.chuang_btn.click()
    zixuanDapan_page.hx_left()

    zixuanDapan_page.shen_btn.click()
    zixuanDapan_page.hu_btn.click()
    zixuanDapan_page.hx_right()
    sleep(1)
    zixuanDapan_page.hx_tapblank()
    optional_page.zixuanIndexItemName_staText.click()
    zixuanDapan_page.shen_btn.click()
    zixuanDapan_page.hx_tapblank()
    optional_page.zixuanIndexItemName_staText.click()
    zixuanDapan_page.chuang_btn.click()
    zixuanDapan_page.hx_tapblank()

    optional_page.zixuanIndexItemName_staText.click()
    zixuanDapan_page.fenshitu_scr.click()
    fenshikxian_page.change_gupiao(3)
    fenshikxian_page.fanhui_button.click()

# 自选－> 编辑自选－> 添加股票
def test_step41(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    bianjizixuan_page = BianjizixuanPage(driver)
    tianjiazixuan_page = TianjiazixuanPage(driver)
    searchStock_page = SearchStockPage(driver)
    home_page = HomePage(driver)
    public_method = PublicMethod(driver)

    public_page.zixuan_button.click()
    public_method.public_tap_element(optional_page.bianji_button)

    # step42 进入股票搜索页面
    bianjizixuan_page.tianjiagupiao_button.click()
    sleep(1)

    # step43-45 输入股票代码 添加自选股
    stocks = [('AU9999', 'addHJ9999_btn'), ('600000', 'addPFYH_btn'), ('000001', 'addPAYH_btn'),
              ('900901', 'addYSBG_btn'), ('200011', 'addSWYB_btn'), ('010107', 'add21GZ_btn'),
              ('100213', 'addGZ0213_btn'), ('500058', 'addJJYF_btn'), ('150008', 'addRHXK_btn'),
              ('400002', 'addCB5_btn'), ('399001', 'addSZCZ_btn'), ('dji', 'addDQS_btn'), ('BIDU', 'addBD_btn'),
              ('510050', 'add50ETF_btn'), ('TJAG00', 'addY15_btn'), ('00001', 'addCH_btn'), ('hsi', 'addHSZS_btn')]
    for stockCode, stockName in stocks:
        print stockCode, stockName
        searchStock_page.hx_send_keys(stockCode)
        try:
            eval('tianjiazixuan_page.{}.click()'.format(stockName))
        except:
            print '该股票已添加过'
        tianjiazixuan_page.qingchuwenben_button.click()
    # step 46 返回编辑自选页面
    tianjiazixuan_page.fanhui_button.click()
    sleep(1)
    # step 47 返回自选页面
    bianjizixuan_page.fanhui_button.click()
    sleep(1)

    public_method.public_tap_element(optional_page.bianji_button)
   #对添加的股票进行判断
    assert optional_page.HSZS_stock_staText
    assert optional_page.CH_stock_staText
    assert optional_page.Y15_stock_staText
    assert optional_page.ETF50_stock_staText
    assert optional_page.BD_stock_staText
    assert optional_page.DQS_stock_staText
    assert optional_page.SZCZ_stock_staText
    assert optional_page.CB5_stock_staText
    assert optional_page.RHXK_stock_staText
    assert optional_page.JJYF_stock_staText
    assert optional_page.GZ0213_stock_staText
    assert optional_page.GZ217_stock_staText
    assert optional_page.SWYB_stock_staText
    assert optional_page.YSBG_stock_staText
    assert optional_page.PAYH_stock_staText
    assert optional_page.PFYH_stock_staText
    assert optional_page.HJ9999_stock_staText

    bianjizixuan_page.fanhui_button.click()

#编辑自选
def test_step49(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    bianjizixuan_page = BianjizixuanPage(driver)
    public_method = PublicMethod(driver)


    # step 49 点击自选
    public_page.zixuan_button.click()

    # step50-52
    public_method.public_tap_element(optional_page.bianji_button)
    bianjizixuan_page.hx_upglide()
    bianjizixuan_page.hx_upglide()
    sleep(1)

    # 置顶三次操作
    lenth = public_method.public_getlength()
    if lenth > 1:
        for n in range(3):
            eval('driver.find_element_by_xpath'
                 '("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[{0}]/UIAButton[2]").click()'.format(
                lenth))
            #bianjizixuan_page.cell020_zhiding_btn.click()
            sleep(1)
    # 第一条为上证指数
    bianjizixuan_page.hx_glide()
    sleep(1)
    bianjizixuan_page.fanhui_button.click()

    public_method.public_tap_element(optional_page.bianji_button)
    sleep(1)

    assert bianjizixuan_page.cell001_stock_staText.text == u'上证指数'
    assert bianjizixuan_page.cell002_stock_staText.text == u'创业板指'
    assert bianjizixuan_page.cell003_stock_staText.text == u'同花顺'

    bianjizixuan_page.fanhui_button.click()

#自选－> 编辑自选－> 拖动股票
def test_step53(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    bianjizixuan_page = BianjizixuanPage(driver)
    public_method = PublicMethod(driver)

    # step 49 点击自选
    public_page.zixuan_button.click()
    public_method.public_tap_element(optional_page.bianji_button)

    action1 = TouchAction(driver)
    action1.press(bianjizixuan_page.cell002_tuodong_btn).wait(100).move_to(bianjizixuan_page.cell001_tuodong_btn).wait(
        100).release()
    action1.perform()
    action2 = TouchAction(driver)
    action2.press(bianjizixuan_page.cell003_tuodong_btn).wait(100).move_to(bianjizixuan_page.cell001_tuodong_btn).wait(
        100).release()
    action2.perform()
    sleep(1)

    bianjizixuan_page.fanhui_button.click()
    sleep(1)

    public_method.public_tap_element(optional_page.bianji_button)

    assert bianjizixuan_page.cell001_stock_staText.text == u'同花顺'
    assert bianjizixuan_page.cell002_stock_staText.text == u'创业板指'
    assert bianjizixuan_page.cell003_stock_staText.text == u'上证指数'

    bianjizixuan_page.fanhui_button.click()

# 删除前三支股票
def test_step(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    bianjizixuan_page = BianjizixuanPage(driver)
    public_method = PublicMethod(driver)

    # step 49 点击自选
    public_page.zixuan_button.click()
    public_method.public_tap_element(optional_page.bianji_button)

    # 删除前三支股票
    bianjizixuan_page.cell001_btn.click()
    bianjizixuan_page.cell002_btn.click()
    bianjizixuan_page.cell003_btn.click()
    bianjizixuan_page.shanchu_button.click()
    # step55
    bianjizixuan_page.fanhui_button.click()

#搜索添加股票
def test_step56(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    searchStock_page = SearchStockPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    bianjizixuan_page = BianjizixuanPage(driver)
    public_method = PublicMethod(driver)

    # step 49 点击自选
    public_page.zixuan_button.click()

    # step56-66
    optional_page.sousuo_button.click()
    sleep(1)
    searchStock_page.hx_send_keys('1A0001')
    try:
        searchStock_page.zixuanadd_button.click()
    except:
        print '该股票上证指数已添加过'
    searchStock_page.qingchuwenben_button.click()
    searchStock_page.hx_send_keys('399006')
    sleep(2)
    try:
        fenshikxian_page.jiazixuan_staText.click()
    except:
        print '该股票创业板指已添加过'
    fenshikxian_page.fanhui_button.click()
    optional_page.sousuo_button.click()
    sleep(1)
    searchStock_page.hx_send_keys('300033')
    sleep(2)
    try:
        fenshikxian_page.jiazixuan_staText.click()
    except:
        print '该股票同花顺已添加过'
    fenshikxian_page.fanhui_button.click()

    public_page.zixuan_button.click()
    public_method.public_tap_element(optional_page.bianji_button)

    assert bianjizixuan_page.cell001_stock_staText.text == u'同花顺'
    assert bianjizixuan_page.cell002_stock_staText.text == u'创业板指'
    assert bianjizixuan_page.cell003_stock_staText.text == u'上证指数'

    bianjizixuan_page.fanhui_button.click()

# 看主力资金
def test_step067_71(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    kanzhulizijin_page = KanZhulizijinPage(driver)

    public_page.zixuan_button.click()
    optional_page.zijin_btn.click()
    kanzhulizijin_page.hx_ergodic_hushen_zhibiao()

    # step 72
    kanzhulizijin_page.pageGotoFenshikxian()
    kanzhulizijin_page.fanhui_btn.click()

# 新闻
def test_step78_88(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    zixuanguxinwen_page = ZixuanguxinwenPage(driver)
    zixun_page = ZixunPage(driver)

    public_page.zixuan_button.click()
    optional_page.xinwen_btn.click()
    assert zixuanguxinwen_page.zixuanguxinwen_staText

    zixuanguxinwen_page.hx_upglide()
    zixuanguxinwen_page.hx_downglide()
    zixuanguxinwen_page.hx_downglide()
    zixuanguxinwen_page.cell01.click()
    zixun_page.fanhui_btn.click()
    zixuanguxinwen_page.yanbao_btn.click()
    zixuanguxinwen_page.hx_upglide()
    zixuanguxinwen_page.hx_downglide()
    zixuanguxinwen_page.hx_downglide()
    zixuanguxinwen_page.cell01.click()
    zixun_page.fanhui_btn.click()
    zixuanguxinwen_page.fanhui_btn.click()

#自选股公告
def test_step90(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    zixuangugonggao_page = ZixuangugonggaoPage(driver)
    zixun_page = ZixunPage(driver)

    public_page.zixuan_button.click()
    optional_page.gonggao_btn.click()
    assert zixuangugonggao_page.zixuangugonggao_staText.text == u'自选股公告'
    # step 90-96
    zixuangugonggao_page.hx_upglide()
    zixuangugonggao_page.hx_downglide()
    zixuangugonggao_page.hx_downglide()
    zixuangugonggao_page.cell01.click()
    zixun_page.fanhui_btn.click()
    zixuangugonggao_page.fanhui_btn.click()

#自选页面上下滑动及排序，进入个股分时页面切换股票
def test_step97(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)

    public_page.zixuan_button.click()

    # 自选列表排序操作
    optional_page.hx_zixuan_ergodic()
    #step 97-98
    #  上下滑
    optional_page.hx_upglide()
    optional_page.hx_glide()
    optional_page.hx_glide()
    # step99-100
    # 左右滑
    optional_page.hx_right()
    optional_page.hx_left()
    sleep(1)

    #step 106点击个股进入分时并切换股票
    optional_page.pageGotoFenshikxian()
    sleep(1)

#长按操作
def t_step114(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)

    public_page.zixuan_button.click()

    optional_page.zuixin_staText.click()
    optional_page.hx_longPress(optional_page.cell001)
    optional_page.zhidi_btn.click()
    # 待扩展
    optional_page.quxiaopaixu_btn.click()
    optional_page.zuixin_staText.click()
    optional_page.hx_upglide()
    optional_page.hx_longPress(optional_page.cell017)
    optional_page.zhiding_btn.click()
    optional_page.quxiaopaixu_btn.click()
    optional_page.hx_glide()
    optional_page.hx_longPress(optional_page.cell001)
    optional_page.shanchu_btn.click()
    optional_page.hx_longPress(optional_page.cell001)
    optional_page.shanchu_btn.click()

#自选股分组
def test_step136_158(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    zixuangufenzu_page = ZixuangufenzuPage(driver)

    public_page.zixuan_button.click()
    optional_page.fenzu_btn.click()

    # zixuangufenzu_page.xinjianfenzu_btn.click()
    # zixuangufenzu_page.guanbi_btn.click()
    # zixuangufenzu_page.guanlifenzu_btn.clcik()
    # zixuangufenzu_page.guanbi_btn.click()
    zixuangufenzu_page.chakanxiangqing_btn.click()
    sleep(1)
    zixuangufenzu_page.guanbi_btn.click()
    optional_page.zx_left()

    bankuainame = ['bankuai1', 'bankuai2', 'bankuai3', 'bankuai4', 'bankuai5', 'bankuai6', 'bankuai7', 'bankuai8']
    for name in bankuainame:
        optional_page.fenzu_btn.click()
        eval('zixuangufenzu_page.{}_btn.click()'.format(name))
        optional_page.hx_zixuan_ergodic()
        optional_page.pageGotoFenshikxian()

    optional_page.fenzu_btn.click()
    zixuangufenzu_page.zixuangu_btn.click()
    optional_page.zx_right()
    optional_page.zx_left()
    optional_page.fenzu_btn.click()
    zixuangufenzu_page.hx_tapblank()

#10.00.50 自选股新闻公告按照自选股分组分类显示
def tst_step159(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    zixuangufenzu_page = ZixuangufenzuPage(driver)
    zixuanguxinwen_page = ZixuanguxinwenPage(driver)
    zixuangugonggao_page = ZixuangugonggaoPage(driver)
    zixun_page = ZixunPage(driver)

    public_page.zixuan_button.click()

    bankuainame = ['bankuai1', 'bankuai2', 'bankuai3', 'bankuai4', 'bankuai5', 'bankuai6', 'bankuai7', 'bankuai8']
    for name in bankuainame:
        optional_page.fenzu_btn.click()
        eval('zixuangufenzu_page.{}_btn.click()'.format(name))
        optional_page.xinwen_btn.click()
        assert eval('zixuanguxinwen_page.xinwen_{0}_staText'.format(name))
        zixuanguxinwen_page.cell01.click()
        zixun_page.fanhui_btn.click()
        zixuanguxinwen_page.yanbao_btn.click()
        assert eval('zixuanguxinwen_page.yanbao_{0}_staText'.format(name))
        zixuanguxinwen_page.cell01.click()
        zixun_page.fanhui_btn.click()
        zixuanguxinwen_page.fanhui_btn.click()
        optional_page.gonggao_btn.click()
        assert eval('zixuangugonggao_page.gonggao_{0}_staText'.format(name))
        zixuangugonggao_page.cell01.click()
        zixun_page.fanhui_btn.click()
        zixuangugonggao_page.fanhui_btn.click()
    optional_page.fenzu_btn.click()
    zixuangufenzu_page.zixuangu_btn.click()
"""
