<template>
  	<div>
		<el-table :data="tableData"style="width: 100%">
			<el-table-column prop="id"label="id"width="180"></el-table-column>
			<el-table-column prop="city"label="city"width="180"></el-table-column>
<!-- 			<el-table-column prop=""label="姓名"width="180"></el-table-column>
			<el-table-column prop="address"label="地址"></el-table-column> -->
		</el-table>
		<div class="block">
			<el-pagination layout="prev, pager, next":total="1000" @current-change="get"></el-pagination>
		</div>
	</div>
</template>


<script>
	export default {
		name: 'page',
		data(){
			return{
				tableData:[],
			}
		},
		mounted: function () {
    		this.get(1);
  		},
		methods:{
			get(val){
				this.$http.get("http://127.0.0.1:8000/city?page="+val).then(function (res) {
					this.tableData=[];
					var data = res.body;
					for (var i=0;i<data.length;i++){
						var a = {};
						a["city"] = data[i].fields.name;
						a["id"] = data[i].pk;
						this.tableData.push(a);
					}
				})
			}
		},
	}
</script>