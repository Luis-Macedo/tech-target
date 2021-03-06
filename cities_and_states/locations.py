import psycopg2 as db_connect
import json

def myConn():
    host_name="localhost"
    db_user="postgres"
    db_password="macedo"
    db_name="techtarget"
    return db_connect.connect(host=host_name,user=db_user,password=db_password,database=db_name)
        
connect = myConn()

def export_region(connect):

    f = open ('regioes.json', "r", encoding='utf-8')
    data = json.loads(f.read())
   
    sql = """INSERT INTO public.user_country_region(region_id, region_name) VALUES (%s, %s)"""
    try:
        cur = connect.cursor()
        for i in data['data']:
            cur.execute(sql, (i['Id'], i['Nome']))
            connect.commit()
            
    except:
        print("erro na regiao")

def export_state(connect):

    f = open ('estados.json', "r", encoding='utf-8')
    data = json.loads(f.read())

    sql = """INSERT INTO public.user_country_state(region_id, state_code, state_name, acronym) 
        VALUES (%s, %s, %s, %s)"""

    try:
        cur = connect.cursor()
        for i in data['data']:
            cur.execute(sql, (i['Regiao'], i['CodigoUf'], i['Nome'], i['Uf']))
            connect.commit()
            
    except:
        print("erro no estado")
    
    
def export_city(connect):
    f = open ('municipios.json', "r", encoding='utf-8')
    data = json.loads(f.read())
    
    sql = """INSERT INTO public.user_country_city(city_code, city_name, state_id) 
        VALUES (%s, %s, %s)"""

    try:
        cur = connect.cursor()
        for i in data['data']:
            cur.execute(sql, (i['Codigo'], i['Nome'], i['Uf']))
            connect.commit()
            
    except:
        print("erro na cidade")
    
    f.close()
    connect.close()

export_region(connect)
export_state(connect)
export_city(connect)

