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
        change_shadow1: function () {
            this.shadow1 = 'always',
                this.shadow2 = 'hover',
                this.shadow3 = 'hover',
                this.background1 = 'background:#ECF5FF',
                this.background2 = 'background:#FFFFFF',
                this.background3 = 'background:#FFFFFF'
        },
        change_shadow2: function () {
            this.shadow1 = 'hover',
                this.shadow2 = 'always',
                this.shadow3 = 'hover',
                this.background1 = 'background:#FFFFFF',
                this.background2 = 'background:#ECF5FF',
                this.background3 = 'background:#FFFFFF'
        },
        change_shadow3: function () {
            this.shadow1 = 'hover',
                this.shadow2 = 'hover',
                this.shadow3 = 'always',
                this.background1 = 'background:#FFFFFF',
                this.background2 = 'background:#FFFFFF',
                this.background3 = 'background:#ECF5FF',
                NProgress.start();
            axios
                .get('http://39.96.4.4:5000/files')
                .then(response => {
                    (this.json_data = response.data), this.tableDDD = this.json_data[0], NProgress.done(),
                        this.$message({
                            message: '数据更新成功',
                            type: 'success'
                        })
                }).catch(function (error) {
                NProgress.done();
                this.app3.$message.error('获取数据失败');
            })

        }
    },
    computed: {
        usedHint: function () {
            return ('已使用' + this.usedPercent + '%');
        },
        usedPercent: function () {
            return (Number((this.json_data[1] / 530000000).toFixed(1))); //这个值大概是50G
        },
    }
});
