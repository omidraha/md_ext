README
=======

Extra third party extensions for ``Python-Markdown``

Install
--------

```bash
  $ pip install md_ext
```

Usage
-----

```python

import markdown

data = "![alt](image.png){width=600}"
md = markdown.Markdown(extensions=['md_ext.img'])
html = md.convert(data)
print(html)
```

Output:

```python
'<p><img src="image.png" width="600" /></p>'
```
