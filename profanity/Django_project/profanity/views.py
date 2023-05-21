from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
from .models import profanity
from better_profanity import profanity
import os
from django.conf import settings
from django.core.files import File
from better_profanity import Profanity
import pandas as pd

# Create your views here.
def home(request):
    
   return render(request,'1.html')
def profanity(request):
    if request.method == 'GET':
    
      name = request.GET["name"]
      comment = request.GET["comment"]
      words= ['shit','fuck','bitch','terrorism','offense','fat','a55', 'anal', 'anus', 'ar5e', 'arrse', 'arse' ,'ass', 'a$$', 'ar$e', 'ass-fucker',
 'asses', 'assfucker' ,'assfukka' ,'asshole', 'assholes', 'asswhole' ,'a_s_s','stupid','idiot',
 'b!tch', 'b00bs' ,'b17ch' ,'b1tch', 'ballbag', 'balls', 'ballsack', 'bastard',
 'beastial' ,'beastiality', 'bellend', 'bestial', 'bestiality', 'bi\\+ch',
 'biatch' ,'bitch' ,'bitcher', 'bitchers', 'bitches' ,'bitchin' ,'bitching',
 'bloody' ,'blow job', 'blowjob' ,'blowjobs', 'boiolas', 'bollock', 'bollok',
 'boner' ,'boob' ,'boobs', 'booobs', 'boooobs', 'booooobs', 'booooooobs',
 'breasts' ,'buceta', 'bugger' ,'bunny fucker', 'butthole', 'buttmuch',
 'buttplug' ,'c0ck' ,'c0cksucker' ,'carpet muncher', 'cawk' ,'chink' ,'cipa',
 'cl1t' ,'clit' ,'clitoris', 'clits' ,'cnut' ,'cock', 'cock-sucker',
 'cock sucker' ,'cockface', 'cockhead', 'cockmunch', 'cockmuncher', 'cocks',
 'cocksuck' ,'cocksucked', 'cocksucker' ,'cocksucking' ,'cocksucks' ,'cocksuka',
 'cocksukka','cok', 'cokmuncher', 'coksucka' ,'coon' ,'cox' ,'crap', 'cum',
 'cummies' ,'cummiez' ,'cummer' ,'cumming', 'cums', 'cumshot' ,'cunilingus',
 'cunillingus' ,'cunnilingus', 'cunt', 'cuntlick' ,'cuntlicker', 'cuntlicking',
 'cunts' ,'cunt-muncher' ,'cuntmuncher', 'cuntmunch', 'cyalis', 'cyberfuc',
 'cyberfuck','cyberfucked' ,'cyberfucker', 'cyberfuckers' ,'cyberfucking',
 'd1ck' ,'damn' ,'dick' ,'dickhead', 'dildo', 'dildos', 'dink', 'dinks', 'dirsa',"dank","otha","ommala","badu",
 'dlck' ,'dog-fucker' ,'doggin' ,'dogging', 'donkeyribber', 'doosh', 'duche',
 'dyke' ,'ejaculate', 'ejaculated', 'ejaculates' ,'ejaculating' ,'ejaculatings',
 'ejaculation' ,'ejakulate', 'f u c k' ,'f u c k e r', 'f4nny', 'fag' ,'fagging',
 'faggitt' ,'faggot' ,'faggs', 'fagot', 'fagots', 'fags', 'fanny', 'fannyflaps','pussy',
 'rimming' ,'s.o.b.', 'sadist', 'schlong' ,'screwing', 'scroat', 'scrote','sadist','penis','pool',
 'scrotum', 'semen', 'sex' ,'sh!\\+', 'sh!t', 'sh1t' ,'shag', 'shagger','shaggin','holyshit',
 'shagging', 'shemale','shi\\+', 'shit' ,'shitdick', 'shite', 'shited', 'shitey','ugly','distorting',
 'shitfuck' ,'shitfull' ,'shithead' ,'shiting' ,'shits' ,'shitted', 'shitter',
 'shitting' ,'shitty', 'skank', 'slut' ,'sluts', 'smegma' ,'smut', 'snatch','mf','motherfucker',
 'son-of-a-bitch' ,'spac' ,'spunk', 's_h_i_t', 't1tt1e5', 't1tties', 'teets',"son of a bitch",
 'teez', 'testical', 'testicle', 'tit', 'titfuck', 'tits', 'titt' ,'tittie5',
 'tittiefucker' ,'titties', 'tittyfuck', 'tittywank', 'titwank', 'tosser',
 'turd' ,'tw4t', 'twat', 'twathead', 'twatty' ,'twunt', 'twunter' ,'v14gra',
 'v1gra' ,'vagina' ,'viagra', 'vulva' ,'w00se' ,'wang' ,'wank', 'wanker' ,'wanky','titties',
 'whoar' ,'whore' ,'willies' ,'potta','willy' ,'xrated','suck my dick','shut' ,'xxx','fat','idiot','mental','psychopath','psycho','vadakan','street dog','mf','stalker','nude','nudity']
      
    
     
    # if __name__ == '__main__':
    #   Profanity.load_censor_words()
    #   x = Profanity.censor(comment)
    #   print(x)
      
    for i in words:
         while i in comment:
              comment = comment.replace(i, len(i) * '*')
    else:
             print(comment)

    return render(request,"result.html",{'name':name,"comment":comment})