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

### 登录

* 描述：用户登录时请求的接口

* METHOD：HTTP POST

* URL：目前在本机上测试，上线程序时会放在公网服务器上

* 请求字段(XML)：

  * ReqType：固定为`login`
  * UsrName：用户名
  * Passwd：密码

* HTTP请求的body例子：

  ```xml
  <!-- login -->
  <xml>
  	<ReqType><![CDATA[login]]></ReqType>
  	<UsrName><![CDATA[admin]]></UsrName>
  	<Passwd><![CDATA[123456]]></Passwd>
  </xml>
  ```

* 返回字段(XML)：

  - ErrInfo：成功时返回`SUCCESS`

    ```
    SUCCESS:		成功
    PASSWD_ERR:		密码错误
    ```

* 返回值例子(XML)：

  ```xml
  <!-- login -->
  <xml>
  	<ErrInfo><![CDATA[SUCCESS]]></ErrInfo>
  </xml>
  ```

### 查询

* 描述：用户查询信息时请求的接口

* METHOD：HTTP POST

* URL：目前在本机上测试，上线程序时会放在公网服务器上

* 请求字段(XML)：

  * ReqType：固定为`select`
  * Ids：包含0个或多个Id，表示招聘信息在数据库中的ID
  * Labels：包含0个或多个Label，招聘信息标签
  * Keywords：包含0个或多个Keyword，查询关键字
  * Method：查询方式，暂设为`none`

* HTTP请求的body例子：

  ```xml
  <!-- select -->
  <xml>
  	<ReqType><![CDATA[select]]></ReqType>
  	<Ids>
  		<Id><![CDATA[123]]></Id>
  		<Id><![CDATA[456]]></Id>
  	</Ids>
  	<Labels>
  		<Label><![CDATA[c++]]></Label>
  		<Label><![CDATA[web]]></Label>
  	</Labels>
  	<Keywords>
  		<Keyword><![CDATA[Guangzhou]]></Keyword>
  		<Keyword><![CDATA[Netease]]></Keyword>
  	</Keywords>
  	<Method><![CDATA[none]]></Method>
  </xml>
  ```

* 返回字段(XML)：

  - ErrInfo：成功时返回`SUCCESS`

    ```
    SUCCESS:			成功
    SOME_ID_NOT_EXISTS:	按id查找时有些id不存在
    ERR_UNKNOWN:		可能因为该函数还没有实现
    EMPTY_SELECT_REQ:	请求为空
    ```

  - Piece：有0个或多个，每个Piece代表一条招聘信息

    * Id：招聘信息ID
    * Job：职位信息，详情见需求规约
    * Company：公司信息，详情见需求规约
    * Apply：申请信息，详情见需求规约
    * Attr：招聘信息属性，详情见需求规约

* 返回值例子(XML)：

  ```xml
  <!-- sellect -->
  <xml>
  	<ErrInfo><![CDATA[SUCCESS]]></ErrInfo>
  	<Piece>
  		<Id><![CDATA[1234]]></Id>
  		<Job>
  			<Name><![CDATA[C++ Developer]]></Name>
  			<Salary><![CDATA[6000]]></Salary>
  			<Number><![CDATA[10]]></Number>
  			<Info><![CDATA[develope software using c++]]></Info>
  			<Req><![CDATA[undergraduate]]></Req>
  			<Url><![CDATA[none]]></Url>
  		</Job>
  		<Company>
  			<Name><![CDATA[Netease]]></Name>
  			<Info><![CDATA[some company]]></Info>
  			<Url><![CDATA[none]]></Url>
  		</Company>
  		<Apply>
  			<InterviewTime><![CDATA[05.15 9:00]]></InterviewTime>
  			<Tel><![CDATA[1565464654156]]></Tel>
  			<Email><![CDATA[hr@eg.com]]></Email>
  		</Apply>
  		<Attr>
  			<Labels>
  				<Label><![CDATA[python]]></Label>
  				<Label><![CDATA[game]]></Label>
  			</Labels>
  			<Time><![CDATA[2018.05.15]]></Time>
  			<Expire><![CDATA[100]]></Expire>
  		</Attr>
  	</Piece>
  	<!--
  	<Piece>
  		... other pieces
  	</Piece>
  	-->
  </xml>
  ```

### 收藏

* 描述：用户收藏招聘信息时请求的接口

* METHOD：HTTP POST

* URL：目前在本机上测试，上线程序时会放在公网服务器上

* 请求字段(XML)：

  * ReqType：固定为`like`
  * UsrName：用户名
  * Id：收藏信息的ID
  * GetNoti：是否接收通知，取值为`true`或`false`

* HTTP请求的body例子：

  ```xml
  <!-- like -->
  <xml>
  	<ReqType><![CDATA[like]]></ReqType>
  	<UsrName><![CDATA[admin]]></UsrName>
  	<Id><![CDATA[1234]]></Id>
  	<GetNoti><![CDATA[true]]></GetNoti>
  </xml>
  ```

* 返回字段(XML)：

  - ErrInfo：成功时返回`SUCCESS`

    ```
    SUCCESS:		成功
    ...
    ```

* 返回值例子(XML)：

  ```xml
  <!-- like -->
  <xml>
  	<ErrInfo><![CDATA[SUCCESS]]></ErrInfo>
  </xml>
  ```


## 其它

其它需要说明的信息