// pages/changeinfo/index.js
Page({
  data:{
    address:"",
    phone:"",
    id:0
  },
  onLoad:function(options){
    this.setData({
      id:options.id
    })
  },
  onReady:function(){
    // 页面渲染完成
  },
  submit:function(){
    var that=this
    wx.request({
      url: 'https://ganjiacheng.cn/wxapp/editInfo.php',
      data: {
        address:this.data.address,
        phone:this.data.phone,
        id:this.data.id
      },
      success: function(res){
        if(res.data==1){
          wx.redirectTo({
              url: "/pages/myinfo/index?uid="+that.data.id
          })
        }
      }
    })
  },
  bindAddressInput:function(e){
    this.setData({
      address:e.detail.value
    })
  },
  bindPhoneInput:function(e){
    this.setData({
      phone:e.detail.value
    })
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