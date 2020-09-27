import os, sys, shutil,json
from os import path as ppath
import requests
from py2neo import Graph
from py2neo import Path
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
def main(dbname, path):
	graph = Graph(password="GraphDB")
	srcdir= os.path.dirname(os.path.realpath(__file__))+'/'+path
	tgtdir='C:/Users/giaco/AppData/Local/Neo4j/Relate/Data/dbmss/dbms-2c89e8b6-6316-4187-8527-0b577fcdfc03/import/'+path
	if(not ppath.exists(tgtdir)):
		copytree(srcdir,tgtdir)
	for folder in os.listdir(path):
		if os.path.isdir(os.path.join(path,folder)):
			for file in os.listdir(os.path.join(path, folder)):
				file_path = os.path.join(path, folder, file)
				if file.startswith('entities') and file.endswith('.json'):
					query="WITH '"+file_path.replace('\\','/')+"' AS url CALL apoc.load.json(url) YIELD value UNWIND value.identifier as identifier UNWIND value.attributes AS entity CREATE (e:Entity{id:identifier,record_id:entity.record_id,index:entity.index,instance:entity.instance,feature_name:entity.feature_name,value:entity.value})"
					results = graph.run(query)
					print('Imported entities: ' + file_path)

				if file.startswith('activities') and file.endswith('.json'):
					query="WITH '"+file_path.replace('\\','/')+"' AS url CALL apoc.load.json(url) YIELD value UNWIND value.identifier as identifier UNWIND value.attributes AS activity CREATE (a:Activity{id:identifier,function_name:activity.function_name,features_name:activity.features_name,operation_number:activity.operation_number})"
					results = graph.run(query)
					print('Imported activities: ' + file_path)
				if file.startswith('relations') and file.endswith('.json'):
					with open(file_path) as json_file:
						data = json.load(json_file)
						totali=str(len(data))
						i=1
						for d in data:
							#print(str(i)+"/"+totali)
							i=i+1
							if(i%100==0):
								print(str(i)+"/"+totali)
							if(d['prov:relation_type']=='wasGeneratedBy' or d['prov:relation_type']=='wasInvalidatedBy'):
								query="MATCH (e:Entity),(a:Activity) "\
								"WHERE e.id = '"+d['prov:entity']+"' AND a.id = '"+d['prov:activity']+"' "\
								"CALL apoc.create.relationship(e, '"+d['prov:relation_type']+"', NULL, a) "\
								"yield rel as rel return rel,e,a"
							elif(d['prov:relation_type']=='used'):
								query="MATCH (e:Entity),(a:Activity) "\
								"WHERE e.id = '"+d['prov:entity']+"' AND a.id = '"+d['prov:activity']+"' "\
								"CALL apoc.create.relationship(a, '"+d['prov:relation_type']+"', NULL, e) "\
								"yield rel as rel return rel,e,a"
							elif(d['prov:relation_type']=='wasDerivedFrom'):
								query="MATCH (e1:Entity),(e2:Entity) "\
								"WHERE e1.id = '"+d['prov:generatedEntity']+"' AND e2.id = '"+d['prov:usedEntity']+"' "\
								"CALL apoc.create.relationship(e1, '"+d['prov:relation_type']+"', NULL, e2) "\
								"yield rel as rel return rel,e1,e2"
							results = graph.run(query)	
						print('Imported relations: ' + file_path)

"""
query="WITH '"+file_path.replace('\\','/')+"' AS url "\
"CALL apoc.load.json(url) YIELD value WITH value "\
"UNWIND value.`prov:relation_type` AS rtype "\
"MATCH (e:Entity),(a:Activity) "\
"WHERE e.id = value.`prov:entity` AND a.id = value.`prov:activity` "\
"CALL apoc.case(["\
"rtype='','CALL apoc.create.relationship(e, rtype, NULL, a) yield rel as rel return rel,e,a'"\
"],'',{}) return 1"
results = graph.run(query)	
print('Imported relations: ' + file_path)
"""
"""

				
"""
if __name__ == "__main__":
	#futura implementazione per rendere il dbname un parametro
	if len(sys.argv) == 3 :
		main(sys.argv[1], sys.argv[2])
	if len(sys.argv) == 2 :
		main('', sys.argv[1])
	else:
		print('[ERROR] usage: neo4j.py <files_path>')