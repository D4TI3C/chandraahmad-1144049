import time
start_time = time.time()
print("Menghitung Jumlah Uang Kembalian Nominal 1000")
d = raw_input("Masukan Nilai Uang Yang Dibayar : ")
i = raw_input("Masukan Nilai Harga Barang : ")

if d == '1000':
	d=1000

if d == '2000':
	d=2000

if d == '3000':
	d=3000

if d == '4000':
	d=4000

if d == '5000':
	d=5000

if d == '6000':
	d=6000

if d == '7000':
	d=7000

if d == '8000':
	d=8000

if d == '9000':
	d=9000

if d == '10000':
	d=10000


if i == '1000':
	i=1000

if i == '2000':
	i=2000

if i == '3000':
	i=3000

if i == '4000':
	i=4000

if i == '5000':
	i=5000

if i == '6000':
	i=6000

if i == '7000':
	i=7000

if i == '8000':
	i=8000

if i == '9000':
	i=9000

if i == '10000':
	i=10000
	

jumlah = d-i
print ("hasil" , jumlah)
print("time : %s detik " % (time.time() - start_time))