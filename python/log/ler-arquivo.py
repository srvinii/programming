print __doc__
f = open('/home/vinii/Desktop/arq.txt')
for linha in f:
    print linha.rstrip()
f.close()
print '--- fim'
