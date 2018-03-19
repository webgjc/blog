//index.js
//获取应用实例
var app = getApp()
Page({
  data: {
    userInfo: {},
    imgUrls: [],
    uid:0,
    tj:{},
    tjprice:[],
    main1:[],
    main2:[]
  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  //页面加载完成后事件
  onLoad: function () {
    //为了使得回调函数里可以获得外对象的属性
    var that = this
    //加载主要商品信息
    wx.request({
      url: 'https://ganjiacheng.cn/wxapp/mainInfo.php',
      success: function(res){
        console.log(res)
        var arr=res.data.all
        let len=Math.round(res.data.all.length/2)
        var mainl=arr.slice(0,len)
        var mainr=arr.slice(len,res.data.all.length)
        var tjprarr=[];
        for(let j in res.data.tj){
          tjprarr.push(res.data.all[res.data.tj[j][0]-1][3])
        }
        that.setData({
          tj:res.data.tj,
          main1:mainl,
          main2:mainr,
          imgUrls:res.data.lb,
          tjprice:tjprarr
        })
      }
    }),
    //获取个人信息
    wx.getUserInfo({
      success:function(res){
        that.setData({
          userInfo:res.userInfo
        })
      }
    }),
    //登录接口，用于服务器新建/保存信息
    wx.login({
      success:function(res){
        wx.request({
          url: 'https://ganjiacheng.cn/wxapp/login.php',
          data: {
              code: res.code,
              gender:that.data.userInfo.gender,
              username:that.data.userInfo.nickName,
              logourl:that.data.userInfo.avatarUrl
          },
          success: function(res){
            that.setData({
              uid:res.data.id
            })
          }
        })
      }
    })
  }
})
