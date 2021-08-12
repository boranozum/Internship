import psycopg2
import argparse
import json
import random


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("-l","--load")

    args = parser.parse_args()

    conn = psycopg2.connect(
        dbname = "company_code_db",
        user = "postgres",
        password = "root",
        host = "localhost"
    )

    print("1")

    with conn:
        conn.autocommit = False
        with conn.cursor() as cur:

            with open(args.load,) as file:

                data = json.load(file)
                
                for company in data["companies"]:
                    try:
                        
                        id = random.randint(10000,99999)
                        mcc_code_length = random.randint(1,23)
                        iab_code_length = random.randint(1,19)
                        
                        mcc_codes = random.sample(list(data["mcc_codes"][0].items()),mcc_code_length)
                        iab_codes = random.sample(list(data["iab_codes"][0].items()),iab_code_length)
                        
                        
                        cur.execute("INSERT INTO companies VALUES(%s,%s,%s);",(id,company["name"],company["url"]))

                        
                        for iab in iab_codes:
                            
                            cur.execute("INSERT INTO iab_codes VALUES(%s,%s,%s);",(id,iab[0],iab[1]))

                        for mcc in mcc_codes:
                            
                            cur.execute("INSERT INTO mcc_codes VALUES(%s,%s,%s);",(id,mcc[1],mcc[0]))
                        
                        
                    except Exception as e:
                        print(e)
                        conn.rollback()

                    else:
                        conn.commit()
                        print("okey")
