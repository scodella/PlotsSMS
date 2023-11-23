from array import *

class sms():

    def __init__(self, modelname):
        if modelname.find("T1tttt") != -1: self.T1tttt()
        if modelname.find("T2tt") != -1: self.T2tt()
        if modelname.find("T2bW") != -1: self.T2bW()
        if modelname.find("TChipmSlepSnu") != -1: self.TChipmSlepSnu()
        if modelname.find("TChipmWW") != -1: self.TChipmWW()
        if modelname.find("TSlepSlep") != -1: self.TSlepSlep()
        if modelname.find("T5ttttDM175") != -1: self.T5ttttDM175()
        if modelname.find("T5tttt") != -1: self.T5tttt()
        if modelname.find("T1bbbb") != -1: self.T1bbbb()
        if modelname.find("T1qqqq") != -1: self.T1qqqq()
        if modelname.find("T5qqqqVV") != -1: self.T5qqqqVV()


    def T1tttt(self):
        # model name
        self.modelname = "T1tttt"
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow t #bar{t} "+lsp_s;
        self.label2= "";
        # scan range to plot
        self.Xmin = 600.
        self.Xmax = 2200.
        self.Ymin = 0.
        self.Ymax = 1900.
        self.Zmin = 0.001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{g}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.boxOn = False
        
    def T2tt(self):
        # model name
        self.modelname = "T2tt"
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{t} #tilde{t}, #tilde{t} #rightarrow t "+lsp_s;
        self.label2= "";
        # scan range to plot
        self.Xmin = 150.
        self.Xmax = 700. #1200.
        self.Ymin = 0.
        self.Ymax = 900. #1200.
        self.Zmin = 0.01 #0.001
        self.Zmax = 100.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{t}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = True
        self.boxOn = True
        
    def TChipmSlepSnu(self):
        # model name
        self.modelname = "TChipmSlepSnu"
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        charg = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{#pm}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        charp = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{+}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        charm = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{-}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow "+charp+" "+charm+",  "+charg+" #rightarrow #tilde{l} #nu / #tilde{#nu} l,  #tilde{l} (#tilde{#nu}) #rightarrow l (#nu) "+lsp_s;
        self.label2= "BR("+charg+" #rightarrow #tilde{l} #nu) = 0.5,  m#kern[0.1]{_{#lower[-0.12]{#tilde{l}(#tilde{#nu})}}} = (m#kern[0.1]{_{#lower[-0.12]{"+charg+"}}} + m#kern[0.1]{_{#lower[-0.12]{"+lsp_s+"}}})/2";
        # scan range to plot
        self.Xmin = 100.
        self.Xmax = 1500.
        self.Ymin = 0.
        self.Ymax = 900.
        self.Zmin = 0.0001
        self.Zmax = 100.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{"+charg+"}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.boxOn = False
        
    def TSlepSlep(self):
        # model name
        self.modelname = "TSlepSlep"
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        slep  = "#lower[-0.12]{#tilde{#font[12]{l}}}"
        sele  = "#lower[-0.12]{#tilde{#font[12]{e}}}#kern[0]{#scale[0.85]{_{L/R}}}"
        smuo  = "#lower[-0.12]{#tilde{#mu}}#kern[0]{#scale[0.85]{_{L/R}}}"
        Wpm = "W#scale[0.85]{^{#pm}}"
        #self.label= "pp #rightarrow "+sele+" "+sele+",  "+smuo+" "+smuo
        #self.label2= "BR("+slep+" #rightarrow #font[12]{l} "+lsp_s+") = 1"
        self.label= "pp #rightarrow "+sele+" "+sele+"/"+smuo+" "+smuo+", "+slep+"#rightarrow #font[12]{l} "+lsp_s
        self.label2= ""
        # scan range to plot
        self.Xmin = 100.
        self.Xmax = 1000. 
        self.Ymin = 0.
        #self.Ymax = 900.
        self.Ymax = 800.
        self.Zmin = 0.0001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{"+slep+"}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.boxOn = False
        
    def TChipmWW(self):
        # model name
        self.modelname = "TChipmWW"
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        charg = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{#pm}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        charp = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{+}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        charm = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{-}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        Wpm = "W#scale[0.85]{^{#pm}}"
        self.label= "pp #rightarrow "+charp+" "+charm+",  "+charg+" #rightarrow "+Wpm+" "+lsp_s;
        self.label2= "";
        # scan range to plot
        self.Xmin = 100.
        self.Xmax = 600.
        self.Ymin = 0.
        self.Ymax = 300.
        self.Zmin = 0.001
        self.Zmax = 100.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{"+charg+"}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.boxOn = False
       
    def T2bW(self):
        # model name
        self.modelname = "T2bW"
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        charg = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{#pm}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        Wpm = "W#scale[0.85]{^{#pm}}"
        self.label= "pp #rightarrow #tilde{t} #tilde{t}, #tilde{t} #rightarrow b "+ charg + " #rightarrow b "+Wpm+" "+lsp_s;
        self.label2= "#scale[0.8]{m_{"+charg+"} = (m_{#tilde{t}} + m_{"+lsp_s+"})/2}";
        # scan range to plot
        self.Xmin = 200.
        self.Xmax = 1000.
        self.Ymin = 0.
        self.Ymax = 800.
        self.Zmin = 0.001
        self.Zmax = 100.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{t}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.boxOn = False
 
    def T5tttt(self):
        # model name
        self.modelname = "T1tttt"
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow t #bar{t} "+lsp_s;
        self.label2= "";
        # scan range to plot
        self.Xmin = 600.
        self.Xmax = 2200.
        self.Ymin = 0.
        self.Ymax = 1900.
        self.Zmin = 0.001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{g}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.boxOn = False
        
    def T5ttttDM175(self):
        # model name
        self.modelname = "T5ttttDM175"
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{g} #tilde{g},  #tilde{g} #rightarrow #tilde{t}_{1} t,  #tilde{t}_{1} #rightarrow #bar{t} "+lsp_s;
        self.label2= "m_{#tilde{t}_{1}} - m_{#tilde{#chi}^{0}_{1}} = 175 GeV";
        # scan range to plot
        self.Xmin = 600.
        self.Xmax = 1700.
        self.Ymin = 0.
        self.Ymax = 1800.
        self.Zmin = 0.001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{g}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.boxOn = False
        
    def T1bbbb(self):
        # model name
        self.modelname = "T1bbbb"
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow b #bar{b} "+lsp_s;
        self.label2= "";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 600.
        self.Xmax = 2300.
        self.Ymin = 0.
        self.Ymax = 1900.
        self.Zmin = 0.001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{g}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.boxOn = False

    def T1qqqq(self):
        # model name
        self.modelname = "T1qqqq"
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow q #bar{q} #tilde{#chi}^{0}_{1}";
        self.label2= "";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 600.
        self.Xmax = 2200.
        self.Ymin = 0.
        self.Ymax = 1900.
        self.Zmin = 0.001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{g}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.boxOn = False

    def T5qqqqVV(self):
        # model name
        self.modelname = "T5qqqqVV"
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow q #bar{q} V #tilde{#chi}^{0}_{1}";
        self.label2= "";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 600.
        self.Xmax = 2200.
        self.Ymin = 0.
        self.Ymax = 1900.
        self.Zmin = 0.001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{g}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.boxOn = False
