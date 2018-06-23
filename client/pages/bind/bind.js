let data = require('./data.mock.js');

let parser = require('../../utils/util.js');
let jsonToXML = parser.jsonToXML;
let XMLToJson = parser.XMLToJson;

const baseUrl = "http://localhost:80";


Page({
  data: {
    userEmail:'',
    userInput: "",
    userGet: "075628",
    message:'The identifying code is ',
    hidden: false
  },
  userEmailInput:function(e) {
    this.setData({
      userEmail: e.detail.value
    })
  },
  userGetInput: function (e) {
    this.setData({
      userGet: e.detail.value
    })
  },
  send:function(){

    let xml_request = jsonToXML(this.data.message, this.data.userGet);
    this.checkValid(xml_request, function (res) {

      if (res) {

      }
    });
  },
  checkValid: function (xml_request, callback) {
    wx.request({
      url:'www.'+ this.data.userEmail,
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
  next: function () {
    if(this.data.userGet.match( this.data.userInput) != null)
    {
      wx.navigateTo({
        url: '../SignIn/SignIn'
      })
    }
    
  },
  skip: function () {
    wx.navigateTo({
      url: '../SignIn/SignIn'
    })
  },
  onLoad: function (options) {
    // 页面初始化 options为页面跳转所带来的参数
    console.log("bind OnLoad");
  },
  onReady: function () {
    // 页面渲染完成
    console.log("bind OnReady");
  },
  onShow: function () {
    // 页面显示
    console.log("bind OnShow");
  },
  onHide: function () {
    // 页面隐藏
    console.log("bind OnHide");
  },
  onUnload: function () {
    // 页面关闭
    console.log("bind OnUnload");
  }
})