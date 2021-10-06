const ids = ['english', 'chinese', 'spanish', 'hindi', 'arabic', 'portuguese', 'russian', 'japanese', 'javanese', 'german', 'korean', 'french', 'telugu', 'italian', 'tagalog'];
let elements = [];

for (let i = 0; i<ids.length; i++) {
     elements.push(document.getElementById(ids[i]));
}

const bg = document.getElementById('bg');

const translationList = [
     ['Digital Dialects',225],
     ['数字方言', 90], 
     ['Dialectos digitales', 90], 
     ['डिजिटल बोलियाँ', 90], 
     ['Dialetos Digitais', 90], 
     ['Цифровые диалекты', 90], 
     ['デジタル方言', 90], 
     ['Dialek Digital', 70], 
     ['Digitale Dialekte', 70], 
     ['디지털 방언', 70],
     ['Dialectes numériques', 70], 
     ['డిజిటల్ మాండలికాలు', 70], 
     ['Dialetti digitali', 50], 
     ['Mga Dayalektong Digital', 50],
     ['اللهجات الرقمية'
     , 50] //arabic
]

WordCloud(document.getElementById('bg'), { 
     list: translationList,
     color: 'white',
     backgroundColor: 'black',
     minRotation: -90 * Math.PI/180,
     maxRotation: 90 * Math.PI/180,
     // minRotation: 0,
     // maxRotation: 0,
     rotationSteps: 2,
     gridSize: 50,
     rotateRatio: 0.5,
     // shape: 'cardiod',
     drawOutOfBound: false,
     shrinkToFit: true,
} );

// chinese simplified, spanish, hindi, arabic, portugese, russian, japanese, javanese, german, korean, french, telugu, italian, tagalog

document.getElementById("btn").onclick = generateFile;

function generateFile() {
     html2canvas(bg).then(canvas => {
          let downloadLink = document.createElement('a');
          downloadLink.setAttribute('download', 'BannerImage.png');
          canvas.toBlob(function(blob) {
            let url = URL.createObjectURL(blob);
            downloadLink.setAttribute('href', url);
            downloadLink.click();
          });
     });
}