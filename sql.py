import sqlite3

conn=sqlite3.connect('LoginCredentialsDetails.db')
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS UserDetails(
          Userid Text PRIMARY KEY,
          UserName Text[15],
          Password Text,
          Society_Name Text,
          Ph_number Integer[10],
          Flat_number Integer[4],
          Tower_number Text[3],
          Email_id email,
          Vehicle_number_1 Text,
          Vehicle_number_2 Text)""")

# c.execute("INSERT INTO UserDetails(Userid, UserName, Password, Society_Name, Ph_number , Flat_number, Tower_number, Email_id , Vehicle_number_1, Vehicle_number_2)" Values())

# c.execute("""INSERT INTO UserDetails(Userid, UserName, Password, Society_Name, Ph_number , Flat_number, Tower_number, Email_id) Values("Pratyay111", "Pratyay", "admin@123", "Technica-ITSol", 9876543210, 501, "A1", "admin@technicaitsol.com")""")
# c.execute("""INSERT INTO UserDetails(Userid, UserName, Password, Society_Name, Ph_number , Flat_number, Tower_number, Email_id) Values("Priyanshu111", "Priyanshu", "admin@123", "Technica-ITSol", 9876543210, 501, "A1", "admin@technicaitsol.com")""")
# c.execute("""INSERT INTO UserDetails(Userid, UserName, Password, Society_Name, Ph_number , Flat_number, Tower_number, Email_id) Values("Arjun111", "Arjun", "admin@123", "Technica-ITSol", 9876543210, 501, "A1", "admin@technicaitsol.com")""")

c.execute("""CREATE TABLE IF NOT EXISTS SocietyDetails(
          Userid Text PRIMARY KEY,
          Password Text,
          Society_Name Text,
          Ph_number Integer[10],
          Email_id email)""")

# c.execute("""INSERT INTO SocietyDetails(Userid, Password, Society_Name, Ph_number, Email_id) Values("Maintainence", "admin@321", "Dummy", 0123456789, "dummy@society.com")""")
conn.commit()