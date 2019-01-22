import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

from gensim.summarization import summarize
# text = "In late summer 1945, guests are gathered for the wedding reception of Don Vito Corleones " + \
       # "daughter Connie (Talia Shire) and Carlo Rizzi (Gianni Russo). Vito (Marlon Brando),"  + \
       # "the head of the Corleone Mafia family, is known to friends and associates as Godfather. "  + \
       # "He and Tom Hagen (Robert Duvall), the Corleone family lawyer, are hearing requests for favors "  + \
       # "because, according to Italian tradition, no Sicilian can refuse a request on his daughter's wedding " + \
       # " day. One of the men who asks the Don for a favor is Amerigo Bonasera, a successful mortician "  + \
       # "and acquaintance of the Don, whose daughter was brutally beaten by two young men because she"  + \
       # "refused their advances; the men received minimal punishment from the presiding judge. " + \
       # "The Don is disappointed in Bonasera, who'd avoided most contact with the Don due to Corleone's" + \
       # "nefarious business dealings. The Don's wife is godmother to Bonasera's shamed daughter, " + \
       # "a relationship the Don uses to extract new loyalty from the undertaker. The Don agrees " + \
       # "to have his men punish the young men responsible (in a non-lethal manner) in return for " + \
        # "future service if necessary."
		
text = "This is the story of a very greedy rich man who chanced upon meeting a fairy. The fairy’s hair was caught in a few tree branches." + \
		"Realising he had an opportunity to make even more money, he asked for a wish in return for helping the fairy. He said," + \
		"’All that I touch should turn to gold’, and his wish was granted by the grateful fairy."+ \
		"The greedy man rushed home to tell his wife and daughter about his new boon, all the while touching stones and pebbles and" + \
		"converting them into gold. Once he got home, his daughter rushed to greet him. As soon as he bent down to scoop her up in " + \
		"his arms, she turned into a gold statue. He realized his folly and spent the rest of his days searching for the fairy " + \
		"to take away his wish."
		
print(summarize(text))
