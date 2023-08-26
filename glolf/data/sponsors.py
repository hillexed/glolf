import random


sponsors = ["Nutrisocks"]

corporations = []

# https://github.com/dariusk/corpora/blob/master/data/words/nouns.json
short_nouns = ['abbey', 'adage', 'ankle', 'ardor', 'arrow', 'baker', 'balls', 'banjo', 'baron', 'bases', 'basin', 'basis', 'begun', 'bingo', 'bones', 'bonus', 'booty', 'broth', 'brunt', 'cabal', 'chasm', 'chili', 'clerk', 'cumin', 'daddy', 'demon', 'diver', 'drink', 'dumps', 'eater', 'envoy', 'error', 'falls', 'feces', 'flask', 'flora', 'fluke', 'foyer', 'fries', 'gusto', 'hands', 'heads', 'heath', 'hello', 'homer', 'jones', 'juror', 'liner', 'litre', 'logic', 'manga', 'mango', 'maple', 'mayor', 'means', 'metre', 'miner', 'mirth', 'motto', 'mover', 'movie', 'nexus', 'nylon', 'oasis', 'ounce', 'owner', 'pasta', 'piles', 'plaza', 'poker', 'quart', 'reins', 'rocks', 'scrum', 'setup', 'skate', 'sloth', 'snack', 'snail', 'snark', 'specs', 'squad', 'squid', 'stole', 'taker', 'tempo', 'terry', 'tiger', 'trout', 'villa', 'vista', 'vogue', 'width', 'words',
# https://github.com/dariusk/corpora/blob/master/data/materials/abridged-body-fluids.json
    "bile",
    "blood",
    "serum",
    "cerebrospinal",
    "fluid"
    "cerumen",
    "earwax",
    "chyle",
    "chyme",
    "endolymph",
    "perilymph",
    "acid",
    "juice",
    "lymph",
    "mucus",
    "saliva",
    "sebum",
    "synovial",
    "sweat",
    "tears",
    "clubs", "clubs", "turf", "turf", "fields","fields","jetpacks"
]
# from https://github.com/dariusk/corpora/blob/master/data/words/adjs.json
adjectives = [ "Aristotelian",
      "Arthurian",
      "Bohemian",
      "Brethren",
      "Mosaic",
      "Oceanic",
      "Proctor",
      "Terran",
      "Tudor",
      "abroad",
      "absorbing",
      "abstract",
      "academic",
      "accelerated",
      "accented",
      "accountant",
      "acquainted",
      "acute",
      "addicting",
      "addictive",
      "adjustable",
      "admired",
      "adult",
      "adverse",
      "advised",
      "aerosol",
      "afraid",
      "aggravated",
      "aggressive",
      "agreeable",
      "alienate",
      "aligned",
      "all-round",
      "alleged",
      "almond",
      "alright",
      "altruistic",
      "ambient",
      "ambivalent",
      "amiable",
      "amino",
      "amorphous",
      "amused",
      "anatomical",
      "ancestral",
      "angelic",
      "angrier",
      "answerable",
      "antiquarian",
      "antiretroviral",
      "appellate",
      "applicable",
      "apportioned",
      "approachable",
      "appropriated",
      "archer",
      "aroused",
      "arrested",
      "assertive",
      "assigned",
      "athletic",
      "atrocious",
      "attained",
      "authoritarian",
      "autobiographical",
      "avaricious",
      "avocado",
      "awake",
      "awesome",
      "backstage",
      "backwoods",
      "balding",
      "bandaged",
      "banded",
      "banned",
      "barreled",
      "battle",
      "beaten",
      "begotten",
      "beguiled",
      "bellied",
      "belted",
      "beneficent",
      "besieged",
      "betting",
      "big-money",
      "biggest",
      "biochemical",
      "bipolar",
      "blackened",
      "blame",
      "blessed",
      "blindfolded",
      "bloat",
      "blocked",
      "blooded",
      "blue-collar",
      "blushing",
      "boastful",
      "bolder",
      "bolstered",
      "bonnie",
      "bored",
      "boundary",
      "bounded",
      "bounding",
      "branched",
      "brawling",
      "brazen",
      "breeding",
      "bridged",
      "brimming",
      "brimstone",
      "broadest",
      "broiled",
      "broker",
      "bronze",
      "bruising",
      "buffy",
      "bullied",
      "bungling",
      "burial",
      "buttery",
      "candied",
      "canonical",
      "cantankerous",
      "cardinal",
      "carefree",
      "caretaker",
      "casual",
      "cathartic",
      "causal",
      "chapel",
      "characterized",
      "charcoal",
      "cheeky",
      "cherished",
      "chipotle",
      "chirping",
      "chivalrous",
      "circumstantial",
      "civic",
      "civil",
      "civilised",
      "clanking",
      "clapping",
      "claptrap",
      "classless",
      "cleansed",
      "cleric",
      "cloistered",
      "codified",
      "colloquial",
      "colour",
      "combat",
      "combined",
      "comely",
      "commissioned",
      "commonplace",
      "commuter",
      "commuting",
      "comparable",
      "complementary",
      "compromising",
      "conceding",
      "concentrated",
      "conceptual",
      "conditioned",
      "confederate",
      "confident",
      "confidential",
      "confining",
      "confuse",
      "congressional",
      "consequential",
      "conservative",
      "constituent",
      "contaminated",
      "contemporaneous",
      "contraceptive",
      "convertible",
      "convex",
      "cooked",
      "coronary",
      "corporatist",
      "correlated",
      "corroborated",
      "cosmic",
      "cover",
      "crash",
      "crypto",
      "culminate",
      "cushioned",
      "dandy",
      "dashing",
      "dazzled",
      "decreased",
      "decrepit",
      "dedicated",
      "defaced",
      "defective",
      "defenseless",
      "deluded",
      "deodorant",
      "departed",
      "depress",
      "designing",
      "despairing",
      "destitute",
      "detective",
      "determined",
      "devastating",
      "deviant",
      "devilish",
      "devoted",
      "diagonal",
      "dictated",
      "didactic",
      "differentiated",
      "diffused",
      "dirtier",
      "disabling",
      "disconnected",
      "discovered",
      "disdainful",
      "diseased",
      "disfigured",
      "disheartened",
      "disheveled",
      "disillusioned",
      "disparate",
      "dissident",
      "doable",
      "doctrinal",
      "doing",
      "dotted",
      "double-blind",
      "downbeat",
      "dozen",
      "draining",
      "draught",
      "dread",
      "dried",
      "dropped",
      "dulled",
      "duplicate",
      "eaten",
      "echoing",
      "economical",
      "elaborated",
      "elastic",
      "elective",
      "electoral",
      "elven",
      "embryo",
      "emerald",
      "emergency",
      "emissary",
      "emotional",
      "employed",
      "enamel",
      "encased",
      "encrusted",
      "endangered",
      "engraved",
      "engrossing",
      "enlarged",
      "enlisted",
      "enlivened",
      "ensconced",
      "entangled",
      "enthralling",
      "entire",
      "envious",
      "eradicated",
      "eroded",
      "esoteric",
      "essential",
      "evaporated",
      "ever-present",
      "evergreen",
      "everlasting",
      "exacting",
      "exasperated",
      "excess",
      "exciting",
      "executable",
      "existent",
      "exonerated",
      "exorbitant",
      "exponential",
      "export",
      "extraordinary",
      "exultant",
      "exulting",
      "facsimile",
      "fading",
      "fainter",
      "faith-based",
      "fallacious",
      "faltering",
      "famous",
      "fancier",
      "fast-growing",
      "fated",
      "favourable",
      "fearless",
      "feathered",
      "fellow",
      "fermented",
      "ferocious",
      "fiddling",
      "filling",
      "firmer",
      "fitted",
      "flammable",
      "flawed",
      "fledgling",
      "fleshy",
      "flexible",
      "flickering",
      "floral",
      "flowering",
      "flowing",
      "foggy",
      "folic",
      "foolhardy",
      "foolish",
      "footy",
      "forehand",
      "forked",
      "formative",
      "formulaic",
      "foul-mouthed",
      "fractional",
      "fragrant",
      "fraudulent",
      "freakish",
      "freckled",
      "freelance",
      "freight",
      "fresh",
      "fretted",
      "frugal",
      "fulfilling",
      "fuming",
      "funded",
      "funny",
      "garbled",
      "gathered",
      "geologic",
      "geometric",
      "gibberish",
      "gilded",
      "ginger",
      "glare",
      "glaring",
      "gleaming",
      "glorified",
      "glorious",
      "goalless",
      "gold-plated",
      "goody",
      "grammatical",
      "grande",
      "grateful",
      "gratuitous",
      "graven",
      "greener",
      "grinding",
      "grizzly",
      "groaning",
      "grudging",
      "guaranteed",
      "gusty",
      "half-breed",
      "hand-held",
      "handheld",
      "hands-off",
      "hard-pressed",
      "harlot",
      "healing",
      "healthier",
      "healthiest",
      "heart",
      "heart-shaped",
      "heathen",
      "hedonistic",
      "heralded",
      "herbal",
      "high-density",
      "high-performance",
      "high-res",
      "high-yield",
      "hissy",
      "hitless",
      "holiness",
      "homesick",
      "honorable",
      "hooded",
      "hopeless",
      "horrendous",
      "horrible",
      "hot-button",
      "huddled",
      "human",
      "humbling",
      "humid",
      "humiliating",
      "hypnotized",
      "idealistic",
      "idiosyncratic",
      "ignited",
      "illustrated",
      "illustrative",
      "imitated",
      "immense",
      "immersive",
      "immigrant",
      "immoral",
      "impassive",
      "impressionable",
      "improbable",
      "impulsive",
      "in-between",
      "in-flight",
      "inattentive",
      "inbound",
      "inbounds",
      "incalculable",
      "incomprehensible",
      "indefatigable",
      "indigo",
      "indiscriminate",
      "indomitable",
      "inert",
      "inflate",
      "inform",
      "inheriting",
      "injured",
      "injurious",
      "inking",
      "inoffensive",
      "insane",
      "insensible",
      "insidious",
      "insincere",
      "insistent",
      "insolent",
      "insufferable",
      "intemperate",
      "interdependent",
      "interesting",
      "interfering",
      "intern",
      "interpreted",
      "intersecting",
      "intolerable",
      "intolerant",
      "intuitive",
      "irresolute",
      "irritate",
      "jealous",
      "jerking",
      "joining",
      "joint",
      "journalistic",
      "joyful",
      "keyed",
      "knowing",
      "lacklustre",
      "laden",
      "lagging",
      "lamented",
      "laughable",
      "layered",
      "leather",
      "leathern",
      "leery",
      "left-footed",
      "legible",
      "leisure",
      "lessening",
      "liberating",
      "life-size",
      "lifted",
      "lightest",
      "limitless",
      "listening",
      "literary",
      "liver",
      "livid",
      "lobster",
      "locked",
      "long-held",
      "long-lasting",
      "long-running",
      "long-suffering",
      "loudest",
      "loveliest",
      "low-budget",
      "low-carb",
      "lowering",
      "lucid",
      "luckless",
      "lusty",
      "luxurious",
      "magazine",
      "maniac",
      "manmade",
      "maroon",
      "mastered",
      "mated",
      "material",
      "materialistic",
      "meaningful",
      "measuring",
      "mediaeval",
      "medical",
      "meditated",
      "medley",
      "melodic",
      "memorable",
      "memorial",
      "metabolic",
      "metallic",
      "metallurgical",
      "metering",
      "midair",
      "midterm",
      "midway",
      "mighty",
      "migrating",
      "mind-blowing",
      "mind-boggling",
      "minor",
      "mirrored",
      "misguided",
      "misshapen",
      "mitigated",
      "mixed",
      "modernized",
      "molecular",
      "monarch",
      "monastic",
      "morbid",
      "motley",
      "motorized",
      "mounted",
      "multi-million",
      "multidisciplinary",
      "muscled",
      "muscular",
      "muted",
      "mysterious",
      "mythic",
      "nail-biting",
      "natural",
      "nauseous",
      "negative",
      "networked",
      "neurological",
      "neutered",
      "newest",
      "night",
      "nitrous",
      "no-fly",
      "noncommercial",
      "nonsense",
      "north",
      "nuanced",
      "occurring",
      "offensive",
      "oldest",
      "oncoming",
      "one-eyed",
      "one-year",
      "onstage",
      "onward",
      "opaque",
      "open-ended",
      "operating",
      "opportunist",
      "opposing",
      "opt-in",
      "ordinate",
      "outdone",
      "outlaw",
      "outsized",
      "overboard",
      "overheated",
      "oversize",
      "overworked",
      "oyster",
      "paced",
      "panting",
      "paralyzed",
      "paramount",
      "parental",
      "parted",
      "partisan",
      "passive",
      "pastel",
      "patriot",
      "peacekeeping",
      "pedestrian",
      "peevish",
      "penal",
      "penned",
      "pensive",
      "perceptual",
      "perky",
      "permissible",
      "pernicious",
      "perpetuate",
      "perplexed",
      "pervasive",
      "petrochemical",
      "philosophical",
      "picturesque",
      "pillaged",
      "piped",
      "piquant",
      "pitching",
      "plausible",
      "pliable",
      "plumb",
      "politician",
      "polygamous",
      "poorest",
      "portmanteau",
      "posed",
      "positive",
      "possible",
      "postpartum",
      "prank",
      "pre-emptive",
      "precocious",
      "predicted",
      "premium",
      "preparatory",
      "prerequisite",
      "prescient",
      "preserved",
      "presidential",
      "pressed",
      "pressurized",
      "presumed",
      "prewar",
      "priced",
      "pricier",
      "primal",
      "primer",
      "primetime",
      "printed",
      "private",
      "problem",
      "procedural",
      "process",
      "prodigious",
      "professional",
      "programmed",
      "progressive",
      "prolific",
      "promising",
      "promulgated",
      "pronged",
      "proportionate",
      "protracted",
      "pulled",
      "pulsed",
      "purgatory",
      "quick",
      "rapid-fire",
      "raunchy",
      "razed",
      "reactive",
      "readable",
      "realizing",
      "recognised",
      "recovering",
      "recurrent",
      "recycled",
      "redeemable",
      "reflecting",
      "regal",
      "registering",
      "reliable",
      "reminiscent",
      "remorseless",
      "removable",
      "renewable",
      "repeating",
      "repellent",
      "reserve",
      "resigned",
      "respectful",
      "rested",
      "restrict",
      "resultant",
      "retaliatory",
      "retiring",
      "revelatory",
      "reverend",
      "reversing",
      "revolving",
      "ridiculous",
      "right-hand",
      "ringed",
      "risque",
      "robust",
      "roomful",
      "rotating",
      "roused",
      "rubber",
      "run-down",
      "running",
      "runtime",
      "rustling",
      "safest",
      "salient",
      "sanctioned",
      "saute",
      "saved",
      "scandalized",
      "scarlet",
      "scattering",
      "sceptical",
      "scheming",
      "scoundrel",
      "scratched",
      "scratchy",
      "scrolled",
      "seated",
      "second-best",
      "segregated",
      "self-taught",
      "semiautomatic",
      "senior",
      "sensed",
      "sentient",
      "sexier",
      "shadowy",
      "shaken",
      "shaker",
      "shameless",
      "shaped",
      "shiny",
      "shipped",
      "shivering",
      "shoestring",
      "short",
      "short-lived",
      "signed",
      "simplest",
      "simplistic",
      "sizable",
      "skeleton",
      "skinny",
      "skirting",
      "skyrocketed",
      "slamming",
      "slanting",
      "slapstick",
      "sleek",
      "sleepless",
      "sleepy",
      "slender",
      "slimmer",
      "smacking",
      "smokeless",
      "smothered",
      "smouldering",
      "snuff",
      "socialized",
      "solid-state",
      "sometime",
      "sought",
      "spanking",
      "sparing",
      "spattered",
      "specialized",
      "specific",
      "speedy",
      "spherical",
      "spiky",
      "spineless",
      "sprung",
      "squint",
      "stainless",
      "standing",
      "starlight",
      "startled",
      "stately",
      "statewide",
      "stereoscopic",
      "sticky",
      "stimulant",
      "stinky",
      "stoked",
      "stolen",
      "storied",
      "strained",
      "strapping",
      "strengthened",
      "stubborn",
      "stylized",
      "suave",
      "subjective",
      "subjugated",
      "subordinate",
      "succeeding",
      "suffering",
      "summary",
      "sunset",
      "sunshine",
      "supernatural",
      "supervisory",
      "supply-side",
      "surrogate",
      "suspended",
      "suspenseful",
      "swarthy",
      "sweating",
      "sweeping",
      "swinging",
      "swooning",
      "sympathize",
      "synchronized",
      "synonymous",
      "synthetic",
      "tailed",
      "tallest",
      "tangible",
      "tanked",
      "tarry",
      "technical",
      "tectonic",
      "telepathic",
      "tenderest",
      "territorial",
      "testimonial",
      "theistic",
      "thicker",
      "threatening",
      "tight-lipped",
      "timed",
      "timely",
      "timid",
      "torrent",
      "totalled",
      "tougher",
      "traditional",
      "transformed",
      "trapped",
      "traveled",
      "traverse",
      "treated",
      "trial",
      "trunk",
      "trusting",
      "trying",
      "twisted",
      "two-lane",
      "tyrannical",
      "unaided",
      "unassisted",
      "unassuming",
      "unattractive",
      "uncapped",
      "uncomfortable",
      "uncontrolled",
      "uncooked",
      "uncooperative",
      "underground",
      "undersea",
      "undisturbed",
      "unearthly",
      "uneasy",
      "unequal",
      "unfazed",
      "unfinished",
      "unforeseen",
      "unforgivable",
      "unidentified",
      "unimaginative",
      "uninspired",
      "unintended",
      "uninvited",
      "universal",
      "unmasked",
      "unorthodox",
      "unparalleled",
      "unpleasant",
      "unprincipled",
      "unread",
      "unreasonable",
      "unregulated",
      "unreliable",
      "unremitting",
      "unsafe",
      "unsanitary",
      "unsealed",
      "unsuccessful",
      "unsupervised",
      "untimely",
      "unwary",
      "unwrapped",
      "uppity",
      "upstart",
      "useless",
      "utter",
      "valiant",
      "valid",
      "valued",
      "vanilla",
      "vaulting",
      "vaunted",
      "veering",
      "vegetative",
      "vented",
      "verbal",
      "verifying",
      "veritable",
      "versed",
      "vinyl",
      "virgin",
      "visceral",
      "visual",
      "voluptuous",
      "walk-on",
      "wanton",
      "warlike",
      "washed",
      "waterproof",
      "waved",
      "weakest",
      "well-bred",
      "well-chosen",
      "well-informed",
      "wetting",
      "wheeled",
      "whirlwind",
      "widen",
      "widening",
      "willful",
      "willing",
      "winnable",
      "winningest",
      "wireless",
      "wistful",
      "woeful",
      "wooded",
      "woodland",
      "wordless",
      "workable",
      "worldly",
      "worldwide",
      "worst-case",
      "worsted",
      "worthless"]

