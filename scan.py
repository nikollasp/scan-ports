from socket import *
import threading

def scan (host):
    print("Scaneando...")
    doorOpen=[]

    for port in range(1,1000):
        if port %2 == 0:
            conect = client = socket(AF_INET, SOCK_STREAM)
            conect.settimeout(0.01)
    
            #print(port)

            if  conect.connect_ex((host,port))== 0:
                doorOpen.append(port)
                #print("PORTA ABERTA")
    print("PORTAS ABERTAS: ",doorOpen)

def scanImpar (host):
    print("Scaneando...")
    doorOpen=[]

    for port in range(1,1000):
        if port %2 == 1:
            conect = client = socket(AF_INET, SOCK_STREAM)
            conect.settimeout(0.01)
    
            #print(port)

            if  conect.connect_ex((host,port))== 0:
                doorOpen.append(port)
                #print("PORTA ABERTA")
    print("PORTAS ABERTAS: ",doorOpen)



#main
host = str(input("Digite o IP para scanear: "))
threading.Thread(target=scan(host)).start()
scanImpar(host)


print("FINALIZADO")

