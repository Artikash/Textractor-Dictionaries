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
	vs: "Suru verb",
	"adj-i": "Adjective",
	iru: "iru"
}

const converted = [];
const original = JSON.parse(document.body.innerText);
for (const name in original) {
	for (const rule of original[name]) {
		const kanaMapping = [rule.kanaOut, rule.kanaIn];
		if (!(rule.rulesIn.length === 0 || rule.rulesIn.length === 1)) alert("WARNING");
		for (const ruleOut of rule.rulesOut) {
			converted.push({ kanaMapping, name, ruleIn: JMDict[ruleOut], ruleOut: "" });
			if (rule.rulesIn.length) converted.push({ kanaMapping, name, ruleIn: JMDict[ruleOut], ruleOut: "<<" + JMDict[rule.rulesIn[0]] })
		}
	}
}
saveStringToFile(
	converted
		.filter(rule => rule.kanaMapping[0])
		.map(rule => `|ROOT|1${rule.kanaMapping[0]}<<${rule.ruleIn}|INFLECTS TO|(.*)${rule.kanaMapping[1] + rule.ruleOut}|NAME| ← ${rule.name}|END|`)
		.join("\n"),
	"inflections.txt"
);
