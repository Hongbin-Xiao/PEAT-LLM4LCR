<template>
  <div style="position: relative;
  width: 100%; /* 或者其他宽度 */
  height: auto; /* 或者其他高度 */">
    <div class="fileUploadDiv">
      <div><h2 style="text-align: center; line-height: 50px;box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.1);">上传合同</h2>
      </div>

      <div>
        <el-upload
            :limit="1"
            class="upload-drag"
            drag
            :before-upload="beforeUpload"
            :on-success="handleSuccess"
            :on-error="handleError"
            style="margin-top: 10px;box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.1);"
            :http-request="func"
            action=""
        >
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
          <div class="el-upload__tip" slot="tip" style="display: grid; place-items: center; line-height: 30px;">
            只能上传txt文件，限制一个，且不超过500kb
          </div>
        </el-upload>
      </div>

      <el-collapse v-if="isVisible" style="display: flex">

        <el-card style="width: 900px; margin-top: 10px; box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.1);">
          <div slot="header" style="text-align: center">
            <span>原文</span>
          </div>
          <div style="white-space: pre-wrap;text-align: left">{{ fileText }}</div>
        </el-card>

        <el-card style="width: 900px; margin-top: 10px; box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.1);">
          <div slot="header" style="text-align: center">
            <span>建议</span>
          </div>
          <div style="white-space: pre-wrap;text-align: left">内容</div>
        </el-card>
      </el-collapse>

    </div>
  </div>

</template>

<script>
export default {
  name: 'FileInput',

  data() {
    return {
      resultList: [],
      isVisible: false,
      fileText: '',
    }
  },

  methods: {
    func(upload) {

      this.isVisible = false
      const loading = this.$loading({
        lock: true,
        text: '正在审查中',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.7)',
      });

      const formData = new FormData()
      formData.append('file', upload.file)
      console.log(formData)

      //fileAnalysis
      //test
      this.request.post("model/test",
          formData,
          {
            header: {
              'Content-Type': 'multipart/form-data',
            }
          }
      ).then(res => {
        if (res.data) {
          this.fileText = res.data.fileText
          this.isVisible = true
          this.$message.success('文件上传成功！');
        } else {
          this.$message.error('文件上传失败！')
        }
      }).catch(error => {
        this.$message.error('系统异常！')
      }).finally(() => {
        loading.close();
        document.body.style.overflow = '';
        document.body.style.overflowY = 'auto';
      })
    },

    beforeUpload(file) {
      //判断上传的文件是不是txt
      const isTXT = file.type === 'text/plain';

      if (!isTXT) {
        this.$message.error('只能上传txt文件!');
        return false;
      }

      return true;
    },

    handleSuccess(response, file, fileList) {
      this.$message.success('文件上传成功！');
    },

    handleError(err, file, fileList) {
      this.$message.error('文件上传失败！');
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

.headLine {
  width: 1000px;
  height: 83px;
  display: flex;
  align-items: center;
}

.upload-drag {
  text-align: center;
}

.upload-drag .el-upload__text {
  color: #606266;
}

.upload-drag .el-upload__text em {
  color: #409eff;
}

.el-upload-dragger {
  width: 1000px;
  height: 300px;
}

.fileUploadDiv {
  position: absolute;
  top: -180px;
  left: 50%;
  transform: translateX(-50%);

}

.el-collapse-item__header {
  display: flex;
  align-items: center;
  justify-content: center;
}

.el-collapse-item__arrow {
  margin: 0px;
}

.el-card__body {
  padding-top: 0px;
}

.el-upload__tip {
  margin-top: 0px;
}

.el-upload-list__item-name {
  padding: 0px;
  margin: 0px;
}

.el-upload-list__item:first-child {
  margin: 0px;
}
</style>