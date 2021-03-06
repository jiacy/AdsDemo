## 功能说明
- 进入指定APP，在Feed流页面滑动截屏 指定次数
- 使用框架https://github.com/openatx/uiautomator2

## 使用说明
- 在config.py中配置pkg_name、swipe_times、设备序列号udid
- 运行runner.py
- 运行结束查看screenshot目录中的截图，截图以时间戳命名

## 环境配置
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


## 额外说明
- 目前滑动一屏是大约估算出来的, 可根据需要调整下面的参数（屏幕相对坐标）
```angular2html
self.swipe_by_percent(start_x_per=0.5, start_y_per=0.8, end_y_per=0.3, end_x_per=0.5, times=times, duration=duration)
```

