import Review
import os

#Tambahan baru:
import time
import random

# cek pembayaran
def CekBayar(ListReview,GameName):
    codes = ["XXYY12", "BQQPR1", "MMR20K", "MMR900", "MMR1DI", "MMRR69", "69A420"]
    while True:
        
        print("\n>>>Misalkan user mendapatkan email yang berisi kode pembayarannya<<<\n")
        print(">>>Di dalam email user:<<<\n")
        print("Thank you for purchase, congratulations on your new game.")
        print("We hope you can enjoy the game to its fulless.")
        print("This is your payment code:", codes[random.randint(0,len(codes)-1)])
        print("\n>>>Akhir dari email user<<<\n")

        time.sleep(5)
        print("Please check your email for your payment code.")
        code = input("\nPlease enter the payment code (enter 2 to cancel): ")
        code = code.upper()
        if(code in codes):
            Review.PendapatGame(ListReview,GameName)
            break
        elif (code == "2"):
            return None
        else:
            print("The payment code is wrong.")

def Transfer(ListReview,GameName):
    print("\n1. BCB\t4. Mundiri \n2. BMI\t5. Berlian \n3. BERI\t6. Cancel\n")
    pilih1 = int(input("Please choose the destination Bank: "))

    if(pilih1 == 1):
        print("Please transfer to account number: 1234567890 (Uap Beruap) of bank BCB")
        print("After that send the payment confirmation to our customer service and then you will recieve the payment code")
        CekBayar(ListReview,GameName)
    elif(pilih1 == 2):
        print("Please transfer to account number: 2345678901 (Uap Beruap) of bank Mundiri")
        print("After that send the payment confirmation to our customer service and then you will recieve the payment code")
        CekBayar(ListReview,GameName)
    elif(pilih1 == 3):
        print("Please transfer to account number: 3456789010 (Uap Beruap) of bank BMI")
        print("After that send the payment confirmation to our customer service and then you will recieve the payment code")
        CekBayar(ListReview,GameName)
    elif(pilih1 == 4):
        print("Please transfer to account number: 4567890101 (Uap Beruap) of bank Berlian")
        print("After that send the payment confirmation to our customer service and then you will recieve the payment code")
        CekBayar(ListReview,GameName)
    elif(pilih1 == 5):
        print("Please transfer to account number: 5678901011 (Uap Beruap) of bank Beri")
        print("After that send the payment confirmation to our customer service and then you will recieve the payment code")
        CekBayar(ListReview,GameName)
    elif(pilih1 == 6):
        print("The payment method has been canceled.")
        return None
    else:
        # print("Masukkan angka 1 sampai 6 saja.")
        # print("Mohon maaf untuk pilihan bank lain masih belum tersedia, silahkan pilih cara pembayaran lainnya.")
        print("Please only input number 1 through 6.")
        print("We are sorry, but the bank of your choice is not yet available, please choose another payment option.")

def Pulsa():
    # print("\n1.Buka menu panggilan dan ketikkan kode *858# dan tekan panggil/OK    \n2.Ketik angka 1 untuk pilihan Transfer Pulsa \n3.Masukkan 081233558800 dan nominal pulsa yang harus dibayarkan \n4.Setelah muncul notifkasi pada layar, masukkan angka 1 untuk konfirmasi ")
    print("\n1.Open the menu Calls on your phone and insert code *858# and press call/OK   \n2.Press number 1 to choose transferthe credit \n3.Insert 081233558800 and the amount of credits to be paid \n4.After a notification appeared on your screen, press number 1 to confirm. A code will then be send to you.")

def Ovo():
    # print("\n1.Buka aplikasi OPO anda \n2.Masukkan security pin anda \n3.Pilih menu transfer \n4.Masukkan nominal yang harus dibayarkan \n5.Pilih antar OPO \n6.Masukkan nomor 085335588811 \n7.Konfirmasi\n8.Masukkan kode security pin ")
    print("\n1.Open your OPO application \n2.Insert your security pin \n3.Choose transfer \n4.Insert the amount that has to be paid \n5.Choose Between OPO \n6.Insert number 085335588811 \n7.Confirm\n8.Insert your security pin. A code will then be send to you")

def Gopay():
    # print("\n1.Buka aplikasi Gopek anda \n2.Masukkan security pin anda \n3.Pilih menu bayar \n4.Masukkan nomor 081233565700 \n5.Masukkan nominal yang harus dibayarkan \n6.Klik konfirmasi \n7.Pilih bayar \n8.Masukkan kode security pin ")
    print("\n1.Open your Gopek application \n2.Insert your security pin \n3.Choose the pay option \n4.Insert the number 081233565700 \n5.Insert the amount that has to be paid \n6.Click confirm \n7.Choose pay \n8.Insert your security pin")

