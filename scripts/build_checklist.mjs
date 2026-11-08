import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const out = path.join(root, 'outputs', 'HW03-01a1ba88');
const previewDir = path.join(root, '.git', 'checklist-previews');
await fs.mkdir(previewDir, {recursive:true});
const data = JSON.parse(await fs.readFile(path.join(root, 'scripts', 'checklist_data.json'), 'utf8'));
const wb = Workbook.create();
const summary = wb.worksheets.add('Summary');
const checklist = wb.worksheets.add('Checklist');
const execution = wb.worksheets.add('Execution');
const dark = '#243B53', light = '#EDF2F7', amber = '#FFF7DD';

function style(sheet, range, widths) {
  sheet.showGridLines = false;
  sheet.getRange(range).format.font = {name:'Arial',size:10,color:'#182B3A'};
  sheet.getRange(range).format.verticalAlignment = 'top';
  sheet.getRange(range).format.wrapText = true;
  widths.forEach((width,index)=>sheet.getRangeByIndexes(0,index,Number(range.match(/\d+$/)[0]),1).format.columnWidth=width);
}
function header(sheet, address) {
  sheet.getRange(address).format = {fill:dark,font:{name:'Arial',size:10,bold:true,color:'#FFFFFF'},
    wrapText:true,horizontalAlignment:'center',verticalAlignment:'center',rowHeight:32};
}
style(summary,'A1:H31',[25,15,18,16,15,15,19,17]);
summary.getRange('A2').values = [['HW03 GUI Checklist']];
summary.getRange('A2').format.font = {name:'Arial',size:15,bold:true};
summary.getRange('A4:H4').values = [['Phiên bản','1.1','Ngày','08/11/2026','Góp ý người dùng','Có góp ý 6 mục',null,null]];
summary.getRange('A4:H4').format.rowHeight=32;
summary.getRange('A6:H6').values = [['IA','Mục thiết kế','Lượt dự kiến','Đã chạy','Passed','Failed','Chưa chạy','Tỷ lệ đã chạy']];
header(summary,'A6:H6');
for(let j=0;j<4;j++) {
  const row=7+j, ia=`IA-0${j+1}`;
  summary.getRange(`A${row}`).values=[[ia]];
  summary.getRange(`B${row}:H${row}`).formulas=[[
    `=COUNTIFS(Checklist!$B$6:$B$48,A${row})`,
    `=B${row}*3`,
    `=SUM(E${row}:F${row})`,
    `=COUNTIFS(Execution!$D$6:$D$134,A${row},Execution!$F$6:$F$134,"Passed")`,
    `=COUNTIFS(Execution!$D$6:$D$134,A${row},Execution!$F$6:$F$134,"Failed")`,
    `=C${row}-D${row}`, `=D${row}/C${row}`]];
}
summary.getRange('A11').values=[['Tổng']];
summary.getRange('B11:H11').formulas=[['=SUM(B7:B10)','=SUM(C7:C10)','=SUM(D7:D10)','=SUM(E7:E10)','=SUM(F7:F10)','=SUM(G7:G10)','=D11/C11']];
summary.getRange('B7:G11').setNumberFormat('#,##0');
summary.getRange('H7:H11').setNumberFormat('0.0%');
summary.getRange('A11:H11').format.fill=light;
summary.getRange('A11:H11').format.font.bold=true;
summary.getRange('A14:F14').values=[['Nền tảng dự kiến','Mục cần chạy','Đã chạy','Passed','Failed','Chưa chạy']];
header(summary,'A14:F14');
for(let p=0;p<3;p++) {
  const row=15+p;
  summary.getRange(`A${row}`).values=[[`P${p+1}`]];
  summary.getRange(`B${row}:F${row}`).formulas=[['=$B$11',`=SUM(D${row}:E${row})`,
    `=COUNTIFS(Execution!$B$6:$B$134,A${row},Execution!$F$6:$F$134,"Passed")`,
    `=COUNTIFS(Execution!$B$6:$B$134,A${row},Execution!$F$6:$F$134,"Failed")`,`=B${row}-C${row}`]];
}
summary.getRange('A20:B24').values=[['P1','Chrome/Windows'],['P2','Firefox/Windows'],['P3','Safari/macOS hoặc Android Chrome - chốt trước execution'],['Ô vàng','Người thực thi điền actual, kết quả và evidence'],['Trạng thái','Chưa chạy = không có kết quả; bị blocker ghi Notes, không gán Passed/Failed giả']];
summary.getRange('B20:H24').format.columnWidth=18;
// Keep long instructions in their own wide unmerged cells below the compact summary.
summary.getRange('A26').values=[['43 mục thiết kế; Execution có 129 lượt dự kiến trên 3 nền tảng. Chưa phải kết quả thực thi.']];
summary.getRange('A27').values=[['Nguồn: SRS EShop FR-04/11/21–24; S13 tr.8,11–22; B01–B08, B10 tại GUI_Checklist.md (AI đề xuất).']];
summary.getRange('A28').values=[['Failed phải có Notes và ảnh thật; bug do sinh viên tự viết. Chốt human review trước chạy.']];
summary.getRange('A26:H28').format.wrapText=false;
summary.getRange('A20:A24').format.font.bold=true;
summary.getRange('B20:B24').format.wrapText=false;
summary.getRange('B7:H17').format.horizontalAlignment='right';

