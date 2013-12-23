import sys

def load_preamble( orig_texfile , plos_texfile ):
    preamble=[]
    f=open(plos_texfile,"r")
    while True:
        l=f.readline()
        if (l==''): break
        if (r"\begin{document}" in l ):
            break
        else:
            preamble.append(l)
    f.close()
    f=open(orig_texfile,"r")
    while True:
        l=f.readline()
        if (l==''): break
        if (r"\begin{document}" in l ):
            break
        else:
            if ("newcommand" in l):
                preamble.append(l)
    return "".join(preamble)

def author_specs(authors,corr,email):
    """
    authors is a list of lists.
    For example:
    ["Author1", "Dept/Program/Center", "Institution Name", 
    "City", "State", "Country"]
    """
    tmp=""
    la=len(authors)
    for i in range(la):
        a=authors[i]
        if (i==corr):
            tmp=tmp+(a[0]+"$^{%d,\\ast}$"%(i+1))
        else:
            tmp=tmp+(a[0]+"$^{%d}$"%(i+1))
    if (i<(la-1)):
        tmp+=",\n"
    else:
        tmp+="\n"
    tmp+="\\\\\n"
    for i in range(la):
        a=authors[i]
        tmp+="\\bf{%d} %s %s, %s, %s, %s, %s\n"%\
        (i+1,a[0],a[1],a[2],a[3],a[4],a[5])
        tmp+="\\\\\n"
    tmp+="$\\ast$ E-mail:%s\n"%email     
    return tmp 


def document(title,abstract,doc):
    tmp=""
    tmp+="""\\begin{document}

%% Title must be 150 characters or less
\\begin{flushleft}
{\\Large
\\textbf{%s}
}\n
"""%(title)
    
    tmp+="\\end{flushleft}\n"
    tmp+="\\section*{Abstract}\n"
    tmp+=abstract
    tmp+=doc
    tmp+="\\end{document}"
    return tmp

def extract_abstract(orig_texfile):
    a=""
    f=open( orig_texfile , "r" )
    ins=False
    while True:
        l=f.readline()
        if (l==''):break
        if ("begin{abstract}" in l):
            ins=True
            continue
        if ("end{abstract}" in l):
            break
        if (ins):
            a+=l
    return a


def slurp_content(orig_texfile):
    c=""
    figure=""
    f=open(orig_texfile,"r")
    ins=False
    infig=False
    while True:
        l=f.readline()
        if (l==''):break
        if ( "maketitle" in l ):
            ins = True
            continue
        if ( "begin{figure}" in l):
            infig=True
            figure+=l
            continue
        if ("end{figure}" in l):
            figure+=l
            infig=False
            continue
        if (infig):
            figure+=l
            continue
        if ( "bibliography{" in l):
            break
        if (ins):
            c+=l
    return (c,figure)    


#############################################
orig_texfile="../beta_paper.tex"
plos_texfile="plos_template.tex"
dept="Statistical Genomics"
institution=r"Centro Nacional de An\'alisis Gen\'omico"
city="Barcelona"
state="Catalonia"
country="Spain"
ema=["Emanuele Raineri",dept,institution,city,state,country]
marc=["Marc Dabad",dept,institution,city,state,country]
simon=["Simon Heath",dept,institution,city,state,country ]
authors=[ema,marc,simon]
#print author_specs(authors,0,"emanuele.raineri@gmail.com")
title="A note on exact differences between beta distributions in genomic (methylation) studies"
abstract=extract_abstract(orig_texfile)
preamble = load_preamble(orig_texfile,plos_texfile)
content,figures=slurp_content(orig_texfile)
print preamble
print document(title,abstract,content)
#print figures
