from pathlib import Path
from html.parser import HTMLParser
import html,re,json,sys
root=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
translations=Path(sys.argv[2]) if len(sys.argv)>2 else Path(__file__).resolve().parents[1]/'translations/en.tsv'
D=dict(line.split('\t',1) for line in translations.read_text().splitlines() if '\t' in line)
allowed={'ai','Aisha Ismail','.','Menu +','tasmiya.ismail07@gmail.com','GitHub ↗','LifeLab — Aisha Ismail','LifeLab','ConduzPT — Aisha Ismail','ConduzPT','Stellamus','stellamus','SENSORA Social','SENSORA Social — Aisha Ismail','Stellamus — Aisha Ismail','Loures, Portugal','atelier aurora','↘','↗','+'}
class Translate(HTMLParser):
 def __init__(self,source):
  super().__init__(convert_charrefs=True);self.source=source;self.skip=0;self.edits=[];self.unknown=set();self.lines=[0]
  for m in re.finditer('\n',source):self.lines.append(m.end())
 def source_position(self):
  l,c=self.getpos();return self.lines[l-1]+c
 def handle_starttag(self,tag,attrs):
  if tag in ('style','script'):self.skip+=1
  raw=self.get_starttag_text();new=raw
  def repl(m):
   key=m.group(1).lower();value=html.unescape(m.group(3));out=value
   if key in ('aria-label','title','alt','placeholder','content') and value in D:out=D[value]
   if key=='lang' and tag=='html':out='en'
   if key in ('href','src') and (value.split('?')[0] in ('style.css','site.js','favicon.svg') or value.startswith(('downloads/','life-lab/'))):out='../'+value
   if out==value:return m.group(0)
   return m.group(1)+'='+m.group(2)+html.escape(out,quote=True)+m.group(2)
  new=re.sub(r'([\w-]+)\s*=\s*([\"\x27])(.*?)\2',repl,raw,flags=re.S)
  if new!=raw:self.edits.append((self.source_position(),self.source_position()+len(raw),new))
 def handle_startendtag(self,tag,attrs):
  self.handle_starttag(tag,attrs)
  if tag in ('style','script'):self.skip-=1
 def handle_endtag(self,tag):
  if tag in ('style','script'):self.skip-=1
 def handle_data(self,data):
  if self.skip or not data.strip():return
  key=data.strip()
  if key not in D:
   if key not in allowed:self.unknown.add(key)
   return
  start=self.source_position();end=self.source.find('<',start)
  if end<0:end=len(self.source)
  lead=data[:len(data)-len(data.lstrip())];trail=data[len(data.rstrip()):]
  self.edits.append((start,end,html.escape(lead+D[key]+trail,quote=False)))
 def result(self):
  out=self.source
  for start,end,repl in sorted(self.edits,reverse=True):out=out[:start]+repl+out[end:]
  return out

def switch(lang,page):
 pt='../'+page if lang=='en' else page
 en=page if lang=='en' else 'en/'+page
 return '<div class="language-switch" role="group" aria-label="'+('Language' if lang=='en' else 'Idioma')+'"><a href="'+pt+'" lang="pt-PT" hreflang="pt-PT" aria-label="Ver esta página em português"'+(' aria-current="true"' if lang=='pt' else '')+'>PT</a><span aria-hidden="true">/</span><a href="'+en+'" lang="en" hreflang="en" aria-label="Read this page in English"'+(' aria-current="true"' if lang=='en' else '')+'>EN</a></div>'

def decorate(source,lang,page):
 source=re.sub(r'<div class="language-switch".*?</div>','',source,flags=re.S)
 source=re.sub(r'<link rel="alternate" hreflang="(?:pt-PT|en|x-default)"[^>]*>','',source)
 s=switch(lang,page)
 if page=='demo-atelier.html':
  source=source.replace('</footer>',s+'</footer>')
  css='<style>.language-switch{display:inline-flex;align-items:center;gap:8px;margin-left:18px}.language-switch a{padding:6px 8px;text-decoration:none;border:1px solid currentColor;border-radius:5px;font:600 13px system-ui}.language-switch a[aria-current]{background:#152a30;color:white}</style>'
  source=source.replace('</head>',css+'</head>')
 else:source=source.replace('<button class="menu"',s+'<button class="menu"',1)
 pt='../'+page if lang=='en' else page;en=page if lang=='en' else 'en/'+page
 source=source.replace('</head>',f'<link rel="alternate" hreflang="pt-PT" href="{pt}"><link rel="alternate" hreflang="en" href="{en}"><link rel="alternate" hreflang="x-default" href="{pt}"></head>')
 source=source.replace('href="style.css"','href="style.css?v=20261103-lang"').replace('href="../style.css"','href="../style.css?v=20261103-lang"')
 source=source.replace('src="site.js"','src="site.js?v=20261103-lang"').replace('src="../site.js"','src="../site.js?v=20261103-lang"')
 return source
(root/'en').mkdir(exist_ok=True)
unknown={}
for p in root.glob('*.html'):
 source=p.read_text(); source=re.sub(r'<div class="language-switch".*?</div>','',source,flags=re.S)
 source=re.sub(r'<link rel="alternate" hreflang="(?:pt-PT|en|x-default)"[^>]*>','',source)
 # Always translate the Portuguese original rather than a prior English output.
 t=Translate(source);t.feed(source);english=decorate(t.result(),'en',p.name)
 (root/'en'/p.name).write_text(english)
 p.write_text(decorate(source,'pt',p.name))
 if t.unknown:unknown[p.name]=sorted(t.unknown)
print(json.dumps({'english_pages':len(list((root/'en').glob('*.html'))),'untranslated':unknown},ensure_ascii=False))
if unknown:sys.exit(1)
