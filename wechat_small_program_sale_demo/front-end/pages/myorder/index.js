// pages/myorder/index.js
Page({
  data:{
    color:['LightCoral','YellowGreen','DeepSkyBlue','Silver'],
    uid:0,
    orderInfo:[],
    s:["未接单","派送中","未评价","已结束"]
  },
  onLoad:function(options){
    // 页面初始化 options为页面跳转所带来的参数
    this.setData({
      uid:options.uid
    })
    var that=this
    wx.request({
      url: 'https://ganjiacheng.cn/wxapp/myOrder.php',
      data: {
        uid:this.data.uid
      },
      success: function(res){
        console.log(res.data)
        that.setData({
          orderInfo:res.data
        })
      }
    })
  },
  link:function(e){
    if(e.currentTarget.dataset.state==2){
        wx.navigateTo({
          url: '/pages/comment/index?sid='+e.currentTarget.dataset.sid+'&uid='+this.data.uid+'&oid='+e.currentTarget.dataset.oid
        })
    }
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