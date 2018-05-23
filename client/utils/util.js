const formatTime = date => {
  const year = date.getFullYear()
  const month = date.getMonth() + 1
  const day = date.getDate()
  const hour = date.getHours()
  const minute = date.getMinutes()
  const second = date.getSeconds()

  return [year, month, day].map(formatNumber).join('/') + ' ' + [hour, minute, second].map(formatNumber).join(':')
}

const formatNumber = n => {
  n = n.toString()
  return n[1] ? n : '0' + n
}

const jsonToXML = (username, pass) => {
  let xml_str = "<xml>\
  <ReqType><![CDATA[login]] > </ReqType>\
  < UsrName > <![CDATA[" + username + "]] > </UsrName>\
  < Passwd > <![CDATA[" + pass + "]] > </Passwd>\
  < /xml>";
  return xml_str;
}

// <xml>
//   <ErrInfo><![CDATA[想学]] ></ErrInfo>
// </xml>


const XMLToJson = xmlString => {
  let ret_json;
  // 
  var count1 = 0;
  var count2 = 0;
  var begin, end;
  for(var i = 0; i <xmlString.length; i++)
  {
    if(xmlString[i] == '[')
    {
      count1++;
      if (count1 == 2)
        begin = i;
    }
    else if(xmlSting[i] == ']')
    {
      end = i;
      break;
    }
  }
  var str;
  for(var i = begin+1; i < end; i++)
    str+=xmlString[i];
  ret_json = str;
  return ret_json;

}
module.exports = {
  formatTime: formatTime,
  jsonToXML: jsonToXML,
  XMLToJson: XMLToJson
}
