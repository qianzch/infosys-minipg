Page({
  data: {

  },
  more: function () {
    wx.navigateTo({
      url: '../more_info/more_info'
    })
  },
  onLoad: function (options) {
    // 页面初始化 options为页面跳转所带来的参数
    console.log("Star OnLoad");
  },
  onReady: function () {
    // 页面渲染完成
    console.log("Star OnReady");
  },
  onShow: function () {
    // 页面显示
    console.log("Star OnShow");
  },
  onHide: function () {
    // 页面隐藏
    console.log("Star OnHide");
  },
  onUnload: function () {
    // 页面关闭
    console.log("Star OnUnload");
  }
})