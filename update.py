import os
import glob

# 1. 最新のPDFファイルを探す
pdf_dir = "kairan/docs"
pdf_files = glob.glob(os.path.join(pdf_dir, "*.pdf"))

if not pdf_files:
    print("PDFファイルが見つかりません。")
else:
    # ファイル名で並び替えて最新のものを取得
    latest_pdf = os.path.basename(max(pdf_files, key=os.path.getctime))

    # 2. kairan/index.html を読み込んで書き換える
    html_path = "kairan/index.html"
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # PDFのリンク箇所を最新のファイル名に置き換え
    # (前回お渡ししたテンプレートの 20260419_kairan.pdf の部分を書き換えます)
    import re

    new_html = re.sub(r"docs/.*?\.pdf", f"docs/{latest_pdf}", html_content)

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_html)

    print(f"更新完了！最新PDF: {latest_pdf} を反映しました。")
