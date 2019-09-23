function saveToFile(data = new Blob(0), fileName = "data.bin") {
	Object.assign(document.createElement("a"), { download: fileName, href: window.URL.createObjectURL(data) }).click();
};

function saveStringToFile(string, fileName = "data.txt") {
	saveToFile(new Blob([string], { type: "text/plain" }), fileName);
}

const JMDict = {
	v5: "Godan verb",
	v1: "Ichidan verb",
	vk: "Kuru verb",
	vs: "suru",
	"adj-i": "adjective (keiyoushi)"
}

const converted = [];
const original = JSON.parse(document.body.innerText);
for (const _ in original) {
	for (const rule of original[_]) {
		const kanaMapping = [rule.kanaOut, rule.kanaIn];
		if (!(rule.rulesIn.length === 0 || rule.rulesIn.length === 1)) alert("WARNING");
		for (const ruleOut of rule.rulesOut) {
			converted.push({ kanaMapping, ruleIn: JMDict[ruleOut], ruleOut: JMDict[rule.rulesIn[0]] });
		}
	}
}
saveStringToFile(
	converted
		.filter(rule => rule.kanaMapping[0])
		.sort((a, b) => a.ruleIn.localeCompare(b.ruleIn) || a.kanaMapping[0].localeCompare(b.kanaMapping[0]))
		.map(rule => `Rule("${rule.kanaMapping[0]}", "${rule.kanaMapping[1]}", "${rule.ruleIn}", "${rule.ruleOut}")`)
		.join(",\n"),
	"inflections.txt"
);