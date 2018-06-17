// Exc3
// map for getting announcments sorted by date

function(doc) {
  if(doc.subject) {
    emit(doc.date, doc);
  }
}

//Exc 4
// map for summing number of used letters in object props
function(doc) {
  for(var prop in doc) {
    if(doc.hasOwnProperty(prop)) {
      if(prop != '_rev' && prop != '_id') {
        (prop + doc[prop]).replace(/[^a-zA-Z]+/g,'').split('').forEach(function(letter){
          emit(letter.toLowerCase(), 1);
        });
      }
    }
  }
}

//reduct to sum returned letters
function(key, values) {
  return sum(values);
}
