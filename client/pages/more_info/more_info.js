Page({
  data: {
    hidden1: false,
    hidden2: false
  },
  edit: function () {
    wx.navigateTo({
      url: '../edit/edit'
    })
  },
  onLoad: function (options) {
    // 页面初始化 options为页面跳转所带来的参数
    console.log("more_info OnLoad");
  },
  onReady: function () {
    // 页面渲染完成
    console.log("more_info OnReady");
  },
  onShow: function () {
    // 页面显示
    console.log("more_info OnShow");
  },
  onHide: function () {
    // 页面隐藏
    console.log("more_info OnHide");
  },
  onUnload: function () {
    // 页面关闭
    console.log("more_info OnUnload");
  }
})