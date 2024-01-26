# sca-core

sca-core目前包含的功能主要有：

1）配置解析和管理

2）日志打印

3）rabbit基类

4）多线程和多进程操作封装

## 安装方式

    pip install sca-core
    
当前版本是0.1.1

## 使用指南

使用
    
    import sca_core as sca
   
导入模块。sca_core实现上是把库里的文件都导入到__init__.py，所以不需要指定sca_core下的文件。
另外，最好使用sc别名，避免和其他库使用上冲突。

### 配置解析和管理
约定：项目根目录放置配置文件settings.ini，按模块label分块配置各服务模块，格式类似：

    [rabbit]
    host = 127.0.0.1
    port = 5671
    user = guest
    password = guest
    

通用配置（如log_path）放到[settings]下，[settings]建议放到配置文件最后。

程序内通过sca.sca_config('label','item')调用,要确保item的key是存在的，否则解析配置会抛出异常。

如果不确定item是否存在可以使用sca.sca_config('label','item','')，不存在的item会赋默认的空值。

对于非docker部署模式，根目录可以放settings.local.ini用于本地开发使用，该文件不要提到git里。

### 日志打印
在项目中调用sca.log_init_config(log_dir="xx")进行日志配置初始化，可以自定义日志存放目录，默认从settings.ini里面读取，格式类似：

    [settings]
    log_dir = .

程序内通过sca.log_info("xxxxx")进行日志打印。

#### 多线程和多进程封装
示例代码：

    def handle_process_work(job):
        sca.log_info("job={0}".format(job))
        time.sleep(0.1)
    
    def test_multi_process():
        jobs = [i for i in range(100)]
        sca.execute_multi_core("dumb", handle_process_work, jobs, 4, True)

execute_multi_core的最后一个参数表示使用多线程还是多进程，如果work num是1就主进程顺序执行了。
