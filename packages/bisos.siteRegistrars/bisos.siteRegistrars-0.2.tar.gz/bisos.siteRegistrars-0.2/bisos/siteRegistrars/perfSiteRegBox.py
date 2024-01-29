# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: =CS-Lib= A RO service for registration of Boxes at a site.
#+end_org """

####+BEGIN: b:py3:cs:file/dblockControls :classification "cs-u"
""" #+begin_org
* [[elisp:(org-cycle)][| /Control Parameters Of This File/ |]] :: dblk ctrls classifications=cs-u
#+BEGIN_SRC emacs-lisp
(setq-local b:dblockControls t) ; (setq-local b:dblockControls nil)
(put 'b:dblockControls 'py3:cs:Classification "cs-u") ; one of cs-mu, cs-u, cs-lib, bpf-lib, pyLibPure
#+END_SRC
#+RESULTS:
: cs-u
#+end_org """
####+END:

####+BEGIN: b:prog:file/proclamations :outLevel 1
""" #+begin_org
* *[[elisp:(org-cycle)][| Proclamations |]]* :: Libre-Halaal Software --- Part Of BISOS ---  Poly-COMEEGA Format.
** This is Libre-Halaal Software. © Neda Communications, Inc. Subject to AGPL.
** It is part of BISOS (ByStar Internet Services OS)
** Best read and edited  with Blee in Poly-COMEEGA (Polymode Colaborative Org-Mode Enhance Emacs Generalized Authorship)
#+end_org """
####+END:

####+BEGIN: b:prog:file/particulars :authors ("./inserts/authors-mb.org")
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: Authors, version
** This File: /bisos/git/bxRepos/bisos-pip/siteRegistrars/py3/bisos/siteRegistrars/csSiteRegBox.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGINNOT: b:py3:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing

from bisos import siteRegistrars
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['csSiteRegBox'], }
csInfo['version'] = '202401192758'
csInfo['status']  = 'inUse'
csInfo['panel'] = "[[../../panels/_nodeBase_/fullUsagePanel-en.org]]"
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/PyFwrk/bisos-pip/bisos.cs/_nodeBase_/fullUsagePanel-en.org][BISOS CmndSvcs Panel]]   [[elisp:(org-cycle)][| ]]
** TODO Document this module.
** TODO Add sectioning for Invoker and performer.
** Relevant Panels:
** Status: In use with BISOS
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO complete fileName in particulars.
#+end_org """

####+BEGIN: b:prog:file/orgTopControls :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Controls |]] :: [[elisp:(delete-other-windows)][(1)]] | [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]

#+end_org """
####+END:

####+BEGIN: b:py3:file/workbench :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Workbench |]] :: [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:orgItem/basic :type "=PyImports= " :title "*Py Library IMPORTS*" :comment "-- with classification based framework/imports"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =PyImports=  [[elisp:(outline-show-subtree+toggle)][||]] *Py Library IMPORTS* -- with classification based framework/imports  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:framework/imports :basedOn "classification"
""" #+begin_org
** Imports Based On Classification=cs-u
#+end_org """
from bisos import b
from bisos.b import cs
from bisos.b import b_io
from bisos.common import csParam

import collections
####+END:

from bisos.siteRegistrars import invSiteRegBox

import pwd
import pathlib

####+BEGIN: b:py3:cs:orgItem/section :title "Common Parameters Specification" :comment "based on cs.param.CmndParamDict -- As expected from CSU-s"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *Common Parameters Specification* based on cs.param.CmndParamDict -- As expected from CSU-s  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:func/typing :funcName "commonParamsSpecify" :comment "~CSU Specification~" :funcType "ParSpc" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-ParSpc [[elisp:(outline-show-subtree+toggle)][||]] /commonParamsSpecify/  ~CSU Specification~  [[elisp:(org-cycle)][| ]]
#+end_org """
def commonParamsSpecify(
####+END:
        csParams: cs.param.CmndParamDict,
) -> None:
    pass

####+BEGIN: b:py3:cs:orgItem/section :title "CSU-Lib Executions" :comment "-- cs.invOutcomeReportControl"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *CSU-Lib Executions* -- cs.invOutcomeReportControl  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

# NOTYET, Perhaps duplicate

# G = cs.globalContext.get()
# icmRunArgs = G.icmRunArgsGet()

perfName = "siteRegistrar"
roSiteRegistrarSapPath = cs.ro.SapBase_FPs.perfNameToRoSapPath(perfName)  # static method

cs.invOutcomeReportControl(cmnd=True, ro=True)

