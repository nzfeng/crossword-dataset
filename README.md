left off at "railroad"

# Crossword dataset
This is **manually curated** dataset of \~35,000 words and phrases that I have deemed suitable as entries for (American) word puzzles, primarily American-style crosswords. All entries are contained in a single alphabetized .txt file, with each entry occupying a separate line. I have left original punctuation in the entries if possible, for better human readability; standardization of the entries and further sorting is left to the user.

Any entry is included only if (1) it is commonly used in everyday American English, and (2) it can stand alone as a non-awkward crossword entry. This dataset includes nouns, adjectives, verbs; it contains few gerunds, adverbs, and proper nouns. It also includes short phrases, idioms, and sets of words that often go together (i.e. "school night", "secret santa", "ride shotgun", etc.) See the "Rules for inclusion" section for more details about how I decided whether an entry should belong. See "Curation process" for where I curated these entries from.

This dataset is used in my open-source [MsFit]() crossword construction software. Feel free to use this dataset for your own project; if for an academic publication, a BibTex entry is at the bottom of the README.

## Motivation
I wanted to make crossword puzzles that fit my standards. I quickly realized that the main challenge of crossword construction, at any level of algorithmic involvement, is having a good bank of words to choose from. <!-- Most of the demand for human crossword constructors, after supplying any theme entries, seems to just be guiding construction towards having quality fills.-->

I found that existing crossword and natural language processing (NLP) datasets weren't strict enough by the standards I was seeking. Crossword datasets are usually formed by scraping indiscriminately from other datasets, including existing puzzles, which contain entries I wanted to avoid. Meanwhile, the criteria for acceptable crossword entries is too niche for any NLP datasets to be applicable. What makes a "good" crossword entry is also subject to taste, and can be more subtle than, e.g. selecting for part-of-speech or corpus frequency.

Since what is considered a "good" crossword entry is a matter of taste, I concluded that any good wordset must be curated to taste, manually. Since the number of words in the English language is on the order of 10^5, manual curation was at least possible. 

