# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import urllib2
import psycopg2

def bse_url_builder(url):
    temp = 'http://www.google.com/finance/info?q=BOM:'
    final_url = temp + url
    socket1 = urllib2.urlopen(final_url)
    data = socket1.read()

    # returns a list of dictionaries
    #print data
    return data
    
def url_json_reader(data, tablename):
    dynamic_sql = "Insert into " + tablename + "("
    colname = ""
    values = ""
    for line in data.split('\n'):
        if line == "// [":
            print "continue"
        elif line == "]":
            print "continue"
        else:
            try:
                key = line.strip(',').strip(' ').split(":")[0].strip('"').strip(' ').strip('"')
                temp_value = line.strip(',').strip(' ').split(":")[1].strip('"').strip(' ').strip('"')
                #print (key, type(key))
                tempcol = column_mapping[key]
                if len(colname) == 0:
                    colname = tempcol
                    values = temp_value
                else:
                    temp_value = "'" + temp_value + "'"
                    colname = colname + "," + tempcol
                    values = values + "," + temp_value
            except KeyError:
                #print 'Invalid key'
                continue
                #print ('Keyerror: ',line.strip(',').split(":")[0])
                #continue
            except IndexError:
                continue
    dynamic_sql = dynamic_sql + colname +  ")" +" values " + "(" + values + ")"
    print dynamic_sql
    cur = pg_connect('postgres', 'postgres','localhost','admin')
    pg_execute(cur,dynamic_sql)

# create an instance of connection and return a cursor to the parent class
def pg_connect(dbname , user, host, password):
    try:
        str1 = str('"' + "dbname = " + "'" +dbname + "'" + " user=" + "'" +user+ "'"  + " host= " + "'" +host+ "'"  + " password=" + "'" +password+ "'"  + '"')
        print str1
        command = "conn = psycopg2.connect(" + str1 + ")"
        #print command
        exec command
        
        # set commit level to auto commit
        conn.set_isolation_level(0)
        cur = conn.cursor()
        print "Connected"
        #print "Connected"
    except:
            print "Connect Error!"
    return cur

def pg_execute(cur, i ):
    custom_query= i
    custom_command = 'cur.execute("' + custom_query + '")'
    try:
        
        exec custom_command
        rows = cur.fetchall()
        return rows
    except Exception,e:
        print e.args, e.message
        #return e.message

url = "524091"
#,532683,500112"

column_mapping = {
"id": "id"
,"t" : "ticker"
,"e" : "Index"
,"l" : "lastTradePrice"
,"l_fix" : "lastTradeFix"
,"l_cur" : "lastTradedCurrency"
,"s": "LastTradeSize"
,"ltt":"LastTradeTime"
,"lt" : "LastTradeDateTimeLong"
,"lt_dts" : "LastTradeDateTime"
,"c" : "Change"
,"c_fix" : "ChangeFix"
,"cp" : "ChangePercentage"
,"cp_fix" : "ChangePercentageFix"
,"ccol" : "ccol"
,"pcls_fix" : "PreviousClosePrice"
}

if __name__ == "__main__":
    # reading data from bse and storing as string in data variable
    #data = bse_url_builder(url)
    data = '\n// [\n{\n"id": "5255401"\n,"t" : "524091"\n,"e" : "BOM"\n,"l" : "570.00"\n,"l_fix" : "570.00"\n,"l_cur" : "Rs.570.00"\n,"s": "0"\n,"ltt":"3:30PM GMT+5:30"\n,"lt" : "Jun 8, 3:30PM GMT+5:30"\n,"lt_dts" : "2016-06-08T15:30:00Z"\n,"c" : "+16.60"\n,"c_fix" : "16.60"\n,"cp" : "3.00"\n,"cp_fix" : "3.00"\n,"ccol" : "chg"\n,"pcls_fix" : "553.4"\n}\n]\n'
    # parse the downloaded data for storage
    url_json_reader(data, 'stock_db.BSE_SCRIPTS')
    
