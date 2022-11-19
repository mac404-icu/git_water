# git 自动灌水工具

## git auto upload
需要以管理员权限运行
## 奇怪的需求
通过修改系统时间，在一段时间内随机批量commit代码文件。

## 可设置的参数

||||
|----|----|----|
begin_str | "2022/07/30" | 开始日期
end_str | "2022/11/19" | 结束日期
begin_hour | 9 | 每天开始工作时间
end_hour | 17 | 每天结束工作时间
is_955 | True | True：节假日不提交；False：节假日也提交
src_root | "D:/project_2022/code" | 准备好的样板代码
dis_root | "D:/project_2022/empty" | 仅执行了git init的空项目