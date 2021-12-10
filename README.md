
# Magic Text Summarizer


### Introduction

Create meaningful outline from long texts using BERT, GTP-2 and XLNet.

#### Requirements
- `transformers==4.10.2`
- `bert-extractive-summarizer==0.8.1`
- `spacy==2.2.4`
- `sentencepiece==0.1.96`

#### Install
```bash
git clone https://github.com/mohitsingh538/magic_text_summarize.git
```
```bash
pip install requirements.txt
```

#### Usage
Summarize using `GPT-2`:
```bash
from magic_text_summarize.magic_text_summarizer import Summarize_Paragraph

body = '''   '''

# For GTP-2
paragraph_summarizer = Summarize_Paragraph('GPT-2')

summary = paragraph_summarizer.this_paragraph(body)
```

<h4>Available Options:</h4>

- `GTP-2`
- `BERT`
- `XLNet`

#### Contact

**Issues should be raised directly in the repository.** For additional questions or comments please email me at mohit@terrebrown.com
