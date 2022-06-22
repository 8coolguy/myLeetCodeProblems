/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
    var map =new Map();
    for(let i =0; i<s.length; i++){
        if(map.has(s.charAt(i))){
            let t =map.get(s.charAt(i))+1;
            map.set(s.charAt(i), t);
        }else{
            map.set(s.charAt(i),1);
        }
    }
    let tot=0;
    var keys =map.entries();
    let max =0;
    console.log(map.values());
    for(const t of map.values()){
        if(t%2==0){
            tot+=t;
        }else if(t%2==1){
            console.log(t);
            if(t > max) {
                tot+=Math.max(0,max-1)
                max=t;
            }else{
                tot+=t-1
            }
        }
        console.log(tot);
        
        
    }
    
    return tot +max;
};