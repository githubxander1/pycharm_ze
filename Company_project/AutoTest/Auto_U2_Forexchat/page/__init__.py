import uiautomator2 as u2
d=u2.connect('127.0.0.1:21513')


EditGroupProfile=d(description="编辑群资料")
Description=d.xpath('//*[contains(@content-desc,"群介绍")]')
Input=d(text='请输入群介绍')
Cancel=d.xpath('//*[contains(@content-desc,"编辑群介绍")]/android.widget.ImageView[1]')
Sure=d.xpath('//*[@content-desc="确定"]')