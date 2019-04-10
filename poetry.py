
import random

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravvagantly", "tantalizingly", "furiously", "sensuously"]

pnouns = (random.sample(nouns, k=3))
pn1 = pnouns[0]
pn2 = pnouns[1]
pn3 = pnouns[2]
pverbs = (random.sample(verbs, k=3))
pv1 = pverbs[0]
pv2 = pverbs[1]
pv3 = pverbs[2]
padjectives = (random.sample(adjectives, k=3))
pa1 = padjectives[0]
pa2 = padjectives[1]
pa3 = padjectives[2]
padverb = (random.sample(adverbs, k=1))
pprepositions = (random.sample(prepositions, k=2))
pp1 = pprepositions[0]
pp2 = pprepositions[1]

if "aeiou".find(pa1[0]) != -1: # first letter is a vowel
	article = "An"
else:
	article = "A"

print("{} {} {}".format(article, pa1, pn1))
print()
print("{} {} {} {} {} the {} {}".format(article, pa1, pn1, pv1, pp1, pa2, pn2))
print("{} the {} {}".format(pa1, pn1, pv2))
print("the {} {} {} a {} {}".format(pn2, pv3, pp2, pa3, pn3))

