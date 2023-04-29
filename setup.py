import os
import yaml
import configparser
from xml.etree import ElementTree as et

# read config
config = configparser.ConfigParser()
config.read('config.ini')

# set project props
project_props = {}
project_props['project_name'] = config.get('init', 'project_name')
project_props['description'] = config.get('init', 'description')
project_props['port'] = config.get('init', 'port')


print(f'Setting up project: {project_props}')

ns = "http://maven.apache.org/POM/4.0.0"
et.register_namespace('', ns)
tree = et.ElementTree()
tree.parse('pom.xml')

artifact_id_tree_element = tree.getroot().find("{%s}artifactId" % ns)
artifact_id_tree_element.text = project_props['project_name']

name_tree_element = tree.getroot().find("{%s}name" % ns)
name_tree_element.text = project_props['project_name']

description_tree_element = tree.getroot().find("{%s}description" % ns)
description_tree_element.text = project_props['description']

version_tree_element = tree.getroot().find("{%s}version" % ns)
version_tree_element.text = "0.0.0"

tree.write("pom.xml")

with open('docker/docker-compose.yml', 'r') as file:
    data = yaml.safe_load(file)

    # Modify the ports field of the 'app' service
    data['services']['app']['ports'] = project_props['port'] + ':8080'

# Write the updated dictionary back to the YAML file
with open('docker/docker-compose.yml', 'w') as file:
    yaml.dump(data, file)

os.remove('config.ini')
os.remove('setup.py')
