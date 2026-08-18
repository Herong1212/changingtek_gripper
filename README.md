English | [简体中文](./README.zh-CN.md)

# ChangingTek Gripper ROS Packages

This repository is a collection of ROS packages for **ChangingTek Co., Ltd.** gripper products. Each subdirectory contains a complete ROS package for a specific gripper model, including URDF models, meshes, launch files, configuration files, and control scripts.

## Supported Products

| Package | Description |
|---------|-------------|
| [crt_ctag2f90_gripper_visualization](./crt_ctag2f90_gripper_visualization) | CTAG2F90 two-finger gripper |
| [crt_ctag2f90c_gripper_visualization](./crt_ctag2f90c_gripper_visualization) | CTAG2F90C two-finger gripper |
| [crt_ctag2f90d_gripper_visualization](./crt_ctag2f90d_gripper_visualization) | CTAG2F90D two-finger gripper |
| [crt_ctag2f120_gripper_visualization](./crt_ctag2f120_gripper_visualization) | CTAG2F120 two-finger gripper |
| [crt_ctag2f120s_gripper_visualization](./crt_ctag2f120s_gripper_visualization) | CTAG2F120S two-finger gripper |
| [crt_ctdh3f110_gripper_visualization](./crt_ctdh3f110_gripper_visualization) | CTDH3F110 three-finger gripper |
| [crt_cthm2f650_gripper_visualization](./crt_cthm2f650_gripper_visualization) | CTHM2F650 two-finger gripper |
| [crt_cthm3f460_gripper_visualization](./crt_cthm3f460_gripper_visualization) | CTHM3F460 three-finger gripper |
| [crt_ctm2f110_gripper_visualization](./crt_ctm2f110_gripper_visualization) | CTM2F110 two-finger gripper |
| [crt_ctm3f123_gripper_visualization](./crt_ctm3f123_gripper_visualization) | CTM3F123 three-finger gripper |
| [crt_ctmg60_gripper_visualization](./crt_ctmg60_gripper_visualization) | CTMG60 two-finger gripper |
| [crt_ctpm14_gripper_visualization](./crt_ctpm14_gripper_visualization) | CTPM14 two-finger gripper |
| [crt_ctpm2f20_gripper_visualization](./crt_ctpm2f20_gripper_visualization) | CTPM2F20 two-finger gripper |
| [crt_ctpm2f50_gripper_visualization](./crt_ctpm2f50_gripper_visualization) | CTPM2F50 two-finger gripper |
| [crt_ctpm2f50f_gripper_visualization](./crt_ctpm2f50f_gripper_visualization) | CTPM2F50F two-finger gripper |
| [crt_ctpm2f50h_gripper_visualization](./crt_ctpm2f50h_gripper_visualization) | CTPM2F50H two-finger gripper |
| [crt_ctpm3f20e_gripper_visualization](./crt_ctpm3f20e_gripper_visualization) | CTPM3F20E three-finger gripper |

## Package Structure

Each gripper package follows a standard ROS package structure:

```
crt_xxx_gripper_visualization/
├── CMakeLists.txt          # CMake build configuration
├── package.xml             # ROS package manifest
├── config/                 # Configuration files (e.g., joint names YAML)
├── docs/                   # Documentation (README.md, README.zh-CN.md, images)
├── launch/                 # ROS launch files
├── meshes/                 # 3D mesh files (STL)
├── scripts/                # Python control scripts
└── urdf/                   # URDF / Xacro model files
```

## Quick Start

### 1. Prerequisites

- Ubuntu 18.04 LTS or compatible
- ROS Melodic (or later)
- Python 3.x

### 2. Build

Copy the desired gripper package folder into your ROS workspace `src` directory, then build:

```sh
cd ~/ws_catkin
catkin_make
```

### 3. Launch

```sh
source ~/ws_catkin/devel/setup.bash
roslaunch crt_xxx_gripper_visualization display.launch
```

> **Note:** Replace `crt_xxx_gripper_visualization` with the actual package name of your gripper model.

### 4. Control

Some packages include Python control scripts in the `scripts/` directory. Refer to the `docs/README.md` inside each package for detailed usage instructions.

## Documentation

For detailed instructions on each gripper model, please refer to the `docs` folder within the corresponding subdirectory:

- `docs/README.md` — English documentation
- `docs/README.zh-CN.md` — 简体中文文档

## License

This project is licensed under the [BSD 3-Clause License](./LICENSE).

## Contact

For technical support or business inquiries, please contact **ChangingTek Co., Ltd.**