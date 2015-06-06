var constructionData = require('../data/construction_data.json');

var dataArray = constructionData["data"];

var arrayForMapbox = [];

for(i = 0; i < dataArray.length; i++){
  singleArray = dataArray[i];
  newArray = [];
  newArray.push(singleArray[singleArray.length - 1][1]);
  newArray.push(singleArray[singleArray.length - 1][2]);
  arrayForMapbox.push(newArray);
}




