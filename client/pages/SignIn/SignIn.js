let data = require('./data.mock.js');
const baseUrl = "http://localhost:80";
let parser = require('../../utils/util.js');
let jsonToXML = parser.jsonToXML;
let XMLToJson = parser.XMLToJson;

Page({
  data: {
    userName: '',
    userPwd: ""
  },
  //事件处理函数
  userNameInput: function (e) {
    this.setData({
      userName: e.detail.value
    })
  },
  passWdInput: function (e) {
    this.setData({
      userPwd: e.detail.value
    })
  },
  signin: function (e) {
    console.log("用户名：" + this.data.userName + " 密码：" + this.data.userPwd);
    let username = this.data.userName;
    let pass = this.data.userPwd;
    let xml_request = jsonToXML(username, pass);
    this.checkValid(
      xml_request, function(res) {

      if(res) {

      }
    }),
    wx.switchTab({
      url: '../Home/Home',
    });
    
  }, 
  checkValid: function (xml_request, callback) {
    wx.request({
      url: baseUrl, //+ '/user/signin',
      data: xml_request,
      method:"POST",
      success:function(res) {
        console.log(res);
        callback(res);
      },
      complete:function() {
        console.info("complete request");
      }
    })
  },
  onLoad: function (options) {
    // 页面初始化 options为页面跳转所带来的参数
    console.log("Sign In OnLoad");
  },
  onReady: function () {
    // 页面渲染完成
    console.log("Sign In OnReady");
  },
  onShow: function () {
    // 页面显示
    console.log("Sign In OnShow");
  },
  onHide: function () {
    // 页面隐藏
    console.log("Sign In OnHide");
  },
  onUnload: function () {
    // 页面关闭
    console.log("Sign In OnUnload");
  }
})
