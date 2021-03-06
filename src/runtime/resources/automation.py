import os, sys, json

LAB_DIRECTORY_STRUCTURE = [
    {'name': 'about', 'isDir': True, 'files': ['overview.html']},
    {'name': 'chapter', 'isDir': True, 'files': []},
    {'name': 'combinedopenended', 'isDir': True, 'files': []},
    {'name': 'course', 'isDir': True, 'files': []},
    {'name': 'discussion', 'isDir': True, 'files': []},
    {'name': 'drafts', 'isDir': True, 'files': []},
    {'name': 'html', 'isDir': True, 'files': []},
    {'name': 'info', 'isDir': True, 'files': []},
    {'name': 'peergrading', 'isDir': True, 'files': []},
    {'name': 'policies', 'isDir': True, 'files': []},
    {'name': 'problem', 'isDir': True, 'files': []},
    {'name': 'sequential', 'isDir': True, 'files': []},
    {'name': 'static', 'isDir': True, 'files': []},
    {'name': 'tabs', 'isDir': True, 'files': []},
    {'name': 'vertical', 'isDir': True, 'files': []},
    {'name': 'video', 'isDir': True, 'files': []},
    {'name': 'videoalpha', 'isDir': True, 'files': []},
    {'name': 'course.xml', 'isDir': False}
]
def directoryGenerator(labpath):
    print "Generating..."
    if not os.path.exists(labpath):
        os.makedirs(labpath)
        
    os.chdir(labpath)
    
    for i in LAB_DIRECTORY_STRUCTURE:
        if i['isDir']:
            os.mkdir(i['name'])
            if i['files'] != []:
                os.chdir(i['name'])
                for f in i['files']:
                    open(f, 'w').close()
                os.chdir('..')
        else:
            open(i['name'], 'w').close()
            
    os.chdir('..')
    print "Completed Generating!"
def labStructureGenerator(labpath):
    os.chdir(labpath)
    labspec = json.loads(open('labspec.json', 'r').read())
    print os.getcwd()

    course = open('course.xml', 'w')
    course_data = labspec['course']
    course.write('<course url_name="%s" org="%s" course="%s"/>'\
                     %(course_data['id'], course_data['org'], \
                           course_data['id']))

    os.chdir('about')

    overview = open('overview.html', 'w')
    overview_data = """<section class="about">
  <h2>About This Course</h2>
  <p> %s </p>
</section>""" % labspec['overview']

    overview.write(overview_data)
    os.chdir('..')

    os.chdir('course')
    experiments_list = labspec['experiments']
    experiments_metadata = """ """
    for experiment in experiments_list:
        experiments_metadata = experiments_metadata + \
          ('\n  <chapter url_name="%s"/>' \
               % experiment['name'].replace(" ","_"))
        os.chdir('../chapter')
        experiment_file = open(experiment['name'].replace(" ", "_") +\
                                   '.xml', 'w')

        subsection_metadata = """ """
        for subsection in experiment['subsections']:
            subsection_metadata = subsection_metadata + \
              '\n  <sequential url_name="%s"/>' \
              % (experiment['name'].replace(" ","_")+"_"+\
                     subsection['name'].replace(" ","_"))
            os.chdir('../sequential')
            subsection_file = open(experiment['name'].replace(" ","_") +\
                                       "_" + \
                                       subsection['name'].replace(" ","_") + \
                                       '.xml', 'w')
            subsection_vertical_data = """<sequential display_name="%s">
  <vertical url_name="%s"/>
</sequential>""" % (subsection['name'], experiment['name'].replace(" ","_")+\
                        "_"+subsection['name'].replace(" ","_") + "_" + "Unit")
            subsection_file.write(subsection_vertical_data)
            subsection_file.close()
            os.chdir('../vertical')
            unit_file = open(experiment['name'].replace(" ","_") + "_" + \
                                 subsection['name'].replace(" ","_") +\
                                 "_Unit.xml",'w')
            unit_file_data = """<vertical display_name="%s">
  <html url_name="%s"/>
</vertical>""" % ("Unit", experiment['name'].replace(" ","_")+"_"+\
                      subsection['name'].replace(" ","_") + "_Unit_html")
            unit_file.write(unit_file_data)
            unit_file.close()
            os.chdir('../html')
            unit_file_xml = open(experiment['name'].replace(" ","_")+\
                                     "_"+subsection['name'].replace(" ","_") +\
                                     "_Unit_html.xml",'w')
            unit_file_html = open(experiment['name'].replace(" ","_")+"_"+\
                                      subsection['name'].replace(" ","_") +\
                                      "_Unit_html.html",'w')
            unit_file_html.write("<h2>%s</h2>"%subsection['name'])
            unit_file_html.close()
            unit_file_xml_data =  """<html file_name="%s" filename="%s"/>""" \
              % (experiment['name'].replace(" ","_")+"_"+\
                     subsection['name'].replace(" ","_") + "_Unit_html",
                     experiment['name'].replace(" ","_")+"_"+\
                     subsection['name'].replace(" ","_") + "_Unit_html")
            unit_file_xml.write(unit_file_xml_data)
            unit_file_xml.close()
            os.chdir('../chapter')

        subsection_data = """<chapter display_name="%s">%s
</chapter>""" % (experiment['name'], subsection_metadata)
        experiment_file.write(subsection_data)
        experiment_file.close()
        os.chdir('../course')

    experiments_data = """<course display_name="%s">%s
</course>""" % (course_data['display_name'], experiments_metadata)

    experiments = open(course_data['id']+'.xml', 'w')
    experiments.write(experiments_data)
    experiments.close()
    os.chdir('..')
def generateLab(labpath):
    os.chdir(labpath)
    if os.path.isfile('labspec.json'):
        directoryGenerator(labpath)
        labStructureGenerator(labpath)
    else:
        print "Place a labspec.json file in the lab folder and"\
          "give the absolute path of the lab folder"
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage : python <Automation-Script> <Absolute Path of lab>"
    else:
        generateLab(sys.argv[1])