suffixes = [", Inc."," Inc.",", Inc.", ", Inc."," Inc.",", Inc.", ", Ltd.", ", Unltd.", ", Unltd."," Corporation"," Co.", " Group", "Incorporated", "Association","LLLLC"]

#adjectives = [a for a in adjectives if len(a) < 10]

def generate_sponsor(rng=random):
    # generates a funny sponsor name in all lowercase with no spaces
    # used as tourney IDs, hopefully there's never a collision
    sponsor_name = rng.choice(sponsors)
    sponsor_name.replace(", Inc","")


    adjective = rng.choice(adjectives)


    if len(adjective) < 7 and False:
        # find the last vowel and cut it off
        last_vowel_index = max([adjective.rfind(v) for v in "aeiou"])
        truncated_adjective = adjective[0:last_vowel_index]
        cutoff_letter = adjective[last_vowel_index:last_vowel_index+1]

    else:
        # long word. try to find the first vowel after the first 3 letters
        back_part_of_word = adjective[3:]
        first_vowel_index = min([back_part_of_word.find(v) for v in "aeiou" if v in back_part_of_word] + [999])
        first_vowel_index += 3
        if first_vowel_index == 999:
            # sigh, didn't find it. vowel is in the first part of the word
            first_vowel_index = min([adjective.find(v) for v in "aeiou" if v in adjective])

        # now cut off the vowel
        truncated_adjective = adjective[0:first_vowel_index]
        cutoff_letter = adjective[first_vowel_index:first_vowel_index+1]

    noun = rng.choice(short_nouns)


    if cutoff_letter in noun and rng.random() < 1:
        index = noun.find(cutoff_letter)
        if index < len(noun)/2:
            noun = noun[index:] # make a portmanteau

    if len(noun) > 2 and "aeiou" not in noun[0:2]: # try to stop long strings of consonants
        noun = noun[1:]

    companyname = truncated_adjective + noun

    return companyname.lower()

def apply_corporate_suffix(companyname):
    #add a "Inc." or "Ltd" to a company name
    seed = companyname
    rng = random.Random(seed)
    return companyname + rng.choice(suffixes)

def generate_sponsor_based_on_name(seed):

    rng = random.Random(seed)
    return generate_sponsor(rng)

if __name__ == "__main__":
  for i in range(10):
    print(generate_sponsor().title())