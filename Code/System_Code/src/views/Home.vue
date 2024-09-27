<template>
  <el-container>

    <!--头部区域-->
    <el-header style=" height:auto; display: flex;">
      <Header/>
    </el-header>

    <!--主体区域-->
    <el-main style=" height:auto; display: flex;overflow: visible">
      <FileInput/>
    </el-main>

  </el-container>
</template>

<script>
import Header from "../components/Header.vue";
import FileInput from "../components/FileUpload.vue";
export default {
  components:{Header,FileInput},
}
</script>

<style>
  body{
    margin: 0px;
    padding: 0px;
  }
</style>
