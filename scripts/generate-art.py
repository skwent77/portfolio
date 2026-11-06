from pathlib import Path
from html import escape
OUT = Path(__file__).resolve().parents[1] / 'assets'

def text(x,y,value,size=14,fill='#30382f',family='monospace',extra=''):
 return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-family="{family}" {extra}>{escape(value)}</text>'
def rect(x,y,w,h,fill,stroke='none',r=0):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}"/>'
def line(x1,y1,x2,y2,stroke='#a3ada1',extra=''):
 return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{stroke}" fill="none" {extra}/>'
def save(name,bg,body):
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="960" height="540"><defs><pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse"><path d="M30 0H0V30" fill="none" stroke="#829087" stroke-opacity=".09"/></pattern><marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0 0L6 3L0 6" fill="none" stroke="#9aa69b"/></marker></defs>{rect(0,0,960,540,bg)}{body}</svg>'
 (OUT/f'{name}.svg').write_text(svg)

b=rect(0,0,960,540,'url(#grid)')+text(40,42,'01 / LANGUAGE → KNOWLEDGE',11,'#7c8274')
b+=text(48,130,'Stock Term',42,'#253a2e','Georgia')+text(48,180,'Agent.',42,'#253a2e','Georgia')
b+=text(50,222,'A question becomes understanding.',12,'#777f70')
b+=rect(48,276,310,56,'#fafbf7','#d9ded3',4)+text(65,310,'Q  What is a dividend?',13,'#4c5b44')
b+=line(205,333,205,362)+rect(48,364,310,84,'#e1e8da','none',4)+text(65,393,'RETRIEVED CONTEXT',10,'#6f7f62')+text(65,421,'Relevant terms, clear answers.',12,'#4c5b44')
b+=rect(434,100,468,350,'#263c30','none',6)+text(462,133,'RETRIEVAL PIPELINE',11,'#a9bea8')
for i,label in enumerate(['Question embedding','ChromaDB · vector search','Context → explanation']):
 y=164+i*90
 b+=rect(467,y,400,61,'#344c3d','#4d6750',3)+text(490,y+36,label,15,'#e0e8d8')
 if i<2:b+=line(666,y+62,666,y+83,'#9aa69b','marker-end="url(#arrow)"')
b+=text(48,505,'RAG / SEMANTIC SEARCH / MCP',10,'#78816e')+text(899,505,'CONCEPT DIAGRAM',9,'#78816e',extra='text-anchor="end"')
save('stock','#eef0e8',b)

b=text(40,42,'02 / REASONING IN A LOOP',11,'#7e8e85')+text(48,122,'Think. Act. Observe.',39,'#e8eae0','Georgia')+text(48,154,'An agent learns from its next step.',12,'#88988e')
b+=f'<circle cx="720" cy="283" r="141" fill="none" stroke="#566c5b" stroke-width="1" stroke-dasharray="3 7"/><circle cx="720" cy="283" r="90" fill="none" stroke="#3a4b3f"/>'
for x,y,num,label in [(620,177,'01','REASON'),(750,315,'02','ACT'),(556,359,'03','OBSERVE')]:
 b+=rect(x,y,150,58,'#26352c','#5b6a59',3)+text(x+15,y+22,num,10,'#8ea98a')+text(x+15,y+43,label,13,'#e2e9d8')
b+=rect(48,214,410,220,'#1c2520','#354339',4)+text(68,246,'agent / runtime',11,'#8a9b8b')+line(67,264,440,264,'#354339')
for i,(label,color) in enumerate([('> thought   understand the task','#9eaf9a'),('> action    select a tool','#d8e4c8'),('> observe   read the result','#9eaf9a'),('> repeat    refine the next step','#d8e4c8')]):b+=text(70,301+i*32,label,12,color)
b+=text(48,505,'ReAct / TOOL USE / AGENT DESIGN',10,'#7e8e85')+text(899,505,'CONCEPT DIAGRAM',9,'#7e8e85',extra='text-anchor="end"')
save('local','#18231e',b)

b=text(40,42,'03 / LEARNING WITHOUT LABELS',11,'#78828f')+text(48,115,'Two views. One representation.',34,'#dce4ec','Georgia')
for x,y in [(60,181),(60,330)]:
 b+=rect(x,y,144,104,'#3b4d62','#718398',3)
 b+=f'<path d="M{x+25} {y+68}L{x+42} {y+45}H{x+98}L{x+119} {y+68}V{y+83}H{x+24}Z" fill="#a4b1be"/><circle cx="{x+44}" cy="{y+82}" r="9" fill="#283547"/><circle cx="{x+100}" cy="{y+82}" r="9" fill="#283547"/>'
 b+=line(x+148,y+52,330,y+52,'#9aa69b','marker-end="url(#arrow)"')
for y,label,subtitle in [(186,'ONLINE NETWORK','encoder → projector → predictor'),(335,'TARGET NETWORK','encoder → projector')]:
 b+=rect(337,y,390,94,'#324354','#596e83',4)+text(360,y+34,label,12,'#bacbd8')+text(360,y+63,subtitle,12,'#899db0')
b+=line(730,233,818,233)+line(818,233,818,382)+line(730,382,818,382)+text(794,315,'≈',36,'#a4b8c8','Georgia')+text(350,310,'momentum update',10,'#8d9cad')
b+=text(48,505,'BYOL / PYTORCH / SKT AI FELLOWSHIP',10,'#8a9caf')+text(899,505,'CONCEPT DIAGRAM',9,'#8a9caf',extra='text-anchor="end"')
save('byol','#253548',b)