####+BEGIN: b:py3:cs:orgItem/section :title "CSU-Lib Examples" :comment "-- Providing examples_csu"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *CSU-Lib Examples* -- Providing examples_csu  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:func/typing :funcName "examples_csu" :comment "~CSU Specification~" :funcType "eType" :retType "" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-eType  [[elisp:(outline-show-subtree+toggle)][||]] /examples_csu/  ~CSU Specification~ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def examples_csu(
####+END:
        sectionTitle: typing.AnyStr = '',
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr* |]] Examples of Service Access Instance Commands.
    #+end_org """

    # def cpsInit(): return collections.OrderedDict()
    # def menuItem(verbosity): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'

    cmndOutcome = b.op.Outcome()

    if (thisUniqBoxId := invSiteRegBox.thisBoxUUID().cmnd(
            rtInv=cs.RtInvoker.new_py(), cmndOutcome=b.op.Outcome(),
    ).results) == None: return(b_io.eh.badOutcome(cmndOutcome))

    if (thisBoxPath := perf_boxFind().cmnd(
            rtInv=cs.RtInvoker.new_py(), cmndOutcome=b.op.Outcome(),
            uniqBoxId=thisUniqBoxId,
    ).results) == None: return(b_io.eh.badOutcome(cmndOutcome))

    thisBoxNu = thisBoxPath.name
    thisBoxName = f"box{thisBoxNu}"

    perfName = "localhost"

    if sectionTitle == 'default':
        cs.examples.menuChapter('*Performer Only Commands*')

    cmndName = "perf_siteBoxesBaseObtain" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "perf_boxCreate" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ; cps['boxNu'] = thisBoxNu ; cps['uniqBoxId'] = thisUniqBoxId
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "perf_boxRead" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ; cps['boxNu'] = thisBoxNu
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "perf_boxUpdate" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ; cps['boxNu'] = thisBoxNu ; cps['boxName'] = thisBoxName
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "perf_boxDelete" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ; cps['boxNu'] = thisBoxNu
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "perf_boxFind" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['uniqBoxId'] = thisUniqBoxId
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "perf_boxesList" ; cmndArgs = "" ;
    cps = collections.OrderedDict()
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "perf_boxNuGetNext" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "perf_boxesRepoPush" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "perf_boxesRepoPull" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "perf_lock" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "perf_unlock" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    if sectionTitle == 'default': cs.examples.menuChapter('*RO Svc Commands*')

    cmndName = "ro_boxAdd" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ; cps['perfName'] = perfName ; cps['uniqBoxId'] = thisUniqBoxId
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "ro_boxRead" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ; cps['perfName'] = perfName ; cps['boxNu'] = thisBoxNu
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "ro_boxUpdate" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ; cps['perfName'] = perfName ; cps['boxNu'] = thisBoxNu ; cps['uniqBoxId'] = thisUniqBoxId
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "ro_boxDelete" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ; cps['perfName'] = perfName ; cps['boxNu'] = thisBoxNu
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "ro_boxFind" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ; cps['perfName'] = perfName ; cps['boxName'] = thisBoxName
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "ro_boxFind" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ; cps['perfName'] = perfName ; cps['uniqBoxId'] = thisUniqBoxId
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "ro_boxesList" ; cmndArgs = "" ;
    cps = collections.OrderedDict()
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    if sectionTitle == 'default':
        cs.examples.menuChapter('*roPy_ and roPerf_ examples*')

    cmndName = "roPy_givenUniqBoxIdFindBoxNuExample" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['uniqBoxId'] = thisUniqBoxId
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "roPerf_givenUniqBoxIdFindBoxNuExample" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['uniqBoxId'] = thisUniqBoxId
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    if sectionTitle == 'default':
        cs.examples.menuChapter('*Place Holders*')

    cmndName = "roPyExInvoker" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ; # cps['icmsPkgName'] = icmsPkgName
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='full')

    cmndName = "roPyExPerformer" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ; # cps['icmsPkgName'] = icmsPkgName
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')



