Page({
  data: {

  },
  cancel: function () {
    wx.switchTab({
      url: '../Home/Home'
    })
  },
  confirm: function () {
    wx.switchTab({
      url: '../Home/Home'
    })
  },
  onLoad: function (options) {
    // 页面初始化 options为页面跳转所带来的参数
    console.log("edit OnLoad");
  },
  onReady: function () {
    // 页面渲染完成
    console.log("edit OnReady");
  },
  onShow: function () {
    // 页面显示
    console.log("edit OnShow");
  },
  onHide: function () {
    // 页面隐藏
    console.log("edit OnHide");
  },
  onUnload: function () {
    // 页面关闭
    console.log("edit OnUnload");
  }
})