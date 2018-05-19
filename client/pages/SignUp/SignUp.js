Page({
  data: {
    items: [
      { name: '普通用户', value: '普通用户' },
      { name: '企业用户', value: '企业用户' },
    ]
  },
  signup: function () {
    wx.navigateTo({
      url: '../bind/bind'
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