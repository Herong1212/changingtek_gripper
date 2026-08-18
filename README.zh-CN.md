<img src="https://gw.alipayobjects.com/zos/antfincdn/R8sN%24GNdh6/language.svg" width="18"> [English](./README.md) | 简体中文

# 知行机器人机械爪 ROS 功能包

本仓库是**知行机器人（ChangingTek Co., Ltd.）**机械爪产品的 ROS 功能包集合。每个子目录包含一个完整的 ROS 功能包，涵盖特定型号机械爪的 URDF 模型、网格文件、启动文件、配置文件和控制脚本。

## 支持的产品

| 功能包 | 说明 |
|--------|------|
| [crt_ctag2f90_gripper_visualization](./crt_ctag2f90_gripper_visualization) | CTAG2F90 二指机械爪 |
| [crt_ctag2f90c_gripper_visualization](./crt_ctag2f90c_gripper_visualization) | CTAG2F90C 二指机械爪 |
| [crt_ctag2f90d_gripper_visualization](./crt_ctag2f90d_gripper_visualization) | CTAG2F90D 二指机械爪 |
| [crt_ctag2f120_gripper_visualization](./crt_ctag2f120_gripper_visualization) | CTAG2F120 二指机械爪 |
| [crt_ctag2f120s_gripper_visualization](./crt_ctag2f120s_gripper_visualization) | CTAG2F120S 二指机械爪 |
| [crt_ctdh3f110_gripper_visualization](./crt_ctdh3f110_gripper_visualization) | CTDH3F110 三指机械爪 |
| [crt_cthm2f650_gripper_visualization](./crt_cthm2f650_gripper_visualization) | CTHM2F650 二指机械爪 |
| [crt_cthm3f460_gripper_visualization](./crt_cthm3f460_gripper_visualization) | CTHM3F460 三指机械爪 |
| [crt_ctm2f110_gripper_visualization](./crt_ctm2f110_gripper_visualization) | CTM2F110 二指机械爪 |
| [crt_ctm3f123_gripper_visualization](./crt_ctm3f123_gripper_visualization) | CTM3F123 三指机械爪 |
| [crt_ctmg60_gripper_visualization](./crt_ctmg60_gripper_visualization) | CTMG60 二指机械爪 |
| [crt_ctpm14_gripper_visualization](./crt_ctpm14_gripper_visualization) | CTPM14 二指机械爪 |
| [crt_ctpm2f20_gripper_visualization](./crt_ctpm2f20_gripper_visualization) | CTPM2F20 二指机械爪 |
| [crt_ctpm2f50_gripper_visualization](./crt_ctpm2f50_gripper_visualization) | CTPM2F50 二指机械爪 |
| [crt_ctpm2f50f_gripper_visualization](./crt_ctpm2f50f_gripper_visualization) | CTPM2F50F 二指机械爪 |
| [crt_ctpm2f50h_gripper_visualization](./crt_ctpm2f50h_gripper_visualization) | CTPM2F50H 二指机械爪 |
| [crt_ctpm3f20e_gripper_visualization](./crt_ctpm3f20e_gripper_visualization) | CTPM3F20E 三指机械爪 |

## 功能包结构

每个机械爪功能包遵循标准的 ROS 功能包结构：

```
crt_xxx_gripper_visualization/
├── CMakeLists.txt          # CMake 构建配置
├── package.xml             # ROS 功能包清单
├── config/                 # 配置文件（如关节名称 YAML）
├── docs/                   # 文档（README.md、README.zh-CN.md、图片）
├── launch/                 # ROS 启动文件
├── meshes/                 # 3D 网格文件（STL）
├── scripts/                # Python 控制脚本
└── urdf/                   # URDF / Xacro 模型文件
```

## 快速开始

### 1. 环境要求

- Ubuntu 18.04 LTS 或兼容版本
- ROS Melodic（或更高版本）
- Python 3.x

### 2. 构建

将所需的机械爪功能包文件夹复制到你的 ROS 工作空间的 `src` 目录下，然后进行构建：

```sh
cd ~/ws_catkin
catkin_make
```

### 3. 启动

```sh
source ~/ws_catkin/devel/setup.bash
roslaunch crt_xxx_gripper_visualization display.launch
```

> **注意：** 请将 `crt_xxx_gripper_visualization` 替换为你实际使用的机械爪型号对应的功能包名称。

### 4. 控制

部分功能包在 `scripts/` 目录下提供了 Python 控制脚本。详细的使用说明请参考各功能包内的 `docs/README.md` 文件。

## 文档说明

关于每个机械爪型号的详细使用说明，请参考对应子目录下的 `docs` 文件夹：

- `docs/README.md` — 英文文档
- `docs/README.zh-CN.md` — 简体中文文档

## 许可证

本项目采用 [BSD 3-Clause 许可证](./LICENSE)。

## 联系我们

如需技术支持或商务合作，请联系**知行机器人（ChangingTek Co., Ltd.）**。