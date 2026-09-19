import glob

old_tag = '<link rel="icon" type="image/svg+xml" href="favicon.svg" />'
new_tags = '''<link rel="icon" type="image/x-icon" href="favicon.ico" />
  <link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png" />
  <link rel="icon" type="image/svg+xml" href="favicon.svg" />
  <link rel="apple-touch-icon" href="favicon-32x32.png" />'''

for f in glob.glob('website/*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        c = file.read()
    if old_tag in c:
        c = c.replace(old_tag, new_tags)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(c)
        print('Updated favicon tags in:', f)
