// pages/comment/index.js
Page({
  data:{
    value:[],
    sid:[],
    items:[],
    uid:0,
    oid:0
  },
  onLoad:function(options){
    // 页面初始化 options为页面跳转所带来的参数
    var that=this
    wx.request({
      url: 'https://ganjiacheng.cn/wxapp/comSpecInfo.php',
      data: {
        sid:options.sid
      },
      success: function(res){
        that.setData({
          items:res.data,
          uid:options.uid,
          oid:options.oid
        })
      }
    })
  },
  changeVal:function(e){
    this.data.value[e.currentTarget.dataset.id]=e.detail.value
  },
  submit:function(){
    var data=''
    for(var i in this.data.value){
      data+=i+"&"+this.data.value[i]+"|"
    }
    wx.request({
      url: 'https://ganjiacheng.cn/wxapp/addComment.php',
      data: {
        data:data,
        uid:this.data.uid,
        oid:this.data.oid
      },
      success: function(res){
        if(res.data==1){
          wx.showToast({
            title: '提交成功',
            icon: 'success',
            duration: 2000
          })
          setTimeout(function(){
            wx.hideToast()
            wx.navigateBack({
              delta: 3
            })
          },1500)
        }else{
          wx.showToast({
            title: '提交失败',
            icon: 'fail',
            duration: 2000
          })
        }
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