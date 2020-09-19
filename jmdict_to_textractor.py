# Arguments:
# 1. JMDict file name (usually JMDict or JMDict_e)
# 2. Output file name (should be SavedDictionary.txt)
# 3. Language (eng for English, other JMDict codes work)
# Example usage: python jmdict_to_textractor.py JMDict SavedDictionary.txt eng

from xml.etree.ElementTree import parse
from sys import argv
from collections import namedtuple
from itertools import chain, product

Term = namedtuple("Term", ["words", "parts_of_speech"])

def inflect(term):
	inflections = set(term.words)
	for word, part_of_speech in product(term.words, term.parts_of_speech):
		if "Godan verb" in part_of_speech:
			inflections.add(word + "<<Godan verb")
		if "Ichidan verb" in part_of_speech:
			inflections.add(word + "<<Ichidan verb")
		if "Kuru verb" in part_of_speech:
			inflections.add(word + "<<Kuru verb")
		if "suru" in part_of_speech:
			inflections.add(word + "<<Suru verb")
		if "adjective (keiyoushi)" in part_of_speech:
			inflections.add(word + "<<Adjective")
	return inflections

outfile = open(argv[2], "w", encoding="utf-8")
for entry in parse(argv[1]).getroot().iter("entry"):
	exclude = { r_ele.find("reb").text for r_ele in entry.iter("r_ele") if not r_ele.find("re_nokanji") is None }
	definitions_by_term = {}
	parts_of_speech = tuple()
	for sense in entry.iter("sense"):
		parts_of_speech = tuple(pos.text for pos in sense.iter("pos")) or parts_of_speech
		definitions = { gloss.text for gloss in sense.iter("gloss")
			if gloss.attrib.get("{http://www.w3.org/XML/1998/namespace}lang", "eng") == argv[3] }
		if not definitions: continue
		defined_words = tuple(stag.text for stag in chain(sense.iter("stagk"), sense.iter("stagr")))\
			or tuple(eb.text for eb in chain(entry.iter("keb"), entry.iter("reb")))
		definitions_by_term.setdefault(Term(defined_words, parts_of_speech), set()).update(definitions)

	for term, definitions in definitions_by_term.items():
		outfile.writelines(f"|TERM|{inflection}" for inflection in inflect(term))
		outfile.write(f"|DEFINITION|<p><small> ({', '.join(filter(lambda word: word not in exclude, term.words))})</small>")
		outfile.writelines(f"\n<p>{definition}" for definition in definitions)
		outfile.write("|END|\n")
outfile.write(open("inflections.txt", "r", encoding="utf-8").read())
