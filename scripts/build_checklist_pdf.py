"""Print the canonical Markdown checklist with legible Vietnamese typography."""
import re
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, LongTable, TableStyle

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'outputs/HW03-01a1ba88/GUI_Checklist.md'
OUT=ROOT/'output/pdf/GUI_Checklist.pdf'
OUT.parent.mkdir(parents=True,exist_ok=True)
pdfmetrics.registerFont(TTFont('ArialVN','C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('ArialVNBold','C:/Windows/Fonts/arialbd.ttf'))
pdfmetrics.registerFontFamily('ArialVN',normal='ArialVN',bold='ArialVNBold',italic='ArialVN',boldItalic='ArialVNBold')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='VNBody',fontName='ArialVN',fontSize=9,leading=12,spaceAfter=5))
styles.add(ParagraphStyle(name='VNCell',fontName='ArialVN',fontSize=8.1,leading=10.8))
styles.add(ParagraphStyle(name='VNHeadCell',fontName='ArialVNBold',fontSize=8.1,leading=10.8,textColor=colors.white))
styles.add(ParagraphStyle(name='VNTitle',fontName='ArialVNBold',fontSize=17,leading=21,spaceAfter=12))
styles.add(ParagraphStyle(name='VNHeading',fontName='ArialVNBold',fontSize=12,leading=16,spaceBefore=10,spaceAfter=7,keepWithNext=True))

def inline(text):
    text=escape(text.replace('\u2013','-').replace('\u2014','-'))
    text=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',text)
    text=re.sub(r'`([^`]+)`',r'\1',text)
    return text.replace('&lt;br&gt;','<br/>')

def para(text,style='VNBody'):
    return Paragraph(inline(text),styles[style])

lines=SOURCE.read_text(encoding='utf-8').splitlines()
story=[]
index=0
while index<len(lines):
    line=lines[index]
    if line.startswith('|'):
        rows=[]
        while index<len(lines) and lines[index].startswith('|'):
            cells=[v.strip() for v in lines[index].strip().strip('|').split('|')]
            if not all(re.fullmatch(r'[:\- ]+',v) for v in cells):
                rows.append(cells)
            index+=1
        columns=len(rows[0])
        width=landscape(A4)[0]-64
        widths=([47,35,90,170,207,85,52,42,55] if columns==9 else [width/columns]*columns)
        widths=[v*width/sum(widths) for v in widths]
        table=LongTable([[para(cell,'VNHeadCell' if r==0 else 'VNCell') for cell in row] for r,row in enumerate(rows)],colWidths=widths,repeatRows=1,hAlign='LEFT')
        table.setStyle(TableStyle([
            ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#243B53')),
            ('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),5),
            ('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),
            ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F3F6F9')]),
            ('LINEBELOW',(0,0),(-1,0),0.5,colors.HexColor('#243B53')),
        ]))
        story.extend([table,Spacer(1,9)])
        continue
    if line.startswith('# '): story.append(para(line[2:],'VNTitle'))
    elif line.startswith('## '): story.append(para(line[3:],'VNHeading'))
    elif line.startswith('- '): story.append(para('• '+line[2:]))
    elif line.strip(): story.append(para(line))
    index+=1

def footer(canvas,doc):
    canvas.setFont('ArialVN',8)
    canvas.setFillColor(colors.HexColor('#526574'))
    canvas.drawString(32,17,'HW03 - FR-04 / FR-11 | Checklist thiết kế v1.0 | Chưa thực thi')
    canvas.drawRightString(landscape(A4)[0]-32,17,f'Trang {doc.page}')

doc=SimpleDocTemplate(str(OUT),pagesize=landscape(A4),leftMargin=32,rightMargin=32,topMargin=27,bottomMargin=32,
                      title='HW03 GUI Checklist FR-04 FR-11',author='AI-assisted draft; student review pending')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(OUT)
