from xml.etree.ElementTree import parse
from sys import argv
from collections import namedtuple
from itertools import chain

Rule = namedtuple("Rule", ["uninflected", "inflected", "from_part_of_speech", "to_part_of_speech"])
rules = [
	Rule("い", "ければ", "adjective (keiyoushi)", "undefined"),
	Rule("い", "そう", "adjective (keiyoushi)", "undefined"),
	Rule("い", "すぎる", "adjective (keiyoushi)", "Ichidan verb"),
	Rule("い", "かったら", "adjective (keiyoushi)", "undefined"),
	Rule("い", "かったり", "adjective (keiyoushi)", "undefined"),
	Rule("い", "くて", "adjective (keiyoushi)", "undefined"),
	Rule("い", "く", "adjective (keiyoushi)", "undefined"),
	Rule("い", "くない", "adjective (keiyoushi)", "adjective (keiyoushi)"),
	Rule("い", "さ", "adjective (keiyoushi)", "undefined"),
	Rule("い", "かった", "adjective (keiyoushi)", "undefined"),
	Rule("い", "くありません", "adjective (keiyoushi)", "undefined"),
	Rule("い", "くありませんでした", "adjective (keiyoushi)", "undefined"),
	Rule("いく", "いったら", "Godan verb", "undefined"),
	Rule("いく", "いったり", "Godan verb", "undefined"),
	Rule("いく", "いって", "Godan verb", "undefined"),
	Rule("いく", "いった", "Godan verb", "undefined"),
	Rule("う", "えば", "Godan verb", "undefined"),
	Rule("う", "っちゃう", "Godan verb", "Godan verb"),
	Rule("う", "いなさい", "Godan verb", "undefined"),
	Rule("う", "いそう", "Godan verb", "undefined"),
	Rule("う", "いすぎる", "Godan verb", "Ichidan verb"),
	Rule("う", "いたい", "Godan verb", "adjective (keiyoushi)"),
	Rule("う", "ったら", "Godan verb", "undefined"),
	Rule("う", "ったり", "Godan verb", "undefined"),
	Rule("う", "って", "Godan verb", "undefined"),
	Rule("う", "わず", "Godan verb", "undefined"),
	Rule("う", "わぬ", "Godan verb", "undefined"),
	Rule("う", "わせる", "Godan verb", "Ichidan verb"),
	Rule("う", "え", "Godan verb", "undefined"),
	Rule("う", "い", "Godan verb", "undefined"),
	Rule("う", "わない", "Godan verb", "adjective (keiyoushi)"),
	Rule("う", "われる", "Godan verb", "Ichidan verb"),
	Rule("う", "った", "Godan verb", "undefined"),
	Rule("う", "います", "Godan verb", "undefined"),
	Rule("う", "いません", "Godan verb", "undefined"),
	Rule("う", "いました", "Godan verb", "undefined"),
	Rule("う", "いませんでした", "Godan verb", "undefined"),
	Rule("う", "いましょう", "Godan verb", "undefined"),
	Rule("う", "える", "Godan verb", "Ichidan verb"),
	Rule("う", "おう", "Godan verb", "undefined"),
	Rule("う", "わされる", "Godan verb", "Ichidan verb"),
	Rule("う", "っとく", "Godan verb", "Godan verb"),
	Rule("おう", "おうたら", "Godan verb", "undefined"),
	Rule("おう", "おうたり", "Godan verb", "undefined"),
	Rule("おう", "おうて", "Godan verb", "undefined"),
	Rule("おう", "おうた", "Godan verb", "undefined"),
	Rule("く", "けば", "Godan verb", "undefined"),
	Rule("く", "いちゃう", "Godan verb", "Godan verb"),
	Rule("く", "っちゃう", "Godan verb", "Godan verb"),
	Rule("く", "きなさい", "Godan verb", "undefined"),
	Rule("く", "きそう", "Godan verb", "undefined"),
	Rule("く", "きすぎる", "Godan verb", "Ichidan verb"),
	Rule("く", "きたい", "Godan verb", "adjective (keiyoushi)"),
	Rule("く", "いたら", "Godan verb", "undefined"),
	Rule("く", "いたり", "Godan verb", "undefined"),
	Rule("く", "いて", "Godan verb", "undefined"),
	Rule("く", "かず", "Godan verb", "undefined"),
	Rule("く", "かぬ", "Godan verb", "undefined"),
	Rule("く", "かせる", "Godan verb", "Ichidan verb"),
	Rule("く", "け", "Godan verb", "undefined"),
	Rule("く", "き", "Godan verb", "undefined"),
	Rule("く", "かない", "Godan verb", "adjective (keiyoushi)"),
	Rule("く", "かれる", "Godan verb", "Ichidan verb"),
	Rule("く", "いた", "Godan verb", "undefined"),
	Rule("く", "きます", "Godan verb", "undefined"),
	Rule("く", "きません", "Godan verb", "undefined"),
	Rule("く", "きました", "Godan verb", "undefined"),
	Rule("く", "きませんでした", "Godan verb", "undefined"),
	Rule("く", "きましょう", "Godan verb", "undefined"),
	Rule("く", "ける", "Godan verb", "Ichidan verb"),
	Rule("く", "こう", "Godan verb", "undefined"),
	Rule("く", "かされる", "Godan verb", "Ichidan verb"),
	Rule("く", "いとく", "Godan verb", "Godan verb"),
	Rule("ぐ", "げば", "Godan verb", "undefined"),
	Rule("ぐ", "いじゃう", "Godan verb", "Godan verb"),
	Rule("ぐ", "ぎなさい", "Godan verb", "undefined"),
	Rule("ぐ", "ぎそう", "Godan verb", "undefined"),
	Rule("ぐ", "ぎすぎる", "Godan verb", "Ichidan verb"),
	Rule("ぐ", "ぎたい", "Godan verb", "adjective (keiyoushi)"),
	Rule("ぐ", "いだら", "Godan verb", "undefined"),
	Rule("ぐ", "いだり", "Godan verb", "undefined"),
	Rule("ぐ", "いで", "Godan verb", "undefined"),
	Rule("ぐ", "がず", "Godan verb", "undefined"),
	Rule("ぐ", "がぬ", "Godan verb", "undefined"),
	Rule("ぐ", "がせる", "Godan verb", "Ichidan verb"),
	Rule("ぐ", "げ", "Godan verb", "undefined"),
	Rule("ぐ", "ぎ", "Godan verb", "undefined"),
	Rule("ぐ", "がない", "Godan verb", "adjective (keiyoushi)"),
	Rule("ぐ", "がれる", "Godan verb", "Ichidan verb"),
	Rule("ぐ", "いだ", "Godan verb", "undefined"),
	Rule("ぐ", "ぎます", "Godan verb", "undefined"),
	Rule("ぐ", "ぎません", "Godan verb", "undefined"),
	Rule("ぐ", "ぎました", "Godan verb", "undefined"),
	Rule("ぐ", "ぎませんでした", "Godan verb", "undefined"),
	Rule("ぐ", "ぎましょう", "Godan verb", "undefined"),
	Rule("ぐ", "げる", "Godan verb", "Ichidan verb"),
	Rule("ぐ", "ごう", "Godan verb", "undefined"),
	Rule("ぐ", "がされる", "Godan verb", "Ichidan verb"),
	Rule("ぐ", "いどく", "Godan verb", "Godan verb"),
	Rule("こう", "こうたら", "Godan verb", "undefined"),
	Rule("こう", "こうたり", "Godan verb", "undefined"),
	Rule("こう", "こうて", "Godan verb", "undefined"),
	Rule("こう", "こうた", "Godan verb", "undefined"),
	Rule("す", "せば", "Godan verb", "undefined"),
	Rule("す", "しちゃう", "Godan verb", "Godan verb"),
	Rule("す", "しなさい", "Godan verb", "undefined"),
	Rule("す", "しそう", "Godan verb", "undefined"),
	Rule("す", "しすぎる", "Godan verb", "Ichidan verb"),
	Rule("す", "したい", "Godan verb", "adjective (keiyoushi)"),
	Rule("す", "したら", "Godan verb", "undefined"),
	Rule("す", "したり", "Godan verb", "undefined"),
	Rule("す", "して", "Godan verb", "undefined"),
	Rule("す", "さず", "Godan verb", "undefined"),
	Rule("す", "さぬ", "Godan verb", "undefined"),
	Rule("す", "させる", "Godan verb", "Ichidan verb"),
	Rule("す", "せ", "Godan verb", "undefined"),
	Rule("す", "し", "Godan verb", "undefined"),
	Rule("す", "さない", "Godan verb", "adjective (keiyoushi)"),
	Rule("す", "される", "Godan verb", "Ichidan verb"),
	Rule("す", "した", "Godan verb", "undefined"),
	Rule("す", "します", "Godan verb", "undefined"),
	Rule("す", "しません", "Godan verb", "undefined"),
	Rule("す", "しました", "Godan verb", "undefined"),
	Rule("す", "しませんでした", "Godan verb", "undefined"),
	Rule("す", "しましょう", "Godan verb", "undefined"),
	Rule("す", "せる", "Godan verb", "Ichidan verb"),
	Rule("す", "そう", "Godan verb", "undefined"),
	Rule("す", "しとく", "Godan verb", "Godan verb"),
	Rule("そう", "そうたら", "Godan verb", "undefined"),
	Rule("そう", "そうたり", "Godan verb", "undefined"),
	Rule("そう", "そうて", "Godan verb", "undefined"),
	Rule("そう", "そうた", "Godan verb", "undefined"),
	Rule("つ", "てば", "Godan verb", "undefined"),
	Rule("つ", "っちゃう", "Godan verb", "Godan verb"),
	Rule("つ", "ちなさい", "Godan verb", "undefined"),
	Rule("つ", "ちそう", "Godan verb", "undefined"),
	Rule("つ", "ちすぎる", "Godan verb", "Ichidan verb"),
	Rule("つ", "ちたい", "Godan verb", "adjective (keiyoushi)"),
	Rule("つ", "ったら", "Godan verb", "undefined"),
	Rule("つ", "ったり", "Godan verb", "undefined"),
	Rule("つ", "って", "Godan verb", "undefined"),
	Rule("つ", "たず", "Godan verb", "undefined"),
	Rule("つ", "たぬ", "Godan verb", "undefined"),
	Rule("つ", "たせる", "Godan verb", "Ichidan verb"),
	Rule("つ", "て", "Godan verb", "undefined"),
	Rule("つ", "ち", "Godan verb", "undefined"),
	Rule("つ", "たない", "Godan verb", "adjective (keiyoushi)"),
	Rule("つ", "たれる", "Godan verb", "Ichidan verb"),
	Rule("つ", "った", "Godan verb", "undefined"),
	Rule("つ", "ちます", "Godan verb", "undefined"),
	Rule("つ", "ちません", "Godan verb", "undefined"),
	Rule("つ", "ちました", "Godan verb", "undefined"),
	Rule("つ", "ちませんでした", "Godan verb", "undefined"),
	Rule("つ", "ちましょう", "Godan verb", "undefined"),
	Rule("つ", "てる", "Godan verb", "Ichidan verb"),
	Rule("つ", "とう", "Godan verb", "undefined"),
	Rule("つ", "たされる", "Godan verb", "Ichidan verb"),
	Rule("つ", "っとく", "Godan verb", "Godan verb"),
	Rule("とう", "とうたら", "Godan verb", "undefined"),
	Rule("とう", "とうたり", "Godan verb", "undefined"),
	Rule("とう", "とうて", "Godan verb", "undefined"),
	Rule("とう", "とうた", "Godan verb", "undefined"),
	Rule("ぬ", "ねば", "Godan verb", "undefined"),
	Rule("ぬ", "んじゃう", "Godan verb", "Godan verb"),
	Rule("ぬ", "になさい", "Godan verb", "undefined"),
	Rule("ぬ", "にそう", "Godan verb", "undefined"),
	Rule("ぬ", "にすぎる", "Godan verb", "Ichidan verb"),
	Rule("ぬ", "にたい", "Godan verb", "adjective (keiyoushi)"),
	Rule("ぬ", "んだら", "Godan verb", "undefined"),
	Rule("ぬ", "んだり", "Godan verb", "undefined"),
	Rule("ぬ", "んで", "Godan verb", "undefined"),
	Rule("ぬ", "なず", "Godan verb", "undefined"),
	Rule("ぬ", "なぬ", "Godan verb", "undefined"),
	Rule("ぬ", "なせる", "Godan verb", "Ichidan verb"),
	Rule("ぬ", "ね", "Godan verb", "undefined"),
	Rule("ぬ", "に", "Godan verb", "undefined"),
	Rule("ぬ", "なない", "Godan verb", "adjective (keiyoushi)"),
	Rule("ぬ", "なれる", "Godan verb", "Ichidan verb"),
	Rule("ぬ", "んだ", "Godan verb", "undefined"),
	Rule("ぬ", "にます", "Godan verb", "undefined"),
	Rule("ぬ", "にません", "Godan verb", "undefined"),
	Rule("ぬ", "にました", "Godan verb", "undefined"),
	Rule("ぬ", "にませんでした", "Godan verb", "undefined"),
	Rule("ぬ", "にましょう", "Godan verb", "undefined"),
	Rule("ぬ", "ねる", "Godan verb", "Ichidan verb"),
	Rule("ぬ", "のう", "Godan verb", "undefined"),
	Rule("ぬ", "なされる", "Godan verb", "Ichidan verb"),
	Rule("ぬ", "んどく", "Godan verb", "Godan verb"),
	Rule("のたまう", "のたもうたら", "Godan verb", "undefined"),
	Rule("のたまう", "のたもうたり", "Godan verb", "undefined"),
	Rule("のたまう", "のたもうて", "Godan verb", "undefined"),
	Rule("のたまう", "のたもうた", "Godan verb", "undefined"),
	Rule("ぶ", "べば", "Godan verb", "undefined"),
	Rule("ぶ", "んじゃう", "Godan verb", "Godan verb"),
	Rule("ぶ", "びなさい", "Godan verb", "undefined"),
	Rule("ぶ", "びそう", "Godan verb", "undefined"),
	Rule("ぶ", "びすぎる", "Godan verb", "Ichidan verb"),
	Rule("ぶ", "びたい", "Godan verb", "adjective (keiyoushi)"),
	Rule("ぶ", "んだら", "Godan verb", "undefined"),
	Rule("ぶ", "んだり", "Godan verb", "undefined"),
	Rule("ぶ", "んで", "Godan verb", "undefined"),
	Rule("ぶ", "ばず", "Godan verb", "undefined"),
	Rule("ぶ", "ばぬ", "Godan verb", "undefined"),
	Rule("ぶ", "ばせる", "Godan verb", "Ichidan verb"),
	Rule("ぶ", "べ", "Godan verb", "undefined"),
	Rule("ぶ", "び", "Godan verb", "undefined"),
	Rule("ぶ", "ばない", "Godan verb", "adjective (keiyoushi)"),
	Rule("ぶ", "ばれる", "Godan verb", "Ichidan verb"),
	Rule("ぶ", "んだ", "Godan verb", "undefined"),
	Rule("ぶ", "びます", "Godan verb", "undefined"),
	Rule("ぶ", "びません", "Godan verb", "undefined"),
	Rule("ぶ", "びました", "Godan verb", "undefined"),
	Rule("ぶ", "びませんでした", "Godan verb", "undefined"),
	Rule("ぶ", "びましょう", "Godan verb", "undefined"),
	Rule("ぶ", "べる", "Godan verb", "Ichidan verb"),
	Rule("ぶ", "ぼう", "Godan verb", "undefined"),
	Rule("ぶ", "ばされる", "Godan verb", "Ichidan verb"),
	Rule("ぶ", "んどく", "Godan verb", "Godan verb"),
	Rule("む", "めば", "Godan verb", "undefined"),
	Rule("む", "んじゃう", "Godan verb", "Godan verb"),
	Rule("む", "みなさい", "Godan verb", "undefined"),
	Rule("む", "みそう", "Godan verb", "undefined"),
	Rule("む", "みすぎる", "Godan verb", "Ichidan verb"),
	Rule("む", "みたい", "Godan verb", "adjective (keiyoushi)"),
	Rule("む", "んだら", "Godan verb", "undefined"),
	Rule("む", "んだり", "Godan verb", "undefined"),
	Rule("む", "んで", "Godan verb", "undefined"),
	Rule("む", "まず", "Godan verb", "undefined"),
	Rule("む", "まぬ", "Godan verb", "undefined"),
	Rule("む", "ませる", "Godan verb", "Ichidan verb"),
	Rule("む", "め", "Godan verb", "undefined"),
	Rule("む", "み", "Godan verb", "undefined"),
	Rule("む", "まない", "Godan verb", "adjective (keiyoushi)"),
	Rule("む", "まれる", "Godan verb", "Ichidan verb"),
	Rule("む", "んだ", "Godan verb", "undefined"),
	Rule("む", "みます", "Godan verb", "undefined"),
	Rule("む", "みません", "Godan verb", "undefined"),
	Rule("む", "みました", "Godan verb", "undefined"),
	Rule("む", "みませんでした", "Godan verb", "undefined"),
	Rule("む", "みましょう", "Godan verb", "undefined"),
	Rule("む", "める", "Godan verb", "Ichidan verb"),
	Rule("む", "もう", "Godan verb", "undefined"),
	Rule("む", "まされる", "Godan verb", "Ichidan verb"),
	Rule("む", "んどく", "Godan verb", "Godan verb"),
	Rule("る", "れば", "Godan verb", "undefined"),
	Rule("る", "っちゃう", "Godan verb", "Godan verb"),
	Rule("る", "りなさい", "Godan verb", "undefined"),
	Rule("る", "りそう", "Godan verb", "undefined"),
	Rule("る", "りすぎる", "Godan verb", "Ichidan verb"),
	Rule("る", "りたい", "Godan verb", "adjective (keiyoushi)"),
	Rule("る", "ったら", "Godan verb", "undefined"),
	Rule("る", "ったり", "Godan verb", "undefined"),
	Rule("る", "って", "Godan verb", "undefined"),
	Rule("る", "らず", "Godan verb", "undefined"),
	Rule("る", "らぬ", "Godan verb", "undefined"),
	Rule("る", "らせる", "Godan verb", "Ichidan verb"),
	Rule("る", "れ", "Godan verb", "undefined"),
	Rule("る", "り", "Godan verb", "undefined"),
	Rule("る", "らない", "Godan verb", "adjective (keiyoushi)"),
	Rule("る", "られる", "Godan verb", "Ichidan verb"),
	Rule("る", "った", "Godan verb", "undefined"),
	Rule("る", "ります", "Godan verb", "undefined"),
	Rule("る", "りません", "Godan verb", "undefined"),
	Rule("る", "りました", "Godan verb", "undefined"),
	Rule("る", "りませんでした", "Godan verb", "undefined"),
	Rule("る", "りましょう", "Godan verb", "undefined"),
	Rule("る", "れる", "Godan verb", "Ichidan verb"),
	Rule("る", "ろう", "Godan verb", "undefined"),
	Rule("る", "らされる", "Godan verb", "Ichidan verb"),
	Rule("る", "っとく", "Godan verb", "Godan verb"),
	Rule("乞う", "乞うたら", "Godan verb", "undefined"),
	Rule("乞う", "乞うたり", "Godan verb", "undefined"),
	Rule("乞う", "乞うて", "Godan verb", "undefined"),
	Rule("乞う", "乞うた", "Godan verb", "undefined"),
	Rule("副う", "副うたら", "Godan verb", "undefined"),
	Rule("副う", "副うたり", "Godan verb", "undefined"),
	Rule("副う", "副うて", "Godan verb", "undefined"),
	Rule("副う", "副うた", "Godan verb", "undefined"),
	Rule("厭う", "厭うたら", "Godan verb", "undefined"),
	Rule("厭う", "厭うたり", "Godan verb", "undefined"),
	Rule("厭う", "厭うて", "Godan verb", "undefined"),
	Rule("厭う", "厭うた", "Godan verb", "undefined"),
	Rule("問う", "問うたら", "Godan verb", "undefined"),
	Rule("問う", "問うたり", "Godan verb", "undefined"),
	Rule("問う", "問うて", "Godan verb", "undefined"),
	Rule("問う", "問うた", "Godan verb", "undefined"),
	Rule("往く", "往ったら", "Godan verb", "undefined"),
	Rule("往く", "往ったり", "Godan verb", "undefined"),
	Rule("往く", "往って", "Godan verb", "undefined"),
	Rule("往く", "往った", "Godan verb", "undefined"),
	Rule("恋う", "恋うたら", "Godan verb", "undefined"),
	Rule("恋う", "恋うたり", "Godan verb", "undefined"),
	Rule("恋う", "恋うて", "Godan verb", "undefined"),
	Rule("恋う", "恋うた", "Godan verb", "undefined"),
	Rule("沿う", "沿うたら", "Godan verb", "undefined"),
	Rule("沿う", "沿うたり", "Godan verb", "undefined"),
	Rule("沿う", "沿うて", "Godan verb", "undefined"),
	Rule("沿う", "沿うた", "Godan verb", "undefined"),
	Rule("添う", "添うたら", "Godan verb", "undefined"),
	Rule("添う", "添うたり", "Godan verb", "undefined"),
	Rule("添う", "添うて", "Godan verb", "undefined"),
	Rule("添う", "添うた", "Godan verb", "undefined"),
	Rule("行く", "行ったら", "Godan verb", "undefined"),
	Rule("行く", "行ったり", "Godan verb", "undefined"),
	Rule("行く", "行って", "Godan verb", "undefined"),
	Rule("行く", "行った", "Godan verb", "undefined"),
	Rule("請う", "請うたら", "Godan verb", "undefined"),
	Rule("請う", "請うたり", "Godan verb", "undefined"),
	Rule("請う", "請うて", "Godan verb", "undefined"),
	Rule("請う", "請うた", "Godan verb", "undefined"),
	Rule("負う", "負うたら", "Godan verb", "undefined"),
	Rule("負う", "負うたり", "Godan verb", "undefined"),
	Rule("負う", "負うて", "Godan verb", "undefined"),
	Rule("負う", "負うた", "Godan verb", "undefined"),
	Rule("逝く", "逝ったら", "Godan verb", "undefined"),
	Rule("逝く", "逝ったり", "Godan verb", "undefined"),
	Rule("逝く", "逝って", "Godan verb", "undefined"),
	Rule("逝く", "逝った", "Godan verb", "undefined"),
	Rule("いる", "い", "Ichidan verb", "undefined"),
	Rule("える", "え", "Ichidan verb", "undefined"),
	Rule("きる", "き", "Ichidan verb", "undefined"),
	Rule("ぎる", "ぎ", "Ichidan verb", "undefined"),
	Rule("ける", "け", "Ichidan verb", "undefined"),
	Rule("げる", "げ", "Ichidan verb", "undefined"),
	Rule("じる", "じ", "Ichidan verb", "undefined"),
	Rule("せる", "せ", "Ichidan verb", "undefined"),
	Rule("ぜる", "ぜ", "Ichidan verb", "undefined"),
	Rule("ちる", "ち", "Ichidan verb", "undefined"),
	Rule("てる", "て", "Ichidan verb", "undefined"),
	Rule("でる", "で", "Ichidan verb", "undefined"),
	Rule("にる", "に", "Ichidan verb", "undefined"),
	Rule("ねる", "ね", "Ichidan verb", "undefined"),
	Rule("ひる", "ひ", "Ichidan verb", "undefined"),
	Rule("びる", "び", "Ichidan verb", "undefined"),
	Rule("へる", "へ", "Ichidan verb", "undefined"),
	Rule("べる", "べ", "Ichidan verb", "undefined"),
	Rule("みる", "み", "Ichidan verb", "undefined"),
	Rule("める", "め", "Ichidan verb", "undefined"),
	Rule("りる", "り", "Ichidan verb", "undefined"),
	Rule("る", "れば", "Ichidan verb", "undefined"),
	Rule("る", "ちゃう", "Ichidan verb", "Godan verb"),
	Rule("る", "なさい", "Ichidan verb", "undefined"),
	Rule("る", "そう", "Ichidan verb", "undefined"),
	Rule("る", "すぎる", "Ichidan verb", "Ichidan verb"),
	Rule("る", "たい", "Ichidan verb", "adjective (keiyoushi)"),
	Rule("る", "たら", "Ichidan verb", "undefined"),
	Rule("る", "たり", "Ichidan verb", "undefined"),
	Rule("る", "て", "Ichidan verb", "undefined"),
	Rule("る", "ず", "Ichidan verb", "undefined"),
	Rule("る", "ぬ", "Ichidan verb", "undefined"),
	Rule("る", "させる", "Ichidan verb", "Ichidan verb"),
	Rule("る", "よ", "Ichidan verb", "undefined"),
	Rule("る", "ろ", "Ichidan verb", "undefined"),
	Rule("る", "ない", "Ichidan verb", "adjective (keiyoushi)"),
	Rule("る", "た", "Ichidan verb", "undefined"),
	Rule("る", "ます", "Ichidan verb", "undefined"),
	Rule("る", "ません", "Ichidan verb", "undefined"),
	Rule("る", "ました", "Ichidan verb", "undefined"),
	Rule("る", "ませんでした", "Ichidan verb", "undefined"),
	Rule("る", "ましょう", "Ichidan verb", "undefined"),
	Rule("る", "れる", "Ichidan verb", "Ichidan verb"),
	Rule("る", "られる", "Ichidan verb", "Ichidan verb"),
	Rule("る", "よう", "Ichidan verb", "undefined"),
	Rule("る", "とく", "Ichidan verb", "Godan verb"),
	Rule("れる", "れ", "Ichidan verb", "undefined"),
	Rule("くる", "きちゃう", "Kuru verb", "Godan verb"),
	Rule("くる", "きなさい", "Kuru verb", "undefined"),
	Rule("くる", "きそう", "Kuru verb", "undefined"),
	Rule("くる", "きすぎる", "Kuru verb", "Ichidan verb"),
	Rule("くる", "きたい", "Kuru verb", "adjective (keiyoushi)"),
	Rule("くる", "きたら", "Kuru verb", "undefined"),
	Rule("くる", "きたり", "Kuru verb", "undefined"),
	Rule("くる", "きて", "Kuru verb", "undefined"),
	Rule("くる", "こず", "Kuru verb", "undefined"),
	Rule("くる", "こぬ", "Kuru verb", "undefined"),
	Rule("くる", "こさせる", "Kuru verb", "Ichidan verb"),
	Rule("くる", "こい", "Kuru verb", "undefined"),
	Rule("くる", "き", "Kuru verb", "undefined"),
	Rule("くる", "こない", "Kuru verb", "adjective (keiyoushi)"),
	Rule("くる", "きた", "Kuru verb", "undefined"),
	Rule("くる", "きます", "Kuru verb", "undefined"),
	Rule("くる", "きません", "Kuru verb", "undefined"),
	Rule("くる", "きました", "Kuru verb", "undefined"),
	Rule("くる", "きませんでした", "Kuru verb", "undefined"),
	Rule("くる", "きましょう", "Kuru verb", "undefined"),
	Rule("くる", "これる", "Kuru verb", "Ichidan verb"),
	Rule("くる", "こられる", "Kuru verb", "Ichidan verb"),
	Rule("くる", "こよう", "Kuru verb", "undefined"),
	Rule("くる", "きとく", "Kuru verb", "Godan verb"),
	Rule("る", "れば", "Kuru verb", "undefined"),
	Rule("る", "ちゃう", "Kuru verb", "Godan verb"),
	Rule("る", "なさい", "Kuru verb", "undefined"),
	Rule("る", "そう", "Kuru verb", "undefined"),
	Rule("る", "すぎる", "Kuru verb", "Ichidan verb"),
	Rule("る", "たい", "Kuru verb", "adjective (keiyoushi)"),
	Rule("る", "たら", "Kuru verb", "undefined"),
	Rule("る", "たり", "Kuru verb", "undefined"),
	Rule("る", "て", "Kuru verb", "undefined"),
	Rule("る", "ず", "Kuru verb", "undefined"),
	Rule("る", "ぬ", "Kuru verb", "undefined"),
	Rule("る", "させる", "Kuru verb", "Ichidan verb"),
	Rule("る", "い", "Kuru verb", "undefined"),
	Rule("る", "ない", "Kuru verb", "adjective (keiyoushi)"),
	Rule("る", "た", "Kuru verb", "undefined"),
	Rule("る", "ます", "Kuru verb", "undefined"),
	Rule("る", "ません", "Kuru verb", "undefined"),
	Rule("る", "ました", "Kuru verb", "undefined"),
	Rule("る", "ませんでした", "Kuru verb", "undefined"),
	Rule("る", "ましょう", "Kuru verb", "undefined"),
	Rule("る", "れる", "Kuru verb", "Ichidan verb"),
	Rule("る", "られる", "Kuru verb", "Ichidan verb"),
	Rule("る", "よう", "Kuru verb", "undefined"),
	Rule("る", "とく", "Kuru verb", "Godan verb"),
	Rule("する", "しちゃう", "suru", "Godan verb"),
	Rule("する", "しなさい", "suru", "undefined"),
	Rule("する", "しそう", "suru", "undefined"),
	Rule("する", "しすぎる", "suru", "Ichidan verb"),
	Rule("する", "したい", "suru", "adjective (keiyoushi)"),
	Rule("する", "したら", "suru", "undefined"),
	Rule("する", "したり", "suru", "undefined"),
	Rule("する", "して", "suru", "undefined"),
	Rule("する", "せず", "suru", "undefined"),
	Rule("する", "せぬ", "suru", "undefined"),
	Rule("する", "させる", "suru", "Ichidan verb"),
	Rule("する", "しろ", "suru", "undefined"),
	Rule("する", "せよ", "suru", "undefined"),
	Rule("する", "しない", "suru", "adjective (keiyoushi)"),
	Rule("する", "される", "suru", "Ichidan verb"),
	Rule("する", "した", "suru", "undefined"),
	Rule("する", "します", "suru", "undefined"),
	Rule("する", "しません", "suru", "undefined"),
	Rule("する", "しました", "suru", "undefined"),
	Rule("する", "しませんでした", "suru", "undefined"),
	Rule("する", "しましょう", "suru", "undefined"),
	Rule("する", "しよう", "suru", "undefined"),
	Rule("する", "しとく", "suru", "Godan verb"),
	Rule("る", "れば", "suru", "undefined")
]

Term = namedtuple("Term", ["words", "parts_of_speech"])

def inflect(term, depth = int(argv[4])):
	inflections = set(term.words)
	if depth <= 0: return inflections
	for word in term.words:
		for part_of_speech in term.parts_of_speech:
			for rule in filter(lambda rule:
				rule.from_part_of_speech in part_of_speech
				and word.endswith(rule.uninflected),
				rules
			):
				inflections |= inflect(Term([word[:-len(rule.uninflected)] + rule.inflected], [rule.to_part_of_speech]), depth - 1)
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
		outfile.write(f"|DEFINITION|<small>({', '.join(filter(lambda word: word not in exclude, term.words))})</small>")
		outfile.writelines(f"\n<p>{definition}</p>" for definition in definitions)
		outfile.write("|END|\n")