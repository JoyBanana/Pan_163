var app3 = new Vue({
  el: '#app3',
  data: {
    json_data: [null, 0],
    shadow1: 'hover',
    shadow2: 'hover',
    shadow3: 'hover',
    background1: 'background:#FFFFFF',
    background2: 'background:#FFFFFF',
    background3: 'background:#FFFFFF',
    tableDDD: null
  },
  methods: {
    change_shadow1: function() {
      this.shadow1 = 'always',
        this.shadow2 = 'hover',
        this.shadow3 = 'hover',
        this.background1 = 'background:#ECF5FF',
        this.background2 = 'background:#FFFFFF',
        this.background3 = 'background:#FFFFFF'
    },
    change_shadow2: function() {
      this.shadow1 = 'hover',
        this.shadow2 = 'always',
        this.shadow3 = 'hover',
        this.background1 = 'background:#FFFFFF',
        this.background2 = 'background:#ECF5FF',
        this.background3 = 'background:#FFFFFF'
    },
    change_shadow3: function() {
      this.shadow1 = 'hover',
        this.shadow2 = 'hover',
        this.shadow3 = 'always',
        this.background1 = 'background:#FFFFFF',
        this.background2 = 'background:#FFFFFF',
        this.background3 = 'background:#ECF5FF',
        NProgress.start();
      axios //ajax请求后端接口
        .get('http://localhost:5000/files')
        .then(response => {
          (this.json_data = response.data), this.tableDDD = this.json_data[0].slice(0,10), NProgress.done(),
            this.$message({
              message: '数据更新成功',
              type: 'success'
            })
        }).catch(function(error) {
          NProgress.done();
          this.app3.$message.error('获取数据失败');
        })

    },
    checkDetail: function(value) {//跳转下载文件
      window.open('https://joybanana.nos-eastchina1.126.net/' + value)
    },
    handleCurrentChange(value) { //按照页码返回对应数据
      //value是当前的页码,每页10条
      //先判断是不是最后一页
      var ttt = this.json_data[0].length - (value * 10 - 10)
      if (ttt < 10) { //是最后一页
        this.tableDDD = this.json_data[0].slice((value * 10 - 10),this.json_data[0].length)
      } else {
        this.tableDDD = this.json_data[0].slice((value * 10 - 10),(value * 10))
      }
    }
  },
  computed: {
    usedHint: function() { //显示出来使用容量
      return ('已使用' + this.usedPercent + '%');
    },
    usedPercent: function() { //计算使用了多少容量%
      return (Number((this.json_data[1] / 530000000).toFixed(1))); //这个值大概是50G
    },
    list_total: function() { //计算有多少条数据
      if (this.json_data[0] == null) {
        return 0
      } else {
        return this.json_data[0].length
      }
    }
  }
});
