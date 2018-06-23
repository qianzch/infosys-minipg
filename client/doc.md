# 客户端开发文档

## 接口说明

### 注册

> 如果服务端还没有完成相关接口，此处可以提出对接口的期望，如果服务端接口与需求不一致，可以提在issue中

* 如：希望服务端给出注册接口

  * 描述：注册时请求的接口

  * METHOD：HTTP GET

  * URL：www.example.com/reg.py

  * 字段：

    * usr_name
    * passwd

  * e.g. www.example.com/reg.py?usr_name=root&passwd=123456

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
    101:	Invalid Passwd
    102:	User Already Existes
    ...
    ```

## 其它

其它需要说明的信息