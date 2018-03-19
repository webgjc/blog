// pages/buyInfo/index.js
Page({
  data:{
    uid:'',
    addres:'',
    phone:'',
    contain:'',
    price:'',
    sid:''
  },
  onLoad:function(options){
    // 页面初始化 options为页面跳转所带来的参数
    var that=this
    wx.request({
      url: 'https://ganjiacheng.cn/wxapp/userInfo.php',
      data: {
        id:options.uid
      },
      success: function(res){
        that.setData({
          uid:options.uid,
          contain:options.contain,
          price:options.price,
          address:res.data['address'],
          phone:res.data['phone'],
          sid:options.sid
        })
      }
    })
  },
  pay:function(){
    wx.showToast({
      title: '成功支付',
      icon: 'success',
      duration: 2000
    })
    var that=this
    setTimeout(function(){
        wx.request({
        url: 'https://ganjiacheng.cn/wxapp/addOrder.php',
        data: {
          uid:that.data.uid,
          contain:that.data.contain,
          address:that.data.address,
          phone:that.data.phone,
          price:that.data.price,
          sid:that.data.sid
        },
        success: function(res){
          console.log(res)
          if(res.data==1){
            wx.hideToast()
            wx.navigateTo({
              url: '/pages/myorder/index?uid='+that.data.uid
            })
          }else{
             wx.showToast({
                title: '错误,请联系管理员',
                icon: 'fail',
                duration: 2000
              })
          }
        }
      })
    },1500)
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