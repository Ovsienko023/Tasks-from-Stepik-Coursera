var inp_1 = 'Andsirdaarrevarariarewbutovearrmararan';
var inp_2 = 'ar';

function testRegExp(s, sub_s) {
    var inp_1 = s;
    var inp_2 = sub_s;

    var myPattern = new RegExp(inp_2, 'g');
    var res = inp_1.match(myPattern);
    return res;
}


