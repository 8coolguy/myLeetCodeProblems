//not my soltion because i wrote practically same code and it does not work
var floodFill = function(image, sr, sc, newColor) {
    /**
    DFS - start from the source and explore all the directions
    */
    const rows = image.length;
    const cols = image[0].length;
    const sourceCellColor = image[sr][sc];
    
    fill(sr, sc);
    
    function fill(sr, sc) {
        // boundary
        if (sr < 0 || sr >= rows || sc < 0 || sc >= cols) return;
        
        if (image[sr][sc] === newColor || image[sr][sc] !== sourceCellColor) return;
        
        const directions = [[0, 1], [1, 0], [-1, 0], [0, -1]];
        
        // fill the cell
        image[sr][sc] = newColor;
        
        // start exploring and fill
        for (let i = 0; i < directions.length; i++) {
            let direction = directions[i];
            fill(sr + direction[0], sc + direction[1]);
        }
    }
    
    return image;
};