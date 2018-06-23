Page({
  data: {
    hidden: false
  },
  logout: function () {
    wx.navigateTo({
      url: '../SignIn/SignIn',
    })
  },
  star: function () {
    wx.navigateTo({
      url: '../star/star',
    })
  },
  edit: function () {
    wx.navigateTo({
      url: '../edit/edit'
    })
  },
  onLoad: function (options) {
    // 页面初始化 options为页面跳转所带来的参数
    console.log("user_info OnLoad");
  },
  onReady: function () {
    // 页面渲染完成
    console.log("user_info OnReady");
  },
  onShow: function () {
    // 页面显示
    console.log("user_info OnShow");
  },
  onHide: function () {
    // 页面隐藏
    console.log("user_info OnHide");
  },
  onUnload: function () {
    // 页面关闭
    console.log("user_info OnUnload");
  }
})