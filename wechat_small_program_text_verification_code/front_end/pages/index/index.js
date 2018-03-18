//index.js
//获取应用实例
var app = getApp()
Page({
  data: {
    imgult:'',
    imgfile:''
  },
  //图片预览
  ch:function(e){
    var that=this
    if(that.data.imgfile==''){
      return
    }
    wx.previewImage({
      current: that.data.imgfile,
      urls: [that.data.imgfile] 
    })
  },
  //发送请求
  //成功后把图片下载到本地
  formSubmit: function(e) {
    var that = this
    wx.request({
      url: 'https://yourdomain.com/yzm.php',
      data: {
        data: e.detail.value.input ,
      },
      header: {
          'content-type': 'application/json'
      },
      success: function(res) {
        that.setData({
          imgurl:res.data
        }),
        wx.downloadFile({
          url: 'https://yourdomain.cn/EXAMPLE_TMP_SERVERPATHtest.png',
          success: function(res) {
            var tempFilePaths = res.tempFilePath
            that.setData({     
              imgfile:res.tempFilePath
            })
            //console.log(that.data.imgfile)
          }
        })
      }
    })
  },
})
