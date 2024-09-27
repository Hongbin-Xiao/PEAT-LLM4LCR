<template>
  <div class="center-div" id="app">

    <div class="headLine"><h2>Causality in Requirements Artifacts (CiRA)</h2></div>

    <div class="nav">
      <a>Home</a>
      <a>Demonstration</a>
      <a>Examples</a>
      <a>References</a>
    </div>

    <div>
      <h2>Causality Extraction: Demo</h2>

      <p>On this page you can explore the automatic, step-wise extraction of cause-effect relations from natural
        language sentences through our accessible online demo. The code behind this demonstration is open source and
        publicly available on GitHub. You can also look at some examples for inspiration.</p>

      <div class="core">
        <h2>Step 1: Classification</h2>

        <p>Enter a requirements and click 'analyze' to let CiRA automatically determine whether the requirement is
          causal and hence eligible for further processing. You can find more details on the classifier in our
          corresponding paper.</p>

      </div>

    </div>

    <div>
      <el-input v-model="url" placeholder="请输入内容" clearable size="medium" style="width: 90%"></el-input>
      <el-button type="primary" @click="func">提交分析</el-button>
    </div>

    <el-form>
      <el-input size="medium" type="textarea" autosize style="width: 100%" v-for="(item, index) in resultList"
                :key="index" :value="item">{{ item }}
      </el-input>
    </el-form>

    <el-upload
        :limit="1"
        class="upload-drag"
        drag
        :before-upload="beforeUpload"
        :on-success="handleSuccess"
        :on-error="handleError"
        action=""
        :http-request="func"
        style=""
    >
      <i class="el-icon-upload"></i>
      <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
      <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb</div>
    </el-upload>

  </div>
</template>
<style>
.el-header, .el-footer {
  background-color: #B3C0D1;
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-aside {
  background-color: #D3DCE6;
  color: #333;
  text-align: center;
  line-height: 200px;
}

.el-main {
  background-color: #E9EEF3;
  color: #333;
  text-align: center;
  line-height: 160px;
}

body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
</style>

<script>
export default {
  data() {
    return {
      url: '',
      resultList: [],
    }
  },

  methods: {
    func() {
      this.request.get("model/test2", {params: {'url': this.url}}).then(res => {
        if (res.data) {
          this.resultList = res.data.result
          this.$message.success('成功！')
        } else {
          this.$message.error('失败！')
        }
      }).catch(error => {
        this.$message.error('系统异常！')
      })
    },
  }
}

</script>

<style>

body {
  background-color: #f7f7f7;
  color: rgb(49, 46, 46);
  margin: 0px 114px;
  padding: 50px 20px;
}

a {
  padding: 0px 8px;
}

h2 {
  margin: 17px 0px;
}

p {
  margin: 14px 0px;
}

.center-div {
  /*display: flex;*/
  justify-content: center;
  align-items: center;
  margin: 0 auto;
  height: 380px;
  width: 1000px;
  background-color: white;
}

.headLine {
  width: 1000px;
  height: 83px;
  display: flex;
  align-items: center;
}
</style>