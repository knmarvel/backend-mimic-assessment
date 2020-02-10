![Kano's logo](https://i.imgur.com/Yc5nxbI.png)

# Mimic 
Build a "mimic" dict that maps each word that appears in the alice.txt file to a list of all the words that immediately follow that word in the file. The list of words can be be in any order and should include duplicates. So for example the key "and" might have the list ["then", "best", "then", "after", ...] listing all the words which came after "and" in the text.

For development, use the short `imdev.txt` file.  When your python mimic dictionary is created from this file, it should look like this if you print it out:
```python
{
    "" : ["I"],
    "I" : ["am", "don't"], 
    "am": ["a"], 
    "a": ["software"],
    "software" : ["developer,"],
    "developer," : ["and"],
    "and" : ["I"],
    "I" : ["don't"],
    "don't" : ["care"],
    "care" : ["who"],
    "who" : ["knows"]
}
```
Notice that the first entry in the dicttionary above is the empty string `""`.  Since we are creating a dictionary of 'next' word lists, it implies that there exists a previous word key for each next-list value.  This of course is true, except in the case of the first entry of the dictionary. Use the empty string as a seed for the first entry in the dictionary.

With the mimic dict, it's fairly easy to emit random text that mimics the original. Print a word, then look up what words might come next and pick one at random as the next word.

For fun, feed your program to itself as input.

# Sample Output, using alice.txt as input
```
Alice's shoulder, and seemed to the same order,' continued the hall; but, after glaring at all the Mock Turtle: `crumbs would be a good opportunity of authority over the Mouse. `--I proceed. "Edwin and she came a child!' said the Gryphon: and all round it, and sharks are all over the King replied. `Yes, please do!' said nothing. `When I'M a whisper, half no right distance--but then Alice, and it. She went on, three weeks!' `I'm glad there seemed to sing this:-- `Fury said Alice, and she had to see Shakespeare, in her hands at the Gryphon, and, last word with a minute or other; but he had gone down off staring at the Cat, she began: `O Mouse, do next! If they lessen from being drowned in the Panther received knife and turns out again. In the words did not to say "What a Caterpillar called him as she was to the court, `Bring me see--how IS the roof of delight, which the King said, just explain the first one for two guinea-pigs, who only yesterday things are you?' She was gone, and there was in a few minutes, and tumbled head first, and look at the words
```


## PR (Pull Request) Workflow for this Assignment
1. *Fork* this repository into your own personal github account.
2. Then *Clone* your own repo to your local development machine.
3. Create a separate branch named `dev`, and checkout the branch.
5. Commit your changes, then `git push` the branch back to your own github account.
5. From your own Github repo, create a pull request (PR) from your `dev` branch back to your own master.
6. Copy/Paste the URL **link to your PR** as your assignment submission.
7. Your grader will post code review comments inline with your code, in your github account. Be sure to respond to any comments and make requested changes. **RESUBMIT** a new link to your PR after making changes.  This is the code review iteration cycle.
