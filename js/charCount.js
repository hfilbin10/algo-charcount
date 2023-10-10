// exports.charCount = function(string) {

// };
function charCount(inputString) {
    
    const charCounts = {};

    // Remove spaces and punctuation, and convert to lowercase
    const cleanedString = inputString.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();

    // Count the occurrences of each character
    for (const char of cleanedString) {
        charCounts[char] = (charCounts[char] || 0) + 1;
    }

    // Sort the character counts by count (descending) and character (ascending)
    const sortedCounts = Object.entries(charCounts).sort((a, b) => {
        if (a[1] === b[1]) {
            return a[0].localeCompare(b[0]);
        }
        return b[1] - a[1];
    });

    // Convert the sorted counts to the desired format
    const result = sortedCounts.map(([char, count]) => [char, count]);

    return result;
}
console.log(charCount("aaabbc"))