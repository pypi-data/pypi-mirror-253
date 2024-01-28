function ansiToHtml(text) {
    // ANSI color and style codes to HTML
    const ansiToHtmlStyles = {
        '0': '',
        '1': 'font-weight:bold;',
        '3': 'font-style:italic;',
        '4': 'text-decoration:underline;',
        '30': 'color:black;',
        '31': 'color:red;',
        '32': 'color:green;',
        '33': 'color:yellow;',
        '34': 'color:blue;',
        '35': 'color:magenta;',
        '36': 'color:cyan;',
        '37': 'color:white;',
        '40': 'background-color:black;',
        '41': 'background-color:red;',
        '42': 'background-color:green;',
        '43': 'background-color:yellow;',
        '44': 'background-color:blue;',
        '45': 'background-color:magenta;',
        '46': 'background-color:cyan;',
        '47': 'background-color:white;'
    };

    let openSpans = 0;

    const convertedText = text.replace(/\u001b\[(\d+)(;\d+)*m/g, (match, ...codes) => {
        const styles = codes.slice(0, -2).map(code => ansiToHtmlStyles[code]).filter(Boolean).join('');
        openSpans += 1;
        return `<span style="${styles}">`;
    }).replace(/\u001b\[0m/g, () => {
        openSpans -= 1;
        return '</span>';
    });

    // Close any unclosed spans
    return convertedText + '</span>'.repeat(openSpans);
}