function convertAnsiToHtml(ansiText) {
            
    var htmlText = ansiText
        // Handle Reset
        .replace(/\033\[0m/g, '</span>')
        // Handle Bold
        .replace(/\033\[1m/g, '<span style="font-weight: bold;">')
        // Handle Underline
        .replace(/\033\[4m/g, '<span style="text-decoration: underline;">')
        // Handle Colors
        .replace(/\033\[(3[0-7])m/g, (match, p1) => {
            const color = ansiColorToHtmlRgb(p1);
            return `<span style="color: ${color};">`;
        });
    htmlText += '</span>';
    return htmlText;
}

function ansiColorToHtmlRgb(ansiCode) {
    const colors = {
        '30': 'rgb(0,0,0)',       // Black
        '31': 'rgb(255,0,0)',     // Red
        '32': 'rgb(0,255,0)',     // Green
        '33': 'rgb(255,255,0)',   // Yellow
        '34': 'rgb(0,0,255)',     // Blue
        '35': 'rgb(255,0,255)',   // Magenta
        '36': 'rgb(0,255,255)',   // Cyan
        '37': 'rgb(255,255,255)'  // White
    };
    return colors[ansiCode] || 'inherit';
}