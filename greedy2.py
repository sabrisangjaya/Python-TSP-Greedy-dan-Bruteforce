counter,rutebrute,rutegreedy,waktupenyembuhan,waktuperjalanan=0,[],[],5,10

def bruteforce(node, kota, rute, wktempuh,groupy):
    rute.append(node)
    global rutebrute,counter
    if len(rute) > 1:
        wktempuh += kota[rute[-2]][node]*waktuperjalanan
        wktempuh += groupy[node]*waktupenyembuhan
    if (len(kota) == len(rute)) and (rute[0] in kota[rute[-1]]):
        rute.append(rute[0])
        wktempuh += kota[rute[-2]][rute[0]]*waktuperjalanan
        wktempuh += groupy[rute[0]]*waktupenyembuhan
        counter+=1
        print(counter,"-",rute,"=",wktempuh)
        rutebrute.append([wktempuh, rute])
        return
    for i in kota:
        if (i not in rute) and (node in kota[i]):
            bruteforce(i, dict(kota), list(rute), wktempuh,groupy)

def basic_greedy(kota,start,groupy):
    kotasekarang = start
    rtgreedy = []
    rtgreedy.append(kotasekarang)
    wktempuhgreedy = 0
    while len(kota)+1>len(rtgreedy):
        minjaraktetangga = None
        minjarak = None
        for tetangga in kota[kotasekarang]:
            if tetangga != kotasekarang and tetangga not in rtgreedy and len(kota)!=len(rtgreedy):
                if minjarak is not None:
                    if minjarak > ((kota[kotasekarang][tetangga]*waktuperjalanan) +(groupy[tetangga]*waktupenyembuhan)):
                        minjarak = kota[kotasekarang][tetangga]*waktuperjalanan
                        minjarak += groupy[tetangga]*waktupenyembuhan
                        minjaraktetangga = tetangga
                else:
                    minjarak = kota[kotasekarang][tetangga]*waktuperjalanan
                    minjarak += groupy[tetangga]*waktupenyembuhan
                    minjaraktetangga = tetangga
        if(len(kota)==len(rtgreedy)):
        	minjarak = kota[kotasekarang][start]*waktuperjalanan
        	minjarak += groupy[start]*waktupenyembuhan
        	minjaraktetangga = start

        for i in kota[start]:
            if(i not in rtgreedy):
                print(i,"=",kota[kotasekarang][i]*10,"+",groupy[i]*5,"|",end='')
        print("")
        for i in kota[start]:
            if(i not in rtgreedy):
                print(i,"=",(kota[kotasekarang][i]*10)+(groupy[i]*5),"|",end='')
        print("")
        tetanggaterdekat = (minjaraktetangga, minjarak)
        rtgreedy.append(tetanggaterdekat[0])
        if(len(kota)+1>len(rtgreedy)):
        	print("Pilih ", tetanggaterdekat[0],"\n")
        else:
        	print("Kembali ke",tetanggaterdekat[0]," +",tetanggaterdekat[1])
        kotasekarang = tetanggaterdekat[0]
        wktempuhgreedy += tetanggaterdekat[1]
    rutegreedy.append(rtgreedy)
    rutegreedy.append(wktempuhgreedy)
    
if __name__ == '__main__':
    groupymap = {
        'A': {'B': 6, 'C': 4, 'D': 4, 'E': 20, 'F':12,'G':8}, 
        'B': {'A': 6, 'C':4, 'D':6,'E':7,'F':4,'G':12}, 
        'C': {'A': 4, 'B': 4, 'D': 12, 'E': 8, 'F': 9, 'G': 4},  
        'D': {'A': 4, 'B': 6, 'C': 12, 'E': 3, 'F': 5, 'G': 12}, 
        'E': {'A': 20, 'B': 7, 'C': 8, 'D': 3, 'F': 8, 'G': 8},  
        'F': {'A': 12, 'B': 4, 'C': 9, 'D': 5, 'E': 8, 'G': 5},  
        'G': {'A': 8, 'B':12, 'C': 4, 'D': 12, 'E':8, 'F': 5}
    }
    groupies={'A':0,'B': 2, 'C': 4, 'D': 5, 'E': 1, 'F':2,'G':3}
    
    print("\nSemua Kemungkinan : ")
    bruteforce('A', groupymap, [], 0,groupies)
    rutebrute.sort()

    print("\nMaps : ")
    for groupy in groupymap:
        print(groupy," -> ",groupymap[groupy])
    print("\nGroupy Yang Harus Disembuhkan: ")
    for groupy in groupies:
        print(groupy," = ",groupies[groupy],"=",groupies[groupy]*waktupenyembuhan," menit")

    print("\nSolusi Brute Force")
    if len(rutebrute) != 0:
        print ("Rute Brute Force :",rutebrute[0][1])
        print ("Waktu Total :",rutebrute[0][0])
    else:
        print ("gagal menemukan rute!")

    print("\nSolusi Greedy")
    print ("Kota = Waktu Tempuh + Waktu Penyembuhan")
    basic_greedy(groupymap,'A',groupies)
    print("Rute Greedy :",rutegreedy[0])
    print("Waktu Total :",rutegreedy[1])

    nomorsolusi=next(i for i,x in enumerate(rutebrute) if rutegreedy[0] in x)
    
    print("\nPerbandingan Bruteforce dan Greedy")
    for i in range(0,nomorsolusi+3):
        if(i==nomorsolusi):
            print("Solusi greedy ->",end='')
        if(i==0):
            print("Solusi bruteforce ->",end='')
        print ("#",i+1," Rute Brute Force :",rutebrute[i][1], "Waktu Total :",rutebrute[i][0])

    exit=input("\n\nTekan enter untuk keluar")