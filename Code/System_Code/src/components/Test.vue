<template>
  <el-card>
    <div
      ref="textContainer"
      contenteditable
      @mouseup="handleSelection"
    >{{ text }}</div>
    <div v-for="(result, index) in results" :key="index" :ref="`result-${index}`">
      <span @click="scrollToResult(index)">{{ result.text }}</span>: {{ result.data }}
    </div>
  </el-card>
</template>

<script>
export default {
  data() {
    return {
      text: '这里是需要分析的文本内容...',
      selectedTexts: [],
      results: []
    };
  },
  methods: {

  }
};
</script>