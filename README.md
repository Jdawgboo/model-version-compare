# Model Version Compare

Compare local model metadata and feature signatures for added, removed, and changed fields.

```bash
cat models.json | python tool.py
python -m unittest -v
```

Breaking-change classification focuses on input signature changes and does not judge model behavior, quality, or compatibility with every consumer.
