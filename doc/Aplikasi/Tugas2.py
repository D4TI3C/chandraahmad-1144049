graph = {
	             'Parungkuda': ['Cibadak'],
	             'Cibadak': ['Cicurug'],
	             'Cicurug': ['Karangtengah'],
	             'Karangtengah': ['Sukabumi Kota'],
	             'Sukabumi Kota': ['Sukaraja'],
	             'Sukaraja': ['Cisaat'],
	             'Cisaat': ['Jampang'],
	             'Jampang': ['PL Ratu'],        
	        }
	

	def rutepalingpendek(graph, lokasi_awal, lokasi_tujuan, rute=[]):
	        rute = rute + [lokasi_awal]
	        if lokasi_awal == lokasi_tujuan:
	            return rute
	            if not graph.has_key(lokasi_awal):
	                    return None
	        rutependek = None
	        for node in graph[lokasi_awal]:
	            if node not in rute:
	                rutebaru = rutepalingpendek(graph, node, lokasi_tujuan, rute)
	                if rutebaru:
	                    if not rutependek or len(rutebaru) < len(rutependek):
	                        rutependek = rutebaru
	        return rutependek
	print("Rute Jalan Raya Parungkuda sampai PL Ratu")
	print("(Parungkuda-Cibadak-Cicurug-Karangtengah-Sukabumi-Kota-Sukaraja-Cisaat-Jampang-PL Ratu)")
	print("Chandra Ahmad Rizki-1144049")
	print("\n")
	lokasi_awal = raw_input("Masukan Lokasi Awal : ")
	lokasi_tujuan = raw_input("Masukan Lokasi Tujuan : ")
	hasilnya = rutepalingpendek(graph, lokasi_awal, lokasi_tujuan, rute=[])
	print "Rute Terpendek", hasilnya ,".",
