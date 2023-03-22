import time
import uiautomator2 as u2

d=u2.connect('127.0.0.1:21513')

Avatar = d(description="群头像")
Name = d.xpath('//*[contains(@content-desc,"群名称")]')
InputGroupName = d(text='请输入群名称')

Description = d.xpath('//*[contains(@content-desc,"群介绍")]')
InputGroupDescription = d(text='请输入群介绍')

Cancel = d.xpath('//*[contains(@content-desc,"编辑群介绍")]/android.widget.ImageView[1]')
Sure = d.xpath('//*[@content-desc="确定"]')