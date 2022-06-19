function solution(inputString) {
    var res =new String();
    var s=[];
    var inside =false; 
    for(let i =0; i<inputString.length; i++){
        if(inputString.charAt(i)==")"){
            while(s.length!=0){
                res+=s.pop()
            }
            inside =!inside;
        }else if(inputString.charAt(i)=="("){
            inside=!inside;
        }
        else if(inside){
            s.push(inputString.charAt(i));
        }
        else{
            res +=inputString.charAt(i);
        }
    }
    return res; 
    }
    //mysolution failed every but 2 hidden cases
    function solution(s) {
        while (true) {
            let c = s.indexOf(")");    
            if (c === -1) break;
            let o = s.substring(0, c).lastIndexOf("(");
            let start = s.substring(0, o);
            let middle = s.substring(o + 1, c).split("").reverse().join("");
            let end = s.substring(c + 1, s.length);
            s = start + middle + end;
        }
        return s;
    }
    
    
    