<!-- TODO: Adding missing plurals: left off at "base_pairs" -->

# MsFit Crossword Dataset
This is **manually curated** dataset of \~42,000 words and phrases in **American English** that I have deemed suitable as entries for (American) word puzzles, primarily American-style crosswords. All entries are contained in a single alphabetized .txt file, with each entry occupying a separate line. I have left original punctuation in the entries if possible, for better human readability; standardization of the entries and further sorting is left to the user. A few Python scripts for standardization/sorting are located in `scripts`.

Any entry is included only if (1) it is commonly used in everyday American English, and (2) it can stand alone as a non-awkward crossword entry. This dataset includes nouns, adjectives, verbs; it contains few gerunds, adverbs, and proper nouns. It also includes short phrases, idioms, and sets of words that often go together (i.e. "school night", "secret santa", "ride shotgun", etc.) See the "Rules for inclusion" section for more details about how I decided whether an entry should belong. See "Curation process" for where I curated these entries from.

This dataset is used in my [MsFit](https://github.com/nzfeng/MsFit) crossword construction software. Feel free to use this dataset for your own project; if for an academic publication, a BibTex entry is at the bottom of the README.

In addition to the main word list `core.txt`, I've also started keeping track of an auxiliary word list `contemporary.txt` that indicates entries that are more likely to be "temporary" rather than core crossword entries: slang, popular media, etc. 

## Motivation
I wanted to make crossword puzzles that fit my standards. I realized that a main challenge of crossword construction, separate of algorithmic involvement, is having a good bank of words to choose from. <!-- Most of the demand for human crossword constructors, after supplying any theme entries, seems to just be guiding construction towards having quality fills.-->

I found that existing crossword and natural language processing (NLP) datasets weren't strict enough by the standards I was seeking. Crossword datasets are usually formed by scraping indiscriminately from other datasets, including existing puzzles, which contain entries I wanted to avoid. Meanwhile, the criteria for acceptable crossword entries is too niche for any NLP datasets to be applicable. What makes a "good" crossword entry is also subject to taste, and can be more subtle than, e.g. selecting for part-of-speech or corpus frequency.

Since the number of words in the English language is on the order of 10^6, I concluded that manual curation was at least possible.

## Rules for inclusion
What makes a "good" wordlist is subjective. Personally, I wanted to make a "core" wordlist of common-knowledge American English entries, with as few "specific" entries as possible (i.e. names, places, pop culture references.) Here is how I decided to choose words (very subjective!):

* The central goal is to only include words and phrases that are often used in spoken and written American English. **Every single entry** in this dataset should be a usable crossword entry. If one is instead interested in using a dataset simply to help them determine if a grid is fillable using an auto-fill functionality, then they can just grab any uncurated wordlist. 
* **Zero crossword-ese** and filler words. All entries should be able to hold their own as lively crossword entries, and ideally lend themselves well to creative clues.
* This dataset should be a "core" crossword dataset with few overly-specific entries. I avoid people -- I don't consider people-related entries as "core" entries. Exceptions are extremely iconic people who are a part of American collective memory at this point, like EINSTEIN or ELVIS.
<!-- * The general ranking of parts of speech is: noun > verb > adjective > adverb > prepositions > article > conjunction > pronouns. -->
* Focus on root words. I only include derivative words (plurals, gerunds, past tense, etc.) if they are commonly used in everyday language, and can act as natural-sounding entries. A good rule of thumb is to avoid adverbs. (On the other hand, words that end in "-ly" but are not adverbs usually make decent adjectives. Ex: EARLY, LONELY, etc.) Also I avoid superlatives if they end in "-est".
* If there are words with multiple derivatives and one is definitely used more often than the others, I only include the commonly-used one. Ex. FIREWORKS vs. FIREWORK, VAGARIES vs. VAGARY.
* For nouns, I avoid gerunds (words that end in "-ing"), and words that end in "-ness", "-tion", "-ment", or "-ism". A lot of these words are in the category of "words that are technically English words but no one uses them." I only include these types of words if they are commonly used in everyday language.
* Similarly, I avoid nouns that end in "-er" that mean "someone who does X", and aren't really used in everyday language. Ex: ADVANCER, etc. Only include if they are common words or refer to commonly-known roles, ex. USER, COMPOSER.
* I try not to include words/phrases that, although they are commonly used, make for boring entries. This is somewhat subjective, especially since boringness also depends on the clueing. But some examples of what I omit are legal terms and phrases, and other dry phrases pertaining to specific fields, government, bureaucracy, banking, and other societal minutiae.
* I don't include full phrases if their abbreviations are more commonly used, i.e. "magnetic resonance imaging" for MRI. The former would be a boring entry; if entries are going to be long, they should be exciting.
* I avoid phrases that depend on too many prepositions or conjunctions ("and", "of", "for", etc.) For shorter entries, I aim to have zero "extra filler words". 
* For shorter entries, I avoid two-word phrases, especially if one of the words is a preposition (ASK_IN, etc.) I only include multi-word phrases if they really do "come as a set", i.e. "BACK_OUT". For long entries, I avoid phrases with more than 3 words.
* I try to avoid partial phrases. I assume these would almost always have fill-in-the-blank clues, which are okay once in a while, to help a solver get started, but that's about it. Best to keep them to a minimum. I completely avoid partial phrases that are awkward on their own, though, like "ONEI" as part of "That's one I haven't heard before."
* I don't include words that have negative prefixes like "un-", "dis-", etc. unless they are just as commonly used as their positive counterpart (if not more common), and come with their own connotations and usage patterns. I.e., if you look the word up in the dictionary and it's simply defined as the negation of something, I don't include it.
<!--* Similarly, try not to include words whose meanings are too evident from their components, such as "southbound." It would be hard to come up with clues. -->
* I avoid British-English spellings, or non-English entries except for those that are commonly used in American English ("vice versa", "pad thai", etc.) When American English puzzles rely on very particular words from other languages, dialects, or variant spellings, it feels cheap.
* I omit offensive, insensitive, or particularly unpleasant entries. I try not to have entries relating to warfare, violence, weapons, chemical agents that have been been used in war, etc. I avoid "gross" entries pertaining to bodily fluids, bodily functions, crimes, abuse, etc. I try to avoid entries with negative connotations (i.e. RACISM, MANIFEST_DESTINY, SUICIDE, etc.) Even if their clues are benign, or if they have benign alternate definitions (like SUICIDE), I think certain connotations are too negative to have visibility in crossword puzzles. 
* I avoid places, except for maybe iconic American places. Good rule of thumb is whether this location would be known to a non-American.
* Most of these rules basically just boil down to "Only include commonly-used words." I try to only include entries that are commonly used, roll off the tongue, can be standalone entries, encourage lively clues, and so on. (Of course this is subjective.)

There might be entries that I've accidentally included that don't adhere to my own rules. Conversely, I've almost certainly missed some good entries.

## Curation process
* I started by manually filtering all \~147k lemmas in [WordNet](https://wordnet.princeton.edu/), which took me about a month. In the end, about 21% I deemed good enough to include in this dataset. 
* I began filtering words from the [Broda wordlist](https://peterbroda.me/crosswords/wordlist/), which presented another \~320k unique entries after removing any words I've already looked at, and words with scores less than 50 (i.e. keeping only words that have been deemed above a certain level of quality, or are unscored.) I'm finding that the dataset is mostly not what I'm looking for, so I probably won't finish sifting through the Broda wordlist anytime soon.
* I've also scraped relevant words & phrases from "[Updates to the OED](https://public.oed.com/updates/)" pages to obtain "fresh" entries.
* I've copied a few vocab lists from ESL sites. 
* [Desi Quintas](http://www.desiquintans.com/nounlist) has a hand-curated plain.txt list of 6801 common nouns in English; their curation criteria aligns really well with what makes a good crossword entry. I've gone through and removed British-English and words I don't like, resulting in \~6250 words. This added maybe another \~1000 entries unique from WordNet and some other filtered words I had at the time.
* I've filtered a list of 10,000+ nouns on [richardharringtonblog.com](https://richardharringtonblog.com/list-of-nouns). First I removed any entries that I had already filtered, which removed the vast majority; I then manually filtered the remaining, which left \~380 entries.
* I went through letter pairs that are legal at the beginning of an English word, typed them into the OED, and grabbed any good-quality headwords, common derivatives, lemmas, and subentries that appear in the auto-complete. 
<!-- TODO: finish going through all letter pairs -->
* I manually went through the entire list of entries I had at this point -- to remove bad entries I had missed the first time around, and to add compelling derivatives and phrases based on the entries I had collected. 
<!-- Especially with less free time around this time, this step took another 2 months or so. -->
* I've also added any random words/phrases that came to me, or that I encounter in daily life that I thought would make a good entry.
<!-- * TODO: Missed a lot of plurals in the earlier parts of the main list -->

Based on my own constructing experience, I'm not convinced adding additional tags to entries (syntactic or semantic) would be helpful.

## Citation
If you find this dataset useful, I would appreciate if you acknowledged it! If you use this dataset for an academic publication, here is a BibTex entry:
```
@misc{msfit-dataset,
  title = {MsFit Crossword Dataset},
  author = {Nicole Feng},
  note = {https://github.com/nzfeng/crossword-dataset},
  year = {2022}
}
```
