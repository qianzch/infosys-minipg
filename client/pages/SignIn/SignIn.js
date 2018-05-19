Page({
  data: {
    
  },
  //事件处理函数
  signin: function () {
    wx.switchTab({
      url: '../Home/Home',
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
