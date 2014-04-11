安装
----------------------
1.  下载二进制包
`$ wget http://mirrors.hust.edu.cn/apache/jena/binaries/apache-jena-2.11.1.tar.gz`
$ tar zxf apache-jena-2.11.1.tar.gz
$ cd apache-jena-2.11.1

2. 安装，
编辑bashrc，设置JENA_HOME这个变量
export JENA_HOME=/path/to/apache-jena-2.11.1

3. 设置
在命令行使用
$ cd $JENA_HOME
$ bin/sparql --version

使用
----------------------
1. 命令行使用
建立数据文件test.rdf：

    <?xml version="1.0" encoding="utf-8"?>
    <rdf:RDF xmlns:contact="http://www.w3.org/2000/10/swap/pim/contact#" xmlns:eric="http://www.w3.org/People/EM/contact#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
      <rdf:Description rdf:about="http://www.w3.org/People/EM/contact#me">
        <contact:fullName>Eric Miller</contact:fullName>
      </rdf:Description>
      <rdf:Description rdf:about="http://www.w3.org/People/EM/contact#me">
        <contact:mailbox rdf:resource="mailto:em@w3.org"/>
      </rdf:Description>
      <rdf:Description rdf:about="http://www.w3.org/People/EM/contact#me">
        <contact:personalTitle>Dr.</contact:personalTitle>
      </rdf:Description>
      <rdf:Description rdf:about="http://www.w3.org/People/EM/contact#me">
        <rdf:type rdf:resource="http://www.w3.org/2000/10/swap/pim/contact#Person"/>
      </rdf:Description>
    </rdf:RDF>

来源： <http://en.wikipedia.org/wiki/Resource_Description_Framework>
 
建立查询文件test.rq：
```
SELECT ?x
WHERE {?x <http://www.w3.org/2000/10/swap/pim/contact#fullName>  "Eric Miller" }
```

查询(数据和查询文件见附件)：
$ ./sparql --data=test/test.rdf --query=test/test.rq

    --------------------------------------------
    | x                                        |
    ============================================
    | <http://www.w3.org/People/EM/contact#me> |
    --------------------------------------------

2. 导入数据
使用tdbloader2
Usage: tdbloader2 --loc location datafile 
如：$ ./tdbloader2 --loc /home/lijian/data/temp test/test.rdf 
在/home/lijian/data/temp下生成数据文件，

使用tdbquery查询：
tdbquery --loc=<path> --query=<query>
如：
$ ./tdbquery --loc=/home/lijian/data/temp --query=test/test.rq
效果：

    ----------------------------------------------------
    | x                                | fname         |
    ====================================================
    | <http://somewhere/JohnSmith/>    | "John Smith"  |
    | <http://somewhere/RebeccaSmith/> | "Becky Smith" |
    | <http://somewhere/SarahJones/>   | "Sarah Jones" |
    | <http://somewhere/MattJones/>    | "Matt Jones"  |
    ----------------------------------------------------
