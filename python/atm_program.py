import random
import datetime
from customer import Customer

atm = Customer(id)

while true:
    id =int(input('Masukkan pin Anda '))
    trial = 0

while (id != int(atm.checkPin()) and trial < 3):
    id = int(input('Pin Anda salah! Silahkan masukkan lagi: '))
    trial += 1

if trial == 3:
    print ('Error! Silahkan mengambil kartu Anda dan coba beberapa saat lagi. ')
    exit() 

while true:
    print('Selamat datang di ATM BOMBOM! ')
    print('\n1 - Cek Saldo \t2 - Debet \t3 - Simpan \t4 - Ganti Pin - \t5 - Keluar')
    selectmenu = int(input(' \n Silahkan memilih menu: '))

if selectmenu == 1:
    print('\n Saldo Anda sekarang: Rp. ' + str(atm.checkBalance()) + '\n')

    elif selectmenu == 2:
        nominal = float(input('Masukkan nominal saldo: '))
        verify withdraw = input('Konfirmasi: Anda akan melakukan debet dengan nominal berikut ? y/n ' + str(nominal) + ' ')

            if verify withdraw == 'y':
                print('Saldo awal Anda adalah: Rp. ' + str(atm.checkBalance()) + "")
            else:
                break

            if nominal < atm.checkBalance():
                atm.withdrawBalance (nominal)
                print('Transaksi debet Anda berhasil!')
                print('Sisa saldo Anda tersisa: Rp. ' + str(atm.checkBalance()) + '')
            else:
                print('Maaf, Saldo anda tidak mencukupi untuk melakukan debet!')
                print('Silahkan lakukan penambahan nominal saldo')

    elif selectmenu == 3:
        nominal = float(input('Masukkan nominal saldo: '))
        verify deposit = input('Konfirmasi: Anda akan melakukan penyimpanan dengan nominal berikut ? y/n ' + str(nominal) + " ")

            if verify deposit == 'y':
                atm.depositBalance(nominal)
                print('Saldo Anda sekarang adalah: Rp.' + str(atm.checkBalance()) + '\n' )
            else:
                break

    elif selectmenu == 4:
        verify_pin = int(input('Masukkan pin Anda: '))
            while verify_pin != int(atm.checkPin()):
                print('Pin anda salah! Silahkan masukkan pin Anda kembali: ')
            update_pin = int(input('Silahkan masukkan pin baru: '))
            print('Pin Anda berhasil diganti! ')
            verify_newpin = int(input('Coba masukkan pin baru Anda: '))
            
            if verify_newpin == update_pin:
                print('Pin baru Anda sukses!')
            else:
                print('Maaf, pin Anda salah!')

    elif selectmenu == 5:
        print('Resi Anda tercetak otomatis saat Anda keluar. \n Harap simpan tanda terima ini \n sebagai bukti transaksi Anda.')
        print('No. Rekord: ', random.randint(100000, 1000000))
        print('Tanggal: ', datetime.datetime.now())
        print('Saldo akhir: ', atm.checkBalance())
        print('Terima kasih telah menggunakan ATM BOMBOM!')
        exit()
    else:
        print('Error! maaf, menu tidak tersedia!')


    
    