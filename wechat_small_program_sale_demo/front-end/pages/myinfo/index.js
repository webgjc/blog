// pages/myinfo/index.js
var app = getApp()
Page({
  data:{
    userinfo:{
      address:"",
      phone:""
    },
    id:0
  },
  onLoad:function(options){
    // 页面初始化 options为页面跳转所带来的参数
    var that=this
    wx.request({
      url: 'https://ganjiacheng.cn/wxapp/userInfo.php',
      data: {id:options.uid},
      method: 'GET', 
      success: function(res){
        console.log(res.data.id);
        res.data.address=res.data.address==""?"未填写":res.data.address
        res.data.phone=res.data.phone==""?"未填写":res.data.phone
        that.setData({
          userinfo:{
            avatarUrl:res.data.logourl,
            nickName:res.data.username,
            address:res.data.address,
            phone:res.data.phone
          },
          id:options.uid
        })
      },
      fail: function(res) {
        // fail
      },
      complete: function(res) {
        // complete
      }
    })
  },
  onReady:function(){
    // 页面渲染完成
  },
  onShow:function(){
    // 页面显示
  },
  onHide:function(){
    // 页面隐藏
  },
  onUnload:function(){
    // 页面关闭
  }
})