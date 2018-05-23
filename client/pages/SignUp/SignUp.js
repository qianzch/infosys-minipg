let data = require('./data.mock.js');

let parser = require('../../utils/util.js');
let jsonToXML = parser.jsonToXML;
let XMLToJson = parser.XMLToJson;

const baseUrl = "http://localhost:80";

Page({
  data: {
    userName: '',
    userPwd1: "",
    userPwd2: "",
    items: [
      { name: '普通用户', value: '普通用户' },
      { name: '企业用户', value: '企业用户' },
    ]
  },
  userNameInput: function (e) {
    this.setData({
      userName: e.detail.value
    })
  },
  passWdInput1: function (e) {
    this.setData({
      userPwd1: e.detail.value
    })
  },
  passWdInput2: function (e) {
    this.setData({
      userPwd2: e.detail.value
    })
  },
  signup: function (e) {
    if(this.data.userPwd1 == this.data.userPwd2)
    {
      console.log("用户名：" + this.data.userName + " 密码：" + this.data.userPwd1);
      let username = this.data.userName;
      let pass = this.data.userPwd1;
      let xml_request = jsonToXML(username, pass);
      this.send(xml_request, function (res) {

        if (res) {

        }
      });

      wx.navigateTo({
        url: '../bind/bind'
      })
    }
  
  },
  send: function (xml_request, callback) {
    wx.request({
      url: baseUrl,
      data: xml_request,
      method: "POST",
      success: function (res) {
        console.log(res);
        callback(res);
      },
      complete: function () {
        console.info("complete request");
      }
    })
  },
  onLoad: function (options) {
    // 页面初始化 options为页面跳转所带来的参数
    console.log("Sign Up OnLoad");
  },
  onReady: function () {
    // 页面渲染完成
    console.log("Sign Up OnReady");
  },
  onShow: function () {
    // 页面显示
    console.log("Sign Up OnShow");
  },
  onHide: function () {
    // 页面隐藏
    console.log("Sign Up OnHide");
  },
  onUnload: function () {
    // 页面关闭
    console.log("Sign Up OnUnload");
  }
})