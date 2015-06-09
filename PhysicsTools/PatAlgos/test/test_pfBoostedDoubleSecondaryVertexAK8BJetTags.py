## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *
## switch to uncheduled mode
process.options.allowUnscheduled = cms.untracked.bool(True)

## to run in un-scheduled mode uncomment the following lines
process.load("PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff")
process.load("PhysicsTools.PatAlgos.selectionLayer1.selectedPatCandidates_cff")

## uncomment the following line to add different jet collections
## to the event content
from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection

# uncomment the following lines to add ak8PFJetsCHS with new b-tags to your PAT output
addJetCollection(
   process,
   labelName = 'AK8PFCHS',
   jetSource = cms.InputTag('ak8PFJetsCHS'),
   jetCorrections = ('AK8PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'Type-2'),
   algo = 'AK',
   rParam = 0.8,
   btagDiscriminators = ['pfBoostedDoubleSecondaryVertexAK8BJetTags']
)
process.patJetsAK8PFCHS.addTagInfos = True


