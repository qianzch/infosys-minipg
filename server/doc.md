# 服务端开发文档

## 接口说明

### 登录

* 一个接口说明的例子：

  * 描述：登录时请求的接口

  * METHOD：HTTP GET

  * URL：www.example.com/login.py

  * 字段：

    * usr_name
    * passwd

  * e.g. www.example.com/login.py?usr_name=root&passwd=123456

  * 返回：json

    ```json
    {
        "status": "success",
        "err_code": "0"
        ...
    }
    ```

  * Error Code

    ```
    0:		Success
    101:	Wrong Passwd
    102:	Invalid User
    ...
    ```

## 其它

其它需要说明的信息