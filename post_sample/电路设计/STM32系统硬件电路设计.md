# STM32 系统硬件电路设计

---

## 背景

在硬件学习的路上，随着知识的逐渐深入，越来越离不开软硬件结合的设计。基本的电路，配合单片机编程，可以更好实现项目的功能。而我发现，平时整理通用的电路模块、以方便复用设计的方法，似乎已经不适用于复杂多变的单片机系统。  
在单片机中，STM32 强大而通用。而网上大部分关于 STM32 的硬件设计教程过于零散（或深奥），故开此坑，总结学习经验，方便日后的工作。

注：因 `100nF 的陶瓷电容` 比较通用，下文将以 `104 电容` `104` 的简称代替。

## 电源电路


STM32 需运行在 2.0V-3.6V 的电压环境下（VDD）。当 VDD 关闭时，实时时钟（RTC）与备份寄存器（Backup regosters）可从 VBAT 取电。

![](https://cdn.jsdelivr.net/gh/linyuxuanlin/Wiki-media/img/20200223195956.png)


STM32 提供一组独立的引脚 VDDA/VSSA 给 ADC 供电，可以被单独滤波和屏蔽（不受噪音干扰），以提高转换精度。  

STM32 各电源引脚需遵守以下设计规则：

* **VDD**
  * 若使用了 ADC，则需提供 2.4V-3.6V 电压
  * 若没有使用 ADC，则可以提供 2.4V-3.6V 电压
  * 总体来一个去耦电容（陶瓷 / 钽电容，标准值 10uF，最小 4.7uF）
  * 每个 VDD 引脚端都需要一个 104 电容
* **VBAT**
  * 若不使用 VBAT，则需连接至 VDD，并增加 104 电容去耦
  * VBAT 输入电压范围在 1.8V-3.6V 之间
* **VDDA/VSSA**
  * 需分别与 VDD/VSS 连接
  * 若芯片有 VREF- 引脚，则需连接至 VSSA
  * VDDA 需要两个去耦电容（104 + 1uF 陶瓷 / 钽电容），连接在 VDDA/VSSA 之间
* **VREF+**
  * 一般情况下，连接至 VDD
  * 如果使用单独的外部参考电压，则需连接 104 + 1uF 的去耦电容
  * 无论如何，VREF+ 的电压范围只能 2.4V-VDDA 之间

## 复位电路

系统复位时，除了时钟标志位 CSR 与备份域寄存器，其他的所有寄存器都会被复位。系统复位的触发条件有以下几种：
1. NRST 复位引脚低电平（外部复位）
2. 窗口看门狗计数终止（WWDG 复位）
3. 独立看门狗计数终止（IWDG 复位）
4. 软件复位（SW 复位）
5. 低功耗管理器复位
我们可以通过查看控制 / 状态寄存器（RCC_CSR）中的复位标志，以识别复位源。

![](https://cdn.jsdelivr.net/gh/linyuxuanlin/Wiki-media/img/20200223205021.png)

## 时钟电路

驱动系统时钟（SYSCLK），可以用到三个不同的时钟源：
* HSI 晶振时钟（内部高速时钟信号）
* HSE 晶振时钟（外部高速时钟信号）
* PLL 时钟


除此之外，STM32 还有两个二级时钟源：
* 40kHz 内部低速 RC：可以驱动独立看门狗，也可选择地通过程序选择驱动 RTC. RTC 用于从停机 / 待机模式下自动唤醒系统。
* 32.768kHz 外部低速晶振，可选择它用来驱动 RTC（RTCCLK）
每个时钟源在不使用时都可以单独被打开或关闭，以优化系统功耗。

### 高速外部时钟信号（HSE）
* 外部时钟源（HSE 旁路）（图 6）
  * 此模式下，需提供一个外部时钟源。需将外部时钟信号连接至 OSC_IN 引脚，同时 OSC_OUT 悬空。芯片型号对应时钟频率如下：
    * **STM32F100xx**：24 MHz
    * **STM32F101xx/STM32F102xx/STM32F103xx**：25 MHz
    * **互联型产品**：50 MHz
* 外部晶体 / 陶瓷谐振器（HSE 晶体）（图 7）
  * 

![](https://cdn.jsdelivr.net/gh/linyuxuanlin/Wiki-media/img/20200223212710.png)


其中，Hi-Z 表示高阻态；REXT 的值与晶体特性有关（典型值的范围是谐振器串行阻抗 RS 的 5-6 倍）；负载电容 CL = CL1 x CL2 / (CL1 + CL2 ) + Cstray，此处 Cstray 是引脚电容以及 PCB 相关的电容，典型值在 2pF-7pF 之间。


---

填坑中，敬请期待~

## 参考与致谢
* [AN2586: Getting started with STM32F10xxx hardware development](https://www.st.com/content/ccc/resource/technical/document/application_note/6c/a3/24/49/a5/d4/4a/db/CD00164185.pdf/files/CD00164185.pdf/jcr:content/translations/en.CD00164185.pdf)