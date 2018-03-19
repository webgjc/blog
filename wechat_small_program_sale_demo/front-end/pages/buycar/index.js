// pages/buycar/index.js
const nums=[]
for(var i=0;i<21;i++){
  nums.push(i);
}
Page({
  data:{
    num:0,
    nums:nums,
    value: [10],
    state:"none",
    items: [],
    allprice:0.0,
    tmpid:0,
    svalue:0,
    uid:0,
    data:[],
    display:"",
    checked:[]
  },
  //勾选时计算总价
  checkboxChange: function(e) {
    let j=0
    for(var i in e.detail.value){
      j+=this.data.items[e.detail.value[parseInt(i)]].price*this.data.items[e.detail.value[parseInt(i)]].num
    }
    this.setData({
      checked:e.detail.value,
      allprice:j
    })
  },
  //改变数量
  show:function(e){
    this.setData({
      state:'',
      ss:1,
      tmpid:e.target.dataset.id,
      value:[this.data.items[e.target.dataset.id].num]
    })
  },
  //修改购物车物品数量
  sure:function(e){
    let obj=this.data.items
    var that=this
    obj[e.target.dataset.id].num=e.target.dataset.value
    this.setData({
      state:'none',
      items:obj
    }),
    wx.request({
      url: 'https://ganjiacheng.cn/wxapp/changeNum.php',
      data: {
        uid:this.data.uid,
        id:e.target.dataset.id,
        num:e.target.dataset.value
      },
      success: function(res){
        console.log(res)
        if(res.data===1){
          wx.showToast({
            title: '修改成功',
            icon: 'success',
            duration: 2000
          })
        }else if(res.data===0){
          wx.showToast({
            title: '修改失败',
            icon: 'fail',
            duration: 2000
          })
        }else{
          wx.showToast({
            title: '修改成功',
            icon: 'success',
            duration: 2000
          })
          var arr=that.data.items
          arr.splice(res.data[0],1)
          console.log(arr)
          that.setData({
            items:arr
          })
        }
      }
    })
  },
  //
  bindChange: function(e) {
    this.setData({
      svalue:e.detail.value[0]
    })
  },
  //加载购物车数据
  onLoad:function(options){
    var that=this
    this.setData({
      uid:options.uid
    })
    wx.request({
      url: 'https://ganjiacheng.cn/wxapp/buyCar.php',
      data: {
        uid:this.data.uid
      },
      success: function(res){
        if(res.data[0].num==null){
          var display="none"
        }else{
          var display=''
        }
        that.setData({
          items:res.data,
          display:display
        })
      }
    })
  },
  //下单
  buy:function(){
    if(this.data.checked==''){
      console.log(1)
    }else{
      var name=''
      var sid=''
      var tmparr=[]
      for(let i in this.data.checked){
        name+=this.data.items[this.data.checked[i]].name+this.data.items[this.data.checked[i]].type+"x"+this.data.items[this.data.checked[i]].num+","
        if(tmparr.indexOf(this.data.items[this.data.checked[i]].sid)==-1){
          sid+=this.data.items[this.data.checked[i]].sid+","
          tmparr.push(this.data.items[this.data.checked[i]].sid)
        }
      }
      wx.navigateTo({
        url: '/pages/buyInfo/index?uid='+this.data.uid+'&contain='+name+''+'&price='+this.data.allprice+"&sid="+sid
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