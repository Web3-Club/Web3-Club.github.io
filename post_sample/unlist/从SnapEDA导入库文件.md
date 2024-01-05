# 从 SnapEDA 导入库文件



---


   * 从 **SnapEDA** 下载的元器件：
     1. 先在 **Shared\Library** 路径下创建 **SnapEDA** 文件夹（便于后期整理）；
     2. 将下载的 **.lia** 文件解压并拷贝至 **SnapEDA** 文件夹内；
     3. 将 **SnapEDA** 文件夹内的 **.lia** 文件 **直接拖进** Altium Designer **左侧** **Projects** 面板，自动弹出 **P-CAD 导入向导** 页面，一直点 **Next** ，直到看见 **Current Layer Mappings** 页面，执行以下操作：
        * 将 **Layer '10'** 右键选择为 **Mechanical Layer 1** ；
        * 将 **Layer '20'** 右键选择为 **Mechanical Layer 13** ；
        * 将 **Layer '21'** 右键选择为 **Mechanical Layer 15** ；
     4. 一直点 **Next** 直至完成。