####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Support Functions" :anchor ""  :extraInfo "Command Services Section"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Support Functions_: |]]  Command Services Section  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: b:py3:cs:func/typing :funcName "boxFpNamesList" :comment "~Name of Box File Params~"  :funcType "eType" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-eType  [[elisp:(outline-show-subtree+toggle)][||]] /boxFpNamesList/  ~Name of Box File Params~ deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def boxFpNamesList(
####+END:
) -> list:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    return invSiteRegBox.boxFpNamesList()
    #return [ 'boxNu', 'boxId',  'uniqueBoxId',  ]


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Performer Only CmndSvcs" :anchor ""  :extraInfo "Command Services Section"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Performer Only CmndSvcs_: |]]  Command Services Section  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "perf_siteBoxesBaseObtain" :comment "" :extent "verify" :ro "noCli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<perf_siteBoxesBaseObtain>>  =verify= ro=noCli   [[elisp:(org-cycle)][| ]]
#+end_org """
class perf_siteBoxesBaseObtain(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo() # NO RO From CLI

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Outcome: Boxes base directory. NOTYET, should become configurable
        #+end_org """): return(cmndOutcome)

        self.captureRunStr(""" #+begin_org
#+begin_src sh :results output :session shared
  csSiteRegBox.cs -i perf_siteBoxesBaseObtain
#+end_src
#+RESULTS:
:
: /bxo/r3/iso/pmb_clusterNeda-boxes/boxes
        #+end_org """)

        self.captureRunStr(""" #+begin_org
#+begin_src sh :results output :session shared
  csInvSiteRegBox.cs -i perf_siteBoxesBaseObtain
#+end_src
#+RESULTS:
:
: bash: csInvSiteRegBox.cs: command not found
        #+end_org """)

        if self.justCaptureP(): return cmndOutcome

        perfName = invSiteRegBox.perfNameGet()

        if perfName == 'siteRegistrar':
            siteBoxesBase = pathlib.Path("/bxo/r3/iso/pmb_clusterNeda-boxes/boxes") # Result

        elif perfName == 'exampleRegistrar':
            roSapPath = cs.ro.SapBase_FPs.perfNameToRoSapPath(perfName)  # static method
            sapBaseFps = b.pattern.sameInstance(cs.ro.SapBase_FPs, roSapPath=roSapPath)
            rosmuControl = sapBaseFps.fps_getParam('rosmuControl')
            siteBoxesBase = pathlib.Path(rosmuControl.parValueGet())

        else:
            siteBoxesBase = pathlib.Path("Problem")

        return cmndOutcome.set(opResults=siteBoxesBase,)



####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "perf_boxCreate" :comment "" :extent "verify" :ro "noCli" :parsMand "boxNu uniqBoxId" :parsOpt "boxName" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<perf_boxCreate>>  =verify= parsMand=boxNu uniqBoxId parsOpt=boxName ro=noCli   [[elisp:(org-cycle)][| ]]
#+end_org """
class perf_boxCreate(cs.Cmnd):
    cmndParamsMandatory = [ 'boxNu', 'uniqBoxId', ]
    cmndParamsOptional = [ 'boxName', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo() # NO RO From CLI

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             boxNu: typing.Optional[str]=None,  # Cs Mandatory Param
             uniqBoxId: typing.Optional[str]=None,  # Cs Mandatory Param
             boxName: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:

        callParamsDict = {'boxNu': boxNu, 'uniqBoxId': uniqBoxId, 'boxName': boxName, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
        boxNu = csParam.mappedValue('boxNu', boxNu)
        uniqBoxId = csParam.mappedValue('uniqBoxId', uniqBoxId)
        boxName = csParam.mappedValue('boxName', boxName)
####+END:
        if self.cmndDocStr(""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  A starting point command.
        #+end_org """): return(cmndOutcome)

        if (siteBoxesBase := perf_siteBoxesBaseObtain().cmnd(
                rtInv=cs.RtInvoker.new_py(), cmndOutcome=cmndOutcome,
        ).results) == None : return(b_io.eh.badOutcome(cmndOutcome))

        newBoxBase = siteBoxesBase.joinpath(boxNu)

        try:
            newBoxBase.mkdir(exist_ok=False)
        except FileExistsError:
            return(b_io.eh.badOutcome(cmndOutcome))

        if not boxName:
            boxName = f"box{boxNu}"

        b.fp.FileParamWriteTo(parRoot=newBoxBase,
                              parName='boxNu',
                              parValue=boxNu,
        )
        b.fp.FileParamWriteTo(parRoot=newBoxBase,
                              parName='uniqueBoxId',
                              parValue=uniqBoxId,
        )
        b.fp.FileParamWriteTo(parRoot=newBoxBase,
                              parName='boxId',
                              parValue=boxName,
        )

        return cmndOutcome.set(opResults=boxNu,)

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "perf_boxRead" :comment "" :extent "verify" :ro "noCli" :parsMand "boxNu" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<perf_boxRead>>  =verify= parsMand=boxNu ro=noCli   [[elisp:(org-cycle)][| ]]
#+end_org """
class perf_boxRead(cs.Cmnd):
    cmndParamsMandatory = [ 'boxNu', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo() # NO RO From CLI

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             boxNu: typing.Optional[str]=None,  # Cs Mandatory Param
    ) -> b.op.Outcome:

        callParamsDict = {'boxNu': boxNu, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
        boxNu = csParam.mappedValue('boxNu', boxNu)
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Given boxNu, uniqBoxId and optionally boxName, update the info if missing. Report if inconsistent.
        #+end_org """): return(cmndOutcome)

        self.captureRunStr(""" #+begin_org
#+begin_src sh :results output :session shared
  csSiteRegBox.cs --boxNu=1002 -i perf_boxRead
#+end_src
#+RESULTS:
:
: ['1002', '4c4c4544-0051-3210-804e-b5c04f334b31', 'box1002']
        #+end_org """)
        if self.justCaptureP(): return cmndOutcome


        boxInfo: typing.Optional[list] = None

        if (siteBoxesBase := perf_siteBoxesBaseObtain().cmnd(
                rtInv=cs.RtInvoker.new_py(), cmndOutcome=cmndOutcome,
        ).results) == None : return(b_io.eh.badOutcome(cmndOutcome))

        boxNuBaseDir = siteBoxesBase.joinpath(boxNu)

        boxFpsDict = b.fp.parsGetAsDictValue(boxFpNamesList(), boxNuBaseDir,)

        stored_boxNu = boxFpsDict['boxNu']
        stored_uniqBoxId = boxFpsDict['uniqueBoxId']
        stored_boxName = boxFpsDict['boxId']

        boxInfo = [stored_boxNu, stored_uniqBoxId, stored_boxName]

        #cs.invOutcomeReportControl(cmnd=False, ro=True)
        return cmndOutcome.set(opResults=boxInfo,)

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "perf_boxUpdate" :comment "" :extent "verify" :ro "noCli" :parsMand "boxNu" :parsOpt "boxName uniqBoxId" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<perf_boxUpdate>>  =verify= parsMand=boxNu parsOpt=boxName uniqBoxId ro=noCli   [[elisp:(org-cycle)][| ]]
#+end_org """
class perf_boxUpdate(cs.Cmnd):
    cmndParamsMandatory = [ 'boxNu', ]
    cmndParamsOptional = [ 'boxName', 'uniqBoxId', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo() # NO RO From CLI

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             boxNu: typing.Optional[str]=None,  # Cs Mandatory Param
             boxName: typing.Optional[str]=None,  # Cs Optional Param
             uniqBoxId: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:

        callParamsDict = {'boxNu': boxNu, 'boxName': boxName, 'uniqBoxId': uniqBoxId, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
        boxNu = csParam.mappedValue('boxNu', boxNu)
        boxName = csParam.mappedValue('boxName', boxName)
        uniqBoxId = csParam.mappedValue('uniqBoxId', uniqBoxId)
####+END:
        if self.cmndDocStr(""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  A starting point command.
        #+end_org """): return(cmndOutcome)

        result: b.op.OpError = b.op.OpError.Success

        if (siteBoxesBase := perf_siteBoxesBaseObtain().cmnd(
                rtInv=cs.RtInvoker.new_py(), cmndOutcome=cmndOutcome,
        ).results) == None : return(b_io.eh.badOutcome(cmndOutcome))

        boxNuBaseDir = siteBoxesBase.joinpath(boxNu)

        if not boxNuBaseDir.exists():
            return(b_io.eh.badOutcome(cmndOutcome))

        boxFpsDict = b.fp.parsGetAsDictValue(boxFpNamesList(), boxNuBaseDir,)

        stored_boxNu = boxFpsDict['boxNu']
        stored_uniqBoxId = boxFpsDict['uniqueBoxId']
        stored_boxName = boxFpsDict['boxId']

        if stored_boxNu != boxNu:
            return(b_io.eh.badOutcome(cmndOutcome.set(
                    opStderr=f"boxNu {boxNu} != stored_boxNu {stored_boxNu}",
                    opResults=b.op.OpError.Failure,
            )))

        if boxName:
            if stored_boxName == boxName:
                        b_io.pr(f"boxName is as stored, update skipped")
            else:
                b.fp.FileParamWriteTo(parRoot=boxNuBaseDir,
                                      parName='boxId',
                                      parValue=boxName,
                                      )
        if uniqBoxId:
            if stored_uniqBoxId == uniqBoxId:
                    b_io.pr(f"uniqBoxId is as stored, update skipped")
            else:
                b.fp.FileParamWriteTo(parRoot=boxNuBaseDir,
                                      parName='uniqueBoxId',
                                      parValue=uniqBoxId,
                                      )

        return cmndOutcome.set(opResults=result,)

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "perf_boxDelete" :comment "" :extent "verify" :ro "noCli" :parsMand "boxNu" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<perf_boxDelete>>  =verify= parsMand=boxNu ro=noCli   [[elisp:(org-cycle)][| ]]
#+end_org """
class perf_boxDelete(cs.Cmnd):
    cmndParamsMandatory = [ 'boxNu', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo() # NO RO From CLI

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             boxNu: typing.Optional[str]=None,  # Cs Mandatory Param
    ) -> b.op.Outcome:

        callParamsDict = {'boxNu': boxNu, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
        boxNu = csParam.mappedValue('boxNu', boxNu)
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Given boxNu, uniqBoxId and optionally boxName, update the info if missing. Report if inconsistent.
        #+end_org """): return(cmndOutcome)

        return cmndOutcome.set(opResults="NOTYET",)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "perf_boxFind" :comment "" :extent "verify" :ro "noCli" :parsMand "" :parsOpt "uniqBoxId boxName" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<perf_boxFind>>  =verify= parsOpt=uniqBoxId boxName ro=noCli   [[elisp:(org-cycle)][| ]]
#+end_org """
class perf_boxFind(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'uniqBoxId', 'boxName', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo() # NO RO From CLI

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             uniqBoxId: typing.Optional[str]=None,  # Cs Optional Param
             boxName: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:

        callParamsDict = {'uniqBoxId': uniqBoxId, 'boxName': boxName, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
        uniqBoxId = csParam.mappedValue('uniqBoxId', uniqBoxId)
        boxName = csParam.mappedValue('boxName', boxName)
####+END:
        if self.cmndDocStr(""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  result: boxBaseDir corresponding to uniqBoxId
        #+end_org """): return(cmndOutcome)

        self.captureRunStr(""" #+begin_org
#+begin_src sh :results output :session shared
  csSiteRegBox.cs --boxName="box1003" -i perf_boxFind
#+end_src
#+RESULTS:
:
: Cmnd -- No Results
        #+end_org """)

        if self.justCaptureP(): return cmndOutcome

        boxBaseDir: typing.Optional[pathlib.Path] = None

        if (siteBoxesBase := perf_siteBoxesBaseObtain().cmnd(
                rtInv=cs.RtInvoker.new_py(), cmndOutcome=cmndOutcome,
        ).results) == None : return(b_io.eh.badOutcome(cmndOutcome))

        parNamesList = boxFpNamesList()

        if uniqBoxId:
            for each in siteBoxesBase.iterdir():
                if each.name.isnumeric():
                    boxFpsDict = b.fp.parsGetAsDictValue(parNamesList, each,)
                    stored_uniqBoxId = boxFpsDict['uniqueBoxId']
                    if stored_uniqBoxId == uniqBoxId:
                        boxBaseDir = each
                        break

        elif boxName:
            for each in siteBoxesBase.iterdir():
                if each.name.isnumeric():
                    boxFpsDict = b.fp.parsGetAsDictValue(parNamesList, each,)
                    stored_boxName = boxFpsDict['boxId']
                    if stored_boxName == boxName:
                        boxBaseDir = each
                        break
        else:
            return(b_io.eh.badOutcome(cmndOutcome.set(opResults=boxBaseDir,)))

        return cmndOutcome.set(opResults=boxBaseDir,)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "perf_boxesList" :comment "" :extent "verify" :ro "noCli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<perf_boxesList>>  =verify= ro=noCli   [[elisp:(org-cycle)][| ]]
#+end_org """
class perf_boxesList(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo() # NO RO From CLI

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:
        if self.cmndDocStr(""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  result: List of all boxes
        #+end_org """): return(cmndOutcome)

        self.captureRunStr(""" #+begin_org
#+begin_src sh :results output :session shared
  csSiteRegBox.cs -i perf_boxesList
#+end_src
#+RESULTS:
:
:
        #+end_org """)
        if self.justCaptureP(): return cmndOutcome

        boxesList: typing.Optional[list] = []

        if (siteBoxesBase := perf_siteBoxesBaseObtain().cmnd(
                rtInv=cs.RtInvoker.new_py(), cmndOutcome=cmndOutcome,
        ).results) == None : return(b_io.eh.badOutcome(cmndOutcome))

        parNamesList = boxFpNamesList()

        relevantPaths = []
        for each in siteBoxesBase.iterdir():
            if each.name.isnumeric():
                relevantPaths.append(each)

        relevantPaths = sorted(relevantPaths)

        for each in relevantPaths:
            if (eachBox := perf_boxRead().cmnd(
                    rtInv=cs.RtInvoker.new_py(),
                    cmndOutcome=cmndOutcome,
                    boxNu=each,
            ).results) is None : return(b_io.eh.badOutcome(cmndOutcome))
            boxesList.append(eachBox)

        return cmndOutcome.set(opResults=boxesList,)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "perf_boxNuGetNext" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<perf_boxNuGetNext>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class perf_boxNuGetNext(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:
        if self.cmndDocStr(""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Outcome: Last existing boxNu + 1. Starts at 1000.
        #+end_org """): return(cmndOutcome)

        lastBoxNu: int = 1000

        if (siteBoxesBase := perf_siteBoxesBaseObtain().cmnd(
                rtInv=cs.RtInvoker.new_py(), cmndOutcome=cmndOutcome,
        ).results) == None : return(b_io.eh.badOutcome(cmndOutcome))

        relevantPaths = []
        for each in siteBoxesBase.iterdir():
            if each.name.isnumeric():
                relevantPaths.append(each)

        relevantPaths = sorted(relevantPaths)

        if relevantPaths:
            lastBoxNu = int(str(relevantPaths[-1].name))

        nextBoxNu = lastBoxNu + 1

        return cmndOutcome.set(opResults=nextBoxNu,)

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "perf_boxesRepoPull" :comment "" :extent "verify" :ro "noCli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<perf_boxesRepoPull>>  =verify= ro=noCli   [[elisp:(org-cycle)][| ]]
#+end_org """
class perf_boxesRepoPull(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo() # NO RO From CLI

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Runs: echo siteBoxesBase | bx-gitRepos -i gitRemPull
        #+end_org """): return(cmndOutcome)

        result: b.op.OpError = b.op.OpError.Success

        if (siteBoxesBase := perf_siteBoxesBaseObtain().cmnd(
                rtInv=cs.RtInvoker.new_py(), cmndOutcome=cmndOutcome,
        ).results) == None : return(b_io.eh.badOutcome(cmndOutcome))

        if b.subProc.WOpW(invedBy=self, log=1).bash(
                f"""echo {siteBoxesBase} | bx-gitRepos -i gitRemPull""",
        ).isProblematic():  return(b_io.eh.badOutcome(cmndOutcome))

        cs.invOutcomeReportControl(cmnd=False, ro=True)
        return cmndOutcome.set(opResults=result,)

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "perf_boxesRepoPush" :comment "" :extent "verify" :ro "noCli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<perf_boxesRepoPush>>  =verify= ro=noCli   [[elisp:(org-cycle)][| ]]
#+end_org """
class perf_boxesRepoPush(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo() # NO RO From CLI

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Runs: echo siteBoxesBase | bx-gitRepos -i  addCommitPush all
        #+end_org """): return(cmndOutcome)

        result: b.op.OpError = b.op.OpError.Success

        if (siteBoxesBase := perf_siteBoxesBaseObtain().cmnd(
                rtInv=cs.RtInvoker.new_py(), cmndOutcome=cmndOutcome,
        ).results) == None : return(b_io.eh.badOutcome(cmndOutcome))

        if b.subProc.WOpW(invedBy=self, log=1).bash(
                f"""echo {siteBoxesBase} | bx-gitRepos -i  addCommitPush all""",
        ).isProblematic():  return(b_io.eh.badOutcome(cmndOutcome))

        return cmndOutcome.set(opResults=result,)

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "perf_boxCreateAndPush" :comment "" :extent "verify" :ro "noCli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<perf_boxCreateAndPush>>  =verify= ro=noCli   [[elisp:(org-cycle)][| ]]
#+end_org """
class perf_boxCreateAndPush(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo() # NO RO From CLI

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Add the box and push.
        #+end_org """): return(cmndOutcome)

        result: b.op.OpError = b.op.OpError.Success

        if (siteBoxesBase := perf_boxesAdd().cmnd(
                rtInv=cs.RtInvoker.new_py(), cmndOutcome=cmndOutcome,
        ).results) == None : return(b_io.eh.badOutcome(cmndOutcome))

        if (siteBoxesBase := perf_boxesRepoPull().cmnd(
                rtInv=cs.RtInvoker.new_py(), cmndOutcome=cmndOutcome,
        ).results) == None : return(b_io.eh.badOutcome(cmndOutcome))

        return cmndOutcome.set(opResults=result,)

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "perf_lock" :comment "" :extent "verify" :ro "noCli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<perf_lock>>  =verify= ro=noCli   [[elisp:(org-cycle)][| ]]
#+end_org """
class perf_lock(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo() # NO RO From CLI

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] NOTYET, Lock a write transaction using https://docs.gitlab.com/ee/user/project/file_lock.html
        #+end_org """): return(cmndOutcome)

        result: b.op.OpError = b.op.OpError.Success

        return cmndOutcome.set(opResults=result,)

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "perf_unlock" :comment "" :extent "verify" :ro "noCli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<perf_unlock>>  =verify= ro=noCli   [[elisp:(org-cycle)][| ]]
#+end_org """
class perf_unlock(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo() # NO RO From CLI

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] NOTYET, Unlock a write transaction using https://docs.gitlab.com/ee/user/project/file_lock.html
        #+end_org """): return(cmndOutcome)

        result: b.op.OpError = b.op.OpError.Success

        return cmndOutcome.set(opResults=result,)


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "RO Service Commands" :anchor ""  :extraInfo "Command Services Section"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _RO Service Commands_: |]]  Command Services Section  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "ro_boxAdd" :comment "" :extent "verify" :ro "cli" :parsMand "uniqBoxId" :parsOpt "boxName" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<ro_boxAdd>>  =verify= parsMand=uniqBoxId parsOpt=boxName ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class ro_boxAdd(cs.Cmnd):
    cmndParamsMandatory = [ 'uniqBoxId', ]
    cmndParamsOptional = [ 'boxName', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             uniqBoxId: typing.Optional[str]=None,  # Cs Mandatory Param
             boxName: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:

        callParamsDict = {'uniqBoxId': uniqBoxId, 'boxName': boxName, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
        uniqBoxId = csParam.mappedValue('uniqBoxId', uniqBoxId)
        boxName = csParam.mappedValue('boxName', boxName)
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Returns a boxNu
        #+end_org """): return(cmndOutcome)

        assignedBoxNu: str = ""
        cmndOutcome.set(opResults=assignedBoxNu,)

        if (siteBoxesBase := perf_siteBoxesBaseObtain().cmnd(
                rtInv=cs.RtInvoker.new_py(), cmndOutcome=cmndOutcome,
        ).results) == None : return(b_io.eh.badOutcome(cmndOutcome))

        boxNuBaseDir = perf_boxFind().cmnd(
                rtInv=cs.RtInvoker.new_py(),
                cmndOutcome=cmndOutcome,
                uniqBoxId=uniqBoxId,
        ).results

        if boxNuBaseDir != None:
            print(boxNuBaseDir)
            return(b_io.eh.badOutcome(cmndOutcome)) # add stderrinfo NOTYET

        if (assignedBoxNu := perf_boxNuGetNext().cmnd(
                rtInv=cs.RtInvoker.new_py(), cmndOutcome=cmndOutcome,
        ).results) is None : return(b_io.eh.badOutcome(cmndOutcome))

        if (boxNu := perf_boxCreate().cmnd(
                rtInv=cs.RtInvoker.new_py(),
                cmndOutcome=cmndOutcome,
                boxNu=str(assignedBoxNu),
                uniqBoxId=uniqBoxId,
                boxName=boxName,
        ).results) is None : return(b_io.eh.badOutcome(cmndOutcome))

        return cmndOutcome.set(opResults=assignedBoxNu,)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "ro_boxRead" :comment "" :extent "verify" :ro "cli" :parsMand "boxNu" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<ro_boxRead>>  =verify= parsMand=boxNu ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class ro_boxRead(cs.Cmnd):
    cmndParamsMandatory = [ 'boxNu', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             boxNu: typing.Optional[str]=None,  # Cs Mandatory Param
    ) -> b.op.Outcome:

        callParamsDict = {'boxNu': boxNu, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
        boxNu = csParam.mappedValue('boxNu', boxNu)
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  A starting point command.
        #+end_org """): return(cmndOutcome)

        return(
            perf_boxRead().cmnd(
                rtInv=cs.RtInvoker.new_py(),
                cmndOutcome=cmndOutcome,
                boxNu=boxNu,
            )
        )


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "ro_boxUpdate" :comment "" :extent "verify" :ro "cli" :parsMand "boxNu" :parsOpt "uniqBoxId boxName" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<ro_boxUpdate>>  =verify= parsMand=boxNu parsOpt=uniqBoxId boxName ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class ro_boxUpdate(cs.Cmnd):
    cmndParamsMandatory = [ 'boxNu', ]
    cmndParamsOptional = [ 'uniqBoxId', 'boxName', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             boxNu: typing.Optional[str]=None,  # Cs Mandatory Param
             uniqBoxId: typing.Optional[str]=None,  # Cs Optional Param
             boxName: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:

        callParamsDict = {'boxNu': boxNu, 'uniqBoxId': uniqBoxId, 'boxName': boxName, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
        boxNu = csParam.mappedValue('boxNu', boxNu)
        uniqBoxId = csParam.mappedValue('uniqBoxId', uniqBoxId)
        boxName = csParam.mappedValue('boxName', boxName)
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  A starting point command.
        #+end_org """): return(cmndOutcome)

        return(
            perf_boxUpdate().cmnd(
                rtInv=cs.RtInvoker.new_py(),
                cmndOutcome=cmndOutcome,
                boxNu=boxNu,
                uniqBoxId=uniqBoxId,
                boxName=boxName,
            )
        )

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "ro_boxDelete" :comment "" :extent "verify" :ro "cli" :parsMand "boxNu" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<ro_boxDelete>>  =verify= parsMand=boxNu ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class ro_boxDelete(cs.Cmnd):
    cmndParamsMandatory = [ 'boxNu', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             boxNu: typing.Optional[str]=None,  # Cs Mandatory Param
    ) -> b.op.Outcome:

        callParamsDict = {'boxNu': boxNu, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
        boxNu = csParam.mappedValue('boxNu', boxNu)
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  A starting point command.
        #+end_org """): return(cmndOutcome)

        return(
            perf_boxDelete().cmnd(
                rtInv=cs.RtInvoker.new_py(),
                cmndOutcome=cmndOutcome,
                boxNu=boxNu,
            )
        )

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "ro_boxFind" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "boxName uniqBoxId" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<ro_boxFind>>  =verify= parsOpt=boxName uniqBoxId ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class ro_boxFind(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'boxName', 'uniqBoxId', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             boxName: typing.Optional[str]=None,  # Cs Optional Param
             uniqBoxId: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:

        callParamsDict = {'boxName': boxName, 'uniqBoxId': uniqBoxId, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
        boxName = csParam.mappedValue('boxName', boxName)
        uniqBoxId = csParam.mappedValue('uniqBoxId', uniqBoxId)
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  A starting point command.
        #+end_org """): return(cmndOutcome)

        return(
            perf_boxFind().cmnd(
                rtInv=cs.RtInvoker.new_py(),
                cmndOutcome=cmndOutcome,
                uniqBoxId=uniqBoxId,
                boxName=boxName,
            )
        )


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "ro_boxesList" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<ro_boxesList>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class ro_boxesList(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  A starting point command.
        #+end_org """): return(cmndOutcome)

        return(
            perf_boxesList().cmnd(
                rtInv=cs.RtInvoker.new_py(),
                cmndOutcome=cmndOutcome,
            )
        )


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Examples" :anchor ""  :extraInfo "Command Services Section Examples"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Examples_: |]]  Command Services Section Examples  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "roPy_givenUniqBoxIdFindBoxNuExample" :ro "py"  :extent "verify" :comment "" :parsMand "uniqBoxId" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<roPy_givenUniqBoxIdFindBoxNuExample>>  =verify= parsMand=uniqBoxId ro=py   [[elisp:(org-cycle)][| ]]
#+end_org """
class roPy_givenUniqBoxIdFindBoxNuExample(cs.Cmnd):
    cmndParamsMandatory = [ 'uniqBoxId', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo() # NO RO From CLI

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             uniqBoxId: typing.Optional[str]=None,  # Cs Mandatory Param
             roSapPath: typing.Optional[str]=None,  # RO pyInv Sap Path
    ) -> b.op.Outcome:

        callParamsDict = {'uniqBoxId': uniqBoxId, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
        # Remotely invoke this same command and return cmndOutcome
        uniqBoxId = csParam.mappedValue('uniqBoxId', uniqBoxId)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Example of using built-in features of an CMND in an ICM.
        #+end_org """)

        # roPath
        roSapPath = "/bisos/var/cs/ro/sap/csExamples.cs/localhost/rpyc/default"

        roPerf_givenUniqBoxIdFindBoxNu().cmnd(
            rtInv=rtInv,
            cmndOutcome=cmndOutcome,
            roSapPath=roSapPath,
            uniqBoxId=uniqBoxId
        )

        b_io.pr(f"{self.__class__.__name__} RESULT= {cmndOutcome.results}")


        return(cmndOutcome)


# VALUABLE CODE HERE

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "roPerf_givenUniqBoxIdFindBoxNuExample" :ro "py"  :extent "verify" :comment "" :parsMand "uniqBoxId" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<roPerf_givenUniqBoxIdFindBoxNuExample>>  =verify= parsMand=uniqBoxId ro=py   [[elisp:(org-cycle)][| ]]
#+end_org """
class roPerf_givenUniqBoxIdFindBoxNuExample(cs.Cmnd):
    cmndParamsMandatory = [ 'uniqBoxId', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo() # NO RO From CLI

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             uniqBoxId: typing.Optional[str]=None,  # Cs Mandatory Param
             roSapPath: typing.Optional[str]=None,  # RO pyInv Sap Path
    ) -> b.op.Outcome:

        callParamsDict = {'uniqBoxId': uniqBoxId, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
        # Remotely invoke this same command and return cmndOutcome
        uniqBoxId = csParam.mappedValue('uniqBoxId', uniqBoxId)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  RO Performer: Given uniqBoxId, outcome box info.
        #+end_org """)

        # Invoker runs this and returns outcome.
        if roSapPath:
            sapBaseFps = b.pattern.sameInstance(cs.ro.SapBase_FPs, roSapPath=roSapPath)
            portNu = sapBaseFps.fps_getParam('perfPortNu')
            ipAddr = sapBaseFps.fps_getParam('perfIpAddr')
            cmndKwArgs = self.cmndCallTimeKwArgs()
            cmndKwArgs.update({'rtInv': rtInv})
            cmndKwArgs.update({'cmndOutcome': cmndOutcome})
            print(f"PyRO at {roSapPath} with {cmndKwArgs}")
            rpycInvResult = cs.rpyc.csInvoke(
                ipAddr.parValueGet(),
                portNu.parValueGet(),
                self.__class__,
                **cmndKwArgs,
            )
            return rpycInvResult

        if (boxNuBase := perf_givenUniqBoxIdFindBoxNuBase().cmnd(
                rtInv=cs.RtInvoker.new_py(), cmndOutcome=cmndOutcome,
                uniqBoxId=uniqBoxId,
        ).results) == None : return(b_io.eh.badOutcome(cmndOutcome))

        boxNu = boxNuBase.name

        # NOTYET, also boxName

        cmndOutcome.set(
            #opError=b.op.OpError.Success,
            opError=None,
            opResults=(f"{self.__class__.__name__} {boxNu}"),
        )

        b_io.pr(f"{self.__class__.__name__} Returning: {cmndOutcome.error} {cmndOutcome.results}")

        return cmndOutcome




####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "parsArgsStdinCmndResultDEFUNCT" :extent "verify" :comment "stdin as input" :parsMand "par1Example" :parsOpt "par2Example" :argsMin 1 :argsMax 9999 :pyInv "methodInvokeArg"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<parsArgsStdinCmndResultDEFUNCT>>  *stdin as input*  =verify= parsMand=par1Example parsOpt=par2Example argsMin=1 argsMax=9999 ro=cli pyInv=methodInvokeArg   [[elisp:(org-cycle)][| ]]
#+end_org """
class parsArgsStdinCmndResultDEFUNCT(cs.Cmnd):
    cmndParamsMandatory = [ 'par1Example', ]
    cmndParamsOptional = [ 'par2Example', ]
    cmndArgsLen = {'Min': 1, 'Max': 9999,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             par1Example: typing.Optional[str]=None,  # Cs Mandatory Param
             par2Example: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
             methodInvokeArg: typing.Any=None,   # pyInv Argument
    ) -> b.op.Outcome:
        """stdin as input"""
        callParamsDict = {'par1Example': par1Example, 'par2Example': par2Example, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        par1Example = csParam.mappedValue('par1Example', par1Example)
        par2Example = csParam.mappedValue('par2Example', par2Example)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] This is an example of a CmndSvc with lots of features.
The features include:

        1) An optional parameter called someParam
        2) A first mandatory argument called action which must be one of list or print.
        3) An optional set of additional argumets.

The param, and args are then validated and form a single string.
That string is then echoed in a sub-prococessed. The stdout of that sub-proc is assigned
to a variable similar to bash back-quoting.

And that variable is then printed.

Variations of this are captured as snippets to be used.
        #+end_org """)

        self.captureRunStr(""" #+begin_org
#+begin_src sh :results output :session shared
  csExamples.cs --par1Example="par1Mantory" --par2Example="par2Optional" -i parsArgsStdinCmndResult arg1 argTwo
#+end_src
#+RESULTS:
:
: cmndArgs= arg1  argTwo
: stdin instead of methodInvokeArg =
: cmndParams= par1Mantory par2Optional
: OpError.Success
        #+end_org """)

        if self.justCaptureP(): return cmndOutcome


        action = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)
        actionArgs = self.cmndArgsGet("1&9999", cmndArgsSpecDict, argsList)

        actionArgsStr = ""
        for each in actionArgs:
            actionArgsStr = actionArgsStr + " " + each

        actionAndArgs = f"""{action} {actionArgsStr}"""


        b.comment.orgMode(""" #+begin_org
*****  [[elisp:(org-cycle)][| *Note:* | ]] Next we take in stdin, when interactive.
After that, we print the results and then provide a result in =cmndOutcome=.
        #+end_org """)

        if not methodInvokeArg:
            methodInvokeArg = b_io.stdin.read()

        print(f"cmndArgs= {actionAndArgs}")
        print(f"stdin instead of methodInvokeArg = {methodInvokeArg}")
        print(f"cmndParams= {par1Example} {par2Example}")

        return cmndOutcome.set(
            opError=b.op.OpError.Success,
            opResults="cmnd results come here",
        )

####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """  #+begin_org
*** [[elisp:(org-cycle)][| *cmndArgsSpec:* | ]] First arg defines rest
        #+end_org """

        cmndArgsSpecDict = cs.arg.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="action",
            argChoices=['echo', 'encrypt', 'ls', 'date'],
            argDescription="Action to be specified by rest"
        )
        cmndArgsSpecDict.argsDictAdd(
            argPosition="1&9999",
            argName="actionArgs",
            argChoices=[],
            argDescription="Rest of args for use by action"
        )

        return cmndArgsSpecDict



####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "pyCmndInvOf_parsArgsStdinCmndResultDEFUNCT" :comment "" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<pyCmndInvOf_parsArgsStdinCmndResultDEFUNCT>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class pyCmndInvOf_parsArgsStdinCmndResultDEFUNCT(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  A starting point command.
        #+end_org """)

        if not (results := parsArgsStdinCmndResult(cmndOutcome=cmndOutcome).cmnd(
                rtInv=cs.RtInvoker.new_py(),
                cmndOutcome=cmndOutcome,
                par1Example="py_par1Val",
                argsList=['echo', 'py_arg2Val'],
                methodInvokeArg="py method invoke arg"
        ).results): return(b_io.eh.badOutcome(cmndOutcome))

        return(cmndOutcome)



####+BEGIN: b:py3:cs:framework/endOfFile :basedOn "classification"
""" #+begin_org
* [[elisp:(org-cycle)][| *End-Of-Editable-Text* |]] :: emacs and org variables and control parameters
#+end_org """

#+STARTUP: showall

### local variables:
### no-byte-compile: t
### end:
####+END:
