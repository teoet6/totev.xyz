import html
from pathlib import Path
import shutil
from lat2cyr import lat2cyr
import os

with open(Path('template')) as f:
	template = f.read()

dist = Path('docs')
for it in dist.iterdir():
	if it.name == 'assets':
		continue

	if it.is_file():
		os.remove(it)
	else:
		shutil.rmtree(it)

dist.mkdir(exist_ok=True)

shutil.copy2(Path('style.css'), dist)

with open(dist/'CNAME', 'w') as f:
	f.write('totev.xyz')

postlist=''

for it in reversed(sorted(Path('posts').iterdir())):
	date = it.name[:10]
	id = it.name[11:]
	title = lat2cyr(id).replace('-', ' ').title()

	with open(it) as f:
		content = f.read()

	output = template.format(title=html.escape(title), content=content, date=html.escape(date))

	(dist/id).mkdir()
	with open(dist/id/'index.html', 'w') as f:
		f.write(output)

	postlist += '<h3><a href={id}>{title}</a></h3>'.format(id=html.escape(id), title=html.escape(title))

with open(Path('index')) as f:
	content = f.read()
output = template.format(title='Съдържание', content=content.format(postlist=postlist))
with open(dist/'index.html', 'w') as f:
	f.write(output)
