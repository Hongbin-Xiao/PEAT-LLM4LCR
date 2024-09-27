<template>
  <div style="position: relative;
  width: 100%; /* 或者其他宽度 */
  height: auto; /* 或者其他高度 */">
    <div class="fileUploadDiv">

      <div>
        <el-upload
            :limit="1"
            class="upload-drag"
            drag
            :before-upload="beforeUpload"
            :on-success="handleSuccess"
            :on-error="handleError"
            style="margin-top: 10px;box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.1);"
            :http-request="fileUpload"
            action=""
        >
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
          <div class="el-upload__tip" slot="tip" style="display: grid; place-items: center; line-height: 30px;">
            只能上传txt文件，限制一个，且不超过500kb
          </div>
        </el-upload>
      </div>

      <!--上传合同——标题-->
      <div>
        <el-button @click="analysis"
                   style="width:100%;font-size: 20px; text-align: center; line-height: 50px;box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.1);">
          上传合同
        </el-button>
      </div>

      <div style="display: flex; font-size: 25px;">

        <el-card v-if="isVisible" ref="contract"
                 style="width:50%; margin-top: 10px; box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.1);">

          <div slot="header" style="text-align: center">
            <span>原文</span>
          </div>

          <!--合同原文-->
          <div style="white-space: pre-wrap;text-align: left"
               ref="textContainer"
               contenteditable
               @mouseup="handleSelection"
               contenteditable="false"
          >
            {{ fileText }}
          </div>

        </el-card>

        <el-card :body-style="{ overflow: 'visible' }" v-if="isVisible2" style="width:50%; margin-top: 10px; box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.1);">

          <div slot="header" style="text-align: center">
            <span>建议</span>
          </div>

          <el-collapse>
            <el-collapse-item title="主体与基本要素建议" name="1">
              <el-input size="medium" type="textarea" autosize style="width: 100%; font-size: 15px;" v-model="resultList[0]" autosize
                        readonly/>
            </el-collapse-item>

            <el-collapse-item title="高风险建议" name="2">
              <el-input size="medium" type="textarea" autosize style="width: 100%; font-size: 15px;" v-model="resultList[1]"/>
            </el-collapse-item>

            <el-collapse-item title="核心条款" name="3">
              <el-input size="medium" type="textarea" autosize style="width: 100%; font-size: 15px;" v-model="resultList[2]"/>
            </el-collapse-item>

            <el-collapse-item title="知识产权" name="4">
              <el-input size="medium" type="textarea" autosize style="width: 100%; font-size: 15px;" v-model="resultList[3]"/>
            </el-collapse-item>
          </el-collapse>

          <!--审查结果
          <div v-for="(result,index) in resultList" :key="index" :ref="`result-${index}`">
            <span @click="scrollToResult(index)">{{ result }}</span>
          </div>
          <div style="white-space: pre-wrap;text-align: left">{{ text }}</div>
          -->
        </el-card>
      </div>

      <!--
      <el-collapse v-if="isVisible">

        <el-card style="width: 100%; margin-top: 10px; box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.1);">

          <div slot="header" style="text-align: center">
            <span>审查结果</span>
          </div>

          <el-collapse-item title="主体与基本要素建议" name="1">
            <el-input size="medium" type="textarea" autosize style="width: 100%" v-model="resultList[0]" autosize
                      readonly/>
          </el-collapse-item>

          <el-collapse-item title="高风险建议" name="2">
            <el-input size="medium" type="textarea" autosize style="width: 100%" v-model="resultList[1]"/>
          </el-collapse-item>

          <el-collapse-item title="核心条款" name="3">
            <el-input size="medium" type="textarea" autosize style="width: 100%" v-model="resultList[2]"/>
          </el-collapse-item>

          <el-collapse-item title="知识产权" name="4">
            <el-input size="medium" type="textarea" autosize style="width: 100%" v-model="resultList[3]"/>
          </el-collapse-item>

        </el-card>

      </el-collapse>
      -->
    </div>
  </div>

</template>

<script>
export default {
  name: 'FileInput',

  data() {
    return {
      resultList: [],//建议的list
      isVisible: false,//原文是否可见
      isVisible2: false,//建议是否可见
      fileName: '',//合同名称
      fileText: '',//合同文本
      text: '',

      //标识选中文本需要的参数
      selectedTexts: [],// 保存用户选择的文本和位置信息
      processedText: ''
    }
  },

  methods: {

    beforeUpload(file) {
      //判断上传的文件是不是txt
      const isTXT = file.type === 'text/plain';
      if (!isTXT) {
        this.$message.error('只能上传txt文件!');
        return false;
      }

      return true;
    },

    fileUpload(upload) {

      this.isVisible = false
      this.isVisible2 = false
      const loading = this.$loading({
        lock: true,
        text: '文件读取中',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.7)',
      });

      const formData = new FormData()
      formData.append('file', upload.file)

      //fileAnalysis
      //test
      this.request.post("model/fileAnalysis",
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
          //this.fileName = upload.file.name

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

    //选中文本标红
    handleSelection() {
      const selection = window.getSelection();
      if (selection.rangeCount > 0 && !selection.isCollapsed) {
        const range = selection.getRangeAt(0);
        const selectedText = selection.toString();

        // 检查是否已经包装过
        if (range.commonAncestorContainer.nodeType === Node.ELEMENT_NODE && range.commonAncestorContainer.nodeName === 'SPAN') {
          // 已经是高亮的文本，不进行操作
          return;
        }

        // 检查选中的文本是否非空
        if (selectedText.trim().length > 0) {
          const span = document.createElement('span');
          span.style = 'font-weight:bold; color:red;';
          span.appendChild(range.extractContents());
          range.insertNode(span);

          // 将选中的文本存储起来
          this.selectedTexts.push(selectedText.trim());
        }
      }
      console.log(this.selectedTexts)
    },

    analysis() {
      const loading = this.$loading({
        lock: true,
        text: '审查中...',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.7)',
      });

      this.request.post("model/fileAnalysis", {'selectedTexts': this.selectedTexts}).then(res => {
        this.resultList = res.data.results
        this.selectedTexts = []
        this.isVisible2 = true
        this.$message.success('审查完成！')
      }).catch(error => {
        this.$message.error('系统异常！')
      }).finally(() => {
        loading.close();
      })
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
  width: 1875px;
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
