from bubplayer import Player
import random


class BlowUpBash:
    def __init__(self):
        self.prompt = ""
        
    def generatePrompt(self):
        possible_prompts = ["con","hea","car","ivi","ump","ive","es","ic","ks","tr","to","bil","sts","tt","wr","omi","ti","ap","rk","en","op","ial","omp","arr","sm","ie","on","nis","ron","fl","ns","lo","ns","no","nds","tr","an","li","re","ut","tim","chi","an","oth","pe","ent","amp","is","al","mo","er","tio","fi","ilo","nes","ch","nt","in","gge","er","sti","bl","ha","din","un","le","in","sms","ba","bu","lu","ra","ina","ni","io","ari","ret","go","con","ion","er","he","no","om","der","ch","pe","al","ant","is","ing","om","olo","per","ula","nch","ss","tha","esi","ano","hob","es","mat","al","te","ic","es","ing","nst","of","rh","su","dr","re","lo","al","po","ho","yp","is","eat","na","er","erg","co","pp","ea","no","rma","io","her","st","war","nc","lay","fa","ize","ba","rip","ze","og","his","oli","mat","ch","ism","rco","az","nce","oun","ar","ic","ph","hi","dar","qui","end","pr","ata","api","ss","sh","iv","utt","ed","ct","rc","iz","ram","at","pe","ip","ti","ut","els","ls","ck","mis","der","mi","nt","re","im","bal","uli","dio","ac","ali"]
        self.prompt = random.choice(possible_prompts)

    def isValidGuess(self, guess):
        if self.prompt in guess:
            pass
