const ids = ['english', 'chinese', 'spanish', 'hindi', 'arabic', 'portuguese', 'russian', 'japanese', 'javanese', 'german', 'korean', 'french', 'telugu', 'italian', 'tagalog'];
let elements = [];

for (let i = 0; i<ids.length; i++) {
     elements.push(document.getElementById(ids[i]));
}

const bg = document.getElementById('bg');

let emptyEntries = 0;
let nsEntries = 0;
let validEntries = 0;
let numDuplicates = 0;

// chinese simplified, spanish, hindi, arabic, portugese, russian, japanese, javanese, german, korean, french, telugu, italian, tagalog

document.getElementById("btn").onclick = generateNFTs;

function generateNFTs() {
     // get words and translations from csv
     let csvFile = document.getElementById('upload').files[0];
     Papa.parse(csvFile, {
          complete: function(results) {
               // console.log(results);
               
               var totalWords = 9894
               var timePerDownload = 500;
               var start = 1;
               // start = 1000;
               var numIterations = totalWords;
               // numIterations = 25;

               var i = start+1;
               var last = i+numIterations;
               // last = totalWords+2;
               var interval = setInterval(function() { 
                    if (i < last) { 
                         makeNFT(results.data[i], i-1);
                         i++;
                    }
                    else { 
                         clearInterval(interval);
                    }
               }, timePerDownload);

               setTimeout(() => {
                    console.log("Empty Entries: " + emptyEntries);
                    console.log("NS Entries: " + nsEntries);
                    console.log("Valid Entries: " + validEntries);
                    console.log("Entries with duplicates: " + numDuplicates);
               }, timePerDownload*(numIterations*1.01));
          }
     });
     // console.log(results);
}

function makeNFT(words, num) {
     let nftName = words[1];
     let numAndName = (("000" + num).slice(-4)) + "_" + nftName;

     // update paragraphs with translations
     var map = {}; 
     let numDups = 0;
     for (let i = 0; i<elements.length; i++) {
          let word = words[i+1];
          let lowercaseWord = word.toLowerCase();
          
          if (map[lowercaseWord])
               numDups++;
          else
               map[lowercaseWord] = true;

          if (word=="") {
               emptyEntries++;
               console.log("Missing entry for " + numAndName);
               return;
          } else if (word=="NS") {
               nsEntries++;
               console.log("NS entry for " + numAndName);
               return;
          } else {
               elements[i].innerText = word;
          }
     }

     validEntries++;

     if (numDups>=5) {
          console.log("Lots of duplicates for " + numAndName);
          numAndName+= "_duplicates";
          numDuplicates++;
     }

     html2canvas(bg).then(canvas => {
          let downloadLink = document.createElement('a');
          downloadLink.setAttribute('download', numAndName + '.png');
          canvas.toBlob(function(blob) {
            let url = URL.createObjectURL(blob);
            downloadLink.setAttribute('href', url);
            downloadLink.click();
          });
     });
}