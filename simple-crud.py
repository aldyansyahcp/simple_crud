import sqlite3
from os import system as sos
from tabulate import tabulate
from time import sleep as sl

def konek():
    try:
        con = sqlite3.connect("db/pendapatan.db")
        return con, con.cursor()
    except Error:
        print("Failed Connecting Database")
        
def tambahdata():
    con, c = konek()
    try:
        id = int(input("ID: "))
        ied = input("Tanggal: ")
        nama = input("Nama: ")
        pot = float(input("Pendapatan Rp."))
        tot = float(input("Pengeluaran bensin,dll Rp."))
        hs = pot-tot
        print(f"Pendapatan bersihmu {hs} tulis dibawah")
        h = input("Pendapatan berih Rp. ")
        #c.execute("CREATE TABLE pendapatan (id, ied, nama, pot, tot, h)")
        c.execute(
            "INSERT INTO pendapatan values (?,?,?,?,?,?)",
            (id,ied,nama,pot,tot,h))
        print("Data telah ditambahkan")
        con.commit()
    except ValueError:
        print("Ngisi data yang bener kntd")
    con.close()
    
def lihatsemua():
    con,c = konek()
    rall = c.execute("SELECT * FROM pendapatan")
    try:
        dat = c.fetchone()
        id = dat[0]
        ied = dat[1]
        nam = dat[2]
        pen = dat[3]
        peg = dat[4]           
        ber = dat[5]            
        tabel = [[id,ied,nam,pen,peg,ber]]
        if dat is not None:
            print(tabulate(tabel, headers=["ID","Tanggal","Nama","Pendapatan","Pengeluaran","Bersih"],tablefmt="fancy_grid"))
        else:
            print(f"{id} is Null")
    except:
        print("Null")
        
def lihat():
    lihatsemua()
    con, c = konek()
    eid = input("Pilih ID: ")
    if eid.isnumeric():
        c.execute("SELECT * FROM pendapatan WHERE id = {}".format(eid))
        data = c.fetchone()
        c.close()
        con.close()
        if data is not None:
            return data
        else:
            print("Data tidak ada tod!")        
    else:
        print("ID yg kamu pilih gaada tod!")

def hapus():
    dat = lihat()
    con,c = konek()
    if dat:        
        c.execute("DELETE FROM pendapatan WHERE id = {}".format(dat[0]))
        con.commit()
        print("data id = {} telah dihapus".format(dat[0]))
    c.close()
    con.close()
    
def update():
    dat = lihat()
    con,c = konek()
    try:
        id = int(input("ID Baru: "))
        tgl = input("Tanggal: ")
        nama = input("Nama: ")
        pen = float(input("Pendapatan Rp."))
        peg = float(input("Pengeluaran bensin,dll Rp."))
        hs = pen-peg
        print("Pendapatan bersihmu {} tulis dibawah".format(hs))
        ber = input("Pendapatan berih Rp. ")
        c.execute(f"UPDATE pendapatan SET ied='{tgl}', nama='{nama}', pot='{pen}', tot='{peg}', h='{ber}' WHERE id ={dat[0]}")
        con.commit()
        print("data ditambahkan")
    except ValueError:
        print("Ngisi yg bener asw")
        con.close()
        c.close()

def main():
    while True:
        print("\n")
        print("="*40)
        print("""█▀ █ █▀▄▀█ █▀█ █░░ █▀▀ ▄▄ █▀▀ █▀█ █░█ █▀▄▄█ █ █░▀░█ █▀▀ █▄▄ ██▄ ░░ █▄▄ █▀▄ █▄█ █▄▀""")
        print("="*40)
        print("Program penghasilan harian driver ojek")
        print("Silahkan dipilih kntd")
        pilih = ("""
            1.Tambah data
            2.Lihat semua data
            3.Lihat salah satu data
            4.Update data
            5.Hapus data
            6.exit
            """)
        print(pilih)
        try:
            pil = int(input("Dipilih kntd: "))
            if pil == 1:
                sos("clear")
                tambahdata()
            elif pil == 2:
                sos("clear")
                lihatsemua()
            elif pil == 3:
                sos("clear")
                lihat()
            elif pil == 4:
                sos("clear")
                update()
            elif pil == 5:
                sos("clear")
                hapus()
            elif pil == 6:
                print("Thank you for using this program")
                exit()
            else:
                print("Milih yg bener asw")
        except ValueError:
            print("Milih pake angka asw")
            exit()
        except KeyboardInterrupt:
            print("CTRL+X exited program")
            exit()
        
if __name__ == "__main__":
    konek()
    main()
