/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
//another pretty straight forward one
var canConstruct = function(ransomNote, magazine) {
    let map =new Map();
    for(let i =0; i< magazine.length; i++){
        let character = magazine[i];
        let getCharacterCount = map.get(character);
        if(getCharacterCount){
            map.set(character,getCharacterCount+1)
        }else{
            map.set(character,1)
        }
        
    }
    for(let i =0; i< ransomNote.length; i++){
        let character = ransomNote[i];
        let getCharacterCount = map.get(character);
        if(getCharacterCount>0){
            map.set(character,getCharacterCount-1);
        }else{
            return false;
        }
        
    }
    return true
};