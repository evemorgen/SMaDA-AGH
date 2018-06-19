
Lab website: <https://upel.agh.edu.pl/weaiib/mod/page/view.php?id=15601>  

# Exercises solutions:  

## Exc 1
All objects are avaliable in [documents.json](documents.json) file.  
To put them into couchdb curl query has been written:  
```bash
curl -X POST $COUCH/pgalczynski -H'content-type: application/json' -d '{ \
>   "date": "2018-03-14", \
>   "subject": "We all gonna die like Hawking did today." \
> }'
```
and so on..  
  
## Exc 2
To create db another curl request has been prepared  
```bash
curl -X PUT $COUCH/pgalczynski
{"ok":true}
```

## Exc 3
Filtering documents for only announcements, object is being checked for "subject" property. To sort by date, simply place doc.date as key in emit function  

function itself:
```javascript
function(doc) {
  if(doc.subject) {
    emit(doc.date, doc);
  }
}
```
to submit such function the following curl will be needed:
```
curl -X PUT -d @foo.js -H'Content-Type: application/json' localhost:5984/lab_db/_design/date

foo.js
{
  "views": {
    "by_date": {
      "map": "function(doc) {\n  if(doc.subject) {\n    emit(doc.date, doc);\n  }\n}"
    }
  }
}
```

To obtain results of this view, we will curl for:
```
curl -s -X GET -H'Content-Type: application/json' localhost:5984/lab_db/_design/date/_view/by_date | python -m json.tool
{
    "offset": 0,
    "rows": [
        {
            "id": "63cb5feb340f426ce0e1affe8d0000fd",
            "key": "2018-03-14",
            "value": {
                "_id": "63cb5feb340f426ce0e1affe8d0000fd",
                "_rev": "1-17d371629c27b614ec0331988e2bcf8d",
                "date": "2018-03-14",
                "subject": "We all gonna die like Hawking did today."
            }
        },
        {
            "id": "63cb5feb340f426ce0e1affe8d00023f",
            "key": "2018-06-19",
            "value": {
                "_id": "63cb5feb340f426ce0e1affe8d00023f",
                "_rev": "1-b53c7e38bb16e55f36ec92006d316a1e",
                "date": "2018-06-19",
                "subject": "STILL ALIVE"
            }
        }
    ],
    "total_rows": 2
}
```

## Exc 4
Creating view that sums numer of letter occurances in all objects properties is relativly simple. Implement map that emits value "1" for every letter of its property (name of property and its value), then sum all these 1's in reduce.  

So it goes like this:  
```javascript
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

//reduce sum of provided letters
function(key, values) {
  return sum(values);
}
```

