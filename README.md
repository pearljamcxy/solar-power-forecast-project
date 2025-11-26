## 1️⃣ 激活虚拟环境（每次开始工作时执行）

cd E:\solar-power-forecast-project
venv\Scripts\Activate

出现：
(venv) PS E:\solar-power-forecast-project>
## 2️⃣ 打开 VS Code（在虚拟环境激活状态下执行）

code .
请确保 VS Code 使用当前 venv 的 Python 解释器。

## 3️⃣ 开发工作说明（notebooks / src / api）

- notebooks/          → EDA、特征工程、模型训练  
- src/                → data_loader、feature_engineering、model_utils  
- api/                → FastAPI 接口文件  
- data/raw/           → 原始数据（不会上传 GitHub）  
- data/processed/     → 处理后数据（不会上传 GitHub）

随时可查看更改：

git status

## 4️⃣ 添加全部更改

git add .

## 5️⃣ 提交更改（写清楚内容）

git commit -m "你的说明，例如：Add EDA notebook"

## 6️⃣ 推送到 GitHub（同步 main 分支）

git push（因为已设置 tracking，之后都只需这一个命令）

## 7️⃣ 安装新库并更新 requirements.txt

安装新库：pip install 库名

更新依赖：

pip freeze > requirements.txt

## 8️⃣ 退出虚拟环境（结束一天工作）

deactivate

## 9️⃣ 若未来遇到 GitHub 推送冲突（极少发生）

### ✔ 若想保留 GitHub 中的更改：
git pull

### ✔ 若本地为主，覆盖 GitHub：
git push --force

# 🎉 每天开发流程总结

激活 venv  
→ code .  
→ 写代码  
→ git add  
→ git commit  
→ git push  
→ deactivate（可选）