import socket


#####################################################
#Socket Connection
#####################################################

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('172.16.10.1', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address

sock.bind(server_address)

sock.listen(1)



while True:
        print >>sys.stderr, 'waiting for a connection'
        connection, client_address = sock.accept()
        try:
            print >>sys.stderr, 'connection from', client_address
            field0 = str(field0)
            field1 = str(field1)
            field2 = str(field2)
            field5 = str(field5)
            field6 = str(field6)
            field7 = str(field7)
            connection.send(field0)
            connection.send(field1)
            connection.send(field2)
            connection.send(field5)
            connection.send(field6)
            connection.send(field7)
        finally:
            connection.close()
    time.sleep(0.5)