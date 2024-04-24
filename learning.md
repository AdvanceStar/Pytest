# Chapter 1: pytest
https://www.bilibili.com/video/BV1hX4y187wi?p=2&spm_id_from=pageDriver&vd_source=0d0be4827220d10b42080ec061114bb1
## pytest即插件
1. 插件
2. 启动点

## 自动化测试VS测试开发
1. pytest用户（自动化测试）
    1. 测试用例编写
    2. 测试框架的维护
2. 维护pytest（测试开发）（关注pytest而不是业务）
    1. 核心开发
    2. 插件开发
## pytest实现
1. 失败重试
2. 并发测试
3. 用例排序
4. 生成报告
5. 统计覆盖率

## 搭建测试平台
### 思路
1. django框架：在线编辑excel和yaml文件
2. pytest：执行django文件并执行，生成报告
3. django展示生成的报告

对于django用于在线编辑和在线展示

allu生成

IO生成异步

解析yaml文件

扩展成基于web的测试开发平台，市面上存在现成的开发工具，但是不应该称为使用者。

### 总结
1. pytest内部插件；
2. 二次开发和重新搭建；
3. django提供基于xx协议的文件提交从而可以展示多次的结果而非新文件覆盖旧文件

### pytest开发
插件系统：pluggy
1. 声明一个函数，称为hook（"pytest_"为重要的约定）
2. **软件**运行中会自动运行**hook**（hook相当于声明约定）
3. **插件**会按照hook的形式实现函数并被软件自动调用

**插件**的特点是可插拔

约定特点 + 约定时间 => 按照约定的，随时可来可走 -- **插件**

必须要等到最后 -- **软件**

hook最重要的特点是**约定**

### pytest的hook清单（所有约定）
1. hookspec.py:中所有函数都是空的，提供了名称、返回值、参数，作为约定是空的，但是在使用时得按照对应的要求进行配置。（内部程序都看一遍pytest_cmdline_main需看一下，是约定的函数）
2. 官方文档：https://docs.pytest.org/en/8.0.x/reference/reference.html

若插件提供了新的hook，则通过代码进行动态获取

### hook规则
使用方法
1. 被动调用：使用该名称即可使用cmd中使用**pytest**直接调用
```python
def pytest_cmdline_main():
    print("i'm hook, which is called by pytest.")
```
2. 掌握主动

装饰器，高级用法，实际上必须有，但是有的简单功能可以省略
