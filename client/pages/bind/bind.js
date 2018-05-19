Page({
  data: {
    hidden: false
  },
  next: function () {
    wx.navigateTo({
      url: '../SignIn/SignIn'
    })
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