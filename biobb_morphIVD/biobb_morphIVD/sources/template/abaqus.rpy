# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2020 replay file
# Internal Version: 2019_09_13-20.49.31 163176
# Run by estefanaxo on Mon Dec  5 15:23:00 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Abaqus Warning: Keyword (dsls_license_config) must point to an existing file.
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=596.996643066406, 
    height=232.039566040039)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
#: Abaqus Warning: Keyword (dsls_license_config) must point to an existing file.
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.ModelFromInputFile(name='L4-L5_shell', 
    inputFileName='/home/estefanaxo/Documentos/phd/tesis/discsToMorph/sources/template/L4-L5_shell.inp')
#: The model "L4-L5_shell" has been created.
#: WARNING: Orientation "LOCALAF" with definition of offset to nodes is not yet supported for rebar layer. 
#: WARNING: Orientation "LOCALAF" with definition of offset to nodes is not yet supported for rebar layer. 
#: WARNING: Orientation "LOCALAF" with definition of offset to nodes is not yet supported for rebar layer. 
#: WARNING: Orientation "LOCALAF" with definition of offset to nodes is not yet supported for rebar layer. 
#: The part "L4-L5-1" has been imported from the input file.
#: 
#: WARNING: The following keywords/parameters are not yet supported by the input file reader:
#: ---------------------------------------------------------------------------------
#: *PERMEABILITY, DEPENDENCIES
#: *PREPRINT
#: The model "L4-L5_shell" has been imported from an input file. 
#: Please scroll up to check for error and warning messages.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['L4-L5_shell'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['L4-L5_shell'].parts['L4-L5-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.meshEditOptions.setValues(enableUndo=True, maxUndoCacheElements=0.5)
p = mdb.models['L4-L5_shell'].parts['L4-L5-1']
p.deleteElement(elements=[p.sets['AF'], p.sets['AF-Z1'], p.sets['AF-Z2'], 
    p.sets['AF_REBARS'], p.sets['BEPLOWER'], p.sets['BEPUPPER'], p.sets['NP'], 
    p.sets['NP-Z1'], p.sets['NP-Z2'], p.sets['NP-Z3'], p.sets['NP-Z4'], 
    p.sets['NP-Z5'], p.sets['REBARS_AI'], p.sets['REBARS_AO'], 
    p.sets['REBARS_PI'], p.sets['REBARS_PO']], deleteUnreferencedNodes=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=106.676, 
    farPlane=171.984, width=107.674, height=47.0073, cameraPosition=(81.6021, 
    81.5349, 78.9989), cameraUpVector=(-0.800397, -0.297433, 0.520479), 
    cameraTarget=(1.71696, 1.64971, -0.886238))
session.viewports['Viewport: 1'].view.setValues(nearPlane=110.931, 
    farPlane=168.267, width=111.969, height=48.8824, cameraPosition=(-35.4851, 
    119.582, -64.927), cameraUpVector=(0.00456215, 0.139946, 0.990149), 
    cameraTarget=(0.906134, 1.91319, -1.88292))
session.viewports['Viewport: 1'].view.setValues(nearPlane=116.254, 
    farPlane=162.415, width=117.342, height=51.228, cameraPosition=(-4.67899, 
    140.316, 1.12246), cameraUpVector=(-0.0288486, -0.351302, 0.935818), 
    cameraTarget=(1.17846, 2.09648, -1.29904))
session.viewports['Viewport: 1'].view.setValues(nearPlane=109.58, 
    farPlane=169.571, width=110.605, height=48.2869, cameraPosition=(47.9386, 
    128.845, 29.0116), cameraUpVector=(-0.140295, -0.513373, 0.84662), 
    cameraTarget=(1.54457, 2.01666, -1.10499))
session.viewports['Viewport: 1'].view.setValues(nearPlane=117.335, 
    farPlane=161.513, width=118.433, height=51.7041, cameraPosition=(1.48185, 
    140.481, -0.909881), cameraUpVector=(0.222723, -0.336891, 0.914822), 
    cameraTarget=(1.14165, 2.11758, -1.3645))
session.viewports['Viewport: 1'].view.setValues(nearPlane=111.187, 
    farPlane=167.438, width=112.228, height=48.9951, cameraPosition=(-32.4566, 
    134.856, -21.5779), cameraUpVector=(0.197668, -0.151427, 0.968503), 
    cameraTarget=(0.883837, 2.07485, -1.5215))
session.viewports['Viewport: 1'].view.setValues(nearPlane=111.537, 
    farPlane=167.087, width=112.581, height=49.1495, cameraPosition=(-32.4566, 
    134.856, -21.5779), cameraUpVector=(0.0577468, -0.184657, 0.981105), 
    cameraTarget=(0.883837, 2.07485, -1.5215))
session.viewports['Viewport: 1'].view.setValues(nearPlane=116.015, 
    farPlane=162.896, width=117.101, height=51.1228, cameraPosition=(-4.38958, 
    140.023, -11.1893), cameraUpVector=(0.016658, -0.265701, 0.963912), 
    cameraTarget=(1.07478, 2.11, -1.45082))
p = mdb.models['L4-L5_shell'].parts['L4-L5-1']
e = p.elements
elements = e.getSequenceFromMask(mask=(
    '[#ffffffff:80 #ffffff #0:80 #ff000000 ]', ), )
p.deleteElement(elements=elements, deleteUnreferencedNodes=ON)
a = mdb.models['L4-L5_shell'].rootAssembly
a.regenerate()
a = mdb.models['L4-L5_shell'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p1 = mdb.models['L4-L5_shell'].parts['L4-L5-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.models['L4-L5_shell'].parts['L4-L5-1'].deleteSets(setNames=('BEPUPPER', 
    'AF', 'AF-Z1', 'AF-Z2', 'AF_REBARS', 'BEPLOWER', ))
mdb.models['L4-L5_shell'].parts['L4-L5-1'].deleteSets(setNames=('ND-SURF', 
    'NP', 'NP-Z1', 'NP-Z2', 'NP-Z3', 'NP-Z4', 'NP-Z5', 'REBARS_AI', 
    'REBARS_AO', 'REBARS_PI', 'REBARS_PO', ))
a = mdb.models['L4-L5_shell'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
mdb.models['L4-L5_shell'].boundaryConditions.delete(('Disp-BC-1', 'Por-BC-1', 
    ))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Carga_noche')
mdb.models['L4-L5_shell'].loads.delete(('SURFFORCE-1', 'SURFFORCE-2', 
    'SURFFORCE-3', 'SURFFORCE-4', ))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='templateCEPlower', model='L4-L5_shell', description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
mdb.jobs['templateCEPlower'].writeInput(consistencyChecking=OFF)
#: The job input file has been written to "templateCEPlower.inp".
