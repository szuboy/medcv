# Read the Docs

- Read the Docs官网：https://readthedocs.org
- Read the Docs使用手册：https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html
- Read the Docs源码：https://github.com/rtfd/readthedocs.org
- Sphinx官网：http://www.sphinx-doc.org
- Sphinx源码：https://github.com/sphinx-doc/sphinx
- Python官网：http://www.python.org
- demo源码：https://github.com/darwindu/readthedocs-demo


## what is Read the Docs?

Read the Docs是什么？看看官方怎么解释：Read the Docs simplifies software documentation by automating building, versioning, and hosting of your docs for you；

它是一个自动化构建的软件系统，可以进行版本管理、文件托管，从而简化文档管理；

它是基于 Sphinx 的在线文档托管系统,接受一个 Git Repository 或 SVN 仓库作为文档来源。也就是说，Read the Docs是一个文件托管系统。那Sphinx又是什么？

Sphinx是一个基于SQL的全文检索引擎，可以结合MySQL，PostgreSQL做全文搜索，它可以提供比数据库本身更专业的搜索功能，使得应用程序更容易实现专业化的全文检索。也就是说，Sphinx是文件检索引擎。

## what is the use of Read the Docs?

Read the Docs有什么用呢？好吧，这也是我写这篇文章的原因，无论是行内，还是业内，现在开源盛行，我们的代码基本上都上传到github，代码管理用github，但是文档管理用啥？我只能告诉你，最佳实践是Read the Docs。

## how to use Read the Docs?

如何使用Read the Docs呢？
- 首先，你需要个github账号；

有需求才有存在的价值；当你拥有github账号后，你会想着上传你的代码和文档，文档怎么管理、维护，以及方便自己、别人的使用。

- 然后，你需要个Read the Docs账号；

注册Reda the Docs账号后，你会发现满脸懵逼，这玩意怎么用？耐心的同学会发现，官方会指导你跳转到Read the Docs使用手册，但是跳转到Read the Docs使用手册，会直接来个命令：pip install sphinx，why？

- 接着，搭建python；

搭建python都是为了pip命令，pip是python的一个工具；

- 接着，搭建Sphinx

想必大家都知道，搭建sphinx就是为了Read the Docs；

- 最后，使用Read the Docs

这是我们的终极目标。

下面我们会按照这些步骤来进行讲解如何开始我们的Read the Docs。

## 注册账号
- 1.注册github账号，略；不用我说，你也会；
- 2.注册Read the Docs账号，略；不用我说，你也会；


## 环境搭建

解释一下：由于大部门同学用windows开发，所以环境搭建基于windows。周边用Mac、Linux的同学可以参考Sphinx官网。

- 1.搭建python；
```
1. 下载安装包，建议3.+版本，下载地址：http://www.python.org/download/；

2. 安装；

3. 配置环境变量，在变量Path增加Python的安装目录，及pip工具目录；
比如：
安装目录：D:\Program Files\Python\Python36-32;
pip工具目录：D:\Program Files\Python\Python36-32\Scripts;

4. 验证，打开cmd，执行python --version 及pip --version命令，表示安装成功；

```

- 2.初始化Sphinx，有两种方法，一种是通过PyPI，一种是通过source；
```
方法一：Installation from PyPI，通过发布包初始化(Read the Doc使用手册使用该方法)

1. 打开cmd，选择安装目录，例如：D:\Program Files\Python\Python36-32\Scripts

2. 执行命令：pip install -U sphinx

方法二：Installation from source，通过源码初始化（作为开发人员，推荐该方法初始化Sphinx）

1. git clone https://github.com/sphinx-doc/sphinx
2. cd sphinx
3. pip install .
```

## 构建Read the Docs项目
- 1.创建文件夹docs: mkdir docs
- 2.进入目录：cd docs
- 3.生成docs项目，sphinx-quickstart
```
执行以上命令会弹出命令框：
// build与source是否隔开，build是存放编译后的文件，source是放配置文件
1. Separate source and build directories (y/n) [n]: y 
// 项目名称
2. Project name: helloworld
// 作者
3. Author name(s): darwindu
// 项目版本
4.  Project release []: 0.1.1
// 语言，英语：en
5. Project language [en]: zh_CN

执行完之后生成项目目录：
|--build 编译后文件
|--source 
|-------|--_static 存放静态文件，比如样式
|-------|--_templates
|-------|--conf.py 项目配置文件
|-------|--index.rst 首页
|--make.bat 执行命令
|--Makefile
```

- 4.编译：make html
```sh
执行命令后：

D:\sphinx-doc>make html
Running Sphinx v3.0.0+
loading translations [zh_CN]... done
making output directory... done
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 1 source files that are out of date
updating environment: 1 added, 0 changed, 0 removed
reading sources... [100%] index
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [100%] index
generating indices... genindex
writing additional pages... search
copying static files... done
copying extra files... done
dumping search index in Chinese (code: zh) ... done
dumping object inventory... done
build succeeded.

The HTML pages are in build\html.

生成html页面：build\html
```
- 5.预览页面：build\html\index.html