style(checklist,'A1:G48',[14,11,30,64,80,36,30]);
checklist.getRange('A2').values=[['Checklist FR-04 và FR-11 - 43 mục']];
checklist.getRange('A2').format.font={name:'Arial',size:15,bold:true};
checklist.getRange('A3').values=[['B = tiêu chí bổ sung AI đề xuất; chưa xác nhận review SV. Kết quả theo môi trường nhập tại Execution.']];
checklist.getRange('A3:G3').format.wrapText=false;
checklist.getRange('A5:G5').values=[['ID','IA','Thành phần / trạng thái','Thao tác và dữ liệu','Kết quả mong đợi','Căn cứ','ID nguồn nháp']];
checklist.getRange('A6:G48').values=data.items.map(i=>[i.id,i.ia,i.component,i.steps,i.expected,i.basis,i.origin.join(', ')]);
checklist.tables.add('A5:G48',true,'ChecklistTable').style='TableStyleLight1';
header(checklist,'A5:G5');
data.items.forEach((i,index)=>{
  const fields=[i.id,i.ia,i.component,i.steps,i.expected,i.basis,i.origin.join(', ')];
  const widths=[14,11,30,64,80,36,30];
  const lines=Math.max(...fields.map((v,c)=>Math.ceil(v.length/(widths[c]*1.25))));
  checklist.getRange(`A${index+6}:G${index+6}`).format.rowHeight=Math.max(42,lines*14+12);
});
checklist.freezePanes.freezeRows(5);
checklist.freezePanes.freezeColumns(2);

style(execution,'A1:K134',[16,12,14,11,64,16,52,45,24,25,46]);
execution.getRange('A2').values=[['Execution - 43 mục × 3 nền tảng']];
execution.getRange('A2').format.font={name:'Arial',size:15,bold:true};
execution.getRange('A3').values=[['Chưa chạy toàn bộ. Điền mã run thực, browser/OS/device/version, thời gian, actual; Failed cần Notes + ảnh.']];
execution.getRange('A3:K3').format.wrapText=false;
execution.getRange('A5:K5').values=[['Run','Nền tảng','ID','IA','Actual / từng biến thể','Kết quả','Notes / blocker','Ảnh / Issue','Thời gian thực thi','Người thực hiện','Browser / OS / device / version']];
const runRows=[];
for(let p=1;p<=3;p++) for(const item of data.items) runRows.push(['',`P${p}`,item.id,item.ia,'','Chưa chạy','','','','','']);
execution.getRange('A6:K134').values=runRows;
execution.tables.add('A5:K134',true,'ExecutionTable').style='TableStyleLight1';
header(execution,'A5:K5');
execution.getRange('A6:K134').format.rowHeight=48;
execution.getRange('A6:A134').format.fill=amber;
execution.getRange('E6:K134').format.fill=amber;
execution.getRange('F6:F134').dataValidation={rule:{type:'list',values:['Chưa chạy','Passed','Failed']}};
execution.getRange('F6:F134').conditionalFormats.add('containsText',{text:'Failed',format:{fill:'#FDE8E8',font:{color:'#9B1C1C',bold:true}}});
execution.getRange('F6:F134').conditionalFormats.add('containsText',{text:'Passed',format:{fill:'#E5F3E9',font:{color:'#14532D'}}});
execution.freezePanes.freezeRows(5);
execution.freezePanes.freezeColumns(4);

// Verify the editable workflow with a disposable input change, then restore it.
execution.getRange('F6').values=[['Passed']];
if(summary.getRange('E11').values[0][0]!==1) throw new Error('Passed count did not recalculate');
execution.getRange('F6').values=[['Failed']];
if(summary.getRange('F11').values[0][0]!==1) throw new Error('Failed count did not recalculate');
execution.getRange('F6').values=[['Chưa chạy']];
wb.recalculate();
if(summary.getRange('B11').values[0][0]!==43 || summary.getRange('C11').values[0][0]!==129 || summary.getRange('D11').values[0][0]!==0) throw new Error('Summary totals incorrect');
console.log((await wb.inspect({kind:'table',range:'Summary!A6:H11',include:'values,formulas',tableMaxRows:6,tableMaxCols:8,maxChars:1800})).ndjson);
console.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!',options:{useRegex:true,maxResults:20},maxChars:1000})).ndjson);
for(const [name,range] of [['Summary','A1:H28'],['Checklist','A5:F8'],['Execution','A5:H9']]) {
  const image=await wb.render({sheetName:name,range,scale:1.2,format:'png'});
  await fs.writeFile(path.join(previewDir,`${name}.png`),new Uint8Array(await image.arrayBuffer()));
}
const exported=await SpreadsheetFile.exportXlsx(wb);
await exported.save(path.join(out,'GUI_Checklist.xlsx'));
console.log('Exported workbook: 43 definitions; 129 unexecuted platform rows; summary formulas verified.');
