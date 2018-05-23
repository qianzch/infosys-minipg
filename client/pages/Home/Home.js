let data = require('./data.mock.js');

let parser = require('../../utils/util.js');
let jsonToXML = parser.jsonToXML;
let XMLToJson = parser.XMLToJson;

const baseUrl = "http://localhost:80";

Page({
  data: {
    content:""
  },
  userQuery: function (e) {
    this.setData({
      content: e.detail.value
    })
  },
  sendKeyWd: function(){
    let xml_request = jsonToXML(" ",this.data.content);
    this.send(xml_request, function (res) {

      if (res) {

      }
    });
  },
  send: function (xml_request, callback) {
    wx.request({
      url: baseUrl + '/user/signup',
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
  more: function () {
    wx.navigateTo({
      url: '../more_info/more_info'
    })
  },
  onLoad: function (options) {
    // 页面初始化 options为页面跳转所带来的参数
    console.log("Home OnLoad");
  },
  onReady: function () {
    // 页面渲染完成
    console.log("Home OnReady");
  },
  onShow: function () {
    // 页面显示
    console.log("Home OnShow");
  },
  onHide: function () {
    // 页面隐藏
    console.log("Home OnHide");
  },
  onUnload: function () {
    // 页面关闭
    console.log("Home OnUnload");
  }
})