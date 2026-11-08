"""Check deliverable consistency and make a PDF contact sheet for visual QA."""
import json
import re
from collections import Counter
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET
from pypdf import PdfReader
from PIL import Image, ImageOps, ImageDraw

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'outputs/HW03-01a1ba88'
PREVIEW=ROOT/'.git/checklist-previews'
data=json.loads((ROOT/'scripts/checklist_data.json').read_text(encoding='utf-8'))
items=data['items']
ids={i['id'] for i in items}
assert len(ids)==len(items)==44
assert Counter(i['ia'] for i in items)=={'IA-01':12,'IA-02':10,'IA-03':9,'IA-04':13}
inventory=(ROOT/'docs/profile_inventory.md').read_text(encoding='utf-8')
source_ids=re.findall(r'^\| (INV-IA\d{2}-\d{2}) \|',inventory,re.M)
assert len(source_ids)==len(set(source_ids))==52
assert set(source_ids)==set(data['mapping'])
assert sum(v=='Tách chờ làm rõ' for v in data['mapping'].values())==4
md=(OUT/'GUI_Checklist.md').read_text(encoding='utf-8')
assert len(re.findall(r'^\| GUI-\d{3} \|',md,re.M))==44
assert all(i['steps'] in md and i['expected'] in md and i['basis'] in md for i in items)
assert all(i['status']=='Chưa chạy' for i in items)

ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with ZipFile(OUT/'GUI_Checklist.xlsx') as z:
    sheet_names=ET.fromstring(z.read('xl/workbook.xml')).find('m:sheets',ns)
    assert [x.attrib['name'] for x in sheet_names]==['Summary','Checklist','Execution']
    shared=ET.fromstring(z.read('xl/sharedStrings.xml'))
    texts=[''.join(si.itertext()) for si in shared]
    def value(cell):
        node=cell.find('m:v',ns)
        if node is None: return None
        return texts[int(node.text)] if cell.attrib.get('t')=='s' else node.text
    run_sheet=ET.fromstring(z.read('xl/worksheets/sheet3.xml'))
    cells={c.attrib['r']:c for c in run_sheet.findall('.//m:c',ns)}
    assert all(value(cells[f'F{r}'])=='Chưa chạy' for r in range(6,138))
    assert Counter(value(cells[f'C{r}']) for r in range(6,138))=={i:3 for i in ids}
    assert run_sheet.find('m:dataValidations',ns) is not None
    pane=run_sheet.find('m:sheetViews/m:sheetView/m:pane',ns)
    print('Execution freeze pane:',pane.attrib if pane is not None else None)
    definitions=ET.fromstring(z.read('xl/worksheets/sheet2.xml'))
    spec_cells={c.attrib['r']:c for c in definitions.findall('.//m:c',ns)}
    assert {value(spec_cells[f'A{r}']) for r in range(6,50)}==ids

pdf=PdfReader(ROOT/'output/pdf/GUI_Checklist.pdf')
pdf_text='\n'.join(page.extract_text() for page in pdf.pages)
assert ids.issubset(set(re.findall(r'GUI-\d{3}',pdf_text)))
assert 'Nguyễn Văn Mẫu' in pdf_text and 'Chưa chạy' in pdf_text
assert not (ROOT/'git_commit_log.txt').exists()

pages=sorted(PREVIEW.glob('pdf-*.png'))
assert len(pages)==len(pdf.pages)
thumbs=[]
for number,page in enumerate(pages,1):
    im=Image.open(page).convert('RGB')
    im.thumbnail((700,500))
    tile=Image.new('RGB',(720,525),'#d9dee4')
    tile.paste(im,((720-im.width)//2,20))
    ImageDraw.Draw(tile).text((8,5),f'Page {number}',fill='black')
    thumbs.append(tile)
contact=Image.new('RGB',(1440,525*((len(thumbs)+1)//2)),'white')
for n,tile in enumerate(thumbs):contact.paste(tile,((n%2)*720,(n//2)*525))
contact.save(PREVIEW/'pdf-contact.png')
print(f'Validated 44 definitions, all 52 source mappings, 132 unexecuted runs, and {len(pdf.pages)} PDF pages.')