I assume that there exist people who have already put forth significant effort into curating their own quality puzzle wordlists; however, I assume such people are likely constructors who make a living off writing puzzles, and therefore have little incentive to share their lists. <!-- (Software/tools in the crossword community in general seems to be weirdly proprietary. Sharing doesn't seem to be in the culture.) -->

## Rules for inclusion
What makes a "good" wordlist is kind of subjective. Personally, I wanted to make a "core" wordlist of common-knowledge American English entries, with as few "specific" entries as possible (i.e. names, places, pop culture references.) After some deliberation, here is how I decided to choose words:

* The central goal is to only include words and phrases that are often used in spoken and written American English. **Every single entry** in this dataset should be a usable crossword entry. If one is interested in using a dataset simply to help them determine if a grid is fillable using an auto-fill functionality, then they can just grab any uncurated wordlist. 
* **Zero crossword-ese** and filler words. All entries should be able to hold their own as lively crossword entries, and ideally lend themselves well to creative clues.
* This dataset should be a "core" crossword dataset with few overly-specific entries. No people -- I don't consider people-related entries as "core" entries. Exceptions are extremely iconic people who are a part of American collective memory at this point, like EINSTEIN or ELVIS.
<!-- * The general ranking of parts of speech is: noun > verb > adjective > adverb > prepositions > article > conjunction > pronouns. -->
* Focus on root words. Only include derivative words (plurals, gerunds, past tense, etc.) if they are commonly used in everyday language, and can act as natural-sounding entries. A good rule of thumb is to avoid adverbs. (On the other hand, words that end in "-ly" but are not adverbs usually make decent adjectives. Ex: EARLY, LONELY, etc.) Also avoid superlatives if they end in "-est".
* If there are words with multiple derivatives and one is definitely used more often than the others, only include the commonly-used one. Ex. FIREWORKS vs. FIREWORK, VAGARIES vs. VAGARY.
* For nouns, avoid gerunds (words that end in "-ing"), and words that end in "-ness", "-tion", "-ment", or "-ism". A lot of these words are in the category of "words that are technically English words but no one uses them." Only include these types of words if they are commonly used in everyday language.
* Similarly, avoid nouns that end in "-er" that mean "someone who does X", and aren't really used in everyday language. Ex: ADVANCER, etc. Only include if they are common words or refer to commonly-known roles, ex. USER, COMPOSER.
* Try not to include words/phrases that, although they are commonly used, make for boring entries. This is somewhat subjective, especially since boringness also depends on the cluing. But some examples of what not to include are legal terms and phrases, and other dry phrases pertaining to specific fields, government, bureaucracy, banking, and other societal minutiae.
* Don't include full phrases if their abbreviations are more commonly used, i.e. "magnetic resonance imaging" for MRI. The former would be a boring entry; if entries are going to be long, they should be exciting.
* Avoid phrases that depend on too many prepositions or conjunctions ("and", "of", "for", etc.) For shorter entries, aim to have zero "extra filler words". 
* For shorter entries, avoid two-word phrases, especially if one of the words is a preposition (ASK_IN, etc.) Only include multi-word phrases if they really do "come as a set", i.e. "BACK_OUT". For long entries, avoid phrases with more than 3 words.
* Try to avoid partial phrases. I assume these would almost always have fill-in-the-blank clues, which are okay once in a while, to help a solver get started, but that's about it. Best to keep them to a minimum. No partial phrases that are awkward on their own, though, like "ONEI" as part of "That's one I haven't heard before."
* Don't include words that have negative prefixes like "un-", "dis-", etc. unless they are just as commonly used as their positive counterpart (if not more common), and come with their own connotations and usage patterns. I.e., if you look the word up in the dictionary and it's simply defined as the negation of something, don't include it.
<!--* Similarly, try not to include words whose meanings are too evident from their components, such as "southbound." It would be hard to come up with clues. -->
* **No British-English spellings**, or non-English entries except for common phrases ("vice versa", etc.) When puzzles rely on other languages, dialects, or variant spellings, it feels cheap.
* **No offensive**, insensitive, or particularly unpleasant entries. No entries relating to warfare, violence, weapons, chemical agents that have been been used in war, etc. Avoid "gross" entries pertaining to bodily fluids, bodily functions, crimes, abuse, etc. No entries with negative connotations or may be triggering (i.e. RACISM, MANIFEST_DESTINY, SUICIDE, etc.) Even if their clues are benign, or they have alternate definitions which are benign (like SUICIDE), the topics that these entries are related to when taken at face-value don't deserve visibility in crossword puzzles. 
* Avoid places, except for maybe iconic American places. Good rule of thumb is whether this location would be known to a non-American.
* Most of these rules basically just boil down to "Only include commonly-used words." Really try to only include entries that are commonly used, roll off the tongue, can be standalone entries, encourage lively clues, and so on.

There might be entries that I've accidentally included that don't adhere to my own rules. Conversely, I've almost certainly missed some good entries. Don't be shy about emailing me or making a PR if you would like to contribute to this wordlist!

## Curation process
* I started by manually filtering all \~147k lemmas in [WordNet](https://wordnet.princeton.edu/), which took me about a month. In the end, about 21% I deemed good enough to include in this dataset. 
* I began filtering words from the [Broda wordlist](https://peterbroda.me/crosswords/wordlist/), which presents another \~320k unique entries after removing any words I've already looked at, and words with scores less than 50 (i.e. keeping only words that have been deemed above a certain level of quality, or are unscored.) I'm finding that the dataset is mostly not what I'm looking for, so I probably won't be finishing sifting through the Broda wordlist anytime soon.
* I've also manually scraped relevant words & phrases from "[Updates to the OED](https://public.oed.com/updates/)" pages to obtain "fresh" entries.
* I've copied a few vocab lists from ESL sites. 
* [Desi Quintas](http://www.desiquintans.com/nounlist) has a hand-curated plain.txt list of 6801 common nouns in English; his curation criteria aligns really well with what makes a good crossword entry. I've gone through and removed British-English and words I don't like, resulting in \~6250 words. This added maybe another \~1000 entries unique from WordNet and some other filtered words I had at the time.
* I've filtered a list of 10,000+ nouns on [richardharringtonblog.com](https://richardharringtonblog.com/list-of-nouns). First I removed any entries that I had already filtered, which removed the vast majority; I then manually filtered the remaining, which left \~380 entries.
* TODO: I went through all letter pairs that are legal at the beginning of an English word, typed them into the OED, and grabbed any good-quality headwords/common derivatives/lemmas/subentries that appear in the auto-complete.
* TODO: Re-go through Broda lists, oed_updates, earlier wordnet lists.
* I've also added any random words/phrases that came to me, or that I encounter in daily life that I thought would make a good entry.

I thought about adding syntactic/semantic tags to entries, and possibly putting them in a database, although that won't happen without other people to help :wink:. On the other hand, I'm also not convinced that this will provide much more benefit relative to the effort this would require, so I'm not planning to do this any time soon.

## Citation
If you find this dataset useful, I would appreciate if you acknowledged it! If you use this dataset for an academic publication, here is a BibTex entry:
```
@misc{crossword-dataset,
  title = {crossword-dataset},
  author = {Nicole Feng},
  note = {https://github.com/nzfeng/crossword-dataset},
  year = {2022}
}
```