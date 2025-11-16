<h1 align="center">Learn IsaacGym</h1>
本代码用于帮助初学者了解IsaacGym仿真，有配套讲解的b站视频，视频链接如下：

[【强化学习+机器人运动控制入门】](https://www.bilibili.com/video/BV1bBCcBtEnw/?share_source=copy_web&vd_source=c82bf2382c36f87c98948fac9c658ca7)

## Environment Setup
采用视频所介绍安装的leggedGym的conda环境，运行时确保调用的legged_gym库是本项目提供的，
而非conda安装的legged_gym库，需要手动进行设置，以下提供三种运行代码的方式：

**PyCharm**

鼠标选中左侧文件浏览栏的legged_gym -> 右键 -> Mark Directory as -> Sources Root

**VSCode**

编辑launch.json为如下内容：
```
{
    "version": "0.2.0",
    "configurations": [
    
        {
            "name": "Python: Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "python": "/home/desny/anaconda3/envs/leggedGym/bin/python",
            "console": "integratedTerminal",
            "justMyCode": true,
            "cwd": "${workspaceFolder}",
            "env": {"PYTHONPATH": "${workspaceFolder}",
                    "LD_LIBRARY_PATH": "/home/desny/anaconda3/envs/leggedGym/lib:$LD_LIBRARY_PATH"},
            "args": [
            ]
        }
    ]
}
```
注意修改python, LD_LIBARARY_PATH为自己的路径；选择的python debugger extension需要是2024.2.0版本（否则不支持python3.8的调试）

**命令行**
```
cd legged_gym
export PYTHONPATH=$(pwd):$PYTHONPATH
```

## Preparation
g1的meshes文件需要自行到unitree官方github下载，或者通过夸克网盘下载。

夸克网盘链接：https://pan.quark.cn/s/60f1149c5164

分享码：66P9
***
将下载的meshes文件夹存放于 resources/robots/g1/ 路径下即可。

## Run
```
python scripts/render_animation.py
```
