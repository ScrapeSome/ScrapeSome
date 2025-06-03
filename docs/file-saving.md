## 📄 File Saving

ScrapeSome allows you to format and save your scraped content with zero hassle—both via the **CLI** and in **Python code**.

---

### 💻 Save Output to File

Use these flags to save your output directly from the command line:

- `--save-to-file` or `-s`: Enable saving to a file
- `--file-name` or `-n`: Desired filename (extension added automatically)
- `--output-format` or `-f`: One of `html`, `text`, `markdown`, or `json`

⚠️ **Note:** When saving to a file, only one URL can be scraped at a time.

#### 📦 Example:

```bash
scrapesome scrape "https://example.com" \
  --output-format markdown \
  --save-to-file \
  --file-name output
```

👉 This saves the result as `output.md`.

---

### Save Output in Code

The `sync_scraper` function supports saving to file using two optional flags:

- `save_to_file=True`: Enables saving
- `file_name="your_file_name"`: Sets the base filename (extension inferred from format)

The output will be returned as a dictionary:

```python
{
    "data": "<formatted content>",
    "file": "your_file_name.<ext>"  # if saving is enabled
}
```

#### 📌 Example:

```python
result = sync_scraper(
    url="https://example.com",
    output_format_type="json",
    save_to_file=True,
    file_name="example_output"
)
print(f"Saved output to {result['file']}")
```

---

Now you're set to save clean, readable data in your preferred format—programmatically or from the CLI.
