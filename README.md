# Fish Rob Master

## 该辅助程序的作用

在Minecraft 1.8.9 PVP中, 当使用鱼竿进行控距时, 通过快速切换至鱼竿, 抛出后在不收回的情况下立刻切换为武器, 根据特性减少鱼竿耐久损失并获得一定优势

## 如何使用

下载并运行fishRobMaster.exe , 自动生成config.json, 通过config.json可以修改默认按键配置为自己的

```json
{
    "trigger_key": "q",
    "subsequent_key": "mouse4",
    "wait_time": 0.0
}
```

>  Trigger_key: 设置为鱼竿键位
>
> subsequent_key: 设置为剑的键位
>
> wait_time: 为鱼竿抛出时间, 默认为*0.01秒*, 可以按照实际PVP情况修改



***仅供学习, 请勿用于公共服务器和比赛作弊***

---

### 参与改进

程序本身使用Python编写, 所使用的第三方库有:

- pyautogui

  `pip install pyautogui`

- keyboard

  `pip install kaybard`
