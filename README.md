# Multi-Omics BioDB（Django）

这是一个基于 Django 的**多组学生物信息数据库**示例项目，支持：

- 基因 ID / Symbol 搜索与查询
- 基因详情展示（跨组学测量结果）
- 多个组学门户页面（基因组、转录组、蛋白组、代谢组、表观组）
- 数据下载与文档/API 门户页面
- Django Admin 后台管理

## 功能页面

- 首页：`/`
- 基因检索：`/search/`
- 基因详情：`/gene/<gene_id>/`
- 组学门户示例：
  - `/portal/genomics/`
  - `/portal/transcriptomics/`
  - `/portal/proteomics/`
  - `/portal/metabolomics/`
  - `/portal/epigenomics/`
- 其他门户：
  - `/portal/downloads/`
  - `/portal/docs/`
- 后台：`/admin/`

## 内置示例

初始迁移会自动写入示例基因及组学数据，可直接查询：

- `BRCA1`
- `TP53`
- `EGFR`

示例链接：

- `http://127.0.0.1:8000/search/?q=BRCA1`
- `http://127.0.0.1:8000/gene/TP53/`

## 运行步骤

```bash
python3 -m pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py createsuperuser  # 可选
python3 manage.py runserver
```

> 如果你要导入真实组学数据，建议通过 Django Admin 或编写 management command 批量导入。
