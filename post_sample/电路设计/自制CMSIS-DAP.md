# 自制 CMSIS-DAP

（未完成）

---

CMSIS DAP 是 ARM 官方推出的开源仿真器，支持所有的 Cortex - ARM 器件，支持 JTAG / SWD 接口，在最新的固件版本中，还支持单线 SWO 接口，可以直接在程序里把相应的数据通过 SWO 接口输出到调试窗口，起到类似串口调试的目的。DAP 主要有以下特点：
1. 完全开源，没有版权限制，所以相应的价格会很便宜
2. 无须驱动，即插即用
3. 在新版本的 DAP 里集成了串口，除了下载调试外还能充当 USB 转串口模块，一机两用
4. 性能方面已经可以满足一般用户的需求


（待更新）



## 参考与致谢
* [x893/CMSIS-DAP](https://github.com/x893/CMSIS-DAP)
* [ARM 官网的 DAP 介绍](http://www.keil.com/pack/doc/cmsis/DAP/html/index.html)
* [电子屌丝的的情怀：CMSIS DAP 仿真器](http://www.stmcu.org.cn/module/forum/thread-610968-1-2.html)
* [CMSIS DAP 仿真器](https://item.taobao.com/item.htm?spm=a1z10.1-c.w5003-21405148310.36.78726a3dta5ieC&id=550828063764&scene=taobao_shop)
* [konosubakonoakua/Various_MCU_Debugger_DIY](https://github.com/konosubakonoakua/Various_MCU_Debugger_DIY)