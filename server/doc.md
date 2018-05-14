# 服务端开发文档

## 服务器信息

* OS：Windows Server 2012
* Python 2.7 with web.py

## 接口说明

### 注册

* 描述：用户注册时请求的接口

* METHOD：HTTP POST

* URL：目前在本机上测试，上线程序时会放在公网服务器上

* 请求字段(XML)：

  * ReqType：固定为`register`
  * UsrName：用户名，不可空
  * Passwd：密码，后期可改为用户名+密码的hash值，不可空
  * Email：用户邮箱，可为空
  * Tel：用户电话，可为空

* HTTP请求的body例子：

  ```xml
  <!-- register -->
  <xml>
  	<ReqType><![CDATA[register]]></ReqType>
  	<UsrName><![CDATA[admin]]></UsrName>
  	<Passwd><![CDATA[123456]]></Passwd>
  	<Email><![CDATA[eg@eg.com]]></Email>
  	<Tel><![CDATA[123456]]></Tel>
  </xml>
  ```

* 返回字段(XML)：

  * ErrInfo：成功时返回`SUCCESS`

    ```
    SUCCESS:		成功
    USR_EXISTED:	用户名已存在
    ```

* 返回值例子：

  ```xml
  <xml>
  	<ErrInfo><![CDATA[{SUCCESS}]]></ErrInfo>
  </xml>
  ```

## 其它

其它需要说明的信息