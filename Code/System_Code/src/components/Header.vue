<template xmlns="http://www.w3.org/1999/html">
  <div style="position: relative">

    <div class="introduceText">
      <h2 style="font-weight: 400;font-size: xxx-large;margin: 0px">
        LLM4LCR
      </h2>
      <p style="margin: 0px;letter-spacing: 5px;">基于大语言模型的法律合同审查方法</p>
      <br></br>
      <div style="letter-spacing: 5px;">
        采用深度学习、自然语言处理技术、知识图谱等人工智能技术，模拟专业律师的合同审核能力，实现对合同的分类识别、风险评估，从而代替人工完成对合同的智能审查，并给出专业的修改意见
      </div>
    </div>

    <el-image :src="require('../assets/pro-banner5.png')" style="max-height: 70%"></el-image>
  </div>
</template>

<script>
export default {
  name: 'Header'
}
</script>

<style>
.introduceText {
  position: absolute;
  top: 30%; /* 根据需要调整 */
  left: 30%; /* 根据需要调整 */
  z-index: 10; /* 确保文本在图片之上 */
  color: #fff; /* 文字颜色，根据背景调整 */
  transform: translate(-50%, -50%); /* 居中对齐 */
  text-align: left;
  width: 550px;
  font-weight: 200;
}
</style>