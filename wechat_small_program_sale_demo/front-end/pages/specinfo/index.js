// pages/specinfo/index.js
Page({
  data:{
     imgUrls: [
      'http://img02.tooopen.com/images/20150928/tooopen_sy_143912755726.jpg',
      'http://img06.tooopen.com/images/20160818/tooopen_sy_175866434296.jpg',
      'http://img06.tooopen.com/images/20160818/tooopen_sy_175833047715.jpg'
    ],
    y:[],
    show:"none",
    scrollY:0,
    value:["小"],
    xz:"点击这里选择",
    id:0,
    seled:0,
    info:{},
    price:[],
    money:0,
    comment:[]
  },
  showsel:function(){
    this.setData({
      show:"",
      scrollY:1000,
      seled:1
    })
  },
  sure:function(e){
    this.setData({
      show:"none",
      xz:this.data.y[e.target.dataset.value[0]],
      money:this.data.price[e.target.dataset.value[0]]
    })
  },
  bindChange:function(e){
    this.setData({
      value:e.detail.value
    })
  }, 
  addBuyCar:function(){
    if(!this.data.seled){
      wx.showToast({
        title: '请先选择型号',
        icon: 'fail',
        duration: 2000
      })
    }else{
      wx.request({
        url: 'https://ganjiacheng.cn/wxapp/addBuyCar.php',
        data: {
          id:this.data.id,
          val:this.data.xz,
          price:this.data.money
        },
        success: function(res){
          console.log(res)
        }
      })
      wx.showToast({
        title: '成功',
        icon: 'success',
        duration: 2000
      })
    }
  },
  onLoad:function(options){
    var that=this
    this.setData({
      id:options.id
    }),
    wx.request({
      url: 'https://ganjiacheng.cn/wxapp/specInfo.php',
      data: {
        id:options.id
      },
      success: function(res){
        console.log(res);
        that.setData({
          info:res.data.info,
          y:res.data.info.type.split(","),
          price:res.data.info.price.split("/"),
          comment:res.data.comment
        })
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