def Dana():
    # print("\n1.Buka aplikasi DANAS anda \n2.Masukkan security pin anda \n3.Pilih menu send \n4.Masukkan nominal yang harus dibayarkan \n5.Masukkan nomor 0833575800 \n6.Pilih send DANAS \n7.Konfirmasi\n8.Masukkan kode security pin")
    print("\n1.Open your DANAS application \n2.Insert your security pin \n3.Choose the send menu \n4.Insert the amount that has to be paid \n5.Insert the number 0833575800 \n6.Choose send DANAS \n7.Confirm \n8.Insert your security pin")

# def main():
#     while True:
#         print("Payment methods:")
#         print("\n1. Money Transfer\t4. Prepaid telephone credit (Telekomunikasi only) \n2. OPO\t\t\t5. Gopek \n3. DANAS\t\t6. Cancel")
#         pilih0 = int(input("Your choice: "))

#         if(pilih0 == 1):
#             print("\n1. BCB\t4. Mundiri \n2. BMI\t5. Berlian \n3. BERI\t6. Cancel")
#             pilih1 = int(input("Please choose the destination Bank: "))

#             if(pilih1 == 1):
#                 print("Please transfer to account number: 1234567890 (Uap Beruap) of bank BCB")
#                 print("After that send the payment confirmation to our customer service and then you will recieve the payment code")
#                 CekBayar()
#             elif(pilih1 == 2):
#                 print("Please transfer to account number: 2345678901 (Uap Beruap) of bank Mundiri")
#                 print("After that send the payment confirmation to our customer service and then you will recieve the payment code")
#                 CekBayar()
#             elif(pilih1 == 3):
#                 print("Please transfer to account number: 3456789010 (Uap Beruap) of bank BMI")
#                 print("After that send the payment confirmation to our customer service and then you will recieve the payment code")
#                 CekBayar()
#             elif(pilih1 == 4):
#                 print("Please transfer to account number: 4567890101 (Uap Beruap) of bank Berlian")
#                 print("After that send the payment confirmation to our customer service and then you will recieve the payment code")
#                 CekBayar()
#             elif(pilih1 == 5):
#                 print("Please transfer to account number: 5678901011 (Uap Beruap) of bank Beri")
#                 print("After that send the payment confirmation to our customer service and then you will recieve the payment code")
#                 CekBayar()
#             elif(pilih1 == 6):
#                 print("The payment method has been canceled.")
#             else:
#                 print("Masukkan angka 1 sampai 6 saja.")
#                 print("Mohon maaf untuk pilihan bank lain masih belum tersedia, silahkan pilih cara pembayaran lainnya.")

#         elif(pilih0 == 2):
#             print("\n1.Buka aplikasi OPO anda \n2.Masukkan security pin anda \n3.Pilih menu transfer \n4.Masukkan nominal yang harus dibayarkan \n5.Pilih antar OPO \n6.Masukkan nomor 085335588811 \n7.Konfirmasi\n8.Masukkan kode security pin ")
#             CekBayar()
#         elif(pilih0 == 3):
#             print("\n1.Buka aplikasi DANAS anda \n2.Masukkan security pin anda \n3.Pilih menu send \n4.Masukkan nominal yang harus dibayarkan \n5.Masukkan nomor 0833575800 \n6.Pilih send DANAS \n7.Konfirmasi\n8.Masukkan kode security pin")
#             CekBayar()
#         elif(pilih0 == 4):
#             print("\n1.Buka menu panggilan dan ketikkan kode *858# dan tekan panggil/OK    \n2.Ketik angka 1 untuk pilihan Transfer Pulsa \n3.Masukkan 081233558800 dan nominal pulsa yang harus dibayarkan \n4.Setelah muncul notifkasi pada layar, masukkan angka 1 untuk konfirmasi ")
#             CekBayar()
#         elif(pilih0 == 5):
#             print("\n1.Buka aplikasi Gopek anda \n2.Masukkan security pin anda \n3.Pilih menu bayar \n4.Masukkan nomor 081233565700 \n5.Masukkan nominal yang harus dibayarkan \n6.Klik konfirmasi \n7.Pilih bayar \n8.Masukkan kode security pin ")
#             CekBayar()
#         elif(pilih0 == 6):
#             print("Pembayaran telah dibatalkan.")
#             os.system("clear")
#             # os.system("cls")
#             break
#         else:
#             print("Maaf metode pembayaran yang anda inginkan masih belum ada, silahkan memilih salah satu dari cara-cara diatas.")