![avatar](https://note.youdao.com/yws/api/personal/file/EEF658991C674C118731B2ECF8CCB460?method=download&shareKey=39429dbb4c44943c9fdf20c3cc43e8cc)

这个效果出来了，至少比较丑，怎么办呢？

- 6.配置主题
```
1. 初始化模板：pip install sphinx_rtd_theme

2. source/conf.py配置
    import sphinx_rtd_theme
    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    
3. 配置完成后，执行make html

主题选择请查阅：https://sphinx-themes.org/
```
重新打开build\html\index.html，是不是好看多了：
![avatar](https://note.youdao.com/yws/api/personal/file/EACDE7A7A2B443EB9A69FC9115734803?method=download&shareKey=8b9d7cb8933d3b56d6b21e08f4953cff)

配置完主题之后，很快你就会发现，Read the Docs编辑文本是使用.rst(reStructuredText)语法，平时我们用markdown比较多，一下子更改会不会项目进度有影响？好吧，我的理解是，让.rst作为文件跳转，另外文档编辑用markdown。

另外想学习.rst语法的可以参考：http://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html

- 7.配置markdown
```
1.pip install recommonmark

2.source/conf.py配置
    增加：extensions = ['recommonmark'] 
    
3.增加README.md文档
***************************************
# helloworld

## 你好，Read the Docs
***************************************

    
4.修改source/index.rst，如下：
***************************************

    .. helloworld documentation master file, created by
       sphinx-quickstart on Sat Jun  1 13:29:49 2019.
       You can adapt this file completely to your liking, but it should at least
       contain the root `toctree` directive.
    
    Welcome to helloworld's documentation!
    ======================================
    
    .. toctree::
       :maxdepth: 2
       :caption: Contents:
        //增加配置，这行注释请去除
        README.md
    
    Indices and tables
    ==================
    
    * :ref:`genindex`
    * :ref:`modindex`
    * :ref:`search`
    
***************************************    

```
重新打开build\html\index.html，如下：
![avatar](https://note.youdao.com/yws/api/personal/file/72253C9FA0634CF9B5F79D4BEA1F0621?method=download&shareKey=bfe03602100830e6cb1dfa9331bf6eaa)

以上内容貌似完成了我们的需求，那怎么用起来，和github关联呢？

## 关联github
- 1.打开github.com, 创建一个工程readthedocs-demo；
- 2.在本地电脑上，创建readthedocs-demo文件夹；
- 3.进入readthedocs-demo目录，创建docs文件夹；
- 4.进入docs文件夹，将开始通过sphinx-quickstart命令生成的文件和文件夹拷贝到改目录；
- 5.返回readthedocs-demo这个目录；
- 6.增加.gitignore文件，忽略docs/build/文件夹内容，这个文件夹不用上传;
- 7.上传至github
```
git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/darwindu/readthedocs-demo.git
git push -u origin master
```
执行完成后，打开github的readthedocs-demo浏览，如下：
![avatar](https://note.youdao.com/yws/api/personal/file/1591BD50A458474996B09290A7F6AD37?method=download&shareKey=a9970b298c2889e583ad7c7415bff224)

docs文件已经上传了，如何关联Read the Docs呢？

## 关联Read the Docs
- 1.打开网址：https://readthedocs.org/
- 2.点击菜单：我的项目
![avatar](https://note.youdao.com/yws/api/personal/file/56F829AE1B9345AAA51415399CC6F183?method=download&shareKey=4d827ec3f1ea269cd3328d558658ecb4)

- 3.点击按钮：Import a Project
![avatro](https://note.youdao.com/yws/api/personal/file/9228DCBDE0874A0297B347B3B1B1C7CB?method=download&shareKey=9592d2c039466578dd8b45c54cbcbf2e)

- 4.选择项目：readthedocs-demo
![avatar](https://note.youdao.com/yws/api/personal/file/C2B2246A278048D9928F349AD5C90B72?method=download&shareKey=d146e6b693e2671aeec518a1c53113f7)

- 5.选择之后，会弹出界面，然后点击下一步，如果提示：项目已经存在的话，将项目名：readthedocs-demo改成readthedocs-demo-zh；如果没有提示，忽略，直接点击下一步

- 6.构建项目docs：Build Version
![avatar](https://note.youdao.com/yws/api/personal/file/28E29903DA384DE2942199AFACEB27B4?method=download&shareKey=77b0975d8d6628235f60f57c8e276d61)

- 7.构建过程，如预期的报错了，contents.rst not found，为啥呢？怎么解决？
```
打开配置source/conf.py，增加如下配置：

# The master toctree document.
master_doc = 'index'

产生这个问题的原因：默认首页名称是contents.rst；
更改一下就可以了，重新提交github，提交后，点击“构建”按钮，等待Read the Docs自动构建；
```
![avator](https://note.youdao.com/yws/api/personal/file/7FBDF9E57B074DCA816DB63DB0C2183F?method=download&shareKey=a3442927363fb25a9075a50ff0d043eb)

- 8.等待片刻后，会发现构建成功，点击“阅读文档”，如下
![avatror](https://note.youdao.com/yws/api/personal/file/6D7801F7149A484AB5BD1320656A6EFB?method=download&shareKey=5e7d4648d9b64a8b4eeea1fbbb6b26ea)
![avatror](https://note.youdao.com/yws/api/personal/file/BAAF09076B7E49F09EAFA5C7E2DDA861?method=download&shareKey=e449c7b847721f7992d5ebfce3bbd678)

goods，是不是很开心，这下好像真的搞定的了；但是，假如...我们需要多语言文档呢？赶紧看看官方文档...
![avatar](https://note.youdao.com/yws/api/personal/file/5172B42719224D0F9B27814CB3AFB635?method=download&shareKey=c5892650def7ff26d289e8c76d51cadf)

## 文档本地化
根据官方提供的方案，文档本地化提供两种方案：
- 第一种：只存在两种语言的文档本地化方案

> 在docs文件夹下提供2中语言的文档；

> 然后，在Read the Docs上创建两个项目，两个项目指向同一个github地址；

- 第二种，存在两种以上的文档本地化方案

> 通过多个.po文件来处理

面对这两种方案，沉思了很久，假如先辈们努力一点的话，可能我们就不要这样辛苦的学习这么多语言了；好吧，我建议还是选择第一种方案，选汉语+英语，应该适应绝大部分场景，最重要是简单而且满足需求；

- 1.在docs文件夹，创建两个文件夹:zh_CN、en
- 2.将开始docs下的文件都放进:zh_CN中，因为开始我们都是通过中文(zh_CN)完成操作的；

```
项目结构如下：
|--en 
|--zh_CN
    |--build 编译后文件
    |--source 
    |-------|--_static 存放静态文件，比如样式
    |-------|--_templates
    |-------|--conf.py 项目配置文件
    |-------|--index.rst 首页
    |--make.bat 执行命令
    |--Makefile
  
```

- 3.进入文件夹en，构建en版本的Read the Docs，执行命令：sphinx-quickstart
```
执行以上命令会弹出命令框：
// build与source是否隔开，build是存放编译后的文件，source是放配置文件
1. Separate source and build directories (y/n) [n]: y 
// 项目名称
2. Project name: helloworld
// 作者
3. Author name(s): darwindu
// 项目版本
4.  Project release []: 0.1.1
// 语言，英语：en
5. Project language [en]: en
```

- 4.修改docs/en/source/conf.py，根据docs/zh_Cn/source/conf.py修改
- 5.增加README.md，修改index.rst
```
README.md
***************************************
# helloworld

## hi, Read the Docs
***************************************

index.rst：
***************************************

    .. helloworld documentation master file, created by
       sphinx-quickstart on Sat Jun  1 13:29:49 2019.
       You can adapt this file completely to your liking, but it should at least
       contain the root `toctree` directive.
    
    Welcome to helloworld's documentation!
    ======================================
    
    .. toctree::
       :maxdepth: 2
       :caption: Contents:
        //增加配置，这行注释请去除
        README.md
    
    Indices and tables
    ==================
    
    * :ref:`genindex`
    * :ref:`modindex`
    * :ref:`search`
    
***************************************   
```

## Read the Docs关联github

- 1.进入本地项目readthedocs-demo目录，创建README.md、README_en.md
```
README.md
*******************************
中文版 | [English Version](./README_en.md)


### 开始使用

|集成方法|文档入口|当前状态|
|:----|:-----|:-----|
|代码演示|[文档](https://readthedocs-demo-zh.readthedocs.io/zh_CN/latest/)|[![Documentation Status](https://readthedocs.org/projects/code-blocks/badge/?version=latest)](https://readthedocs.org/projects/readthedocs-demo-zh/)|


### 联系我们
邮箱：252921602@qq.com
*******************************

README_en.md
*******************************
[中文版](./README.md) | English Version

### start using

|Integration Method|Document Entry|Current Status|
|:----|:-----|:-----|
|Code Demo |[Documents](https://readthedocs-demo-en.readthedocs.io/en/latest/)|[![Documentation Status](https://readthedocs.org/projects/code-blocks-en/badge/?version=latest)](https://readthedocs.org/projects/readthedocs-demo-en/)|


### contact us
Email：252921602@qq.com
*******************************

```

- 2.提交至github，如图
![avatar](https://note.youdao.com/yws/api/personal/file/9606FFBEF4D2481499EC3E2D9E32D895?method=download&shareKey=73ca7e6b7a3f7f136e46795900d69b0b)

## 结束语
完成以上操作，基本掌握了Read the Docs的使用方式，更多的技巧可以通过官方文档获得。