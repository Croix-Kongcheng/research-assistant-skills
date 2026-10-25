# 贡献与维护

每个技能放在 `skills/<skill-name>/`，目录名和 `SKILL.md` 的 `name` 使用同一个小写连字符名称。技能应可独立复制使用，需要的参考文件放在技能自身目录内。

## 修改现有技能

1. 在相应技能内更新规则；共同的工作区约定先修改 `docs/configuration.md`，再同步到两个现有技能各自的 `references/workspace-config.md`。
2. 对照原有能力检查是否误删段落、公式、图片、导航、续写或审校要求。普通笔记的精炼默认值不能替代用户要求的全文精读范围。
3. 执行 `python scripts/validate_skills.py`；新增脚本还要实际运行。结构校验通过后，按改动选择一个隔离工作区中的真实使用情境检查行为。
4. 提交清楚的变更说明，记录实际验证范围，再推送或提出 Pull Request。

不要把个人配置、电脑绝对路径、未经同意的私有笔记、认证信息或未获再分发许可的论文原件混入公开技能。公开示例放在 `examples/`，与技能运行资源分开；实际笔记须经所有者同意，整理相对链接、图片、来源和导出信息，并保留科学结论的证据边界。第三方图和改编材料保留各自许可，不能统一改标 MIT。

## 新增技能

- `SKILL.md` 要有准确的 `name` 与 `description`，说明何时使用；复杂模式再拆到 `references/`。
- 每个引用的本地运行资源都应随该技能发布，不依赖作者电脑或仓库以外的私人文件。
- 如果使用共享工作区约定，把相同的 `workspace-config.md` 随技能发布，并在入口中链接；不需要这套配置的技能可以保持独立。
- 绘图、PDF 或其他代理技能如果只是增强功能，应明确为可选，不隐含要求安装整套个人环境。
- 在 README 技能表中添加入口，并按实际能力补充最小使用示例。
- 在 `THIRD_PARTY_NOTICES.md` 记录改编文字、第三方图片和独立许可；示例应注明真实数据或合成数据。

## 本地更新到 GitHub

```bash
git pull --ff-only
python scripts/validate_skills.py
git add skills docs examples README.md CONTRIBUTING.md scripts
git commit -m "Describe the concrete skill change"
git push
```

使用者已经安装的技能不一定随仓库同步更新；通过其实际安装方式更新完整技能目录，并保留自己的工作区配置。
