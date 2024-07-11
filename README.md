# Stanley's Steno Dictionaries

### Why

For people who want to see my dictionaries.

### How

Download them and load them into Plover as .json dictionaries.


### Contents

- braille.json
    - My starter dictionary for steno-based Braille input.
- smalldict.json
    - Starter dictionary Mirabai gave me as a template (not actively updated or used).
- stan-italiano.json
    -  Dictionary I started when I was doing an Italian class. Not very developed.
- stanespanol.json
    - Main Spanish steno dictionary.
- stanmain.json
    - My main English dictionary.
- stanplover.json
    - Additional entries to correct formatting errors caused by RTF -> JSON conversion.
- usage_stats.txt
    - Shows usage statistics to help learners (or anyone, really) analyze my dictionary usage patterns.


### License

Don't care.

# Stanley's Dictionaries

You've found my dictionary repository! The main dictionary that I update the most is the namesake one, `stanmain.json`. I will update this readme to include more but I'll start with this. Many on the Plover Discord have mentioned that this repo is just dictionaries with no explanation so I'm going to attempt to explain what's going on in my head in general terms and hopefully it'll help whoever is reading this to figure out what the hell it is I'm thinking when seeing my outlines.


# General History

I originally started learning Phoenix Theory back in 2009 or so. After using that theory for a little while, I decided its approach was not for me, especially after learning about the `R-R`. It's basically a form of a shift key in steno where you would repeatedly use `R-R` to cycle through different steno conflicts. After that, I'd found an online PDF of the Philly Clinic Theory. I found a collection of stock dictionaries on Stenovations' website and saw that there was a stock dictionary for Philly of around 30,000 entries available for download for free on their website. I downloaded it and started retraining to override what I had learned from Phoenix. After I got sufficiently advanced, I bought the Magnum Steno book and that became my ultimate theory source of truth.

If you have no exposure to Magnum Theory, I will tell you it is very abstract. You will find things in there based on phonetics, on English spelling, or based on an arbitrary combo that are meant to be memorized as a shape. Accordingly, my theory is a mish-mash of all three of these principles. My way of writing was never meant to be a formalized theory and you should consider it as a guideline, and not absolute in any way. Plus, there are a lot of things from the stock dictionary that I'm still cleaning out that I never use. Anything with a consistent pattern is a pretty clear indication of something I use regularly, though. A whole bunch of entries with `SKPWE-` for "and we..." phrases is a strong signal that this is how I handle phrases that start with that.

# Phonetics

I generally use normal steno conventions with a few exceptions. This usually comes from the fact that I adopted Philly Clinic early on and it wasn't originally designed to be a realtime theory. So you will see lots of instances of me omitting the `E` in long-O phrases like `TKPWO` for go or `STROBG` for stroke.

For some words that end in -a, I use the final `-D` to represent it. I learned this from my colleague, Lisa Hutchinson in Seattle while I was shadowing her on CART jobs. I think it comes from the Italian keyboard. For example, "plethora" would be written as `PHREFRD` or "diaspora" would be written as `TKAOEUFRPD`.

For past-tense verbs with double obstruents (usually /dd/or /td/), I use final `-TD`. For example, "extended," I would write as `STEPBTD`. Or "branded", I would write as `PWRAPBTD`.

I also have a general pattern I use for Spanish-sounding words. Basically, you assume if the word ends in a consonant, and you don't add anything to the end, it ends with an -a. "Santa" like in Santa Maria is written just `SAPBT`. But for -o, I add the asterisk. So "Santo" would be `SA*PBT`. So "Santo Domingo" would be `SA*PBT/TKPH*EUPBG`. The `*` takes care of the final -o.

I use final -DZ to create the gerund or -ing form. But because of how the steno keyboard is laid out, words that end in an -s, -t, or -d, I will drop those and add the -DZ. So the gerund of "break" (breaking) would be `PWRAEUBGDZ`. The gerund of "promise" would be `PROPLDZ` since you can't hit the `-S` at the same time as the `-DZ`.

With the combo `AE`, it can mean I'm disambiguating a homophone or it's a multi-syllabic word. "Rain" is `RAEUPB` but "rainy" is `RAEPB`. "Space" is `SPAEUS` but "spacey" is `SPAES`.

# How much do I brief and/or phrase?

If I can find a one-stroke gibberish syllable that makes sense for it, I will go ahead and brief it that way. If by some way, I can fit all the relevant sounds in a word or phrase in a single stroke, it becomes a single stroke and I will make it a point to memorize it. It's called shorthand for a reason. I know plenty of stenographers that can write twice as many strokes as I can in the same amount of time but my speed primarily comes from my polyglot background and my ability to memorize tons of arbitrary goop and put it to use immediately. Take this with a grain of salt because not everyone possesses the same neurology. Some need to have consistency above all even at the expense of brevity. So I say do what works for you first, always!

# Arbitrary Shapes
In general, I use a ton of shape outlines. This is to say that the individual letters pressed are loosely or not at all related to the actual output. There is no mnemonic or any convenient trick to memorizing these. You have to go through the rote practice to turn these from unrelated gibberish to instant recall. Sorry, I don't have any tips or tricks for learning these. You just have to go for it yourself.

## Right-hand Phrase Enders

| Phrase        | Steno    | Phrase         | Steno    |
| ------------- | -------- | -------------- | -------- |
| been          | `-B`     | some           | `*PLS`   |
| be            | `*B`     | could          | `-BGD`   |
| it            | `*T`     | couldn't       | `*BGD`   |
| like          | `-FPL`   | could be       | `-FRBGD` |
| the           | `-T`     | have           | `-F`     |
| that          | `-LGTS`  | 've            | `*F`     |
| this          | `-TSDZ`  | have been      | `-FB`    |
| these         | `-RPG`   | 've been       | `*FB`    |
| those         | `-FBL`   | has            | `-FPLTD` |
| can           | `-BG`    | hasn't         | `*FPLTD` |
| can't         | `*BG`    | had            | `-D`     |
| can be        | `-FRBG`  | 'd             | `*D`     |
| means         | `-PLS`   | should         | `-RBD`   |
| should be     | `-RBLG`  | do             | `RPBLGS` |
| was           | `-FS`    | don't          | `*RPBLGS`|
| wasn't        | `-FSZ`   | did            | `RPLS`   |
| were          | `-RP`    | didn't         | `*RPLS`  |
| weren't       | `*RP`    | does           | `-RBGZ`  |
| we            | `-FRPBLG`| doesn't        | `*RBGZ`  |
| would         | `-LD`    | will           | `-L`     |
| 'd be         | `*BD`    | 'll            | `*L`     |
| wouldn't      | `*LD`    | won't          | `-FPZ`   |
| would have    | `*FLD`   | won't be       | `*FPZ`   |
| would have been| `*FBLD` | knew           | `-PZ`    |

# Left-hand Phrase Starters

| Phrase           | Steno       |
| ---------------- | ----------- |
| about            | `KPW-`      |
| ---------------- | ----------- |
| and              | `SKP-`      |
| and we           | `SKPWE-`    |
| ---------------- | ----------- |
| but              | `PWH-`      |
| but we           | `PWHAOE-`   |
| ---------------- | ----------- |
| because          | `SKPR-`     |
| because we       | `SKPWRE-`   |
| ---------------- | ----------- |
| for              | `TPR-`      |
| ---------------- | ----------- |
| the only         | `TW-`       |
| ---------------- | ----------- |
| will             | `HR-`       |

# "Don't", "Didn't," "Could't"



** More to come! **
