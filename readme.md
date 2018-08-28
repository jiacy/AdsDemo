#功能说明
- 进入指定APP，在Feed流页面滑动截屏 指定次数
- 使用框架https://github.com/openatx/uiautomator2
#使用说明
- 在config.py中配置pkg_name和swipe_times
- 运行runner.py
- 运行结束查看screenshot目录中的截图，截图以时间戳命名
#环境配置,
- 安装uiautomator2
```angular2html
pip install --upgrade --pre uiautomator2
```
- 预初始化一次，安装相应的APK 和 二进制文件, 安装过程中如果有弹框请手动确认
```angular2html
python -m uiautomator2 init --serail $SERAIL
```
- 如果要扩充编写Case，可使用weditor来查看控件信息
```angular2html
pip install --pre -U weditor
```
- 更多信息请参考：https://github.com/openatx/uiautomator2#installation

