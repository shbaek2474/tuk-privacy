# privacy.md(원문) → index.html. 글은 privacy.md만 고치고 `uv run --with markdown python build.py`로 다시 만든다.
import pathlib, re
import markdown

src = pathlib.Path(__file__).with_name('privacy.md').read_text(encoding='utf-8')
body = markdown.markdown(src, extensions=['tables'])
# 표는 좁은 화면에서 옆으로 밀리지 않게 감싼다(표 안에서만 가로 스크롤)
body = body.replace('<table>', '<div class="table"><table>').replace('</table>', '</table></div>')
body = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" rel="noopener"', body)

page = f'''<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>툭 개인정보 처리방침</title>
  <style>
    :root {{ --bg: #F3F3F0; --text: #161B1B; --sub: #646B6A; --line: #DADCD8; --accent: #2B8183; --head: #E9EAE6; }}
    @media (prefers-color-scheme: dark) {{ :root {{ --bg: #0B0F0F; --text: #EEF2F1; --sub: #97A3A1; --line: #263030; --accent: #4FB3AE; --head: #141A1A; }} }}
    body {{ margin: 0; background: var(--bg); color: var(--text); font: 16px/1.7 -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Noto Sans KR", sans-serif; -webkit-text-size-adjust: 100%; word-break: keep-all; overflow-wrap: anywhere; }}
    main {{ max-width: 720px; margin: 0 auto; padding: 40px 16px 64px; }}
    h1 {{ font-size: 26px; margin: 0 0 4px; letter-spacing: -0.4px; }}
    h1 + p {{ color: var(--sub); font-size: 14px; margin-top: 0; }}
    h2 {{ font-size: 19px; margin: 36px 0 8px; }}
    h3 {{ font-size: 16px; margin: 24px 0 6px; }}
    ul {{ padding-left: 20px; }}
    li {{ margin: 4px 0; }}
    a {{ color: var(--accent); word-break: break-all; }}
    hr {{ border: 0; border-top: 1px solid var(--line); margin: 40px 0; }}
    .table {{ overflow-x: auto; margin: 12px 0; }}
    table {{ border-collapse: collapse; width: 100%; font-size: 14px; line-height: 1.55; }}
    th, td {{ border: 1px solid var(--line); padding: 8px 10px; text-align: left; vertical-align: top; }}
    th {{ background: var(--head); font-weight: 600; white-space: nowrap; }}
  </style>
</head>
<body>
  <main>
{body}
  </main>
</body>
</html>
'''
pathlib.Path(__file__).with_name('index.html').write_text(page, encoding='utf-8')
print('index.html', len(page))
