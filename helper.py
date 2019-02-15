# helper.py contains a set of functions are helpful in other areas, but dont have a home

import re

# cleans a string so that it can be written to file without a UnicodeEncodeError
def clean_to_file(s):
    s = s.encode('ascii', 'ignore').decode('utf-8') # deletes bad stuff?
    s = re.sub(r'\s+', ' ', s) # convert all groups of whitespace to single space
    return s

# cleans a url, at least makes it look better
def clean_url(url):
    # theres definitely better ways to do this but whatever
    url = (url
        .replace('https://southpark.fandom.com/wiki/Portal:Scripts/', '')
        .replace('https://southpark.fandom.com/wiki/', '')
        .replace('/Script', '')
        .replace('_', ' ')
        .replace('%27', "'")
        .replace('%3F', '?')
        .replace('%26', '&')
        .replace('%C3%A8', 'e')#'è')
        .replace('%25', '%')
    )
    return url

# beautifies the string before tweeting it
# useful when textgenrnn model built on words
def clean_tweet(s):
    mappings = [
        # slang words beginning with '
        ["' cause","'cause"],
        ["' scuse","'scuse"],
        ["' nam","'nam"],
        ["' im","'im"],
        ["' ere","'ere"],
        ["' kay","'kay"],
        ["' til","'til"],
        ["' em","'em"],
        ["' bout","'bout"],
        ["' the","'the"],
        ["' member","'member"],
        # slang words ending with '
        ["o '","o'"],
        ["friggin '","friggin'"],
        ["splicin '","splicin'"],
        ["treatin '","treatin'"],
        ["bringin '","bringin'"],
        ["starvin '","starvin'"],
        ["ol '","ol'"],
        ["kickin '","kickin'"],
        ["sayin '","sayin'"],
        ["layin '","layin'"],
        ["fuckin '","fuckin'"],
        ["choppin '","choppin'"],
        ["parents '","parents'"],
        ["goin '","goin'"],
        ["huckin '","huckin'"],
        ["cryin '","cryin'"],
        ["pickin '","pickin'"],
        ["playin '","playin'"],
        ["backstabbin '","backstabbin'"],
        ["movin '","movin'"],
        ["guys '","guys'"],
        ["gettin '","gettin'"],
        ["nothin '","nothin'"],
        ["keepin '","keepin'"],
        ["leavin '","leavin'"],
        ["takin '","takin'"],
        ["laughin '","laughin'"],
        ["freakin '","freakin'"],
        ["kindergartners '","kindergartners'"],
        ["talkin '","talkin'"],
        ["spendin '","spendin'"],
        ["losin '","losin'"],
        ["tryin '","tryin'"],
        ["breakin '","breakin'"],
        ["fudgin '","fudgin'"],
        ["doin '","doin'"],
        ["hittin '","hittin'"],
        ["girls '","girls'"],
        ["whistlin '","whistlin'"],
        ["givin '","givin'"],
        ["hangin '","hangin'"],
        ["frickin '","frickin'"],
        ["clearin '","clearin'"],
        ["sippin '","sippin'"],
        ["somethin '","somethin'"],
        ["havin '","havin'"],
        ["showin '","showin'"],
        ["comin '","comin'"],
        ["students '","students'"],
        ["frontin '","frontin'"],
        ["tellin '","tellin'"],
        ["vampires '","vampires'"],
        ["rapin '","rapin'"],
        ["headin '","headin'"],
        ["lookin '","lookin'"],
        ["mays '","mays'"],
        ["Butters '","Butters'"],
        ["cuttin '","cuttin'"],
        ["an '","an'"],
        ["payin '","payin'"],
        ["n '","n'"],
        ["flippin '","flippin'"],
        ["trees '","trees'"],
        ["callin '","callin'"],
        ["sittin '","sittin'"],
        ["messin '","messin'"],
        ["gon '","gon'"],
        # punctuation
        [" ?","?"],
        [" !","!"],
        [" .","."],
        [" ,",","],
        [" ;",";"],
        [" :",":"],
        [" ' ","'"],
        [" - ","-"],
        ["# ","#"],
        ["[ ","["],
        [" ]","]"]
    ]
    debug = False
    for mapping in mappings:
        s0 = s
        s = s.replace(mapping[0], mapping[1])
        if debug:
            print('"{}".replace("{}", "{}") => "{}"'.format(s0, mapping[0], mapping[1], s))
    return s.strip()