b=text(40,42,'04 / SEEING THE SMALLEST DETAIL',11,'#8e8374')+rect(49,87,512,368,'#ded8ca')
for x in range(50,565,32):b+=line(x,88,x,455,'#cfc8b9')
for y in range(88,456,32):b+=line(50,y,561,y,'#cfc8b9')
b+='<path d="M220 133l31 41-7 28 36 23-11 37 26 18-4 45 37 27-10 43M279 226l37-15 20-34M292 324l-41 9-20 23" fill="none" stroke="#6a655c" stroke-width="2"/>'
b+=rect(202,116,160,296,'none','#ab6e51')+text(210,105,'micro-crack',10,'#976548')
b+=text(611,153,'Micro-crack',32,'#524d42','Georgia')+text(611,193,'Detection',32,'#524d42','Georgia')+line(613,227,899,227,'#c4bcac')
b+=text(613,272,'TEAM F1-SCORE',10,'#928371')+text(610,325,'0.948729',39,'#655c4a','Georgia')+text(613,368,'Xception + EfficientNet-B5',12,'#837763')+text(613,395,'6-model ensemble',12,'#837763')
b+=text(48,505,'COMPUTER VISION / AI KOREA 2020',10,'#8e8374')+text(899,505,'CONCEPT DIAGRAM',9,'#8e8374',extra='text-anchor="end"')
save('crack','#eeeae1',b)

b=text(40,42,'05 / GENERATING A CONNECTION',11,'#868094')+text(48,128,'Peelie',54,'#49425c','Georgia')+text(50,163,'A little more about you.',13,'#8d819c')
b+=rect(48,225,262,195,'#f5f1f9','#d9cfe3',5)+text(69,261,'01 / QUESTIONNAIRE',10,'#978ba2')
for y,w in [(287,176),(310,138),(333,160)]:b+=rect(69,y,w,6,'#ded5e7','none',3)
b+=rect(69,366,114,27,'#776287','none',3)+text(83,384,'Create card →',10,'#f4eff9')
b+=line(312,320,410,320,'#a297af','marker-end="url(#arrow)"')+text(333,304,'ASYNC',10,'#968aa4')
b+=f'<g transform="rotate(-7 630 280)">{rect(458,98,294,338,"#d6c8e1","none",9)}</g>'
b+=rect(485,95,304,348,'#fbf9fd','#c6b7d1',8)+text(510,133,'PEELIE / GENERATED CARD',10,'#9785a7')
b+=f'<circle cx="637" cy="227" r="54" fill="#e9e1ef"/><path d="M604 233q33-58 66 0q-33 37-66 0" fill="none" stroke="#9c87ae" stroke-width="2"/>'
b+=text(637,329,'Curious by nature.',26,'#64506f','Georgia','text-anchor="middle"')+text(637,365,'A new way to introduce yourself.',11,'#9a8aa6',extra='text-anchor="middle"')
b+=text(48,505,'SPRING BOOT / GPT API / ASYNC PROCESSING',10,'#8e8199')+text(899,505,'CONCEPT DIAGRAM',9,'#8e8199',extra='text-anchor="end"')
save('peelie','#ede7f2',b)

b=text(40,42,'06 / A PLACE FOR EVERY LINK',11,'#7b887e')+text(48,122,'CZB',51,'#344b3c','Georgia')+text(48,157,'Less searching. More finding.',13,'#7b8b79')
b+=rect(390,89,513,361,'#fbfcf8','#bcc8b7',5)+rect(391,90,511,37,'#e7ede2','none',4)
for x in [409,424,439]:b+=f'<circle cx="{x}" cy="108" r="3" fill="#9eae96"/>'
b+=text(463,112,'Bookmarks / Collection',10,'#7f8d77')+line(554,128,554,449,'#d5ddce')+text(411,164,'LIBRARY',10,'#8d9d82')
for i,label in enumerate(['All links','Development','Research','Reading list']):
 y=196+i*44
 if i==1:b+=rect(402,y-21,141,33,'#e7edde','none',3)
 b+=text(414,y,label,11,'#6d8062')
for i,(name,url) in enumerate([('A useful reference','docs / development'),('Ideas worth keeping','research / notes'),('Read, then build','articles / reading')]):
 y=164+i*88
 b+=rect(577,y,302,68,'#f2f5ed','#e0e6d8',3)+rect(594,y+18,32,32,'#e0e8d5','none',4)+text(603,y+40,'↗',17,'#819572')+text(642,y+28,name,12,'#516647')+text(642,y+48,url,9,'#93a089')
b+=rect(49,219,234,47,'#e5ecdc','#cbd5c2',3)+text(67,249,'Collection / root',12,'#607554')+line(79,267,79,359,'#9aa78f')+line(79,307,108,307,'#9aa78f')+line(79,359,108,359,'#9aa78f')+text(118,311,'Folder → bookmarks',11,'#7a8c6c')+text(118,363,'Nested collection',11,'#7a8c6c')
b+=text(48,505,'SPRING SECURITY / JWT / HIERARCHICAL DATA',10,'#7b887e')+text(899,505,'CONCEPT DIAGRAM',9,'#7b887e',extra='text-anchor="end"')
save('czb','#e7eddf',b)
(OUT/'favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" rx="3" fill="#263c30"/><text x="20" y="28" text-anchor="middle" font-family="Georgia,serif" font-size="26" fill="#f5f3e9">J.</text></svg>')
print('Generated six project diagrams and favicon.')
