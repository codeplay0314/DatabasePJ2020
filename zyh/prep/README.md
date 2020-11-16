#### 数据预处理

删除了payload字段，运行前需要在linux系统上配置jsoncpp库

> 1.参考https://blog.csdn.net/asmartkiller/article/details/89385471配置，json文件夹已经加入prep文件夹中，不需要再导入
>
> 2.初始数据相对路径和输出数据的相对路径可以根据需要在prep.cpp中重新修改
>
> 3.谁勤快可以封装一下库啥的就不用每次编译都指定链接文件了

##### 使用方法

在prep文件夹中打开终端输入

~~~shell

g++ -o prep prep.cpp -L. libjson_linux-gcc-5.4.0_libmt.a

./prep

~~~

就可以在指定的输出路径下看到输出的json文件了